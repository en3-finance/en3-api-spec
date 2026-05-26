#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit("PyYAML is required: python -m pip install pyyaml") from exc


ROOT = Path(__file__).resolve().parents[1]

BOUNDARY = (
    "Status: public reference / sandbox artifact. This repository is intended to "
    "document and demonstrate the En3 integration surface. Production "
    "cryptography, signing orchestration, policy enforcement, risk logic, ledger "
    "infrastructure, treasury execution, and customer deployments are private by "
    "design."
)

PUBLIC_EVENTS = {
    "organization.created",
    "user.created",
    "wallet.created",
    "address.created",
    "policy.created",
    "transaction.submitted",
    "transaction.simulated",
    "transaction.requires_approval",
    "transaction.approved",
    "transaction.signing",
    "transaction.signed",
    "transaction.broadcast",
    "transaction.settled",
    "transaction.failed",
    "audit.event_created",
    "reconciliation.updated",
}

FORBIDDEN_EVENTS = {
    "audit." + "event_recorded",
    "ledger." + "entry_created",
    "reconciliation." + "entry_created",
}

STATUSES = {
    "WalletStatus": ["created", "address_issued", "active", "suspended", "closed"],
    "TransactionStatus": [
        "submitted",
        "simulated",
        "requires_approval",
        "approved",
        "signing",
        "signed",
        "broadcast",
        "settled",
        "failed",
        "cancelled",
    ],
    "RiskDecision": ["allow", "review_required", "block"],
    "ApprovalStatus": ["not_required", "pending", "approved", "rejected", "expired"],
    "WebhookDeliveryStatus": ["pending", "delivered", "failed", "retrying"],
    "ReconciliationStatus": ["pending", "matched", "exception", "resolved"],
}

PUBLIC_PATHS = [
    "README.md",
    "SECURITY.md",
    "openapi",
    "asyncapi",
    "docs",
    "examples",
    "specs",
    ".specify",
]

SECRET_PATTERNS = [
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |)PRIVATE KEY-----"),
    re.compile(r"\b(?:sk|pk)_(?:live|test)_[A-Za-z0-9]{12,}\b"),
    re.compile(r"https?://(?:mainnet|rpc|eth|polygon|arb|base)[A-Za-z0-9_.:/-]*", re.I),
]

FORBIDDEN_PRIVATE_PHRASES = [
    "real " + "custody",
    "real " + "keys",
    "real " + "rpc",
    "private " + "partner",
    "fund" + "raising",
    "strategic " + "acquirer",
    "adi/",
    "adi " + "grant",
    "customer deployment " + "config",
]


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return yaml.safe_load(handle)


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def iter_public_files():
    for entry in PUBLIC_PATHS:
        path = ROOT / entry
        if path.is_file():
            yield path
        elif path.is_dir():
            for child in path.rglob("*"):
                if child.is_file():
                    yield child


def strip_allowed_boundary(text: str) -> str:
    return text.replace(BOUNDARY, "")


def validate_yaml_and_json():
    openapi = load_yaml(ROOT / "openapi/en3-wallet-api.yaml")
    asyncapi = load_yaml(ROOT / "asyncapi/en3-webhooks.yaml")

    for path in (ROOT / "examples").rglob("*.json"):
        load_json(path)

    return openapi, asyncapi


def validate_contract_values(openapi, asyncapi):
    channels = set(asyncapi["channels"].keys())
    if channels != PUBLIC_EVENTS:
        missing = sorted(PUBLIC_EVENTS - channels)
        extra = sorted(channels - PUBLIC_EVENTS)
        raise AssertionError(f"AsyncAPI public events mismatch. missing={missing} extra={extra}")

    public_event_enum = set(openapi["components"]["schemas"]["PublicEventType"]["enum"])
    if public_event_enum != PUBLIC_EVENTS:
        raise AssertionError("OpenAPI PublicEventType enum does not match canonical public events")

    schemas = openapi["components"]["schemas"]
    for name, expected in STATUSES.items():
        actual = schemas[name]["enum"]
        if actual != expected:
            raise AssertionError(f"{name} mismatch: {actual} != {expected}")

    if "/reconciliation/reports/{reportId}" in openapi["paths"]:
        raise AssertionError("Unsupported reconciliation report endpoint must not be public")
    if "/reconciliation-reports/{reportId}" in openapi["paths"]:
        raise AssertionError("Legacy reconciliation report endpoint must not be public")


def validate_public_boundary():
    errors = []
    for path in iter_public_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        relative = path.relative_to(ROOT)
        if path.suffix in {".md", ".yaml", ".yml"} and "Status: public reference / sandbox artifact." not in text:
            errors.append(f"{relative}: missing public boundary statement")

        scan_text = strip_allowed_boundary(text)
        for event in FORBIDDEN_EVENTS:
            if event in scan_text:
                errors.append(f"{relative}: forbidden event {event}")

        lowered = scan_text.lower()
        for phrase in FORBIDDEN_PRIVATE_PHRASES:
            if phrase in lowered:
                errors.append(f"{relative}: forbidden private phrase {phrase!r}")

        for pattern in SECRET_PATTERNS:
            for match in pattern.finditer(scan_text):
                token = match.group(0)
                if token.startswith("sandbox_") or token.startswith("org_sandbox_"):
                    continue
                errors.append(f"{relative}: possible secret or real endpoint {token[:16]}...")

    if errors:
        raise AssertionError("\n".join(errors))


def main():
    openapi, asyncapi = validate_yaml_and_json()
    validate_contract_values(openapi, asyncapi)
    validate_public_boundary()
    print("public contracts validated")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(exc, file=sys.stderr)
        raise SystemExit(1) from exc

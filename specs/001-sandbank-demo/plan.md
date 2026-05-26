# Implementation Plan: SandBank Demo

Status: public reference / sandbox artifact. This repository is intended to document and demonstrate the En3 integration surface. Production cryptography, signing orchestration, policy enforcement, risk logic, ledger infrastructure, treasury execution, and customer deployments are private by design.

## Source Contract Pack

Use only sanitized files from `../en3-platform/contracts/public`:

- `domain-model.yaml`
- `event-catalog.yaml`
- `status-catalog.yaml`
- `id-conventions.md`
- `error-catalog.md`
- `lifecycle-matrix.md`

## Contract Updates

- Align OpenAPI schemas with exported resources and status vocabularies.
- Remove unsupported reconciliation report endpoint from the public REST contract.
- Align AsyncAPI channels with the canonical event catalog.
- Preserve sandbox-only placeholder URLs and synthetic fixtures.

## Validation

- Add `scripts/validate_public_contracts.py`.
- Parse YAML and JSON examples.
- Compare event channels and status enums to canonical public vocabularies.
- Scan public files for forbidden old events, private terms, and secret-like values.

## Documentation

- Add SandBank API flow.
- Update webhook signature boundary.
- Add transaction lifecycle flow.
- Add explicit public/private boundary doc.

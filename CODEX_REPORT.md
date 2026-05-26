# CODEX Report: SandBank Public API Contracts

## Summary

Aligned the public API and webhook contracts with the sanitized SandBank export pack from `../en3-platform/contracts/public`.

## Implemented

- Created `feat/sandbank-demo` from `main`.
- Added Spec Kit-style artifacts under `.specify/` and `specs/001-sandbank-demo/`.
- Updated `openapi/en3-wallet-api.yaml` with canonical statuses, sandbox endpoints, and SandBank examples.
- Updated `asyncapi/en3-webhooks.yaml` with canonical public events only.
- Added SandBank request, response, webhook, and flow examples under `examples/sandbank/`.
- Added public docs for API flow, webhook signatures, lifecycle, and public/private boundary.
- Added `scripts/validate_public_contracts.py`.

## Validation Results

- `python3 scripts/validate_public_contracts.py` - passed.

## Caveats

- No production custody, signing, policy, ledger, treasury, or customer deployment behavior is represented here.
- The OpenAPI/AsyncAPI contracts are sandbox/reference artifacts.

## REPORT_TO_PASTE_IN_CHAT

Branch: `feat/sandbank-demo`

Commit: see orchestrator final report

Pushed status: see orchestrator final report

Validation:
- `python3 scripts/validate_public_contracts.py` - passed.

Run locally:

```bash
python3 scripts/validate_public_contracts.py
```

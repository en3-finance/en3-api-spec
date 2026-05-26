# Webhook Signatures

Status: public reference / sandbox artifact. This repository is intended to document and demonstrate the En3 integration surface. Production cryptography, signing orchestration, policy enforcement, risk logic, ledger infrastructure, treasury execution, and customer deployments are private by design.

This document describes the public sandbox boundary for webhook signature handling. It is not a production secret-management or key-management document.

## Sandbox Header Shape

Sandbox webhook examples use these headers:

- `En3-Event-Id`
- `En3-Event-Type`
- `En3-Event-Timestamp`
- `En3-Signature`

## Verification Model

Partner backends should:

1. Read the raw request body.
2. Check event idempotency by `En3-Event-Id`.
3. Check timestamp tolerance.
4. Verify the signature using the sandbox webhook material assigned out of band.
5. Store the event before applying state changes.
6. Return a 2xx response only after durable receipt.

## Public Boundary

The public repositories do not contain production webhook secrets, production signing keys, private endpoints, customer payloads, or production delivery infrastructure. Signature examples are contract documentation only.

# Transaction Lifecycle Flow

Status: public reference / sandbox artifact. This repository is intended to document and demonstrate the En3 integration surface. Production cryptography, signing orchestration, policy enforcement, risk logic, ledger infrastructure, treasury execution, and customer deployments are private by design.

## Transaction Statuses

`submitted` -> `simulated` -> `requires_approval` -> `approved` -> `signing` -> `signed` -> `broadcast` -> `settled`

Terminal or alternate statuses:

- `failed`
- `cancelled`

## Approval-Required Event Sequence

The SandBank approval-required path emits:

1. `transaction.submitted`
2. `transaction.simulated`
3. `transaction.requires_approval`
4. `transaction.approved`
5. `transaction.signing`
6. `transaction.signed`
7. `transaction.broadcast`
8. `reconciliation.updated`
9. `transaction.settled`

Audit trail publication uses `audit.event_created`.

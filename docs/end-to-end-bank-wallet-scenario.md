# SandBank Sandbox Wallet Scenario

Status: public reference / sandbox artifact. This repository is intended to document and demonstrate the En3 integration surface. Production cryptography, signing orchestration, policy enforcement, risk logic, ledger infrastructure, treasury execution, and customer deployments are private by design.

SandBank is fictional and synthetic. This scenario is a public reference flow for En3 sandbox API and webhook contracts.

## Flow

1. SandBank creates an En3 sandbox organization.
2. SandBank creates an En3 sandbox user and wallet.
3. En3 issues a synthetic deposit address.
4. SandBank creates a sandbox policy with approval and block thresholds.
5. SandBank registers a webhook endpoint for canonical public events.
6. The user submits an outgoing payment intent.
7. The transaction is simulated.
8. The sandbox policy/risk result requires approval.
9. A sandbox operator approves the transaction.
10. Mock signing, mock broadcast, settlement, reconciliation, and audit events are recorded as sandbox state.
11. Webhooks notify the partner backend.

## Canonical Transaction States

- `submitted`
- `simulated`
- `requires_approval`
- `approved`
- `signing`
- `signed`
- `broadcast`
- `settled`
- `failed`
- `cancelled`

## Canonical Events

- `organization.created`
- `user.created`
- `wallet.created`
- `address.created`
- `policy.created`
- `transaction.submitted`
- `transaction.simulated`
- `transaction.requires_approval`
- `transaction.approved`
- `transaction.signing`
- `transaction.signed`
- `transaction.broadcast`
- `transaction.settled`
- `transaction.failed`
- `audit.event_created`
- `reconciliation.updated`

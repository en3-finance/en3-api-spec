# En3 Public API Constitution

Status: public reference / sandbox artifact. This repository is intended to document and demonstrate the En3 integration surface. Production cryptography, signing orchestration, policy enforcement, risk logic, ledger infrastructure, treasury execution, and customer deployments are private by design.

## Principles

1. Public contracts are synchronized strictly from `../en3-platform/contracts/public`.
2. SandBank is fictional, synthetic, and limited to sandbox/reference artifacts.
3. Public examples use deterministic sandbox identifiers and non-secret placeholder URLs.
4. Production cryptography, custody, signing orchestration, policy enforcement, risk logic, ledger infrastructure, treasury execution, and deployment configuration remain private.
5. Public webhook event names must match the canonical public event catalog.

## Required Vocabulary

Canonical statuses:

- WalletStatus: `created`, `address_issued`, `active`, `suspended`, `closed`
- TransactionStatus: `submitted`, `simulated`, `requires_approval`, `approved`, `signing`, `signed`, `broadcast`, `settled`, `failed`, `cancelled`
- RiskDecision: `allow`, `review_required`, `block`
- ApprovalStatus: `not_required`, `pending`, `approved`, `rejected`, `expired`
- WebhookDeliveryStatus: `pending`, `delivered`, `failed`, `retrying`
- ReconciliationStatus: `pending`, `matched`, `exception`, `resolved`

Canonical public events:

`organization.created`, `user.created`, `wallet.created`, `address.created`, `policy.created`, `transaction.submitted`, `transaction.simulated`, `transaction.requires_approval`, `transaction.approved`, `transaction.signing`, `transaction.signed`, `transaction.broadcast`, `transaction.settled`, `transaction.failed`, `audit.event_created`, `reconciliation.updated`.

Public contracts must not publish legacy audit event names, ledger entry event names, or legacy reconciliation entry event names.

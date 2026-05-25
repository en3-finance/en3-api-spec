# End-to-End Bank Stablecoin Wallet Scenario

This is the canonical public scenario for En3 public artifacts. Downstream SDK, reference-bank, admin, web, and mobile examples should use this model and vocabulary instead of inventing their own.

## Flow

1. A bank customer exists in mock core banking.
2. The bank creates an En3 sandbox user and wallet.
3. En3 issues a deposit address.
4. A stablecoin deposit is detected and reflected in mock balance state.
5. The customer submits an outgoing payment.
6. The transaction is simulated.
7. A sandbox policy/risk check requires approval.
8. An operations admin approves the transaction.
9. The transaction is broadcast and settled in sandbox state.
10. A reconciliation report is updated.
11. Audit events record the lifecycle.
12. Webhooks notify the partner backend.

## Canonical States

- `submitted`
- `simulated`
- `requires_approval`
- `approved`
- `broadcast`
- `settled`
- `failed`

## Canonical Events

- `wallet.created`
- `address.created`
- `transaction.submitted`
- `transaction.simulated`
- `transaction.requires_approval`
- `transaction.approved`
- `transaction.broadcast`
- `transaction.settled`
- `transaction.failed`
- `risk.review_required`
- `reconciliation.report_updated`
- `audit.event_recorded`

## Boundary

This scenario is a public sandbox/reference artifact. Production signing, production custody, production policy enforcement, risk logic, ledger infrastructure, treasury execution, customer deployments, and real infrastructure details are private by design.

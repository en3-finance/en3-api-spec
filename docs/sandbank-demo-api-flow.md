# SandBank Demo API Flow

Status: public reference / sandbox artifact. This repository is intended to document and demonstrate the En3 integration surface. Production cryptography, signing orchestration, policy enforcement, risk logic, ledger infrastructure, treasury execution, and customer deployments are private by design.

SandBank is a fictional, synthetic sandbox scenario.

## Flow

1. Create an organization with `POST /organizations`.
2. Create a user with `POST /users`.
3. Create a wallet with `POST /wallets`.
4. Read wallet state with `GET /wallets/{walletId}`.
5. Issue a synthetic address with `POST /wallets/{walletId}/addresses`.
6. Create a policy with `POST /policies`.
7. Register a webhook endpoint with `POST /webhook-endpoints`.
8. Submit a transaction intent with `POST /transactions`.
9. Simulate it with `POST /transactions/{transactionId}/simulate`.
10. Approve it with `POST /transactions/{transactionId}/approve` when the simulation returns `requires_approval`.
11. Read audit trail entries with `GET /audit-events`.

The public platform contract currently exposes reconciliation as webhook/reference state, not as a REST report retrieval endpoint.

## Examples

SandBank fixtures live under `examples/sandbank/` and use synthetic IDs such as `org_sandbox_000001`, `wal_sandbox_000001`, and `txn_sandbox_000001`.

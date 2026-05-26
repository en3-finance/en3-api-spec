# API Design Principles

Status: public reference / sandbox artifact. This repository is intended to document and demonstrate the En3 integration surface. Production cryptography, signing orchestration, policy enforcement, risk logic, ledger infrastructure, treasury execution, and customer deployments are private by design.

The public En3 API contract is a sandbox artifact. It describes integration shape without publishing production internals.

## Principles

- API-first resources for organizations, users, wallets, addresses, transactions, simulations, approvals, policies, audit events, and webhooks.
- Idempotent create and submit operations should use partner-provided references where practical.
- Webhook delivery should be idempotent and replay-tolerant.
- Transactions should support simulation before approval or execution.
- Policy and approval states should be visible to integrators without exposing enforcement internals.
- Audit events should provide lifecycle visibility without exposing sensitive operational detail.

## Non-Goals

- No production signing implementation.
- No production ledger implementation.
- No risk scoring rules.
- No treasury execution.
- No deployment configuration.

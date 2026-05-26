# Feature Specification: SandBank Demo Public API Contracts

Status: public reference / sandbox artifact. This repository is intended to document and demonstrate the En3 integration surface. Production cryptography, signing orchestration, policy enforcement, risk logic, ledger infrastructure, treasury execution, and customer deployments are private by design.

## User Story

As an integration engineer, I can use this repository as the public source of truth for En3 sandbox REST and webhook contracts using the fictional SandBank demo.

## Scope

- REST API contract in `openapi/en3-wallet-api.yaml`.
- Webhook contract in `asyncapi/en3-webhooks.yaml`.
- SandBank examples under `examples/sandbank/`.
- Public docs for API flow, webhook signatures, transaction lifecycle, and public/private boundary.

## Functional Requirements

- The REST contract exposes organization, user, wallet, address, transaction, simulation, approval, audit event, policy, and webhook endpoint operations supported by the public contract export.
- The REST contract does not expose reconciliation report retrieval unless the public platform contract supports it.
- The webhook contract exposes only canonical public events from the public export.
- Examples use deterministic synthetic IDs and contain no production endpoints, secrets, private business context, or implementation internals.
- Docs repeat the public boundary statement and map to actual/planned sandbox behavior.

## Acceptance Criteria

- JSON examples parse.
- OpenAPI and AsyncAPI YAML parse.
- Canonical statuses and public events match `../en3-platform/contracts/public`.
- Forbidden event names are absent from public files.
- Public files pass a lightweight scan for forbidden private terms and secret-like values.

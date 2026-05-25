# En3 API Spec

Status: public reference / sandbox artifact. This repository is intended to document and demonstrate the En3 integration surface. Production cryptography, signing orchestration, policy enforcement, risk logic, ledger infrastructure, treasury execution, and customer deployments are private by design.

## What This Repo Is

`en3-api-spec` contains OpenAPI, AsyncAPI, webhook schemas, mock examples, and sandbox contracts for the public En3 Wallet-as-a-Service integration surface.

## Who It Is For

This repo is for partner engineers, banks, fintechs, payment providers, reference-app builders, and diligence teams that need to understand how En3 APIs could be integrated.

## What It Demonstrates

- API-first wallet integration model.
- Wallet, address, transaction, simulation, approval, policy, audit, and webhook resources.
- Webhook event names and payload conventions.
- Mock stablecoin payment and control-plane lifecycle.
- One canonical end-to-end scenario: bank customer wallet -> deposit address -> outgoing payment -> policy/risk check -> approval -> settlement -> reconciliation -> audit trail.

## Intentionally Out Of Scope

This repo does not contain production cryptography, signing orchestration, policy enforcement, ledger infrastructure, risk logic, treasury execution, customer deployments, real compliance vendor integrations, private endpoints, or production secrets.

## Contents

- `openapi/en3-wallet-api.yaml` - sandbox REST API contract.
- `asyncapi/en3-webhooks.yaml` - webhook event contract.
- `examples/` - mock request and event payloads.
- `docs/api-design-principles.md` - public API design notes.
- `docs/end-to-end-bank-wallet-scenario.md` - canonical public scenario.
- `docs/webhook-signatures.md` - sandbox webhook signature boundary.

## Related En3 Repositories

- `en3-docs`
- `en3-wallet-sdk`
- `en3-admin-console`
- `en3-reference-bank`
- `en3-web-wallet`
- `en3-mobile-wallet`
- `en3-chain-integrations`

# Solution build plan — [business outcome]

> Design/delivery record, not a Copilot Studio or Power Automate native import artifact.
> Keep in the **business project**, not inside the installed skill.

## Outcome contract

- User/job and business problem:
- Trigger/cadence and freshness target:
- Inputs, source owners and permission:
- Action and destination:
- Baseline -> target KPI:
- Volume, latency, capacity, sensitivity:
- Demo acceptance (happy / empty / failure):

## Chosen architecture

- Baseline considered:
- Recommended approach and rationale:
- Harness evidence for each agent:
- Alternatives rejected and why:
- Estimated credits/cost assumptions and measurement plan:

## Workflow diagram design

- Editable architecture/build Mermaid: `docs/diagrams/workflow.md` (project-relative)
- Editable runtime Mermaid: same file; show trigger, empty/duplicate/failure and delivery checks
- Diagram status: PROPOSED / VERIFIED AGAINST DESIGNER / VERIFIED AGAINST TENANT RUN
- Unbound connector and tenant steps visibly labeled:
- Architecture/diagram change linked to test and build-sheet update:

These Markdown diagrams render in GitHub; they are not executable workflows.
See [diagram-design guide](../references/diagram-design.md) for conventions.

## Component and capability ledger

| Component | Runtime / design surface | Input -> output | Build method | Capability evidence | Status | Owner/blocker |
|---|---|---|---|---|---|---|
| Ingestion | | | | | DESIGNED | |
| Normalize/dedup | | | | | DESIGNED | |
| AI reasoning | | | | | DESIGNED | |
| Persistence (optional) | | | | | DESIGNED | |
| Notification | | | | | DESIGNED | |

Statuses: DESIGNED / GENERATED / LOCAL_VALIDATED / SYNCED / PROVISIONED /
PUBLISHED / TENANT_TESTED / BLOCKED / FAILED. The whole chain is UNVERIFIED
until data and effects are seen end-to-end.

## Handoff contracts

- Business key and correlation ID:
- Schema/version, source/time/provenance:
- Identity and authorized data scope:
- Error, retry, timeout and dedup policy:
- Completion/read-back evidence:
- Connector/DLP/license/endpoint/billing checks:
- Explicit unbound fields (UNBOUND):

## Workflow designer build sheet (when automation is unavailable)

| Order | Trigger / action | Data mapping / expression | Connection and authorization | Failure branch | Evidence |
|---|---|---|---|---|---|
| 1 | | | UNBOUND | | |
| 2 | | | UNBOUND | | |
| 3 | | | UNBOUND | | |

Never substitute this sheet or loose flow JSON for a publishable solution.

## Verification

| Case | Expected result | Local evidence | Tenant evidence | Outcome |
|---|---|---|---|---|
| Normal relevant event | | | | pending |
| Empty/no news | | | | pending |
| Duplicate poll | | | | pending |
| Source/tool error | | | | pending |
| Unauthorized action | | | | pending |
| Teams send/retry | | | | pending |

## Release and value

- Files generated and actual commands:
- Sync/provision/publish IDs and verification (if performed):
- Trigger -> analysis -> persist -> message observed?:
- Precision, missed events, p50/p95 latency, cost per useful outcome:
- Exact remaining binding/approval step and owner:

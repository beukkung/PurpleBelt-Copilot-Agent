# SharePoint blueprint: <business outcome>

Design proposal; replace assumptions with actual metadata/evidence before provisioning.

## Outcome and constraints

Users/jobs: <who needs to find, review, create, approve or retrieve what.>

Success: <task time, completeness, error rate, discovery/adoption or freshness.>

Current site/export: <observed reference or unknown; do not invent a binding.>

Constraints: <Online/Server version, volume/growth/bursts, classification,
security boundaries, retention, identity, connectors/DLP and permitted tools.>

Recommendation: <minimal viable structure and why SharePoint is appropriate.>

## Container map

| Site / List / Library | Existing or proposed | Purpose and owner | Key / document link | Lifecycle | Security scope |
|---|---|---|---|---|---|
| | | | | | |

Relationships: <business keys, document references and enforced versus advisory rules.>

## Data dictionary (repeat per container)

| Display label | Internal name: proposed/observed | Type | Required / default / validation | Unique / index + rationale | Sensitivity / source / owner |
|---|---|---|---|---|---|
| | | | | | |

Built-in fields used: <actual IDs, timestamps, author/editor or version fields.>

Content types/site columns: <reuse when justified; exact term IDs remain pending.>

Nulls, choices, timezone/currency and changes: <rules plus migration implications.>

## Queries and views

| User/tool and purpose | Scope / server-side filter / sort | Projection / paging | Supporting index | Expected matches / growth | Evidence / unknowns |
|---|---|---|---|---|---|
| | | | | | |

Threshold/burst/retention plan: <bounded queries, archive, quotas and recovery capacity.>

## Permissions

| Principal/role | Managed by | Container / scope | Permission level / inheritance | Agent/workflow identity | Denied-access test |
|---|---|---|---|---|---|
| | | | | | |

Sharing/unique-scope plan: <group ownership, policy, expected scope growth and audit.>

## User experience

Home/navigation: <user tasks, page labels, native web parts, next actions and owner.>

Forms/views: <required metadata, empty/error states, mobile/accessibility.>

Formatting artifacts: <target column/view, actual field names, schema, preview evidence.>

## Integrations and lifecycle

| Producer/consumer | Permitted operation or trigger | Identity and data scope | Input/output and freshness | Completion / idempotency / recovery | Evidence |
|---|---|---|---|---|---|
| | | | | | |

Document/record lifecycle: <draft/review/approved, versioning, retention and owner.>

Async work if needed: <ready signal, claim, attempt/lease, states, result/error,
replay, duplicate effects and reconciliation; state limitations explicitly.>

## Implementation and acceptance

Provisioning route: <native manual setup, site script or permitted existing tool.>

Prerequisites: <target, rights, verified tool/schema and real bindings.>

Steps: <containers -> columns/content types -> permissions -> indexes/views ->
forms/formatting -> integrations -> pilot; flag migrations and access changes.>

Rollback/cutover: <preserve existing content/IDs and reconcile dependencies.>

Tests: <roles, data rules, queries, realistic volume, triggers, UI and recovery.>

Evidence: <design / generated / provisioned / tenant-tested; list pending gates.>

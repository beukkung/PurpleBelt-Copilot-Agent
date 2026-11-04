# Design SharePoint around the work people need to finish

Use for SharePoint Online sites, Lists, Document Libraries, metadata, views,
pages, permissions or the storage layer of an agent/workflow. For Server/on-prem,
identify the exact version first; do not assume Online features or schemas apply.
Pure design can proceed without a cloned Copilot Studio workspace or tenant access.

## Contents

- [Users and constraints](#1-discover-users-content-and-constraints)
- [Containers and information architecture](#2-pick-containers-and-information-architecture)
- [Data dictionary](#3-define-the-data-dictionary-and-relationships)
- [Queries, views and growth](#4-design-queries-views-and-growth-together)
- [Permissions and identity](#5-plan-permissions-and-agent-identity)
- [Native user experience](#6-give-users-a-clear-native-experience)
- [Agent/workflow integrations](#7-connect-storage-to-agents-and-workflows)
- [Blueprint and implementation](#8-deliver-a-blueprint-then-an-implementation-handoff)

## 1. Discover users, content and constraints

Inspect existing site/list/library metadata or a sanitized export when available.
Record user jobs, owners, audiences, source of truth, classification, retention,
volume/growth/bursts, access boundaries, search/freshness needs and permitted
administration tools. Distinguish existing resources from proposed resources.
An internal name, site URL, list ID or term ID is a real binding only when observed.

Ask only for facts that change a dependent decision. Continue a blueprint with
explicit assumptions. Evaluate whether SharePoint fits: collaboration, document
lifecycle and moderate structured operations are different from transactional
ledgers, large analytical joins or high-throughput queues. Compare an approved
alternative when requirements exceed demonstrated limits; do not introduce a
premium backend simply to complete a diagram.

## 2. Pick containers and information architecture

| Need | Start with | Check before choosing |
|---|---|---|
| Team collaboration and operations | Existing appropriate Team site | Microsoft 365 group/Teams ownership and permissions |
| Broad publication with a smaller author group | Communication site | Author/publisher roles and audience navigation |
| Document versions, review and metadata | Document Library | Content types, versioning, required metadata and retention |
| Cases, configuration, work items or states | List | Typed fields, queries, relationships, growth and access |
| Distinct confidentiality boundary | Separate secured site/library as justified | Existing access inheritance and actual principal membership |

Use one small coherent site structure rather than creating a site per entity.
Split by lifecycle/security/ownership when it justifies the operational cost.
Use reusable site columns/content types when multiple containers need the same
meaning; avoid elaborate taxonomy for a single small list. Metadata and folders
can coexist: choose folders for meaningful grouping or an intentional permission
boundary, not a deep tree that replaces useful metadata.

Recommend documents in a library when they need document lifecycle features;
use list attachments only when they fit the simpler requirement. Link business
records to documents using stable keys/references. A list ID is scoped to its
container; it is not a portable business key across environments.

## 3. Define the data dictionary and relationships

For each field specify display label, proposed/observed internal name, SharePoint
type, required/default, choices or term source, validation, null behavior, uniqueness,
index rationale, sensitivity, source/owner and consumer. Record built-in fields
separately. Prefer concise stable ASCII internal names for new automation-facing
columns and localized display names; preserve real existing internal names,
including encoded names. Renaming a label does not establish a new internal name.

Choose Single line, Multiple lines, Choice, Number, Currency, Date/Time, Yes/No,
Person/Group, Lookup or Managed Metadata from actual semantics and supported
operations. Do not use strings for every value or add a custom `ID` over the
built-in identifier. Define timezone/UTC handling, amount precision, choice
changes, defaults, field-length and malformed-input rules. Lookups/taxonomy and
multi-value fields need connector query/output evidence; they are not free joins.

Use supported unique constraints where justified and check the chosen field type.
Cross-list relationships do not create a transactional database. Mark business
uniqueness or referential rules that require workflow validation or another
backend. Keep high-churn job state separate from stable business/document data
when ownership, retention or throughput differs. Label any example schema as a
proposal until the site has created and returned its actual metadata.

## 4. Design queries, views and growth together

Write each access pattern before choosing indexes: caller/identity, server-side
predicate, projected columns, sort, page size, pagination strategy, expected
matches at launch and projected growth. Include operational views such as My
work, Ready, Failed/retry, Recent and By department only when a user needs them.
An indexed low-cardinality Status/Department can still select too many records.

The **5,000-item List View Threshold is not the maximum list capacity**. Plan
selective indexed filters, bounded query windows and retention/archive before
growth. Pagination is needed for completeness but does not bypass query-threshold
or lookup limits. An indexed Lookup alone does not avoid the threshold. Validate
real connector operations, supported filter types, pagination and throttling with
representative volume; a small fixture is not scale evidence.

Balance indexes with write overhead. Avoid broad lookup-heavy views, full-list
scans and client-side filtering for restricted data. Evaluate rollover/archival
and recovery backlog before adding another list per period. For job queues,
inherit the claims, leases, output idempotency and recovery contract from
`hybrid-architecture.md`; do not advertise exactly-once or queue-grade throughput
without evidence.

## 5. Plan permissions and agent identity

Create a matrix for business owners, contributors, reviewers, readers and workflow/
agent principals. Record site/library/list scope, permission level, inheritance,
sharing policy and the authority that manages membership. Protect job records,
audit logs and result links too: a restricted document's title, excerpt or analysis
can leak through a broadly readable operational list even if the file itself is secured. Team/group-connected
sites should use their established group model; private/shared channel site
permissions are managed through Teams. Do not propose independent SharePoint
membership edits for those channel sites.

Views, audience targeting, JSON formatting and instructions are presentation,
not authorization. Validate denied access through direct links, native APIs and
the actual agent/flow identity. A service-owned flow's Created By value may be
the service identity; a "created by me" view is not a department privacy rule.
Service-account retrieval must not expose data beyond the requesting user's
authorized scope. Knowledge indexing/permission changes need actual retrieval
tests; new content is not necessarily indexed immediately.

Prefer inherited group-based scopes to unique permissions on every item. The
current documented supported maximum is **50,000 unique scopes** per list/library,
with **5,000** the general recommendation; those are permission scopes, not file
counts or design targets. Plan access boundaries before growth and monitor scope
count. Shared folder inheritance can be useful, but moving existing uniquely
shared items does not automatically clean their scopes. Require a reviewed access
change plan before breaking inheritance or widening access.

## 6. Give users a clear native experience

Specify each page's job, key next action, owner and native web parts. A practical
operations home can expose task-focused links, filtered work lists, document
libraries and guidance. Map navigation labels to users' language. Prefer native
forms/views first; choose Power Apps or SPFx only when necessary and confirmed
permitted. Never assume an app catalog, package installation or PnP tool is allowed.

When useful, generate column/view JSON against the current official schema and
actual internal names. Use semantic labels/icons alongside color, readable
contrast and small/mobile layouts. Formatting JSON changes display, not stored
data, validation rules or permissions; an action button still requires its real
supported operation, identity and authorization. No arbitrary JavaScript/HTML.
The sample at `<builder-root>/assets/sharepoint-status-format.example.json` is
column formatting for a proposed state field, not a whole site or provisioner.

## 7. Connect storage to agents and workflows

Map each consumer to its exact permitted connector operation, input/output,
identity, filter, projection, trigger and version contract. For metadata-only file
triggers, retrieve content separately before analysis. Distinguish create versus
modify triggers; required metadata completion/ready state should precede processing.
Prevent recursive updates and duplicate effects. Fetch structured current values
directly when the freshness target cannot tolerate a knowledge-index delay.

For cross-harness designs read `hybrid-architecture.md`; approval of SharePoint
does not prove that the consumer trigger, Agent node or combined DLP path works.
Apply backend-enforced business/access checks before tools mutate state, and
reconcile a timed-out write before retrying. Versioning is useful recovery
evidence but is not a replacement for retention/backup/records policy.

## 8. Deliver a blueprint, then an implementation handoff

Fill `<builder-root>/assets/sharepoint-blueprint-template.md` in the business
project. Include the container map, data dictionary, permission matrix, query/view
plan, user-facing layout, lifecycle, integration contracts, provisioning route and
acceptance cases. Add a small synthetic example when it makes fields concrete.
Clearly label design, generated artifacts, provisioned objects and tenant-tested
behavior as separate evidence states.

Choose the actual implementation surface: manual native setup, supported site
scripts/templates, or an existing permitted administration/API tool. SharePoint
site-script JSON and formatting JSON are different formats. Verify the current
schema, verbs, tooling and permissions before generating executable provisioning
steps. Prefer exporting inspected existing structures when supported. A blueprint,
CSV, SQL DDL or formatting JSON does not itself create a working SharePoint site.
Do not claim a generic CSV import provisions types, indexes, views or permissions.

For existing sites, inspect dependencies and plan additive migration/backfill,
validation, cutover and rollback. Preserve real IDs, internal names, versions and
user content; do not replace a list or change field types to force a draft design.
Creation requires the actual target and permissions, not just an agent extension.
Never run tenant-wide setup, grants, destructive changes or broad migration as a
side effect of a design request.

Test: missing/invalid metadata, duplicate business keys, date/amount rules,
allowed/denied roles, actual automation identity, query completeness past a first
page, realistic threshold/burst behavior, documents/versions, metadata readiness,
trigger replay/loops, recovery and formatting in the native UI. Record what was
actually checked; parsing JSON does not prove SharePoint schema or UI acceptance.

## Official references (checked 2026-11-04)

- [Information architecture](https://learn.microsoft.com/en-us/sharepoint/information-architecture-modern-experience)
- [Permissions](https://learn.microsoft.com/en-us/sharepoint/modern-experience-sharing-permissions)
- [Permission scopes](https://learn.microsoft.com/en-us/sharepoint/manage-permission-scope)
- [Column indexing](https://support.microsoft.com/en-us/sharepoint/data-and-lists/add-an-index-to-a-list-or-library-column)
- [Large-list filtering](https://learn.microsoft.com/en-us/troubleshoot/sharepoint/lists-and-libraries/fails-filtering-sharepoint-column)
- [Column formatting](https://learn.microsoft.com/en-us/sharepoint/dev/declarative-customization/column-formatting)
- [View formatting](https://learn.microsoft.com/en-us/sharepoint/dev/declarative-customization/view-formatting)
- [Site templates/scripts](https://learn.microsoft.com/en-us/sharepoint/dev/declarative-customization/site-design-overview)
- [Connector actions/triggers](https://learn.microsoft.com/en-us/sharepoint/dev/business-apps/power-automate/sharepoint-connector-actions-triggers)

Recheck version-sensitive limits, schemas, operations and tenant policy before
implementation. The design recommendations above are a synthesis, not a tested
tenant-specific provisioning package.

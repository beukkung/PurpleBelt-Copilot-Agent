# One-Prompt Solution Builder — orchestration protocol

Use when a user asks GitHub Copilot in VS Code to turn **one business request into a working multi-component solution**, such as scheduled news ingestion -> AI analysis -> SharePoint history -> Microsoft Teams notification. This is a development-time orchestrator, **not** a new Microsoft cloud service, a runtime skill or an unattended deployment guarantee.

Read `hybrid-architecture.md`, `workflows.md`, `harness-routing.md` and relevant harness guides on demand. Keep execution within the user's approved environment and tools. This skill is designed to reduce *manual component construction*, not hide explicit authentication or publication gates.

## 0. Execution contract: one request, continuous progress

- Convert the user's prompt into a compact **solution contract**: business user, measurable outcome, trigger and freshness, sources and permission, transformed data, reasoning requirement, expected effects, destination, volume, SLA, budget, sensitive-data handling and acceptance cases.
- Inspect actual workspace, installed extension/CLI versions and available agents/flows/sites. Existing files and authorizations take priority over guesses. Discover the harness **per agent**, not by the VS Code extension.
- Default to the smallest reversible vertical slice. Ask only when an absent **essential** target or permission prevents the next dependent side effect; otherwise continue local drafts, tests and specifications without repeated confirmations.
- Choose at most three architectures including the least complex baseline; recommend one. Do not create two harnesses, a separate agent, SharePoint storage or external APIs unless their value is justified.
- Keep an **execution ledger** and update status per component. Do not stop after generating an architecture plan if authorized build/test actions are possible. Continue: inspect -> plan -> generate -> validate -> connect (if possible) -> test -> publish (when authorized) -> verify -> report.
- Never use non-approved services, personal credentials, proxies or fake connection references to bypass tenant DLP, licensing, egress or policy restrictions. Never put secrets, access tokens or personal financial data into a repository, fixture, prompt log or Teams demo message.

## 1. Choose the build surface by capability, not by marketing label

| Component | Preferred generation/authoring path | What remains gated |
|---|---|---|
| Standard Copilot Studio agent | Existing real Standard workspace + pinned `mcs-*` skills; extension clone/edit/apply and native validation | A new tenant agent may need Studio setup, actual connector binding and explicit publish |
| Microsoft Copilot harness agent | Pinned `mcsa-*` skill, verified `pac` help/version/auth, correct environment and CLI-agent workspace | Cloud init, sync, publication and channel testing are **distinct** operations; CLI support is version-dependent |
| Modern Copilot Studio Workflow (with inline Agent node if useful) | Supported **Studio Workflow designer**; VS Code may prepare prompts, logic, schemas, fixtures and a designer-ready build sheet | This bundle does **not** prove an API/CLI that provisions the entire modern Workflow canvas from VS Code |
| Standard agent flow / Power Automate cloud flow | Tenant-approved designer, verified export/solution tooling or configured permitted flow authoring tools; natural-language Copilot in its supported designer when available | Connection consent, action/trigger configuration and import/binding; a raw JSON draft is not a deployable solution ZIP |
| SharePoint sites/lists/libraries | Read `sharepoint-design.md`; prepare blueprint, column/view-format JSON, schema and permissions | Provision only through a tested, authorized supported API/tool; formatting JSON is not a list/site provisioner |
| Teams delivery | Real approved Teams connector in the **selected** workflow/flow with exact channel or chat destination | Connection identity, channel rights, DLP, real delivery and deduplication evidence |

**Important distinctions (verify current tenant and product documentation):**
- A modern **Workflow Agent node** can call a published compatible agent or configure an **inline agent**. Inline scope suits workflow-specific reasoning; reuse as a shared conversational agent requires a separate published agent. It does not mean a VS Code extension can serialize/push the whole Workflow canvas.
- Microsoft documents **natural-language authoring for agent flows** in the supported Studio designer, while that feature does **not** author the modern Workflow experience. Power Automate cloud-flow Copilot is another designer-specific route. Do not say they are interchangeable or silently use an external-model authoring feature without policy approval.
- The Power Automate **Copilot Studio connector** is documented for published Standard-harness agents, **not** as a generic way to call modern-harness agents. Verify the exact invocation before designing cross-harness handoffs.
- Agentic Builder Preview or product demos do not establish programmatic creation from VS Code. Verify installed tooling and supported commands **before** claiming provisioning.

Official references (recheck before use):
- [Workflow overview](https://learn.microsoft.com/en-us/microsoft-copilot-studio/workflows-experience/flows-overview)
- [Workflow Agent node](https://learn.microsoft.com/en-us/microsoft-copilot-studio/workflows-experience/agent-node-workflow)
- [Agent-flow natural language authoring and limitations](https://learn.microsoft.com/en-us/microsoft-copilot-studio/flow-nl)
- [Cloud-flow Copilot authoring](https://learn.microsoft.com/en-us/power-automate/create-cloud-flow-using-copilot)
- [Workflow as modern agent tool](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/tools-add-workflow)

## 2. Plan the execution graph once; then build by dependency

Create `solution-build-plan.md` **inside the business project**, using `<builder-root>/assets/one-prompt-solution-template.md`. It is a project artifact, not a runtime workflow.

Build graph: **sources -> normalization -> dedup/business rules -> evidence -> bounded prompt or agent -> guardrail -> persistent state (optional) -> notification -> observed result**. For each node record: runtime/surface, owner, typed inputs/outputs, connection identity, supported invocation boundary, deploy method, cost/billing, status and verification evidence.

Prioritize:
1. One demo-able path with a synthetic fixture and an observable output.
2. Source provenance/freshness and failure/empty paths.
3. Idempotent side effects, permissions, notification reliability and live tests.
4. Extra personalization, additional agents and polish only after the main path works.

For scheduled external-news solutions, require: allowed provider/API and rate limits; published vs ingested timestamp; stable story ID or canonical URL; dedup across repeated polls; source references; stale/unverified-news handling; bounded token/credit use; portfolio data scoping; a suppression/escalation policy; and one notification decision per business key. Never call a snapshot 'real-time' or present news-derived financial predictions as facts.

## 3. Build autonomously *within* supported boundaries

1. Inventory existing authorized resources before creating new ones. Preserve user edits, IDs, solution layers and cloud state; inspect drift before applying changes.
2. Generate type-safe contracts, fixture payloads, deterministic logic, prompt/instructions, tests and any **verified native** agent artifacts. Call relevant pinned Microsoft operation skills for agent work.
3. If an actual permitted workflow authoring interface is available, create or update the workflow **there** and capture its ID, test run and bindings. If it is unavailable, generate a **designer-ready build sheet**: exact trigger, chronological actions, conditions, inputs/outputs, connection placeholders clearly marked `UNBOUND`, tests and operator steps. Do **not** fabricate import-ready packages, PAC commands or native Workflow YAML/JSON.
4. Create SharePoint configuration only via supported tools/identity; otherwise generate a field/permission blueprint with template-backed payloads and `NOT_PROVISIONED` status.
5. Keep human choices to consequential writes: specify target environment/channel and request approval before production sends, live resource creation or publication when not already authorized. Local fixture builds and read-only validation should proceed without unnecessary interruption.
6. Bind existing tools through a verified operation and authorized principal. A SharePoint event is not a universal workflow trigger; a created file is not proof of a downstream run. No secrets in files.
7. Repeat native validation and test the changed component, then test the end-to-end path with real trigger/auth/effects when available. Stop unsafe retries; reconcile uncertain effects first.

## 4. Verification and honest completion states

Record a status **separately for every component**. Allowed delivery statuses:
- `DESIGNED`: plan or blueprint only.
- `GENERATED`: inspectable artifacts exist; not necessarily importable.
- `LOCAL_VALIDATED`: named local checks passed, not cloud proof.
- `SYNCED`: a verified native apply/push occurred; not publication.
- `PROVISIONED`: actual resource observed in the target environment; not an end-to-end test.
- `PUBLISHED`: published in the target; does not prove successful delivery.
- `TENANT_TESTED`: actual connected test and effects observed.
- `BLOCKED`: missing verified prerequisite, permission or tool.
- `FAILED`: attempted operation failed; include evidence and safe recovery.

Never promote a component above the evidence available. Show cross-component integration as `UNVERIFIED` until its data handoff and completion effect are observed, even if each component exists. Differentiate trigger fired, agent responded, record written and Teams message delivered. A command exit code alone does not establish business success.

Test at least: normal relevant news, no news, duplicate poll, modified article, malformed feed, source outage, denied connector, stale evidence, AI uncertainty, Teams delivery failure and replay after timeout. Make retries idempotent where the backend supports enforcement; lookup-before-send is not globally atomic.

Measure the **business outcome**: relevant alerts delivered, precision of relevant/impactful alerts, missed important news, source-to-alert latency (p50/p95), duplicate notifications, operator recovery and credits/cost per useful alert. Quality and grounded explanation matter more than number of generated components.

## 5. Required final handoff (no 'all done' without proof)

Return one compact **Solution Delivery Report**:
1. Architecture selected and why; business outcome and acceptance target.
2. Component matrix: name, runtime, path/URL, build status, evidence, blocker/owner.
3. Files actually changed and commands/tools actually executed; separate local, native, tenant and published-channel tests.
4. Actual connection/permission/publication gates and **one actionable next step**. Include a designer-ready workflow guide if native programmatic authoring is unavailable.
5. Measured impact versus targets; mark missing measurements as pending rather than invented.

Do not silently downgrade a user request from 'build' to 'architecture only'. Deliver everything that can genuinely be generated/tested now; explain exactly which remaining steps cannot be automated from the available VS Code toolchain.

# Plan the whole system, then choose each runtime

Use for multi-step business automation, cost/latency optimization, mixed harnesses,
event-driven processing, or a request to build both agents and workflows. A local
workspace's harness identifies that component, not the best architecture for the
entire system. Hybrid is an option, not a requirement to deploy two agents.

## 1. Define the outcome and constraints

Read existing project instructions and actual resources first. Record volume,
burst rate, freshness/latency target, output, correctness target, sensitive data,
identity, approved ingress, connector/DLP constraints, available runtimes and
budget. Mark missing numbers as assumptions. Proceed with independent design
and fixtures; resolve missing identities/bindings before dependent cloud actions.
Define where the freshness clock starts (source publication or internal ingestion)
and whether the SLA covers first notification or completed analysis. Check burst
load, backpressure, pagination/indexing, retention and recovery throughput; an
average daily rate is not capacity proof.

Decompose into ingest, normalize, deduplicate, retrieve, decide, reason, review,
act, persist and notify as applicable. Choose the least expensive sufficient
mechanism for each stage: deterministic rules, a bounded model transformation,
or agent reasoning. A classification task does not automatically need a reasoning
agent. Prompt arithmetic does not replace deterministic business calculations.

## 2. Compare architectures before coding

Explore reasonable alternatives and present at most three material candidates,
including a simple single-runtime baseline. Pick one and explain the tradeoff.
Do not generate a catalog of every integration or accept the user's proposed
transport without checking whether it solves the real problem.

| Candidate family | When useful | Main tradeoff |
|---|---|---|
| One deterministic flow, with a bounded prompt only if needed | Known sequence, little adaptive work | Small component count; limited adaptive analysis |
| One modern workflow with gated agent nodes and deterministic steps | Need conditional reasoning and a synchronous result | Supported native orchestration; modern workflow billing still applies |
| Separate producer/consumer joined by approved durable state/events | Bursts, long analysis, replay/recovery or separate owners | Decoupling and observability; more state, latency and failure modes |

These are families, not fixed templates. Alternatives include sharing a verified
reusable tool/workflow across independently useful agents; scheduled bounded
batch processing; or an approved documented API invocation when its exact target,
auth and policy are confirmed. A queue/service is a candidate only when already
permitted and licensed. Do not add premium HTTP, an external MCP, a personal
account or a proxy to route around restrictions. A single SharePoint list record
can be enough; files are useful for actual document payloads, not mandatory glue.

Add a Standard conversational agent only when users need its topics/control or
an existing agent has a justified role. Do not put two agents on every request
just to call the solution hybrid. Modern workflows also contain deterministic
steps; Standard agents can also invoke models. Neither label proves low cost.
A supported Standard-agent or bounded-prompt path can be the baseline for analysis
when it meets the same quality criteria. A task called "deep" is not evidence
that the most capable model/runtime is necessary.
Runtime gates invoke separately configured components; they do not switch an
existing agent's harness or convert its schema on each request.

## 3. Verify every handoff

Use current official documentation, installed tooling and target evidence.
The following snapshot was checked **2026-11-04**; recheck before relying on it.

| Invocation | Documented boundary | Required proof |
|---|---|---|
| Power Automate cloud flow -> Microsoft Copilot Studio connector | Calls published **Standard** agents; does not support modern/GHCP agents | Correct agent, operation, connection, policy and observed response |
| Modern Copilot Studio workflow -> Agent node | Calls an existing published modern agent or an inline agent | Node availability, actual inputs, structured output and run evidence |
| Modern agent -> its configured service event trigger | SharePoint item, email or schedule examples; **Preview** | Trigger availability, connection, subscription, publish/activation and real event |
| Producer -> approved shared data -> consumer trigger | An asynchronous integration design, not direct agent delegation | Both connector operations allowed; event delivery, identity, input visibility and durable result |
| Direct Standard <-> modern connected-agent delegation | FAQ says unsupported | Do not generate it as an available integration |
| Generic HTTP, SDK or A2A invocation | Not a blanket substitute for the above | Exact endpoint/runtime compatibility, auth, documented support and policy |

Sources: [Power Automate invocation](https://learn.microsoft.com/en-us/power-automate/call-copilot-studio-agent),
[workflow Agent node](https://learn.microsoft.com/en-us/microsoft-copilot-studio/workflows-experience/agent-node-workflow),
[modern event triggers](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-add-event-trigger),
[cross-harness FAQ](https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/faqs-copilot-harness).

Keep support and readiness separate: documented-supported, preview, unsupported,
unknown; then configured/tested/pending in this tenant. One supported link does
not establish the whole chain. A file landing in SharePoint does not itself
activate a workflow, grant its identity access, or start an indexing refresh.
Trigger latency is measured; avoid promising streaming or immediate detection.
Knowledge indexing is not a job notification channel.
Metadata-only file triggers require a separate permitted content-read action
before analysis. Pass the actual retrieved bytes/text, not an assumed file body.

## 4. Specify a handoff contract

Define versioned input/output, business key, correlation ID, producer, consumer,
identity, data scope, transport, allowed effects, completion signal, timeout,
retry/reconciliation policy and owner. No shared conversational memory is implied.
Use `<builder-root>/assets/hybrid-architecture-template.md` for the compact
project artifact; save the filled plan in the business project, not this bundle.

For asynchronous work, model ready -> processing -> succeeded/failed, with
attempts, source version, lease/claim owner, expiry and result/error references
when needed. Publish a ready signal after its referenced input is complete.
Choose create-only events or explicit status-transition filters to prevent the
consumer's result update from triggering itself. Plan recovery for missed events,
partial uploads, permission failures, expired claims and abandoned work.

A business key and lookup-before-create alone do not provide exactly-once
execution. Require an atomic claim/unique constraint/conditional update supported
by the permitted backend, and independently protect consequential output effects.
If unavailable, limit to a single controlled consumer where applicable, disclose
remaining duplicate risk and use reconciliation; do not promise global uniqueness.
Treat replay as a possible repeat of sends/writes. Separate accepted, analyzed,
saved and notified states. Do not claim an asynchronous job already completed.

## 5. Bound reasoning and cost

Plan gates at design time. At runtime apply cheap observable rules before model
calls: duplicates, freshness, scope, changed source version and exact eligibility.
Escalate bounded transformations to agent reasoning only for defined complexity,
conflicting evidence or task failure. A model's self-reported confidence is not
calibrated routing evidence. Enforce stop, timeout and human-review/fallback paths.

Reduce approved data server-side before sending an evidence packet with stable
IDs, relevant fields, source times and provenance. Reuse cached results only when
identity/scope, source version, rules/prompt/model version and freshness permit.
Batch related items only within context/output budgets; preserve per-item outcome
and one item's failure isolation. Reconcile uncertain writes before retrying.

Record input/output/context limits, agent calls, tool calls, iterations, attempts,
timeouts and daily/run budget using controls actually available in the backend.
A number written in an instruction is not an enforced spending cap. Bound the
consumer/dispatcher even if a native per-agent control is unavailable, and report
the remaining exposure. Never assume a scheduled job with zero useful results
or a native modern workflow's non-AI steps is free without checking its meter.

Estimate the whole path with explicit units and dated rate assumptions:

`expected daily cost = deterministic flow/action cost + eligible runs *
measured cost per reasoning run + transfer/storage/notifications + retries`

Eligible runs depend on observed dedup/filter/cache/batch behavior, not invented
percentages. Token count is one driver, not the complete Copilot Credits bill.
Include authoring/testing/evaluation consumption where applicable. If rates or
tenant consumption are unknown, report a symbolic estimate/range with assumptions
and a measurement task; do not claim a saving. Compare cost per successful outcome,
quality and end-to-end latency rather than minimizing tokens alone.

## 6. Produce and verify a concrete plan

Deliver one compact architecture artifact in the business project:

1. Recommendation, assumptions, up to three candidates and tradeoffs.
2. Stage map: owner, implementation surface/runtime, input/output, reasoning level.
3. Handoff ledger with support/readiness evidence and unresolved bindings.
4. Observable gates, enforceable budgets, cache/batch policy and failure recovery.
5. Cost model, acceptance cases and pilot measurements with pass/fail criteria.

Then implement the smallest vertical slice in dependency order: data contracts,
permitted components, verified handoff, reasoning, effects and channel. Keep each
harness in its own correctly bound workspace. Use existing routes before adding
infrastructure. Work on both agent and workflow when authorized and prerequisites
exist; explicitly hand off unsupported authoring steps instead of fabricating
native workflow YAML, deployment commands or import readiness.

Pilot the baseline and chosen alternative on the same labeled representative
inputs (including no-news, duplicate, changed source, timeout, denied access,
replayed event and failure after notification). Measure eligible invocations,
credits, accepted-result rate, p50/p95 end-to-end latency, duplicate effects and
manual recovery. Report static checks, fixtures, real trigger/runtime evidence
and published-channel evidence separately. Change the architecture when evidence
disproves its cost, latency or reliability assumptions.
Evaluate the routing gate too: measure missed relevant/high-impact cases and
incorrectly suppressed revisions, not just fewer reasoning invocations. Use the
same identity/data scope and output criteria for fair cost comparisons.

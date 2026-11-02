# Debugging and evidence

## Diagnose from facts

Capture sanitized input, version, expected/observed outcome, channel, environment
and identity. Establish a failing case before a fix. For flows: run -> nested
action -> actual inputs/outputs -> definition -> upstream data. Inspect relevant
loop iterations. Multiple branches can fail; the last failed item is not always
the sole cause. `ActionFailed` is a wrapper rather than a diagnosis.

For routing inspect orchestration, model descriptions, trigger phrases, overlapping
tools and interruptions. For SharePoint inspect operation inputs, dynamic schema,
logical references, auth and pagination. Rebind components only after inspecting
dependencies; preserve a rollback diff and re-test the affected layers.

## Evidence ledger

Record timestamp, commit/export, operation/command, case, expected and observed
result, evidence level, pass/fail/pending and sanitized artifact location. Store
concise decisions and evidence, never credentials or private chain-of-thought.

| Layer | Example | Does not establish |
|---|---|---|
| Static preflight | YAML parse, duplicate IDs | Microsoft schema, Power Fx, DLP |
| Native diagnostics | Extension/LSP results | Actual business effects |
| Fixtures | Tested local cases | Authenticated tenant behavior |
| Connected tenant | Actual tools and correct records | Published-channel behavior |
| Published channel | Real UX and effect evidence | Every user/case or production readiness |

## Representative cases

1. Happy path: correct tools, arguments, data scope and supported result.
2. Missing input/record: ask or return not_found; no accidental writes.
3. Multiple matches: disambiguate rather than select arbitrarily.
4. Unauthorized user: no prohibited retrieval/mutation.
5. Tool failure/timeout: controlled state, reconcile uncertain writes.
6. Malformed model output: reject schema mismatch; no default success.
7. Duplicate/concurrent requests: one logical operation and existing state returned.
8. Partial success: accurate per-effect state and recovery.
9. Stale/unavailable source: honest freshness/fallback.
10. Prompt injection: unchanged tool/policy boundaries.
11. Interruption/resume: old confirmation cannot authorize a changed action.
12. Published channel: rendering, links, identity and persistence.

Use a meaningful subset for low-impact changes. For agents with tools, golden
answers alone are insufficient: assert calls, arguments, state changes and absent
forbidden effects. Self-confidence is not measured accuracy.

## Original evaluation tools

Read `validate`, `test-auth`, appropriate chat skills, `create-eval`,
`create-eval-set`, `run-eval`, `analyze-evals` or `run-tests-kit`. Test formats and
surfaces differ; a CSV accepted by one is not proof for another. Inspect installed
versions and actual responses. Native diagnostics can require an LSP binary,
dependencies and connection. With no tenant, finish local artifacts and exact
pending target cases; do not generate a fictional passing cloud transcript.

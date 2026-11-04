# Architecture decision: <business outcome>

Design artifact only; this is not a native Copilot Studio configuration or import.

## Recommendation

<Chosen design, why it fits, and why added components justify their cost.>

Constraints: <volume/burst, freshness and latency target, quality, approved ingress,
identity, connectors/DLP, available runtimes, capacity and budget.>

Assumptions/unknowns: <owner, evidence needed and impact if false.>

## Candidates (at most three)

| Candidate | Benefit | Cost/latency/reliability tradeoff | Decision |
|---|---|---|---|
| Simple baseline | | | |
| Alternative | | | |

## Stage map

| Stage / owner | Surface and runtime | Input -> output | Rules / bounded model / reasoning | Gate or bound |
|---|---|---|---|---|
| | | | | |

## Handoff ledger

| Producer -> consumer | Transport and schema version | Identity/scope | Documented support + source/date | Tenant readiness + evidence | Completion/timeout |
|---|---|---|---|---|---|
| | | | | | |

Async contract if applicable: <job/business key, correlation ID, source version,
ready/processing/succeeded/failed, atomic claim or declared limitation,
attempt/lease/recovery, result/error reference, and output idempotency.>

## Cost and controls

Eligible runs/day: <measured value or explicit assumption; dedup/filter/cache/batch.>

Whole-path estimate: <action/flow charges + eligible reasoning work + transfers,
storage, notifications and retries; units, source/date, unknown rates.>

Controls: <context/output, calls, tools, iterations, retries, timeouts and budget;
identify which backend enforces each bound and any unenforced exposure.>

Fallback: <stale/missing data, failed reasoning, pending async work, review path.>

## Pilot and delivery

Same-input baseline/alternative comparison: <labeled sample and acceptance criteria.>

Measure: <success/quality, total credits, p50/p95 latency, model/tool calls,
duplicate effects and manual recovery.>

Implementation order: <contracts -> components -> handoff -> effects -> channel.>

Evidence: <static / fixtures / native / connected / published; mark pending.>

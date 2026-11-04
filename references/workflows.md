# Workflow engineering

For multi-stage systems or cost optimization, first read `hybrid-architecture.md`
and record a stage map plus handoff ledger. Keep Power Automate cloud flows,
Standard agent flows and modern Copilot Studio Workflows distinct.

## Select a surface

Use a direct permitted connector in a topic for simple reads/actions; an agent
flow for reusable typed operations; a cloud flow for event/schedule work. Use
MCP/custom APIs only for a needed approved integration. Confirm the current
agent trigger, response action and solution membership requirements.

The Standard-class Microsoft Copilot Studio connector can invoke a published
**Standard-harness agent** from a Power Automate cloud flow with
`ExecuteCopilot` or `ExecuteCopilotAsyncV2` (Execute Agent and wait). Verify live
operation metadata and rights. This is not a blanket entitlement for premium
actions, AI Builder or another principal's data.

Current Microsoft guidance says this connector does **not** call modern/GHCP
agents from a Power Automate cloud flow. For modern agents, use a supported
Copilot Studio Workflow Agent node. Modern agent event triggers are a separate
Preview surface. Shared-state/event handoff is another design, with two actual
configured endpoints; it does not imply direct connected-agent compatibility.
See the dated invocation table and official sources in `hybrid-architecture.md`.

## Outcome contract

Define purpose, required inputs, authorization, allowed transitions, separate
effect statuses, retry policy and evidence. This is an application design
example, not a Microsoft API schema:

```json
{
  "status": "not_found",
  "requestKey": "synthetic-case-001",
  "correlationId": "synthetic-run-001",
  "recordUpdated": false,
  "notificationStatus": "not_started",
  "message": "No matching record; no changes made."
}
```

## Default-false control

1. Validate typed inputs and authenticated scope.
2. Look up exact business key and check cardinality.
3. Zero -> not_found; multiple -> ambiguous; neither path mutates.
4. Validate eligibility deterministically.
5. Bind required confirmation to this proposal/version.
6. Claim a durable idempotency key with an atomic mechanism where available.
7. Perform the write, capture result and read back when required.
8. Execute downstream effects separately and retain their states.
9. Return a controlled response with only established outcomes.

Initialize success/updated/completed/verified flags to false. An empty foreach
can finish successfully without updating anything. Separate cancellation from
refund, sending from approval, and accepted from completed. Expected business
failures need responses; avoid paths that leave a calling agent waiting forever.

## Duplicate and timeout behavior

Normalize a business key scoped to the record/user/operation lifecycle. Use a
unique field, transactional claim, conditional update or backend constraint.
In SharePoint, assess unique columns and conditional updates actually supported
by the chosen action. A lookup-before-create is a prototype guard, not a global
guarantee; a single flow's concurrency setting does not protect other callers.

Return existing operation state on replay. After an uncertain timeout reconcile
first, then retry only if safe. Reuse the same external idempotency key where
supported. Audit logs are evidence, not transaction management.

## Tooling

If FlowStudio-compatible MCP is already configured and permitted, discover the
current tool schemas. Its flow read/update and action-level output tools can
close the build/debug loop. This bundle provides no FlowStudio server, account,
subscription or connection. The public power-automate-mcp-skills repo is not a
complete self-hostable implementation of that backend.

Without it, work from an actual exported flow or permitted designer. Produce
JSON diffs and explicit deployment steps. Missing authenticated connections or
OAuth consent are real dependencies; do not fabricate connection IDs.

## Test trigger and actions separately

Synthetic action-chain tests do not prove production trigger subscriptions,
event shape or auth. A temporary manual/HTTP trigger is an optional sandbox
technique only if authorized and permitted. Restore the original trigger and
test a representative real event. Replaying a previous run may repeat sends and
writes; inspect authorization and idempotency before replay.

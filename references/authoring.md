# Standard authoring and toolkit routing

This operation map is for Standard agents. Read `harness-routing.md` first;
modern CLI-agents use `harness-agentic.md` and the separate modern toolkit.

## Actual files first

An extension workspace can contain `.mcs.yml` or `.mcs.yaml`; an unpacked solution
can store component YAML as `botcomponents/*/data`. Inspect and preserve the
target format. Do not confuse a solution export with an extension workspace.

UPSTREAM is the absolute `vendor/microsoft/skills-for-copilot-studio` directory
relative to the main skill. Read full original guidance for the operation.

| Task | Original skills under `UPSTREAM/skills/` |
|---|---|
| Clone/pull/push/project discovery | `manage-agent`, `clone-agent`, `int-project-context` |
| Orchestration/settings | `detect-mode`, `edit-agent` |
| New topic/node/schema | `new-topic`, `add-node`, `list-kinds`, `lookup-schema` |
| Topic inventory | `list-topics` |
| Connector/MCP actions | `add-action`, `edit-action` |
| Adaptive Cards | `add-adaptive-card` |
| Grounded answers and knowledge | `add-generative-answers`, `add-knowledge` |
| Variables/triggers/agents | `add-global-variable`, `edit-triggers`, `add-other-agents` |
| Native diagnostics | `validate` |
| Authentication/chat | `test-auth`, `chat-with-agent`, `chat-sdk`, `chat-directline`, `directline-chat` |
| Evaluations | `create-eval`, `create-eval-set`, `run-eval`, `analyze-evals`, `run-tests-kit` |
| Platform patterns/reference | `int-reference`, `int-patterns` |

The installed `mcs-*` wrappers expose these instructions to Copilot discovery.
`create-eval` authors the plugin's own fixture/scenario evaluations; use
`create-eval-set` for the matching Studio agent evaluation surface. Do not
interchange these formats or confuse toolkit tests with business-agent tests.
The four original role files are workflow guides, not automatically registered
Copilot custom agents. Read `agents/copilot-studio-author.md` for substantial edits.

## Resolve instead of inventing

Use the real export, matching schema and lookup helpers for kinds and connector
operations. A schema lookup can run without loading the full schema:

```bash
node "<UPSTREAM>/scripts/schema-lookup.bundle.js" resolve AdaptiveDialog
```

Inspect `--help` for other commands. Read `add-action`/`edit-action` before the
connector helper. Operation inputs, dynamic schema and OData quoting differ
between TaskDialog and inline actions and across versions. Actual native
diagnostics and current operation responses outrank contradictory cached examples.

## Component checks

- Topics: unique node IDs, initialized typed variables, valid jumps/redirects,
  clear interruption, resume and confirmation state.
- Power Fx: distinguish formula `=` from string/interpolation. Verify supported
  functions and result types natively; YAML parsing cannot check formulas.
- Cards: channel-supported version, exact input/output bindings, empty-state
  behavior and repeat submissions. Prefer constrained choices to arbitrary IDs.
- Tools: narrow description, typed contract, correct identity and logical references.
- Knowledge: source scope, citations, authorization and honest not-found path.
- Child agents: explicit input/output and response ownership; bounded delegation.

## Lifecycle

Clone -> inspect -> scoped diff -> diagnostics -> review local/cloud drift ->
apply -> test -> publish -> test the published channel. Use the extension or
verified manager commands available in the installed version. Do not invent
`pac` commands or extension command IDs.

For cross-environment transfer, include required solution components, connection
references and environment variables. Credentials, roles, data and publication
need target setup. Managed solutions are not editable source; raw flow JSON is
not a portable import ZIP. Read the original SETUP_GUIDE for optional native
dependencies, but do not execute setup hooks by default.

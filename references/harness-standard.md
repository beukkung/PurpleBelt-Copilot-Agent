# Standard harness: build with explicit control

Use only after workspace/export evidence identifies a Standard agent. GitHub
Copilot in VS Code is the development assistant, not proof of the Studio harness.

## Route to the pinned toolkit

STANDARD is `<builder-root>/vendor/microsoft/skills-for-copilot-studio`.
Read `STANDARD/SETUP_GUIDE.md` for prerequisites and the specific original
`skills/<operation>/SKILL.md` before each operation. Preserve its directory layout.

| Task | Original operation |
|---|---|
| Connect, clone, pull, push | `manage-agent`, `clone-agent` |
| Create conversations and deterministic branches | `new-topic`, `add-node`, `edit-triggers` |
| Edit instructions and orchestration | `edit-agent` |
| Tools, cards, data | `add-action`, `edit-action`, `add-adaptive-card`, `add-knowledge` |
| Native diagnostics | `validate` |
| Evaluate | `create-eval-set`, `run-eval`, `analyze-evals` |

Discoverable entry points use `mcs-*`. No direct mapping exists from those topics,
Power Fx or global/topic variables to the CLI-agent model. Do not apply Standard
schemas to `cliagent-*` settings. Read `authoring.md` for detailed Standard routing.

## Productive first loop

1. Clone a minimal real agent using the supported extension/toolkit and permitted
   account. Do not manufacture IDs or connection files.
2. Build one connector-free greeting or intake topic using the original schema.
3. Run static preflight, then available native diagnostics.
4. Inspect local/cloud drift, sync using verified operations and test in Studio.
5. Publish only within the user's authorized scope, then test the target channel.

Capture each actual result. An extension being installed does not establish login,
tenant rights, native tool dependencies or connector availability. If native tools
are unavailable, prepare a scoped diff and exact manual test handoff.

## Transfer

Solution ZIP transfer is a separate lifecycle from extension sync. Include required
components and target bindings through supported tooling. A folder of generated
YAML, flow JSON or a ZIP of this repository is not an importable business agent.
This bundle does not provide a tested Solution ZIP builder or full validator for
unpacked `botcomponents/*/data`. Do not imply otherwise.

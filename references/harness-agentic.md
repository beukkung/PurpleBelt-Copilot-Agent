# Microsoft Copilot harness: build around procedures and tools

Use for the Copilot Studio runtime formerly named GitHub Copilot harness. This
is separate from the GitHub Copilot coding assistant. The pinned Microsoft plugin
still uses GHCP, MCS2 and CLI-agent terminology.

AGENTIC is `<builder-root>/vendor/microsoft/copilot-studio-plugin`.
Use this exact pinned directory for plugin resources. The installer does not
register upstream hooks, commands or personas. Resolve `${CLAUDE_PLUGIN_ROOT}` and
plugin-relative paths yourself; do not assume host-specific variables exist or
write a global plugin registry merely to satisfy a placeholder.

## Select from real evidence

Inspect `settings.mcs.yml` for `template: cliagent-*`,
`configuration.authoringModel: CliCopilot`, and
`configuration.recognizer.kind: CLIAgentRecognizer` or `CLICopilotRecognizer`.
These are evidence, not fields to inject into an unrelated
workspace. Run local preflight and report unknown/conflicting markers. Keep
migration source and target in different workspaces.

The README requires PAC CLI **2.9.3+**. Check the installed version and each
operation's actual help output. An installed Studio extension alone does not prove
PAC support, tenant rollout, login, permissions, capacity or tool connections.

## Route to the original operation

| Task | Read under AGENTIC |
|---|---|
| Create a new cloud agent and workspace | `skills/create-agent/SKILL.md` |
| Connect existing work | `skills/clone-agent/SKILL.md`, `skills/pull-agent/SKILL.md` |
| Upload local changes | `skills/push-agent/SKILL.md` |
| Publish the cloud draft | `skills/publish-agent/SKILL.md` |
| Add reusable runtime skills | `skills/add-skill/SKILL.md`, `reference/skill-schema.md` |
| Add grounding | `skills/add-knowledge/SKILL.md`, `reference/knowledge-schema.md` |
| Design or rebuild behavior | `agents/copilot-studio-architect.md` |
| Migrate Standard source | `commands/migrate.md`, `agents/copilot-studio-describer.md` |
| Chat and check results | `commands/chat.md` |
| Delete a cloud agent | `skills/delete-agent/SKILL.md`; only an explicit deletion request |

Operation discovery names use `mcsa-*`, avoiding Standard's `mcs-*` collisions.
The original slash-command installation is host-specific; discovery wrappers load
instructions, not a plugin command runtime.

## Author with the modern model

Read the original architect and authoritative schema before changing YAML.
For ordinary creation/enhancement, use the user's brief and an inventory of actual
workspace behavior. The architect's required migration Describer report is scoped
to migration; do not fabricate a source report or block ordinary authoring on it.

| Requirement | Destination |
|---|---|
| Global behavior, tone and tool policy | `settings.mcs.yml` |
| Reusable task procedure | `behaviors/`, following `reference/skill-schema.md` |
| Factual grounding | `capabilities/knowledge/`, following knowledge schema |
| Live reads, calculations and external effects | Verified `capabilities/tools/` references |

Do not create Standard `AdaptiveDialog` topics, Power Fx or global/topic variables.
Conversation context is not a transactional variable store. Put exact refund
arithmetic, eligibility and idempotent writes in deterministic tools/workflows;
a prose skill describes when to use them. Use narrow skills only for procedures
that need them. Uploaded payload/knowledge sidecars can intentionally omit `kind`.
This deterministic-tool requirement takes precedence over the architect's general
suggestion that simple logic can live in a prose skill. Embedded code must actually
execute in a verified supported runtime and pass fixtures; prose is not execution.
Preserve `mcs.metadata`, native sync metadata and actual identity. Never read or
edit `.mcs/conn.json` just to discover credentials.

## Execute the supported lifecycle

1. Resolve scenario, environment, workspace and publisher prefix from actual inputs.
2. Read the original create/clone instructions, check PAC and authentication.
   `pac copilot init` creates cloud resources and is not a local-only scaffold;
   its resulting service state can vary. Inspect actual results.
3. Pull before authoring/sync as directed by the current operation, review drift
   and preserve user changes. Do not run init over an existing project.
4. Author the smallest useful journey. Require real tool operations and bindings;
   label synthetic data and missing integrations explicitly.
5. Run static preflight. Use native checks actually available in the installed
   tooling, then the original push operation. Do not invent a modern LSP/validate
   command or reuse Standard diagnostics as proof of modern schema validity.
6. Run local behavior fixtures and any supported target-native checks. The pinned
   chat command supports published agents, not an unpublished draft. Mark draft
   runtime testing pending unless a separate supported draft test surface is
   actually available. Do not test an old published version and call it the draft.
7. Use the separate publish operation when authorized, then use original chat and
   target-channel tests on the exact published version. Report calls and effects.

Local skill import only writes files. Push is cloud synchronization. Publish
makes cloud content live. Some pinned upstream add-skill prose calls sync push
"publishing"; preserve these three distinct states in reports. A helper returning
`ok: true` does not prove either cloud state.

When an original guide references `mcs-assistant:<operation>`, load the matching
pinned skill file or `mcsa-*` wrapper; the file installer creates no slash commands.
Use existing explicit user authorization rather than repeating confirmations for
the same resolved action. Clarify when target/scope is ambiguous; deletion needs
explicit deletion intent. Never silently expand an authorized publish target.

The pinned publish guide asks for a non-no-op push as readiness evidence. Do not
manufacture a change or repeat no-op pushes to satisfy that wording. Accept only
verified equivalent evidence that the intended local version is already the exact
target's cloud draft (for example, a successful native readback and reviewed diff).
If that equality cannot be established with supported tooling, leave readiness
pending and explain the missing evidence.

## Migration is a rebuild

Read the full migration workflow first. Describe source behavior, inventory tools
and decide what to carry forward. Map each requirement to instructions, skills,
knowledge, deterministic workflows or explicit gaps. The converter supports only
some action shapes; do not promise every flow/prompt or connection will migrate.
Retain the source agent and verify the new agent against the same acceptance
cases. Do not load both original plugins' global prompts/hooks into one session
indiscriminately; the migration guide flags potential legacy-plugin conflicts.

## Evidence boundary

PurpleBelt includes a pinned WIP plugin, not a runtime entitlement. Local tests
establish installation, routing heuristics and helper behavior only. Tenant
creation, sync, chat, migration and publication must be verified in the actual
environment before claiming a working deployment or faster delivery.

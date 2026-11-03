# Pinned Microsoft toolkits

Commit: `9c42d3a612c6e06389b6e5b4eed579aaed1a8b63`. Full originals remain unchanged.

## Standard skills

| Discovery name | Original instructions | Description |
|---|---|---|
| `mcs-add-action` | [add-action](../vendor/microsoft/skills-for-copilot-studio/skills/add-action/SKILL.md) | Guide users through adding a new connector action to a Copilot Studio agent. Connector actions require UI-based connection setup, so this skill walks users through the Copilot Studio portal steps, then delegates to edit-action for YAML modifications. |
| `mcs-add-adaptive-card` | [add-adaptive-card](../vendor/microsoft/skills-for-copilot-studio/skills/add-adaptive-card/SKILL.md) | Generate and insert an Adaptive Card into a Copilot Studio topic using AdaptiveCardPrompt. Use when the user asks to add an adaptive card, rich card, form card, info card, confirmation card, or interactive card to a topic. |
| `mcs-add-generative-answers` | [add-generative-answers](../vendor/microsoft/skills-for-copilot-studio/skills/add-generative-answers/SKILL.md) | Add generative answer nodes (SearchAndSummarizeContent or AnswerQuestionWithAI) to a Copilot Studio topic. Use this instead of /add-node when the user asks to add grounded answers, knowledge search, generative answers, or AI-powered responses — these nodes require specific patterns (ConditionGroup follow-up, knowledge source references, autoSend, responseCaptureType) that /add-node does not cover. |
| `mcs-add-global-variable` | [add-global-variable](../vendor/microsoft/skills-for-copilot-studio/skills/add-global-variable/SKILL.md) | Add a global variable to a Copilot Studio agent. Use when the user needs a variable that persists across topics in the same conversation and can optionally be visible to the AI orchestrator. |
| `mcs-add-knowledge` | [add-knowledge](../vendor/microsoft/skills-for-copilot-studio/skills/add-knowledge/SKILL.md) | Add a knowledge source (public website or SharePoint) to a Copilot Studio agent. Use when the user asks to add a knowledge source, documentation URL, website, or SharePoint site for the agent to search. |
| `mcs-add-node` | [add-node](../vendor/microsoft/skills-for-copilot-studio/skills/add-node/SKILL.md) | Add or modify a node in an existing Copilot Studio topic. Use when the user asks to add a question, message, condition, variable, or other node to a topic. Do NOT use this for generative answers or knowledge search — use /add-generative-answers instead. |
| `mcs-add-other-agents` | [add-other-agents](../vendor/microsoft/skills-for-copilot-studio/skills/add-other-agents/SKILL.md) | Add child agents, connected agents, or other multi-agent patterns to a Copilot Studio agent. Use when the user asks to create a sub-agent, child agent, connected agent, or call another agent. |
| `mcs-analyze-evals` | [analyze-evals](../vendor/microsoft/skills-for-copilot-studio/skills/analyze-evals/SKILL.md) | Analyze exported evaluation results from Copilot Studio's Evaluate tab. The user provides a CSV file exported from the Copilot Studio UI; this skill parses it, identifies failures, and proposes YAML fixes. No API access or published agent required — just the exported CSV. |
| `mcs-chat-directline` | [chat-directline](../vendor/microsoft/skills-for-copilot-studio/skills/chat-directline/SKILL.md) | Send a message to a Copilot Studio agent via DirectLine v3. Use for agents with no auth or manual auth. Requires a token endpoint URL or DirectLine secret. |
| `mcs-chat-sdk` | [chat-sdk](../vendor/microsoft/skills-for-copilot-studio/skills/chat-sdk/SKILL.md) | Send a message to a Copilot Studio agent via the Copilot Studio Client SDK (M365). Use for agents with integrated auth (Entra ID SSO). Requires an App Registration Client ID. |
| `mcs-chat-with-agent` | [chat-with-agent](../vendor/microsoft/skills-for-copilot-studio/skills/chat-with-agent/SKILL.md) | DEPRECATED: Use /copilot-studio:detect-mode then /copilot-studio:chat-directline or /copilot-studio:chat-sdk instead. |
| `mcs-clone-agent` | [clone-agent](../vendor/microsoft/skills-for-copilot-studio/skills/clone-agent/SKILL.md) | Clone a Copilot Studio agent from the cloud. Guides through environment selection, agent selection, and downloads agent YAML files. |
| `mcs-create-eval` | [create-eval](../vendor/microsoft/skills-for-copilot-studio/skills/create-eval/SKILL.md) | Create plugin development eval scenarios (JSON files with natural prompts and deterministic checks for testing plugin skills). NOT for Copilot Studio in-product evaluation — use /copilot-studio:create-eval-set for that. |
| `mcs-create-eval-set` | [create-eval-set](../vendor/microsoft/skills-for-copilot-studio/skills/create-eval-set/SKILL.md) | Create a test set CSV file for import into Copilot Studio's in-product Evaluate tab. Reads the agent's topics, instructions, and knowledge sources to generate meaningful test cases with appropriate graders (General quality, Compare meaning, Exact match, etc.). Use when the user asks to create, prepare, or generate evaluation test cases for their agent. |
| `mcs-detect-mode` | [detect-mode](../vendor/microsoft/skills-for-copilot-studio/skills/detect-mode/SKILL.md) | Detect a Copilot Studio agent's authentication mode (DirectLine vs M365) by querying Dataverse. Returns the mode and connection details needed to chat. |
| `mcs-directline-chat` | [directline-chat](../vendor/microsoft/skills-for-copilot-studio/skills/directline-chat/SKILL.md) | DEPRECATED: Use /copilot-studio:chat-with-agent instead — it auto-detects DirectLine vs M365 mode. This skill is kept for backwards compatibility only. |
| `mcs-edit-action` | [edit-action](../vendor/microsoft/skills-for-copilot-studio/skills/edit-action/SKILL.md) | Edit an existing action (TaskDialog) in a Copilot Studio agent. Supports connector actions and MCP server actions. Modify inputs, outputs, descriptions, connection mode, and other properties. |
| `mcs-edit-agent` | [edit-agent](../vendor/microsoft/skills-for-copilot-studio/skills/edit-agent/SKILL.md) | Edit Copilot Studio agent settings, instructions, or configuration. Use when the user asks to change agent instructions, display name, conversation starters, AI settings, or generative actions toggle. |
| `mcs-edit-triggers` | [edit-triggers](../vendor/microsoft/skills-for-copilot-studio/skills/edit-triggers/SKILL.md) | Modify topic triggers — trigger phrases and model description. Use when the user asks to add, remove, or change trigger phrases, or edit a topic's model description. |
| `mcs-int-patterns` | [int-patterns](../vendor/microsoft/skills-for-copilot-studio/skills/int-patterns/SKILL.md) | Pattern library for Copilot Studio agent design. Contains proven and recommended implementation patterns with YAML examples. Used by the Advisor agent to suggest patterns and by the Author agent to reference YAML structure during implementation. USE FOR: design guidance, pattern suggestions, review against best practices, troubleshooting known pitfalls, YAML reference during implementation. DO NOT USE FOR: general YAML schema reference (use int-reference), topic creation mechanics (use new-topic). |
| `mcs-int-project-context` | [int-project-context](../vendor/microsoft/skills-for-copilot-studio/skills/int-project-context/SKILL.md) | Shared project context for all Copilot Studio sub-agents. Provides project structure, schema lookup usage, and skill invocation guidance. |
| `mcs-int-reference` | [int-reference](../vendor/microsoft/skills-for-copilot-studio/skills/int-reference/SKILL.md) | Reference tables for Copilot Studio YAML authoring: triggers, actions, variables, entities, Power Fx functions, templates. Preloaded by author and advisor agents. |
| `mcs-list-kinds` | [list-kinds](../vendor/microsoft/skills-for-copilot-studio/skills/list-kinds/SKILL.md) | List all available kind discriminator values from the Copilot Studio YAML schema. Use when the user asks what kinds/types are available. |
| `mcs-list-topics` | [list-topics](../vendor/microsoft/skills-for-copilot-studio/skills/list-topics/SKILL.md) | List all topics in the Copilot Studio agent with their trigger types, phrases, and action counts. Use when the user wants to see what topics exist. |
| `mcs-lookup-schema` | [lookup-schema](../vendor/microsoft/skills-for-copilot-studio/skills/lookup-schema/SKILL.md) | Look up Copilot Studio YAML schema definitions. Use when the user asks about schema structure, element properties, or how to use a specific YAML kind. |
| `mcs-manage-agent` | [manage-agent](../vendor/microsoft/skills-for-copilot-studio/skills/manage-agent/SKILL.md) | Push/pull Copilot Studio agent content via the VS Code extension's LanguageServerHost LSP binary. Handles authentication (interactive browser login for push/pull, device code flow for chat token), sync push, sync pull, clone, and diff operations. |
| `mcs-new-topic` | [new-topic](../vendor/microsoft/skills-for-copilot-studio/skills/new-topic/SKILL.md) | Create a new Copilot Studio topic YAML file. Use when the user asks to create a new topic, conversation flow, or dialog for their agent. |
| `mcs-run-eval` | [run-eval](../vendor/microsoft/skills-for-copilot-studio/skills/run-eval/SKILL.md) | Run evaluations against a Copilot Studio agent via the Power Platform Evaluation API. Works on DRAFT agents — no publish step required. Lists test sets, starts a run, polls until complete, fetches results, and proposes YAML fixes for failures. Use when the user wants to test agent changes without publishing. |
| `mcs-run-tests-kit` | [run-tests-kit](../vendor/microsoft/skills-for-copilot-studio/skills/run-tests-kit/SKILL.md) | Run a batch test suite via the Copilot Studio Kit (Dataverse API). Uses the Power CAT Copilot Studio Kit to execute test cases against a published agent and produces pass/fail results with latencies. Requires the Kit installed in the environment, an App Registration with Dataverse permissions, and a published agent. |
| `mcs-test-auth` | [test-auth](../vendor/microsoft/skills-for-copilot-studio/skills/test-auth/SKILL.md) | Authenticate for Copilot Studio evaluation API and SDK chat. Caches a token that is shared across run-eval and chat-sdk skills. Run this before any eval or SDK chat workflow. Requires an App Registration with MakerOperations and Copilots.Invoke permissions. |
| `mcs-validate` | [validate](../vendor/microsoft/skills-for-copilot-studio/skills/validate/SKILL.md) | Validate Copilot Studio agent YAML files using the LSP binary's full diagnostics (YAML structure, Power Fx, schema, cross-file references). Use when the user asks to check, validate, or verify YAML files. |

## Specialist roles

- [copilot-studio-advisor](../vendor/microsoft/skills-for-copilot-studio/agents/copilot-studio-advisor.md)
- [copilot-studio-author](../vendor/microsoft/skills-for-copilot-studio/agents/copilot-studio-author.md)
- [copilot-studio-manage](../vendor/microsoft/skills-for-copilot-studio/agents/copilot-studio-manage.md)
- [copilot-studio-test](../vendor/microsoft/skills-for-copilot-studio/agents/copilot-studio-test.md)

## Complete directories

- `reference/`: full authoring schema, Adaptive Card schema and connector metadata.
- `templates/`: 18 agent/action/topic/knowledge/variable templates.
- `patterns/`: 15 archived patterns; review safety and version applicability before use.
- `scripts/`: bundled CLI utilities plus their original source.
- `evals/`: fixtures, scenario inputs, evaluation and reporting utilities.
- `tests/`: original test code.
- `hooks/`, `.claude-plugin/`, `.github/`: original setup/plugin/CI metadata, retained but not activated by our installer.
- README, SETUP_GUIDE, LICENSE, SECURITY, CONTRIBUTING and release notes are retained.

Read original operation instructions, not just these descriptions. The four specialist roles are not automatically installed as Copilot custom-agent personas.

## Microsoft Copilot harness toolkit

Original: `vendor/microsoft/copilot-studio-plugin/`

Pinned commit: `4014ae689d1228d86cb3aaab938b1e66f8e2e10d`. All 46 files remain
unmodified; see `../upstream-agentic.lock.json`. Read `harness-agentic.md` first.

| Discovery name | Original instructions |
|---|---|
| `mcsa-add-knowledge` | [add-knowledge](../vendor/microsoft/copilot-studio-plugin/skills/add-knowledge/SKILL.md) |
| `mcsa-add-skill` | [add-skill](../vendor/microsoft/copilot-studio-plugin/skills/add-skill/SKILL.md) |
| `mcsa-clone-agent` | [clone-agent](../vendor/microsoft/copilot-studio-plugin/skills/clone-agent/SKILL.md) |
| `mcsa-create-agent` | [create-agent](../vendor/microsoft/copilot-studio-plugin/skills/create-agent/SKILL.md) |
| `mcsa-delete-agent` | [delete-agent](../vendor/microsoft/copilot-studio-plugin/skills/delete-agent/SKILL.md) |
| `mcsa-publish-agent` | [publish-agent](../vendor/microsoft/copilot-studio-plugin/skills/publish-agent/SKILL.md) |
| `mcsa-pull-agent` | [pull-agent](../vendor/microsoft/copilot-studio-plugin/skills/pull-agent/SKILL.md) |
| `mcsa-push-agent` | [push-agent](../vendor/microsoft/copilot-studio-plugin/skills/push-agent/SKILL.md) |

The four original agent guides are Architect, Describer, Init and Manage.
The `commands/` directory includes chat and migration workflows. These are
references, not automatically registered Copilot custom agents/slash commands.
Shared authoritative references document runtime skill and knowledge schemas.
Helpers include skill import, action-to-tool conversion and knowledge-access
checks; their local tests do not establish live tenant behavior.

Discovery totals: **42 entries** with `all` (1 Builder + 2 harness adapters +
31 Standard operation wrappers + 8 modern operation wrappers). `standard`
installs 33; `agentic` installs 10. Both source snapshots remain on disk, loaded
on demand. Hook files remain inactive.

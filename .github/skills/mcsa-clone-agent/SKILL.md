---
name: mcsa-clone-agent
description: "Use when developing Microsoft Copilot harness (formerly GitHub Copilot harness) agents and the task requires clone agent."
---

# PurpleBelt agentic: clone-agent

Read `../../../SKILL.md` and `../../../references/harness-agentic.md` first.
Then read the complete original skill directory at `../../../vendor/microsoft/copilot-studio-plugin/skills/clone-agent/SKILL.md`.
Resolve all paths from this file. Use the original skill directory for relative references and the original plugin root for `${CLAUDE_PLUGIN_ROOT}`; these are path placeholders, not guaranteed Copilot environment variables.
CLI-agent workspace evidence and current PAC command support are required. Standard topic schemas do not apply.
Installation activates no hooks and supplies no tenant credentials. Local import is not cloud sync; cloud sync is not publish.

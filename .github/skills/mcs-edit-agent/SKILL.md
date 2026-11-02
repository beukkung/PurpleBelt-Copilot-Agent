---
name: mcs-edit-agent
description: "Use when authoring Microsoft Copilot Studio standard agents and the task requires edit agent."
---

# Microsoft Copilot Studio: edit-agent

Read `../../../SKILL.md` first for environment and evidence requirements.
Then read the complete upstream skill at `../../../vendor/microsoft/skills-for-copilot-studio/skills/edit-agent/SKILL.md`.
Resolve these paths relative to this file. Use the original skill directory for every `${CLAUDE_SKILL_DIR}` substitution; it is a path placeholder, not a guaranteed exported environment variable in Copilot.
Resolve original relative references from that original skill directory. Preserve the upstream directory layout.
The standard-harness toolkit does not authorize cross-harness schema reuse, live mutations, secret disclosure, or chain-of-thought logging.
Do not execute plugin hooks or install native dependencies unless required for the requested operation and permitted by the environment.

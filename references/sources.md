# Sources

Reviewed 2026-11-04. Recheck official documentation for changing platform details.

## Official

- https://github.com/microsoft/copilot-studio-plugin — complete unmodified MIT
  snapshot; exact commit and hashes in `../upstream-agentic.lock.json`.
- https://www.microsoft.com/en-us/copilot/blog/copilot-studio/the-github-copilot-harness-in-copilot-studio-is-now-the-microsoft-copilot-harness/
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/choose-harness

- https://github.com/microsoft/skills-for-copilot-studio — complete unmodified MIT
  snapshot; exact commit and every hash are in `../upstream.lock.json`.
- https://docs.github.com/en/copilot/concepts/customizations/agent-skills
- https://code.visualstudio.com/docs/agent-customization/agent-skills
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/visual-studio-code-extension-overview
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/visual-studio-code-extension-edit-agent-components
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/harnesses-overview
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/admin-data-loss-prevention
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-faqs
- https://learn.microsoft.com/en-us/connectors/microsoftcopilotstudio/
- https://learn.microsoft.com/en-us/connectors/sharepoint/
- https://learn.microsoft.com/en-us/connectors/office365/
- https://learn.microsoft.com/en-us/connectors/teams/
- https://learn.microsoft.com/en-us/connectors/planner/
- https://learn.microsoft.com/en-us/connectors/wordonlinebusiness/
- https://learn.microsoft.com/en-us/connectors/visualstudioteamservices/
- https://learn.microsoft.com/en-us/connectors/commondataserviceforapps/

## Hybrid architecture invocation sources (checked 2026-11-04)

- https://learn.microsoft.com/en-us/power-automate/call-copilot-studio-agent
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/workflows-experience/agent-node-workflow
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/authoring-add-event-trigger
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/agents-experience/faqs-copilot-harness
- https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview
- https://learn.microsoft.com/en-us/sharepoint/dev/business-apps/power-automate/sharepoint-connector-actions-triggers

The architecture patterns and cost model are independently synthesized design
guidance, not platform guarantees or measured savings. Invocation support remains
separate from tenant availability and test evidence.

## SharePoint design references (checked 2026-11-04)

- https://learn.microsoft.com/en-us/sharepoint/information-architecture-modern-experience
- https://learn.microsoft.com/en-us/sharepoint/modern-experience-sharing-permissions
- https://learn.microsoft.com/en-us/sharepoint/manage-permission-scope
- https://learn.microsoft.com/en-us/office365/servicedescriptions/sharepoint-online-service-description/sharepoint-online-limits
- https://support.microsoft.com/en-us/sharepoint/data-and-lists/add-an-index-to-a-list-or-library-column
- https://learn.microsoft.com/en-us/troubleshoot/sharepoint/lists-and-libraries/fails-filtering-sharepoint-column
- https://learn.microsoft.com/en-us/sharepoint/dev/declarative-customization/column-formatting
- https://learn.microsoft.com/en-us/sharepoint/dev/declarative-customization/view-formatting
- https://learn.microsoft.com/en-us/sharepoint/dev/declarative-customization/site-design-overview

The SharePoint blueprint is design guidance. Generated formatting JSON is a
separate artifact from native provisioning scripts or Copilot Studio YAML.

## Public reference builds

Event: https://devblogs.microsoft.com/powerplatform/agent-academy-hackathon-winners/

| Repo | Lesson and inspected evidence |
|---|---|
| https://github.com/Ateina/performance-development-assistant | ZIP: taxonomy, loops, cards, SharePoint; approval flow sends email, not a completed approval |
| https://github.com/hutten358/MeetingTasksAgent | ZIP: extraction/review/execution; identity guessing and implicit dates need correction |
| https://github.com/anupamac985/Copilot-Insurance-Agent | ZIP: confirmation/control; default-true update and refund wording need correction |
| https://github.com/experienceswithanishh/vendorguard-copilot-studio | Docs/instructions: rulebook, domain roles; Dataverse/MCP/AI Builder dependencies |
| https://github.com/leila-marspooner/engagement-hub-agent | Docs/prompts: contracts, idempotency, gates; documentation repo, not deployable code |
| https://github.com/JBearCode/frostbyte-ai-advisor | Unpacked topics/flows: retrieval/analysis/write split; premium dependencies |
| https://github.com/Shrusti13/sprint-forge | ZIP: bounded enrichment; README marks attachments partly future work |
| https://github.com/tagr/CalamityCopilotService | YAML/MCP source: fresh data plus stable guidance; external APIs/hosting |
| https://github.com/granjan7779/rj-mcp-d365-server-2 | Tool registry/read source: narrow tool contracts; custom server/D365 |
| https://github.com/ninihen1/copilot-studio-itsm-agent | Flow/topic: controlled execution and action evidence; HTTP/MCP/executors required |
| https://github.com/appieschot/client-kickoff-skill | SKILL.md: two-phase workflow; Cowork skill, not a standard Studio topic |
| https://github.com/Jirawat-Yaito/team-yaito-pmo | Returned 404 during review; implementation not verified |

Only independently synthesized patterns are included; no hackathon application
code, tenant configuration or business records are copied.

Optional FlowStudio reference:
https://github.com/ninihen1/power-automate-mcp-skills — public skills/extension,
separate hosted MCP subscription. Not bundled or activated.

## Precedence

Actual diagnostics/operation responses -> current official docs/schema -> matching
export -> pinned toolkit -> general pattern. Resolve contradictions. Static file
inspection is not a runtime reproduction; archived claims can be version-specific.

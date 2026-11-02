# Environment and capabilities

## Harness

Detect the actual Studio harness independently from the coding assistant.
The Microsoft snapshot targets standard agents, including classic and
generative orchestration. Product names and availability change; use current
official docs and real exports for other harnesses. Read original `detect-mode`
and `edit-agent` skills before editing settings. Treat unknown as unknown.

## Capability ledger

Record capability, allowed/blocked/unknown, observed evidence, principal,
connector class, DLP data group, endpoint restriction and required plan/capacity.
Cover authoring, publication/channel, structured reads/writes, flows, knowledge,
model access, HTTP/MCP and evaluations. Resolve only dependencies of the current
slice; a full tenant policy export is rarely necessary.

Keep tokens, auth caches, `.mcs/conn.json` and sensitive run data out of Git and
logs. Inspect connection metadata locally only when required; report sanitized
configuration names rather than credentials.

## Profiles

| Profile | Default approach |
|---|---|
| Open | Permitted connectors/MCP/code where they improve the outcome |
| Standard only | Approved M365 connectors, direct topics, Power Fx, simple flows |
| Restricted | Permitted documents/data or explicit synthetic input and manual handoff |

Use the user's declared constraints immediately. Unknown is neither permission
nor a permanent ban: continue independent local work and identify a focused
check. Do not route around a restriction using another connector, personal
account, browser session or proxy.

## Classification snapshot

Reviewed 2026-11-02; recheck Microsoft connector docs before relying on it.

| Connector | Power Automate / Copilot Studio |
|---|---|
| SharePoint | Standard |
| Office 365 Outlook | Standard |
| Teams | Standard |
| Planner | Standard |
| Microsoft Copilot Studio | Standard |
| Microsoft Dataverse | Premium |
| Word Online (Business) | Premium |
| Azure DevOps | Premium |

Standard does not mean allowed or free. DLP groups can prevent data sharing
between individually permitted connectors. A Microsoft-owned MCP can be blocked.
Agent-flow consumption and base Studio rights are separate from connector class.
Using SharePoint for business records does not replace internal Studio storage.

No approved ingress means fresh external data is unavailable. Use an explicit
snapshot/replay; a harness cannot manufacture live news.

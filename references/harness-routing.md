# Choose the right build path

Purpose: select the authoring toolkit without mixing runtime schemas.

| Observed evidence | Route | Next read |
|---|---|---|
| Standard workspace/export and Standard components | `standard` | `harness-standard.md` |
| Root `cliagent-*` template, CliCopilot model or CLI recognizer | `agentic` | `harness-agentic.md` |
| Both modern settings and Standard dialogs/agent metadata | `conflict` | Separate source/target and resolve before edits |
| Only GitHub Copilot installed, project name, or user shorthand | `unknown` | Inspect actual settings/export or ask for runtime |

`scripts/preflight.py` reports observed markers as heuristics. A signal is not
full schema validation. A partial modern scaffold must still meet the original
create/clone workflow's complete verification requirements. Inspect evidence,
not just the reported label. Do not rewrite markers to force a route.

For a new project with no workspace, start from the scenario: Standard for an
explicit conversation/controlled bounded process; modern for procedures with
iterative work, files and cross-tool coordination when available and justified.
Record the selected runtime before native creation. Do not silently migrate an
existing agent. Do not infer modern availability, PAC support or capacity from
the presence of an extension. See `environment.md` for capability checks.

Shared guidance: business outcomes, tool/data contracts, hackathon delivery,
authorization, failure handling and evidence levels. Harness-specific guidance:
schemas, authoring folders, native diagnostics, sync, migration and publication.

Keep the large original bundles on disk and load only the relevant operation.
Install discovery profiles with `--harness standard`, `agentic` or `all`.
This changes discoverability, not cloud configuration or runtime capabilities.

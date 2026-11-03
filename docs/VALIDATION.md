# Validation record — 2026-11-02

## Scope

Local bundle quality and skill application were exercised. No Copilot Studio
tenant was connected, no business agent was deployed and no live workflow was run.

## Automated local checks

- Bundle tooling regression tests: strict YAML parsing, duplicate IDs, legitimate
  configuration files, static-only evidence, no connection-secret reads,
  default-true success heuristic, self-contained install, conflict preservation,
  no hook activation and upstream integrity/tampering checks.
- All 152 vendor files compared byte-for-byte via SHA-256 and Git blob hashes
  against the pinned snapshot in `upstream.lock.json`.
- Original Node regression test files: manage-agent security, URL parsing and
  setup-env behavior were run without live authentication.
- Original Python `test_eval_paths.py`: 10 local path-containment tests passed.
- Microsoft schema lookup resolved/summarized `AdaptiveDialog` locally.
- The original basic-agent fixture was parsed by static preflight. A configuration
  false positive found during this smoke test was reproduced, fixed and retested.

Run the current suite rather than treating this dated record as perpetual proof:

```bash
python -m unittest discover -s tests -v
python scripts/verify_bundle.py
node --test vendor/microsoft/skills-for-copilot-studio/tests/manage-agent-security.test.js vendor/microsoft/skills-for-copilot-studio/tests/parse-agent-url.test.js vendor/microsoft/skills-for-copilot-studio/tests/setup-env.test.js
python -B -m unittest discover -s vendor/microsoft/skills-for-copilot-studio/tests -p 'test_*.py' -v
```

## Skill application checks

Two independent fresh-context application runs read the skill and relevant
original Microsoft guidance. One produced a constrained six-hour personalized
news implementation handoff; the other diagnosed a default-success write and
SharePoint authoring failure. Both separated local design from connected proof,
selected relevant toolkit instructions and left unavailable tenant gates pending.
The debug run also exercised read-only schema/connector lookup.

Baseline runs without the skill were already cautious about deployment and
idempotency. No improvement percentage or model benchmark is claimed. The added
value observed was concrete access to the bundled platform guidance and helpers.

## Known unverified prerequisites

`manage-agent.bundle.js --help` encountered a missing
`@azure/msal-node-extensions` dependency in this executor during an application
check. Native authoring/LSP, tenant validation, authentication, cloud chat,
evaluations, apply/publish and published-channel UX remain unverified here.
See Microsoft's original SETUP_GUIDE before configuring native dependencies.

Hash integrity and local regression success do not certify every upstream
pattern, plugin hook, API, optional native package or live workflow.

## Dual-harness update — 2026-11-03

Added the complete modern `microsoft/copilot-studio-plugin` snapshot at
`4014ae689d1228d86cb3aaab938b1e66f8e2e10d` (46 files), without modifying originals.
The existing Standard snapshot remains pinned and unchanged (152 files).

### Checks actually run for this update

- **17/17 PurpleBelt Python tests passed:** prior regression cases plus modern
  settings/metadata-sidecar recognition, conflicting/unknown markers, selected
  discovery profiles, valid installed reference paths, second-bundle integrity,
  nested recognizer detection, symlink rejection and incomplete-toolkit refusal.
  New-feature cases failed against the baseline before the implementation changed.
- **198/198 upstream files matched** SHA-256, byte length and Git blob SHA-1.
- **69/69 modern upstream Node tests passed** after installing its locked package
  dependencies into a separate test directory with install scripts disabled.
  This includes real local skill-import fixture operations and source-contract
  tests. Initial runs without dependencies failed to load `js-yaml` and
  `@azure/msal-node`; dependency setup resolved those failures. No tenant used.
- Standard upstream Node regression files passed (runner reports 14 tests;
  URL parser also reports its own 15 assertions). Standard Python path suite:
  **10/10 passed**. None is a connected-platform test.
- Skill frontmatter validation passed. Checked 66 relative Markdown file links,
  42 discovery entries and their referenced files; no broken targets found.
- Rendered and visually inspected the new SVG banner. Reviewed Markdown structure;
  the actual GitHub page rendering was not browser-tested in this update.

The bundled helper tests do not certify every build target, dependency or native
command. In particular, no whole-plugin build, PAC CLI execution or LSP execution
was performed for the modern harness. The source plugin is WIP.

### Skill application review

A fresh-context baseline without PurpleBelt already separated deterministic
refund calculations and deployment evidence appropriately; no speed/quality gain
is claimed. A fresh-context application of the updated skill correctly selected
the modern toolkit, procedure schema, deterministic tool, sync and publish paths.
It found guide conflicts: published-only chat versus draft testing, migration-only
architect prerequisites, host slash-command references, deterministic calculation
placement and no-op publish readiness. The adapter now explicitly resolves those
issues while keeping the original Microsoft files unchanged. Follow-up review confirmed the corrected workflow and found three tooling issues:
recognizer nesting, symlink rejection after resolution, and incomplete inner
toolkit acceptance. All were reproduced with failing tests, fixed, and rechecked
by the reviewer: **9 focused regressions passed**. The full PurpleBelt suite
passed **21/21** afterward.

### Automation added; tenant gates remain pending

The GitHub Actions workflow defines Linux/Windows bundle checks and modern helper
checks with dependencies outside the pinned tree. Workflow configuration is not
proof that either hosted runner has passed; inspect actual Actions results.
`.gitattributes` preserves upstream bytes on Windows to avoid line-ending drift.

Still unverified: actual tenant creation, authentication, native schema acceptance,
cloud sync, runtime skills, migrated behavior, publication and target-channel UX.
No Solution ZIP builder or complete unpacked-solution validator was added. The
new README describes available tooling, not guaranteed deployed outcomes.

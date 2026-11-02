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

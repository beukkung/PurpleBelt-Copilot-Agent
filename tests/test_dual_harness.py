import json
import hashlib
import tempfile
import unittest
from pathlib import Path
from test_tooling import ROOT, load_script


class HarnessTests(unittest.TestCase):
    def test_misplaced_root_recognizer_does_not_establish_modern_harness(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / 'settings.mcs.yml').write_text('recognizer:\n  kind: CLIAgentRecognizer\n')
            self.assertEqual(load_script('preflight').inspect_workspace(p)['harness'], 'unknown')

    def test_incomplete_inner_toolkit_rejected_before_installation(self):
        mod = load_script('install')
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source, target = root / 'source', root / 'target'
            source.mkdir()
            for name in mod.PARTS:
                path = source / name
                if '.' in name:
                    path.write_text('placeholder')
                else:
                    path.mkdir()
            with self.assertRaisesRegex(ValueError, 'Incomplete toolkit'):
                mod.install(source, target, harness='agentic')
            self.assertFalse(target.exists())

    def test_nested_configuration_recognizer_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / 'settings.mcs.yml').write_text('configuration:\n  recognizer:\n    kind: CLIAgentRecognizer\n')
            self.assertEqual(load_script('preflight').inspect_workspace(p)['harness'], 'agentic')

    def test_integrity_rejects_symlink_to_matching_in_tree_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            vendor = root / 'vendor/microsoft/skills-for-copilot-studio'
            vendor.mkdir(parents=True)
            data = b'original'
            (vendor / 'real').write_bytes(data)
            try:
                (vendor / 'LICENSE').symlink_to('real')
            except OSError:
                self.skipTest('This account cannot create symlinks')
            entry = {'path': 'LICENSE', 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(), 'git_blob_sha1': hashlib.sha1(b'blob 8\0' + data).hexdigest()}
            (root / 'upstream.lock.json').write_text(json.dumps({'file_count': 1, 'files': [entry]}))
            result = load_script('verify_bundle').verify_snapshot(root, 'upstream.lock.json', 'skills-for-copilot-studio')
            self.assertIn('Missing or symlink: LICENSE', result['errors'])

    def test_modern_workspace_and_metadata_sidecar_are_recognized(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / 'settings.mcs.yml').write_text('template: cliagent-1.0.0\nconfiguration:\n  authoringModel: CliCopilot\n  recognizer:\n    kind: CLIAgentRecognizer\n')
            (p / 'behaviors/review').mkdir(parents=True)
            (p / 'behaviors/review/payload.mcs.yml').write_text('mcs.metadata:\n  componentName: payload\n')
            report = load_script('preflight').inspect_workspace(p)
            self.assertEqual(report['harness'], 'agentic')
            self.assertFalse(report['warnings'])
            self.assertFalse(report['tenant_verified'])

    def test_conflicting_harness_markers_block_authoring(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / 'settings.mcs.yml').write_text('template: cliagent-1.0.0\n')
            (p / 'legacy.mcs.yml').write_text('kind: AdaptiveDialog\n')
            report = load_script('preflight').inspect_workspace(p)
            self.assertEqual(report['harness'], 'conflict')
            self.assertIn('mixed_harness_markers', json.dumps(report['blockers']))

    def test_missing_markers_stay_unknown(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / 'settings.mcs.yml').write_text('displayName: Unknown\n')
            self.assertEqual(load_script('preflight').inspect_workspace(p)['harness'], 'unknown')

    def test_profile_installs_only_requested_discovery_entries(self):
        for harness, required, forbidden in [('standard', 'mcs-new-topic', 'mcsa-create-agent'), ('agentic', 'mcsa-create-agent', 'mcs-new-topic')]:
            with self.subTest(harness=harness), tempfile.TemporaryDirectory() as tmp:
                target = Path(tmp)
                result = load_script('install').install(ROOT, target, harness=harness)
                names = set(result['wrappers'])
                self.assertIn(required, names)
                self.assertNotIn(forbidden, names)
                self.assertIn('copilot-studio-' + harness, names)
                self.assertFalse(result['hooks_activated'])
                main = target / '.github/skills/copilot-studio-builder'
                self.assertTrue((main / 'vendor/microsoft/copilot-studio-plugin/skills/create-agent/SKILL.md').is_file())

    def test_second_snapshot_tampering_is_detected(self):
        mod = load_script('verify_bundle')
        report = mod.verify(ROOT)
        self.assertIn('copilot-studio-plugin', report['snapshots'])
        self.assertEqual(report['checked'], 198)
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / 'upstream-agentic.lock.json').write_text((ROOT / 'upstream-agentic.lock.json').read_text())
            (p / 'upstream.lock.json').write_text(json.dumps({'file_count': 0, 'files': []}))
            self.assertTrue(mod.verify(p)['errors'])


if __name__ == '__main__':
    unittest.main()

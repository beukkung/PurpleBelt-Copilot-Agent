import importlib.util
import json
import tempfile
import unittest
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    path = ROOT / 'scripts' / (name + '.py')
    if not path.exists():
        raise AssertionError('Implementation missing: ' + name)
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class PreflightTests(unittest.TestCase):
    def test_duplicate_yaml_keys_block_authoring(self):
        mod = load_script('preflight')
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / 'agent.mcs.yml').write_text('kind: GptComponentMetadata\nkind: AdaptiveDialog\n')
            result = mod.inspect_workspace(p)
            self.assertTrue(result['blockers'])
            self.assertIn('duplicate', json.dumps(result).lower())

    def test_duplicate_action_ids_block_authoring(self):
        mod = load_script('preflight')
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / 'agent.mcs.yml').write_text('kind: GptComponentMetadata\n')
            (p / 'topic.mcs.yml').write_text('kind: AdaptiveDialog\nbeginDialog:\n  kind: OnConversationStart\n  id: main\n  actions:\n  - kind: SendActivity\n    id: repeated\n    activity: Hi\n  - kind: SendActivity\n    id: repeated\n    activity: Again\n')
            self.assertIn('duplicate_node_id', json.dumps(mod.inspect_workspace(p)))

    def test_valid_local_files_do_not_claim_live_validation(self):
        mod = load_script('preflight')
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / 'agent.mcs.yml').write_text('kind: GptComponentMetadata\ndisplayName: Test\n')
            r = mod.inspect_workspace(p)
            self.assertFalse(r['blockers'])
            self.assertEqual(r['validation_level'], 'static-preflight')
            self.assertFalse(r['tenant_verified'])
            self.assertIn('power-fx', ' '.join(r['not_checked']).lower())

    def test_missing_workspace_is_a_blocker(self):
        mod = load_script('preflight')
        self.assertTrue(mod.inspect_workspace(ROOT / 'does-not-exist')['blockers'])

    def test_settings_without_kind_are_recognized_as_configuration(self):
        mod = load_script('preflight')
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / 'agent.mcs.yml').write_text('kind: GptComponentMetadata\n')
            (p / 'settings.mcs.yml').write_text('settings:\n  GenerativeActionsEnabled: true\n')
            report = mod.inspect_workspace(p)
            self.assertFalse(report['warnings'])
            settings = next(x for x in report['files'] if x['file'] == 'settings.mcs.yml')
            self.assertEqual(settings['kind'], 'configuration-yaml')

    def test_conn_file_is_not_opened_or_exposed(self):
        mod = load_script('preflight')
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / 'agent.mcs.yml').write_text('kind: GptComponentMetadata\n')
            (p / '.mcs').mkdir()
            (p / '.mcs/conn.json').write_text('SECRET_SENTINEL')
            r = mod.inspect_workspace(p)
            self.assertTrue(r['connection_metadata_present'])
            self.assertNotIn('SECRET_SENTINEL', json.dumps(r))

    def test_flow_success_initialization_is_reported_as_heuristic(self):
        mod = load_script('preflight')
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / 'agent.mcs.yml').write_text('kind: GptComponentMetadata\n')
            (p / 'workflow.json').write_text(json.dumps({'actions': {'Init': {'type': 'InitializeVariable', 'inputs': {'variables': [{'name': 'policyUpdated', 'type': 'boolean', 'value': True}]}}}}))
            r = mod.inspect_workspace(p)
            self.assertIn('success_initialized_true', json.dumps(r['warnings']))
            self.assertFalse(r['blockers'])


class BundleTests(unittest.TestCase):
    def test_all_original_files_match_pinned_hashes(self):
        mod = load_script('verify_bundle')
        self.assertEqual(mod.verify(ROOT)['errors'], [])

    def test_tampering_is_detected(self):
        mod = load_script('verify_bundle')
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / 'vendor/microsoft/skills-for-copilot-studio').mkdir(parents=True)
            (p / 'vendor/microsoft/skills-for-copilot-studio/LICENSE').write_text('tampered')
            lock = {'file_count': 1, 'files': [{'path': 'LICENSE', 'bytes': 1, 'sha256': 'wrong', 'git_blob_sha1': 'wrong'}]}
            (p / 'upstream.lock.json').write_text(json.dumps(lock))
            self.assertTrue(mod.verify(p)['errors'])


class InstallerTests(unittest.TestCase):
    def test_installed_bundle_is_self_contained_and_all_skills_discoverable(self):
        mod = load_script('install')
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / 'project with spaces'
            result = mod.install(ROOT, target)
            main = target / '.github/skills/copilot-studio-builder'
            self.assertTrue((main / 'SKILL.md').exists())
            self.assertTrue((main / 'vendor/microsoft/skills-for-copilot-studio/scripts/schema-lookup.bundle.js').exists())
            skill_count = sum(len(list((ROOT / 'vendor/microsoft' / repo / 'skills').glob('*/SKILL.md'))) for repo in ('skills-for-copilot-studio', 'copilot-studio-plugin')) + 3
            self.assertEqual(len(result['wrappers']), skill_count)
            for name in result['wrappers']:
                text = (target / '.github/skills' / name / 'SKILL.md').read_text()
                self.assertIn('name: ' + name, text)
                links = re.findall(r'`([^`]+\.md)`', text)
                self.assertTrue(links)
                for link in links:
                    self.assertTrue((target / '.github/skills' / name / link).resolve().is_file(), link)

    def test_existing_user_files_are_never_overwritten(self):
        mod = load_script('install')
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            existing = target / '.github/skills/mcs-add-action'
            existing.mkdir(parents=True)
            (existing / 'SKILL.md').write_text('USER_CONTENT')
            with self.assertRaises(FileExistsError):
                mod.install(ROOT, target)
            self.assertEqual((existing / 'SKILL.md').read_text(), 'USER_CONTENT')
            self.assertFalse((target / '.github/skills/copilot-studio-builder').exists())

    def test_install_does_not_activate_plugin_hooks(self):
        mod = load_script('install')
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp)
            mod.install(ROOT, target)
            self.assertFalse((target / '.claude-plugin').exists())
            self.assertFalse((target / '.github/hooks').exists())


if __name__ == '__main__':
    unittest.main()

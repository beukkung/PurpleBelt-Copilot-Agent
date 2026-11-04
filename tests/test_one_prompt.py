import unittest
from pathlib import Path

from test_tooling import ROOT, load_script


class OnePromptBuilderTests(unittest.TestCase):
    def test_discovery_entry_and_readable_guide(self):
        wrapper = ROOT / '.github/skills/one-prompt-solution-builder/SKILL.md'
        self.assertIn('name: one-prompt-solution-builder', wrapper.read_text(encoding='utf-8'))
        guide = ROOT / 'references/one-prompt-solution-builder.md'
        text = guide.read_text(encoding='utf-8')
        for phrase in ('Power Automate', 'Modern Copilot Studio Workflow', 'Teams', 'SharePoint',
                       'DESIGNED', 'LOCAL_VALIDATED', 'TENANT_TESTED', 'UNVERIFIED'):
            self.assertIn(phrase, text)
        self.assertTrue((ROOT / 'assets/one-prompt-solution-template.md').is_file())

    def test_installer_includes_orchestrator_in_all_profiles(self):
        module = load_script('install')
        for profile in ('standard', 'agentic', 'all'):
            with self.subTest(profile=profile):
                wrappers = module.wrappers(ROOT, profile)
                self.assertIn('one-prompt-solution-builder', wrappers)
                self.assertIn('../copilot-studio-builder/references/one-prompt-solution-builder.md',
                              wrappers['one-prompt-solution-builder'])

    def test_editable_diagram_docs(self):
        diagram = (ROOT / 'docs/diagrams/README.md').read_text(encoding='utf-8')
        guide = (ROOT / 'references/diagram-design.md').read_text(encoding='utf-8')
        self.assertEqual(diagram.count('```mermaid'), 2)
        self.assertEqual(diagram.count('```'), 4)
        self.assertIn('Every 30 minutes', diagram)
        self.assertIn('Microsoft Teams', diagram)
        self.assertIn('delivery effect', diagram)
        self.assertIn('No / timeout', diagram)
        self.assertIn('docs/diagrams/workflow.md', guide)
        self.assertIn('not a directly importable', guide)
        readme = (ROOT / 'README.md').read_text(encoding='utf-8')
        self.assertIn('docs/diagrams/README.md', readme)
        skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        self.assertIn('references/diagram-design.md', skill)

    def test_no_unsupported_zero_touch_claim(self):
        guide = (ROOT / 'references/one-prompt-solution-builder.md').read_text(encoding='utf-8')
        self.assertIn('does **not** prove an API/CLI', guide)
        self.assertIn('not a deployable solution ZIP', guide)
        self.assertIn('never', guide.lower())


if __name__ == '__main__':
    unittest.main()

"""Install a self-contained Copilot skill and discovery wrappers, without activating hooks."""
import argparse
import json
import shutil
from pathlib import Path

PARTS = ('SKILL.md', 'references', 'scripts', 'assets', 'vendor', 'upstream.lock.json', 'upstream-agentic.lock.json', 'LICENSE', 'NOTICE.md', 'requirements.txt')


def wrappers(source, harness='all'):
    if harness not in {'all', 'standard', 'agentic'}:
        raise ValueError('Unknown harness profile: ' + harness)
    vendor = Path(source) / 'vendor/microsoft/skills-for-copilot-studio'
    result = {}
    # Always expose the solution orchestrator; component-specific wrappers remain
    # controlled by --harness. All references are bundled with the main skill.
    result['one-prompt-solution-builder'] = '\n'.join([
        '---', 'name: one-prompt-solution-builder',
        'description: ' + json.dumps('Use when one GitHub Copilot prompt should orchestrate a complete Copilot Studio solution across agents, workflows, SharePoint, Teams and integrations, with validation and explicit release gates.'),
        '---', '', '# PurpleBelt: One-Prompt Solution Builder', '',
        'Read `../copilot-studio-builder/SKILL.md` and `../copilot-studio-builder/references/one-prompt-solution-builder.md` first.',
        'Use `../copilot-studio-builder/assets/one-prompt-solution-template.md` for a build plan in the business project.',
        'Resolve paths relative to this file. Select only the relevant pinned Microsoft skills after identifying each component harness.',
        'One prompt is a continuous development workflow, not proof of zero-touch cloud deployment.',
        'Do not invent workflow APIs, cloud resource identifiers, connections or successful publication.', '',
    ])
    for path in sorted((vendor / 'skills').glob('*/SKILL.md')) if harness in {'all', 'standard'} else []:
        name = path.parent.name
        wrapper_name = 'mcs-' + name
        # Keep activation metadata short; full original guidance is loaded on demand.
        description = 'Use when authoring Microsoft Copilot Studio standard agents and the task requires ' + name.replace('-', ' ') + '.'
        result[wrapper_name] = '\n'.join([
            '---', 'name: ' + wrapper_name, 'description: ' + json.dumps(description), '---', '',
            '# Microsoft Copilot Studio: ' + name, '',
            'Read `../copilot-studio-builder/SKILL.md` first for environment and evidence requirements.',
            'Then read the complete upstream skill at `../copilot-studio-builder/vendor/microsoft/skills-for-copilot-studio/skills/' + name + '/SKILL.md`.',
            'Resolve these paths relative to this file. Use the original skill directory for every `${CLAUDE_SKILL_DIR}` substitution; it is a path placeholder, not a guaranteed exported environment variable in Copilot.',
            'Resolve original relative references from that original skill directory. Preserve the upstream directory layout.',
            'The standard-harness toolkit does not authorize cross-harness schema reuse, live mutations, secret disclosure, or chain-of-thought logging.',
            'Do not execute plugin hooks or install native dependencies unless required for the requested operation and permitted by the environment.', '',
        ])
    if harness in {'all', 'agentic'}:
        modern = Path(source) / 'vendor/microsoft/copilot-studio-plugin'
        for path in sorted((modern / 'skills').glob('*/SKILL.md')):
            operation = path.parent.name
            name = 'mcsa-' + operation
            result[name] = '\n'.join([
                '---', 'name: ' + name,
                'description: ' + json.dumps('Use when developing Microsoft Copilot harness (formerly GitHub Copilot harness) agents and the task requires ' + operation.replace('-', ' ') + '.'),
                '---', '', '# PurpleBelt agentic: ' + operation, '',
                'Read `../copilot-studio-builder/SKILL.md` and `../copilot-studio-builder/references/harness-agentic.md` first.',
                'Then read the complete original skill directory at `../copilot-studio-builder/vendor/microsoft/copilot-studio-plugin/skills/' + operation + '/SKILL.md`.',
                'Resolve all paths from this file. Use the original skill directory for relative references and the original plugin root for `${CLAUDE_PLUGIN_ROOT}`; these are path placeholders, not guaranteed Copilot environment variables.',
                'CLI-agent workspace evidence and current PAC command support are required. Standard topic schemas do not apply.',
                'Installation activates no hooks and supplies no tenant credentials. Local import is not cloud sync; cloud sync is not publish.', '',
            ])
    for profile in ('standard', 'agentic'):
        if harness not in {'all', profile}:
            continue
        name = 'copilot-studio-' + profile
        result[name] = '\n'.join([
            '---', 'name: ' + name,
            'description: ' + json.dumps('Use when a Copilot Studio ' + ('Standard' if profile == 'standard' else 'Microsoft Copilot / GitHub Copilot') + ' harness agent needs harness-specific authoring, validation or deployment guidance.'),
            '---', '', '# PurpleBelt: ' + profile, '',
            'Read `../copilot-studio-builder/SKILL.md`, then `../copilot-studio-builder/references/harness-' + profile + '.md`.',
            'Resolve paths relative to this file. Load only the selected harness and operation.', '',
        ])
    return result


def install(source, target, personal=False, harness='all'):
    source = Path(source).resolve()
    target = Path(target).expanduser().resolve()
    if not (source / 'SKILL.md').is_file():
        raise ValueError('Source must be the Copilot Studio Builder bundle root')
    if target == source or target.is_relative_to(source):
        raise ValueError('Install into a separate project or personal skills directory')
    dest_root = target if personal else target / '.github/skills'
    generated = wrappers(source, harness)
    names = ['copilot-studio-builder', *generated]
    conflicts = [name for name in names if (dest_root / name).exists()]
    if conflicts:
        raise FileExistsError('No files changed; skill paths already exist: ' + ', '.join(conflicts))
    # Validate every source part before creating anything in the user's project.
    for name in PARTS:
        if not (source / name).exists():
            raise ValueError('Incomplete bundle: ' + name)
    for repo in ('skills-for-copilot-studio', 'copilot-studio-plugin'):
        toolkit = source / 'vendor/microsoft' / repo
        if not (toolkit / 'LICENSE').is_file() or not list((toolkit / 'skills').glob('*/SKILL.md')):
            raise ValueError('Incomplete toolkit: ' + repo + '; run verify_bundle.py before installing')
    created = []
    try:
        dest_root.mkdir(parents=True, exist_ok=True)
        main = dest_root / 'copilot-studio-builder'
        main.mkdir()
        created.append(main)
        for name in PARTS:
            src, dst = source / name, main / name
            if src.is_dir():
                shutil.copytree(src, dst, ignore=shutil.ignore_patterns('__pycache__', '*.pyc', '.git'))
            else:
                shutil.copy2(src, dst)
        for name, content in generated.items():
            folder = dest_root / name
            folder.mkdir()
            created.append(folder)
            (folder / 'SKILL.md').write_text(content, encoding='utf-8')
    except Exception:
        for folder in reversed(created):
            shutil.rmtree(folder)
        raise
    return {'main': str(main), 'wrappers': list(generated), 'harness': harness, 'hooks_activated': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', type=Path, required=True, help='Project folder; or a personal skills root with --personal')
    parser.add_argument('--personal', action='store_true', help='Treat --target as the skills root directly')
    parser.add_argument('--harness', choices=('all', 'standard', 'agentic'), default='all', help='Limit discoverable skills; both pinned source bundles remain available')
    args = parser.parse_args()
    try:
        result = install(Path(__file__).resolve().parents[1], args.target, args.personal, args.harness)
    except (OSError, ValueError) as exc:
        parser.exit(2, str(exc) + '\n')
    print(json.dumps(result, indent=2))

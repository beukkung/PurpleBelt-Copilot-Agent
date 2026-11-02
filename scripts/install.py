"""Install a self-contained Copilot skill and discovery wrappers, without activating hooks."""
import argparse
import json
import shutil
from pathlib import Path

PARTS = ('SKILL.md', 'references', 'scripts', 'assets', 'vendor', 'upstream.lock.json', 'LICENSE', 'NOTICE.md', 'requirements.txt')


def wrappers(source):
    vendor = Path(source) / 'vendor/microsoft/skills-for-copilot-studio'
    result = {}
    for path in sorted((vendor / 'skills').glob('*/SKILL.md')):
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
    return result


def install(source, target, personal=False):
    source = Path(source).resolve()
    target = Path(target).expanduser().resolve()
    if not (source / 'SKILL.md').is_file():
        raise ValueError('Source must be the Copilot Studio Builder bundle root')
    if target == source or target.is_relative_to(source):
        raise ValueError('Install into a separate project or personal skills directory')
    dest_root = target if personal else target / '.github/skills'
    generated = wrappers(source)
    names = ['copilot-studio-builder', *generated]
    conflicts = [name for name in names if (dest_root / name).exists()]
    if conflicts:
        raise FileExistsError('No files changed; skill paths already exist: ' + ', '.join(conflicts))
    # Validate every source part before creating anything in the user's project.
    for name in PARTS:
        if not (source / name).exists():
            raise ValueError('Incomplete bundle: ' + name)
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
    return {'main': str(main), 'wrappers': list(generated), 'hooks_activated': False}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target', type=Path, required=True, help='Project folder; or a personal skills root with --personal')
    parser.add_argument('--personal', action='store_true', help='Treat --target as the skills root directly')
    args = parser.parse_args()
    try:
        result = install(Path(__file__).resolve().parents[1], args.target, args.personal)
    except (OSError, ValueError) as exc:
        parser.exit(2, str(exc) + '\n')
    print(json.dumps(result, indent=2))

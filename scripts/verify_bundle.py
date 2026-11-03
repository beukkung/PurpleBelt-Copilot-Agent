"""Verify the complete pinned Microsoft snapshot. Does not execute upstream code."""
import argparse
import hashlib
import json
from pathlib import Path


def verify_snapshot(root, manifest, directory):
    root = Path(root).resolve()
    errors = []
    try:
        lock = json.loads((root / manifest).read_text(encoding='utf-8'))
    except (OSError, ValueError) as exc:
        return {'errors': [str(exc)], 'checked': 0}
    vendor = root / 'vendor/microsoft' / directory
    entries = lock.get('files', [])
    if len(entries) != lock.get('file_count'):
        errors.append('Manifest file_count mismatch')
    expected = set()
    for entry in entries:
        name = entry['path']
        raw_path = vendor / name
        path = raw_path.resolve()
        if not path.is_relative_to(vendor.resolve()):
            errors.append('Unsafe manifest path: ' + name)
            continue
        expected.add(name)
        candidate = vendor
        symlinked = candidate.is_symlink()
        for part in Path(name).parts:
            candidate = candidate / part
            symlinked = symlinked or candidate.is_symlink()
        if not path.is_file() or symlinked:
            errors.append('Missing or symlink: ' + name)
            continue
        data = path.read_bytes()
        blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        if len(data) != entry['bytes'] or hashlib.sha256(data).hexdigest() != entry['sha256'] or blob != entry['git_blob_sha1']:
            errors.append('Content mismatch: ' + name)
    actual = {p.relative_to(vendor).as_posix() for p in vendor.rglob('*') if p.is_file()}
    for name in sorted(actual - expected):
        errors.append('Untracked upstream file: ' + name)
    return {'errors': errors, 'checked': len(entries), 'commit': lock.get('commit')}


def verify(root):
    snapshots = {
        name: verify_snapshot(root, manifest, name)
        for name, manifest in (
            ('skills-for-copilot-studio', 'upstream.lock.json'),
            ('copilot-studio-plugin', 'upstream-agentic.lock.json'),
        )
    }
    return {
        'errors': [name + ': ' + error for name, report in snapshots.items() for error in report['errors']],
        'checked': sum(report['checked'] for report in snapshots.values()),
        'snapshots': snapshots,
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    result = verify(args.root)
    print(json.dumps(result, indent=2))
    raise SystemExit(1 if result['errors'] else 0)

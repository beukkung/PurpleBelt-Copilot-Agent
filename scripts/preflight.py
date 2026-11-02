"""Read-only local inventory and heuristic lint; never tenant or Power Fx validation."""
import argparse
import json
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

EXCLUDED = {'.git', '.mcs', 'vendor', 'node_modules', '.venv', '__pycache__'}


def walk(value):
    if isinstance(value, dict):
        yield value
        for item in value.values():
            yield from walk(item)
    elif isinstance(value, list):
        for item in value:
            yield from walk(item)


def strict_loader():
    class UniqueLoader(yaml.SafeLoader):
        pass

    def mapping(loader, node, deep=False):
        loader.flatten_mapping(node)
        result = {}
        for key_node, value_node in node.value:
            key = loader.construct_object(key_node, deep=deep)
            if key in result:
                raise ValueError('duplicate YAML key at line ' + str(key_node.start_mark.line + 1))
            result[key] = loader.construct_object(value_node, deep=deep)
        return result

    UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)
    return UniqueLoader


def inspect_workspace(root):
    root = Path(root).resolve()
    result = {
        'validation_level': 'static-preflight', 'tenant_verified': False,
        'blockers': [], 'warnings': [], 'files': [], 'connectors': [],
        'connection_metadata_present': False,
        'not_checked': ['Power-Fx semantics', 'Microsoft authoring schema', 'cross-file logical bindings', 'DLP', 'licensing', 'authentication', 'deployment', 'runtime effects'],
    }
    if not root.is_dir():
        result['blockers'].append({'code': 'missing_workspace', 'file': str(root)})
        return result
    result['connection_metadata_present'] = (root / '.mcs/conn.json').is_file()
    if yaml is None:
        result['blockers'].append({'code': 'missing_dependency', 'message': 'Install PyYAML from requirements.txt; YAML was not parsed.'})
        return result
    connectors = set()
    agent_count = 0
    for path in sorted(root.rglob('*')):
        rel = path.relative_to(root)
        if path.is_symlink() or any(part in EXCLUDED for part in rel.parts) or not path.is_file():
            continue
        is_mcs = path.name.endswith(('.mcs.yml', '.mcs.yaml'))
        is_flow = path.name in {'workflow.json', 'definition.json'}
        if not (is_mcs or is_flow):
            continue
        if path.stat().st_size > 5_000_000:
            result['warnings'].append({'code': 'file_too_large', 'file': rel.as_posix()})
            continue
        try:
            raw = path.read_text(encoding='utf-8-sig')
            data = yaml.load(raw, Loader=strict_loader()) if is_mcs else json.loads(raw)
            if not isinstance(data, dict):
                raise ValueError('Expected a mapping at the document root')
        except (OSError, ValueError, yaml.YAMLError) as exc:
            # Avoid echoing tenant content or credentials through parser excerpts.
            result['blockers'].append({'code': 'parse_error', 'file': rel.as_posix(), 'message': 'duplicate YAML key' if 'duplicate YAML key' in str(exc) else type(exc).__name__})
            continue
        kind = data.get('kind')
        if kind == 'GptComponentMetadata':
            agent_count += 1
        config_file = path.name in {'settings.mcs.yml', 'settings.mcs.yaml', 'connectionreferences.mcs.yml', 'connectionreferences.mcs.yaml'}
        if is_mcs and not kind and not config_file:
            result['warnings'].append({'code': 'no_root_kind', 'file': rel.as_posix()})
        ids = set()
        for node in walk(data):
            node_id = node.get('id')
            if node.get('kind') and isinstance(node_id, str):
                if node_id in ids:
                    result['blockers'].append({'code': 'duplicate_node_id', 'file': rel.as_posix(), 'node_id': node_id})
                ids.add(node_id)
            for field in ('connectionReference', 'operationId'):
                if isinstance(node.get(field), str):
                    connectors.add(node[field])
            if node.get('type') == 'InitializeVariable':
                for item in node.get('inputs', {}).get('variables', []):
                    name = item.get('name', '')
                    if item.get('value') is True and any(word in name.lower() for word in ('success', 'updated', 'completed', 'verified')):
                        result['warnings'].append({'code': 'success_initialized_true', 'file': rel.as_posix(), 'variable': name, 'message': 'Heuristic: confirm success is reset on every zero-result and failure path.'})
        result['files'].append({'file': rel.as_posix(), 'kind': kind or ('configuration-yaml' if is_mcs else 'flow-json')})
    if not result['files']:
        result['blockers'].append({'code': 'no_native_files', 'message': 'Provide a cloned agent workspace, not the skill repository.'})
    if not agent_count:
        result['warnings'].append({'code': 'no_agent_metadata', 'message': 'A component-only folder does not establish agent harness or configuration.'})
    result['connectors'] = sorted(connectors)
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('workspace', type=Path)
    args = parser.parse_args()
    report = inspect_workspace(args.workspace)
    print(json.dumps(report, indent=2))
    raise SystemExit(2 if report['blockers'] else 0)

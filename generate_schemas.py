# Script to generate JSON schemas from YAML schemas

import json
import yaml
from pathlib import Path


ENTITIES = [
    'definitions',
    'settings',
    'operator',
    'place',
    'route',
    'connection',
    'translation',
    'graphic'
]
CUSTOM_KEYS = {'examples'}


def remove_custom_keys_in_place(data):
    stack = [data]
    while stack:
        current = stack.pop()

        if isinstance(current, list):
            stack.extend(current)
            continue

        if isinstance(current, dict):
            custom_keys = [k for k in current if k in CUSTOM_KEYS]
            for k in custom_keys:
                del current[k]

            stack.extend(current.values())
            continue


if __name__ == '__main__':
    for entity in ENTITIES:
        yaml_path = Path('schema_yaml') / f'{entity}.yml'
        with open(yaml_path, mode='r') as fin:
            schema = yaml.load(fin, yaml.SafeLoader)

        remove_custom_keys_in_place(schema)

        json_path = Path('schema') / f'{entity}.json'
        with open(json_path, mode='w') as fout:
            json.dump(schema, fout, indent=4)

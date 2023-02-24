import json
import yaml
from pathlib import Path

if __name__ == '__main__':
    ENTITIES = [
        'definitions',
        'settings',
        'agencies',
        'footpaths',
        'graphics',
        'routes',
        'stops',
        'translations',
    ]

    for entity in ENTITIES:
        json_path = Path('schema') / f'{entity}.json'
        with open(json_path, mode='r') as fin:
            schema = json.load(fin)

        yaml_path = Path('schema_yaml') / f'{entity}.yml'
        with open(yaml_path, mode='w') as fout:
            yaml.dump(schema, fout, sort_keys=False)

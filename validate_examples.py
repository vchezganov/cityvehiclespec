# Script to validate examples according schema definitions

import pathlib
import json
import jsonschema


def validate_examples(entity_name: str):
    # path_root = pathlib.Path().resolve()
    # resolver = jsonschema.validators.RefResolver(base_uri=f'{path_root.as_uri()}/',
    #                                              referrer=True)

    # resolver = jsonschema.validators.RefResolver(base_uri='https://github.com/vchezganov/cityvehiclespec/',
    #                                              referrer=True)

    folder_schema = pathlib.Path('schema')
    store = {}

    for f in [
        'definitions.json',
        'place/transit_stop.json',
        'place/access_point.json',
        'place/parking_lot.json',
        'place/transit_stop.json',
    ]:
        with open(folder_schema / f, mode='r') as fin:
            sub_schema = json.load(fin)

        store[sub_schema['$id']] = sub_schema

    with open(folder_schema / f'{entity_name}.json', mode='r') as fin:
        entity_schema = json.load(fin)

    store[entity_schema['$id']] = entity_schema

    resolver = jsonschema.RefResolver(base_uri='https://github.com/vchezganov/cityvehiclespec/schema/',
                                      referrer=True,
                                      store=store)

    folder_examples = pathlib.Path('examples') / entity_name
    for path_example in folder_examples.iterdir():
        if not path_example.is_file():
            continue

        print(f'- {path_example}:', end=' ')

        with open(path_example, mode='r') as fin:
            example = json.load(fin)

        try:
            jsonschema.validate(example, schema=entity_schema, resolver=resolver)
            # jsonschema.validate(example, schema={'$ref': f'{entity_name}.json'}, resolver=resolver)
            print('OK')
        except Exception as ex:
            print('FAIL')
            print(ex)


if __name__ == '__main__':
    for entity_name in ('settings', 'operator', 'place', 'route', 'translation'):
        print('Validating', entity_name)
        validate_examples(entity_name)

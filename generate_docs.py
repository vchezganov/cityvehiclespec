import argparse
import pathlib
import json
import functools
from urllib.parse import urlparse
from dataclasses import dataclass
from typing import Any, Optional

from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(loader=FileSystemLoader('templates'),
                  autoescape=select_autoescape(),
                  trim_blocks=True)


ENTITIES = [
    'settings',
    'operator',
    'place',
    'route',
    'connection',
    'translation',
    'graphic'
]
CUSTOM_KEYS = {'examples'}
UNIQUE_ID = 0


def generate_id() -> str:
    global UNIQUE_ID

    UNIQUE_ID += 1
    return f'block{UNIQUE_ID}'


@dataclass
class RenderData:
    name: str
    kind: str
    description: str
    is_arrow: bool
    is_required: bool
    sub_render: Optional[str] = None
    addition: Optional[str] = None
    examples: Optional[list[str]] = None

    def render(self, render_itself: bool = True):
        optionality = ''
        if self.is_required:
            optionality = '<br /><span class="required">required</span>'

        first_div = f'<div>{self.name}{optionality}</div>'
        if self.is_arrow:
            first_div = f'<div><span class="arrow">{self.name}{optionality}</span></div>'

        description = self.description
        if (addition := self.addition) is not None:
            description += f'''
<pre class="addition">
{addition}
</pre>
            '''

        if (examples := self.examples) is not None:
            for example in examples:
                tmp = json.dumps(example, ensure_ascii=False, indent=2)
                description += f'''
<div markdown="1">
```json
{tmp.strip()}
```
</div>
                '''

        result = ''

        if render_itself:
            itself = f'''
<div class="field">
    {first_div}
    <div>{self.kind}</div>
    <div>{description}</div>
</div>
'''

            if self.is_arrow:
                block_id = generate_id()

                result += f'''
<div id="{block_id}" class="active" onclick="toggle(event);">
    {itself}
</div>
<div id="sub_{block_id}" class="shift hidden">
    {self.sub_render}
</div>
'''
            else:
                result += itself
        else:
            if self.sub_render is not None:
                result += self.sub_render

        return result


class Render:
    def __init__(self, folder_schema: pathlib.Path) -> None:
        self.folder_schema = folder_schema

    def render_field(self,
                     field_name: str,
                     field_data: dict[str, Any],
                     is_required: bool,
                     level: int = 0) -> RenderData:
        field_type = field_data.get('type', 'unknown')
        description = field_data.get('description', '')
        examples = field_data.get('examples')

        # Object
        if field_type == 'object':
            required = field_data.get('required', [])
            properties = field_data.get('properties', {})

            result = ''
            for name, data in properties.items():
                render_data = self.render_field(name, data, name in required)
                result += render_data.render()

            return RenderData(name=field_name,
                              kind=field_type,
                              description=description,
                              is_arrow=len(properties) > 0,
                              is_required=is_required,
                              sub_render=result,
                              examples=examples)

        # Reference
        if (ref_link := field_data.get('$ref')) is not None:
            ref_data = self.parse_ref(ref_link)
            render_data = self.render_field(field_name, ref_data, is_required)
            description = description or render_data.description

            return RenderData(name=render_data.name,
                              kind=render_data.kind,
                              description=description,
                              is_arrow=render_data.is_arrow,
                              is_required=render_data.is_required,
                              sub_render=render_data.sub_render,
                              addition=render_data.addition)

        # Array
        if field_type == 'array':
            if (data := field_data.get('items')) is not None:
                render_data = self.render_field(field_name, data, is_required)
                description = description or render_data.description

                return RenderData(name=field_name,
                                  kind=f'[]{render_data.kind}',
                                  description=description,
                                  is_arrow=render_data.is_arrow,
                                  is_required=is_required,
                                  sub_render=render_data.render(render_itself=False),
                                  addition=render_data.addition,
                                  examples=render_data.examples)

            items = field_data.get('prefixItems', [])
            min_items = field_data.get('minItems', 0)
            max_items = field_data.get('maxItems', 0)

            result = ''
            kinds = []
            for i, data in enumerate(items, start=0):
                is_item_required = i < min_items
                render_data = self.render_field(f'[{i}]', data, is_item_required)
                result += render_data.render()
                kinds.append(render_data.kind)

            kinds = ', '.join(kinds)

            return RenderData(name=field_name,
                              kind=f'[{kinds}]',
                              description=description,
                              is_arrow=True,
                              is_required=is_required,
                              sub_render=result)

        # One of
        one_ofs = field_data.get('oneOf')
        if one_ofs is not None:
            result = ''
            for i, one_of in enumerate(one_ofs, start=1):
                render_data = self.render_field(f'#{i}', one_of, is_required)
                result += render_data.render()

            return RenderData(name=field_name,
                              kind='one of',
                              description=description,
                              is_arrow=True,
                              is_required=is_required,
                              sub_render=result)

        # Enum
        enums = field_data.get('enum')
        if enums is not None:
            all_enums = '\n'.join(enums)

            return RenderData(name=field_name,
                              kind='enum',
                              description=description,
                              is_arrow=False,
                              is_required=is_required,
                              addition=all_enums)

        # Simple type and all other not impleneted types
        if isinstance(field_type, list):
            field_type = ' | '.join(field_type)

        return RenderData(name=field_name,
                          kind=field_type,
                          description=description,
                          is_arrow=False,
                          is_required=is_required,
                          examples=examples)

    @functools.cache
    def load_ref(self, schema_path: str) -> dict[str, Any]:

        with open(self.folder_schema / schema_path, mode='r') as fin:
            definition_schema = json.load(fin)

        stack = [definition_schema]
        while stack:
            current = stack.pop()

            if isinstance(current, dict):
                ref = current.get('$ref')
                if ref is not None and ref.startswith('#'):
                    current['$ref'] = f'{schema_path}{ref}'

                stack.extend(current.values())
                continue

            if isinstance(current, list):
                stack.extend(current)
                continue

        return definition_schema

    @functools.cache
    def parse_ref(self, ref: str) -> dict[str, Any]:
        result = urlparse(ref)
        definition_schema = self.load_ref(result.path)

        if not result.fragment:
            return definition_schema

        sub_path = pathlib.PosixPath(result.fragment)
        data = None

        for key in sub_path.parts:
            if key == '/':
                data = definition_schema
            else:
                data = data[key]

        return data


def remove_custom_keys_in_place(data):
    stack = [data]
    while stack:
        current = stack.pop()

        if isinstance(current, list):
            stack.extend(current)

        elif isinstance(current, dict):
            custom_keys = [k for k in current if k in CUSTOM_KEYS]
            for k in custom_keys:
                del current[k]

            stack.extend(current.values())


def generate_template(folder_schema: pathlib.Path,
                      folder_example: pathlib.Path,
                      folder_output: pathlib.Path,
                      entity_name: str,
                      description: str):
    print('Rendering template:', entity_name)
    output_path = folder_output / f'{entity_name}.markdown'

    # Loading entity schema
    with open(folder_schema / f'{entity_name}.json', mode='r') as fin:
        json_schema = json.load(fin)

    remove_custom_keys_in_place(json_schema)
    entity_schema = json.dumps(json_schema, indent=2, ensure_ascii=False)

    # Loading examples if any
    folder_examples = folder_example / entity_name
    examples = []
    if folder_examples.is_dir():
        example_paths = [e for e in folder_examples.iterdir() if e.is_file() and e.suffix == '.json']
        example_paths.sort()

        for example_path in example_paths:
            with open(example_path, mode='r') as fin:
                json_example = json.load(fin)

            text_example = json.dumps(json_example, indent=2, ensure_ascii=False)
            examples.append(text_example)

    try:
        # Loading entity template
        entity_template = env.get_template(f'{entity_name}.md')

        ctx = {
            'title': entity_name,
            'permalink': entity_name,
            'description': description,
            'schema': entity_schema,
            'examples': examples
        }

        # Rendering template
        with open(output_path, mode='w') as fout:
            entity_template.stream(ctx).dump(fout)
    except Exception as ex:
        print('Exception:', ex)


def generate_docs(folder_schema: pathlib.Path,
                  folder_example: pathlib.Path,
                  folder_output: pathlib.Path,
                  nohtml: bool = False):
    render = Render(folder_schema)

    for entity_name in ENTITIES:
        with open(folder_schema / f'{entity_name}.json', mode='r') as fin:
            entity_schema = json.load(fin)

        print('Rendering documentation:', entity_name)
        render_data = render.render_field(entity_name, entity_schema, True)
        documentation = render_data.render(render_itself=False)

        generate_template(folder_schema, folder_example, folder_output, entity_name, documentation)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='jsonschema2doc',
                                     description='Generating documentation out of JSON schema')

    parser.add_argument('--schema',
                        required=True,
                        help='Schema folder')

    parser.add_argument('--example',
                        required=True,
                        help='Example folder')

    parser.add_argument('--output',
                        required=True,
                        help='Output folder')

    parser.add_argument('--nohtml',
                        default=False,
                        action='store_true',
                        help='No html and body tags to generate')

    args = parser.parse_args()

    generate_docs(pathlib.Path(args.schema), pathlib.Path(args.example), pathlib.Path(args.output), args.nohtml)

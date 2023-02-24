import argparse
import pathlib
import json
import yaml
from urllib.parse import urlparse
from dataclasses import dataclass
from typing import Any, Optional, List, Dict


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
    examples: Optional[List[str]] = None

    def render(self, render_itself: bool = True):
        arrow = ''
        if self.is_arrow:
            arrow = '&nbsp;&gt;'

        optionality = ''
        if self.is_required:
            optionality = '<br /><span class="required">required</span>'

        description = self.description
        if (addition := self.addition) is not None:
            description += f'''
<pre class="addition">
{addition}
</pre>
            '''

        if (examples := self.examples) is not None:
            for example in examples:
                description += f'''
<div markdown="1">
```json
{example.strip()}
```
</div>
                '''

        result = ''

        if render_itself:
            itself = f'''
<div class="field">
    <div>{self.name}{arrow}{optionality}</div>
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
<div id="sub_{block_id}" class="shift">
    {self.sub_render}
</div>
'''
            else:
                result += itself
        else:
            if self.sub_render is not None:
                result += self.sub_render

        return result


def render_field(field_name: str,
                 field_data: Dict[str, Any],
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
            render_data = render_field(name, data, name in required)
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
        ref_data = parse_ref(ref_link)
        render_data = render_field(field_name, ref_data, is_required)
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
            render_data = render_field(field_name, data, is_required)
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
            render_data = render_field(f'[{i}]', data, is_item_required)
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
            render_data = render_field(f'#{i}', one_of, is_required)
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


def parse_ref(ref: str) -> Dict[str, Any]:
    result = urlparse(ref)
    folder_schema = pathlib.Path('schema')

    with open(folder_schema / result.path, mode='r') as fin:
        definition_schema = json.load(fin)

    stack = [definition_schema]
    while stack:
        current = stack.pop()
        if isinstance(current, dict):
            ref = current.get('$ref')
            if ref is not None and ref.startswith('#'):
                current['$ref'] = f'{result.path}{ref}'

            for data in current.values():
                stack.append(data)

        if isinstance(current, list):
            for data in current:
                stack.append(data)

    sub_path = pathlib.PosixPath(result.fragment)
    data = None

    for key in sub_path.parts:
        if key == '/':
            data = definition_schema
        else:
            data = data[key]

    return data


ENTITIES = [
    'settings',
    'agencies',
    'stops',
    'routes',
    'footpaths',
    'translations',
    'graphics'
]


def generate_html(folder_schema: pathlib.Path,
                  folder_output: pathlib.Path,
                  nohtml: bool = False):
    for entity_name in ENTITIES:
        # with open(folder_schema / f'{entity_name}.json', mode='r') as fin:
        #     entity_schema = json.load(fin)
        with open(folder_schema / f'{entity_name}.yml', mode='r') as fin:
            entity_schema = yaml.load(fin, yaml.CLoader)

        render_data = render_field(entity_name, entity_schema, True)
        documentation = render_data.render(render_itself=False)

        entity_path = folder_output / f'{entity_name}.html'

        with open(entity_path, mode='w') as fout:
            if not nohtml:
                fout.write('''
<html>
<head>
    <link rel="stylesheet" type="text/css" href="static/style.css">

    <script type="text/javascript" src="static/script.js"></script>
</head>
<body>
''')

            fout.write('<div class="main">')
            fout.write(documentation)
            fout.write('</div>')

            if not nohtml:
                fout.write('''
</body>
</html>
''')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='jsonschema2doc',
                                     description='Generating documentation out of JSON schema')

    parser.add_argument('--output',
                        default='documentation',
                        help='Output folder')

    parser.add_argument('--nohtml',
                        default=False,
                        action='store_true',
                        help='No html and body tags to generate')

    args = parser.parse_args()

    # generate_html(pathlib.Path('schema'), pathlib.Path(args.output), args.nohtml)
    generate_html(pathlib.Path('schema_yaml'), pathlib.Path(args.output), args.nohtml)

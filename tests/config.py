from pathlib import Path
import json
from referencing import Registry, Resource
from referencing.jsonschema import DRAFT202012
from jsonschema import Draft202012Validator
import re

root_path = Path(__file__).parents[1]
schema_root_path = root_path / 'schema'
va_spec_path = schema_root_path / 'va-spec'

test_path = root_path / 'tests'
fixtures_path = test_path / 'fixtures'

ga4gh_re = re.compile(r'.*\/ga4gh\/schema\/([\w\-\.]+)\/[\w\-\.]+\/(.*)$')

def retrieve_rel_ref(ga4gh_ref: str):
    ga4gh_match = ga4gh_re.match(ga4gh_ref)
    if ga4gh_match is None:
        raise ValueError(f'ga4gh_ref {ga4gh_ref} is not a root GA4GH reference')
    schema_module = ga4gh_match.group(1)
    local_path = ga4gh_match.group(2)
    resolved_path = (schema_root_path / schema_module / local_path).resolve()
    schema = json.loads(resolved_path.read_text())
    return Resource.from_contents(schema)

js_registry = Registry(retrieve=retrieve_rel_ref)
js_def = dict()
validator = dict()

paths = list(schema_root_path.glob('*/json/*'))+list(va_spec_path.glob('*/json/*'))

for schema_path in paths:
    content = json.loads(schema_path.read_text())
    schema_uri = schema_path.as_uri()
    content['id'] = schema_uri
    schema_resource = Resource(contents=content, specification=DRAFT202012)
    js_def[schema_path.stem] = content
    js_registry = js_registry.with_resources([
        (schema_path.name, schema_resource),
        (schema_uri, schema_resource)
    ])

for cls in js_def:
    validator[cls] = Draft202012Validator(js_def[cls], registry=js_registry)
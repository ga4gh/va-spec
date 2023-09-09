import yaml
from pathlib import Path
from jsonschema import validate

ROOT_PATH = Path(__file__).parent.parent
TEST_PATH = ROOT_PATH / 'tests'
FIXTURES_PATH = TEST_PATH / 'fixtures'


with open(FIXTURES_PATH / 'allele.yaml') as f:
    allele = yaml.safe_load(f)

SCHEMA_URI_ROOT = (ROOT_PATH / 'schema').as_uri()


def get_schema(schema_file, schema_class, kw="$defs"):
   return {
      "$ref": SCHEMA_URI_ROOT + f"/{schema_file}.json#/{kw}/{schema_class}"
   }


def test_allele_validation():
    schema = get_schema("vrs", "Allele", kw="$defs")
    assert validate(allele, schema) is None


def test_examples():
    with open(TEST_PATH / 'test_definitions.yaml') as def_file:
        test_spec = yaml.safe_load(def_file)
    for test in test_spec['tests']:
        with open(FIXTURES_PATH / test['test_file']) as datafile:
            data = yaml.safe_load(datafile)
        schema = get_schema(
            test['schema'],
            test['definition'],
            test.get('kw', '$defs')
        )
        assert validate(data, schema) is None

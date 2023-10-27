import pytest
import jsonschema as js
import yaml
from config import cohort_allele_frequency_schema_yaml_path, cohort_allele_frequency_example_yaml_path


def test_cohort_allele_frequency():
    with open(cohort_allele_frequency_schema_yaml_path, 'r') as schema_in, \
            open(cohort_allele_frequency_example_yaml_path, 'r') as example_in:
        schema = yaml.safe_load(schema_in)
        example = yaml.safe_load(example_in)
    js.validate(example, schema)

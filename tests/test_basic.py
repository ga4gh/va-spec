import yaml
from pathlib import Path
from jsonschema import validate
from config import fixtures_path, validator


with open(fixtures_path / 'allele.yaml') as f:
    allele = yaml.safe_load(f)


def test_allele_validation():
    assert validator['Allele'].validate(allele) is None

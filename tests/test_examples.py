from config import test_path, fixtures_path
import yaml
from config import validator

def test_examples():
    with open(test_path / 'test_definitions.yaml') as def_file:
        test_spec = yaml.safe_load(def_file)

    for test in test_spec['tests']:
        with open(fixtures_path / test['test_file']) as datafile:
            data = yaml.safe_load(datafile)
            
        class_validator = validator[test['definition']]

        try:
            assert class_validator.validate(data) is None
        except AssertionError as e:
            raise AssertionError(f"AssertionError in {test['test_file']}: {e}")

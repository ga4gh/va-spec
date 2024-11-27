from config import test_path, fixtures_path
import yaml
from config import validator, js_def, coverage

def _get_trial_use_classes():
    return set([x for x in js_def if x.startswith('va-spec') and js_def[x]['maturity'] == 'trial use'])

va_abstract_classes = {'va-spec.base:SubjectVariantProposition', 'va-spec.base:Condition', 'va-spec.base:Therapeutic'}

def test_examples():
    with open(test_path / 'test_definitions.yaml') as def_file:
        test_spec = yaml.safe_load(def_file)

    for test in test_spec['tests']:
        with open(fixtures_path / test['test_file']) as datafile:
            data = yaml.safe_load(datafile)
        test_cls_name = f"{test['namespace']}:{test['definition']}"
        class_validator = validator[test_cls_name]

        try:
            assert class_validator.validate(data) is None
        except AssertionError as e:
            raise AssertionError(f"AssertionError in {test['test_file']}: {e}")
        
def test_trial_use_class_coverage():
    trial_use_classes = _get_trial_use_classes()
    tested_classes = set()

    with open(test_path / 'test_definitions.yaml') as def_file:
        test_spec = yaml.safe_load(def_file)

    for test in test_spec['tests']:
        test_cls_name = f"{test['namespace']}:{test['definition']}"
        tested_classes.add(test_cls_name)

    assert len(trial_use_classes - tested_classes - va_abstract_classes) == 0

def test_trial_use_property_coverage():
    trial_use_classes = _get_trial_use_classes()
    with open(test_path / 'test_definitions.yaml') as def_file:
        test_spec = yaml.safe_load(def_file)

    with open(test_path / 'tu_coverage_exceptions.yaml') as except_file:
        exceptions = yaml.safe_load(except_file)
    
    for test in test_spec['tests']:
        with open(fixtures_path / test['test_file']) as datafile:
            data = yaml.safe_load(datafile)
        test_cls_name = f"{test['namespace']}:{test['definition']}"
        if test_cls_name not in trial_use_classes:
            continue
        class_definition = js_def[test_cls_name]
        if not isinstance(class_definition, dict):
            raise ValueError('Expected only object data')
        for p in data:
            if p in coverage[test_cls_name]:
                coverage[test_cls_name][p] = True

    no_coverage_properties = set()
    for tu_class in trial_use_classes:
        for tu_class_property, covered in coverage[tu_class].items():
            if tu_class_property in exceptions.get(tu_class, dict()):
                continue
            elif covered is False:
                no_coverage_properties.add(f'{tu_class}.{tu_class_property}')
    
    assert(len(no_coverage_properties) == 0), \
       f"The following properties lack test coverage: {no_coverage_properties}"

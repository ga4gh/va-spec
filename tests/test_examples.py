from jsonschema import ValidationError
from config import test_path, fixtures_path
import yaml
from config import validator, js_def, coverage

# Coverage is enforced on every class at 'draft' maturity or above -- i.e. everything
# except 'deprecated' (no va-spec class is 'normative' yet, but that tier is included
# for when one is). This intentionally covers draft classes too: a class shipping in a
# ballot should have at least one validating example and full property coverage before
# it graduates to trial use, not after.
_COVERED_MATURITIES = {'draft', 'trial use', 'normative'}

def _get_covered_classes():
    return set(x for x in js_def if x.startswith('va-spec') and js_def[x]['maturity'] in _COVERED_MATURITIES)

# Abstract va-spec classes are not directly instantiated, so they have no standalone
# example and their (inherited) properties can never be covered by an instance. The
# 0.4.x metaschema processor emits a JSON schema for every abstract class (0.3.x did
# not), so all abstract classes must be excluded from both coverage checks.
va_abstract_classes = {
    'va-spec:InformationEntity',
    'va-spec:StudyResult',
    'va-spec:Proposition',
    'va-spec:SubjectVariantProposition',
    'va-spec:GeneticContextVariantProposition',
    'va-spec:Condition',
    'va-spec:Therapy',
}

va_excluded_classes = va_abstract_classes

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
        except (AssertionError, ValidationError) as e:
            raise AssertionError(f"AssertionError in {test['test_file']}: {e}")

def test_class_coverage():
    covered_classes = _get_covered_classes()
    tested_classes = set()

    with open(test_path / 'test_definitions.yaml') as def_file:
        test_spec = yaml.safe_load(def_file)

    for test in test_spec['tests']:
        test_cls_name = f"{test['namespace']}:{test['definition']}"
        tested_classes.add(test_cls_name)

    print(covered_classes - tested_classes - va_excluded_classes)
    assert len(covered_classes - tested_classes - va_excluded_classes) == 0

def test_property_coverage():
    covered_classes = _get_covered_classes()
    with open(test_path / 'test_definitions.yaml') as def_file:
        test_spec = yaml.safe_load(def_file)

    with open(test_path / 'tu_coverage_exceptions.yaml') as except_file:
        exceptions = yaml.safe_load(except_file)

    for test in test_spec['tests']:
        with open(fixtures_path / test['test_file']) as datafile:
            data = yaml.safe_load(datafile)
        test_cls_name = f"{test['namespace']}:{test['definition']}"
        if test_cls_name not in covered_classes:
            continue
        class_definition = js_def[test_cls_name]
        if not isinstance(class_definition, dict):
            raise ValueError('Expected only object data')
        for p in data:
            if p in coverage[test_cls_name]:
                coverage[test_cls_name][p] = True

    no_coverage_properties = set()
    for tu_class in covered_classes - va_excluded_classes:
        for tu_class_property, covered in coverage[tu_class].items():
            if tu_class_property in exceptions.get(tu_class, dict()):
                continue
            elif covered is False:
                no_coverage_properties.add(f'{tu_class}.{tu_class_property}')

    assert(len(no_coverage_properties) == 0), \
       f"The following properties lack test coverage: {no_coverage_properties}"

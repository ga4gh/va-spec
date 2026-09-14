"""Negative validation tests.

The example suite (test_examples.py) is positive-only: it confirms valid
instances validate. These cases confirm that invalid instances are *rejected*,
covering the guarantees callers rely on: closed concrete classes, required
fields, `type` const discriminators, and enforcement of the abstract base
contract through a concrete class's `$ref`s.
"""
import pytest
from jsonschema import ValidationError
from config import validator

# (label, class namespace:name, invalid instance)
NEGATIVE_CASES = [
    (
        "concrete class rejects an unknown property (closed)",
        "va-spec:VariantPathogenicityProposition",
        {"type": "VariantPathogenicityProposition", "subject": "ex:v",
         "predicate": "isCausalFor", "object": "ex:c", "notAField": 1},
    ),
    (
        "concrete class rejects a missing required property",
        "va-spec:VariantPathogenicityProposition",
        {"type": "VariantPathogenicityProposition", "subject": "ex:v", "object": "ex:c"},
    ),
    (
        "concrete class rejects a wrong 'type' const",
        "va-spec:VariantPathogenicityProposition",
        {"type": "NotThisType", "subject": "ex:v",
         "predicate": "isCausalFor", "object": "ex:c"},
    ),
    (
        "concrete class rejects a wrong 'predicate' const",
        "va-spec:VariantPathogenicityProposition",
        {"type": "VariantPathogenicityProposition", "subject": "ex:v",
         "predicate": "notTheRightPredicate", "object": "ex:c"},
    ),
    (
        "Statement rejects a missing required 'direction'",
        "va-spec:Statement",
        {"type": "Statement",
         "proposition": {"type": "MyOrgProp", "subject": {"id": "x", "type": "G"},
                         "predicate": "p", "object": "ex:o"}},
    ),
    (
        "Statement rejects a proposition that violates the base contract",
        "va-spec:Statement",
        {"type": "Statement", "direction": "supports",
         "proposition": {"type": "MyOrgProp", "subject": {"id": "x", "type": "G"},
                         "object": "ex:o"}},  # missing required predicate
    ),
    (
        "StudyResult subclass rejects a missing required 'focus'",
        "va-spec:CohortAlleleFrequencyStudyResult",
        {"type": "CohortAlleleFrequencyStudyResult", "focusAlleleCount": 1,
         "locusAlleleCount": 2, "focusAlleleFrequency": 0.5,
         "cohort": {"type": "StudyGroup"}},
    ),
]


@pytest.mark.parametrize(
    "cls,instance",
    [(c[1], c[2]) for c in NEGATIVE_CASES],
    ids=[c[0] for c in NEGATIVE_CASES],
)
def test_invalid_instance_is_rejected(cls, instance):
    with pytest.raises(ValidationError):
        validator[cls].validate(instance)

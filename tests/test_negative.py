"""Negative validation tests.

The example suite (test_examples.py) is positive-only: it confirms valid
instances validate. These cases confirm that invalid instances are *rejected*,
covering the guarantees callers rely on: closed concrete classes, required
fields, `type` const discriminators, covariant narrowing of inherited
subject/object/focus attributes, community-profile conditional (if/then)
constraints, and enforcement of the abstract base contract through a concrete
class's `$ref`s.
"""
import yaml
import pytest
from copy import deepcopy
from jsonschema import ValidationError
from config import validator, fixtures_path

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
        "Statement rejects a missing required 'proposition'",
        "va-spec:Statement",
        {"type": "Statement", "direction": "supports"},
    ),
    (
        "Statement rejects a proposition that violates the base contract",
        "va-spec:Statement",
        {"type": "Statement", "direction": "supports",
         "proposition": {"type": "MyOrgProp", "subject": {"id": "x", "type": "G"},
                         "object": "ex:o"}},  # missing required predicate
    ),
    (
        # Statement.hasEvidenceLines is EvidenceLine | iriReference. A bare
        # Statement (not an EvidenceLine) must be rejected there -- this locks in
        # the "a Statement is not itself an Evidence Line" guarantee.
        "Statement.hasEvidenceLines rejects a bare Statement item",
        "va-spec:Statement",
        {"type": "Statement", "proposition": "ex:prop", "direction": "supports",
         "hasEvidenceLines": [{"type": "Statement", "proposition": "ex:prop",
                               "direction": "supports"}]},
    ),
    (
        # EvidenceLine no longer defines hasEvidenceLines; a nested Evidence Line
        # goes in hasEvidenceItems instead. The removed property must be rejected.
        "EvidenceLine rejects a removed 'hasEvidenceLines' property",
        "va-spec:EvidenceLine",
        {"type": "EvidenceLine", "directionOfEvidenceProvided": "supports",
         "hasEvidenceLines": []},
    ),
    (
        # Statement.hasEvidenceItems was renamed to hasEvidence; the old name
        # must be rejected (Statement is a closed class).
        "Statement rejects the renamed-away 'hasEvidenceItems'",
        "va-spec:Statement",
        {"type": "Statement", "proposition": "ex:prop", "hasEvidenceItems": []},
    ),
    (
        "StudyResult subclass rejects a missing required 'focus'",
        "va-spec:CohortAlleleFrequencyStudyResult",
        {"type": "CohortAlleleFrequencyStudyResult", "focusCount": 1,
         "locusCount": 2, "alleleFrequency": 0.5,
         "cohort": {"type": "StudyGroup"}},
    ),
    (
        # Covariant narrowing: CohortAlleleFrequencyStudyResult narrows the
        # inherited 'focus' to vrs:Allele | iriReference. A value of the wrong
        # shape (here, a MappableConcept) must still be rejected even though
        # it would satisfy the permissive base StudyResult.focus.
        "narrowed 'focus' rejects a value of the wrong type",
        "va-spec:CohortAlleleFrequencyStudyResult",
        {"type": "CohortAlleleFrequencyStudyResult",
         "focus": {"type": "MappableConcept", "name": "not an allele"},
         "focusCount": 1, "locusCount": 2,
         "alleleFrequency": 0.5, "cohort": {"type": "StudyGroup"}},
    ),
    (
        # Covariant narrowing: GeneDiseaseValidityProposition narrows the
        # inherited 'subject' to gkm.core:MappableConcept | iriReference. A
        # variant-shaped value (valid for other Proposition subject slots) must
        # be rejected here.
        "narrowed 'subject' rejects a value of the wrong type",
        "va-spec:GeneDiseaseValidityProposition",
        {"type": "GeneDiseaseValidityProposition",
         "subject": {"type": "Allele", "location": {"type": "SequenceLocation"}},
         "predicate": "variantsInGeneCausalFor",
         "object": {"type": "MappableConcept", "name": "Disease"}},
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


def _load_fixture(name):
    with open(fixtures_path / name) as f:
        return yaml.safe_load(f)


def test_aac_2017_tier_i_requires_supports_direction():
    # civic-assertion-combination-therapy-inline.yaml is a valid Tier I
    # VariantClinicalSignificanceStatement (classification code 'tier i',
    # direction 'supports'). The profile's if/then constraint requires
    # direction == 'supports' whenever the classification is Tier I; flipping it
    # to 'disputes' must be rejected.
    instance = _load_fixture("civic-assertion-combination-therapy-inline.yaml")
    assert instance["classification"]["primaryCoding"]["code"] == "tier i"
    assert instance["direction"] == "supports"

    instance["direction"] = "disputes"
    with pytest.raises(ValidationError):
        validator["va-spec.aac-2017:VariantClinicalSignificanceStatement"].validate(instance)


def test_aac_2017_tier_i_requires_strong_strength():
    # Same base case; the if/then also requires strength.primaryCoding.code ==
    # 'strong' for Tier I. Weakening it to 'potential' must be rejected.
    instance = _load_fixture("civic-assertion-combination-therapy-inline.yaml")
    assert instance["strength"]["primaryCoding"]["code"] == "strong"

    instance["strength"]["primaryCoding"]["code"] = "potential"
    with pytest.raises(ValidationError):
        validator["va-spec.aac-2017:VariantClinicalSignificanceStatement"].validate(instance)


@pytest.mark.parametrize(
    "cls,fixture",
    [
        ("va-spec.acmg-2015:VariantPathogenicityEvidenceLine", "acmg-no-criteria-met-evidence-line.yaml"),
        ("va-spec.acmg-2015:VariantPathogenicityEvidenceLine", "acmg-code-not-met-evidence-line.yaml"),
        ("va-spec.ccv-2022:VariantOncogenicityEvidenceLine", "ccv-no-criteria-met-evidence-line.yaml"),
        ("va-spec.ccv-2022:VariantOncogenicityEvidenceLine", "ccv-code-not-met-evidence-line.yaml"),
    ],
)
def test_not_met_evidence_requires_neutral_without_strength(cls, fixture):
    instance = _load_fixture(fixture)

    invalid_direction = deepcopy(instance)
    invalid_direction["directionOfEvidenceProvided"] = "supports"
    with pytest.raises(ValidationError):
        validator[cls].validate(invalid_direction)

    invalid_strength = deepcopy(instance)
    invalid_strength["strengthOfEvidenceProvided"] = {
        "type": "MappableConcept",
        "primaryCoding": {"code": "supporting", "system": invalid_strength["specifiedBy"]["reportedIn"]["name"]},
    }
    with pytest.raises(ValidationError):
        validator[cls].validate(invalid_strength)

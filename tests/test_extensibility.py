"""Extensibility tests for the open abstract core classes.

The abstract bases (Proposition, StudyResult, SubjectVariantProposition,
InformationEntity) are intentionally left *open* so that implementers can define
and validate their OWN subclasses of Statement / Proposition / StudyResult against
them. These tests lock in that behavior (and that the shared required attributes
are still enforced on any subclass).
"""
import pytest
from jsonschema import ValidationError
from config import validator, js_def

ABSTRACT_BASES = [
    "va-spec:Proposition",
    "va-spec:StudyResult",
    "va-spec:SubjectVariantProposition",
    "va-spec:InformationEntity",
]


@pytest.mark.parametrize("cls", ABSTRACT_BASES)
def test_abstract_base_is_open(cls):
    # Open == does not close the object to additional/unevaluated properties, so a
    # user-defined subclass instance (with extra fields) can validate against it.
    schema = js_def[cls]
    assert schema.get("additionalProperties") is not False, f"{cls} must stay open"
    assert schema.get("unevaluatedProperties") is not False, f"{cls} must stay open"


def test_user_defined_proposition_validates_against_open_base():
    user_proposition = {
        "type": "MyOrgCustomProposition",          # a novel subtype name
        "subject": {"id": "ex:gene1", "type": "Gene"},
        "predicate": "isRelatedTo",
        "object": "ex:condition1",
        "orgSpecificQualifier": {"foo": "bar"},     # extra field the base allows
    }
    validator["va-spec:Proposition"].validate(user_proposition)


def test_user_defined_study_result_validates_against_open_base():
    user_study_result = {
        "type": "MyOrgStudyResult",
        "focus": "ex:allele1",
        "customMeasure": 0.42,
    }
    validator["va-spec:StudyResult"].validate(user_study_result)


def test_statement_accepts_a_user_defined_proposition():
    # Statement.proposition $refs the open Proposition base, so a Statement may
    # carry an implementer's own proposition subtype.
    stmt = {
        "type": "Statement",
        "direction": "supports",
        "proposition": {
            "type": "MyOrgCustomProposition",
            "subject": {"id": "ex:gene1", "type": "Gene"},
            "predicate": "isRelatedTo",
            "object": "ex:condition1",
        },
    }
    validator["va-spec:Statement"].validate(stmt)


def test_statement_hasEvidence_accepts_any_information_entity():
    # Statement.hasEvidence $refs the open InformationEntity base (was the narrow
    # Statement | StudyResult | DataItem | iriReference union). An EvidenceLine --
    # an InformationEntity that was NOT in the old union -- must now be accepted
    # as a direct evidence item.
    stmt = {
        "type": "Statement",
        "proposition": "ex:prop",
        "direction": "supports",
        "hasEvidence": [
            {"type": "EvidenceLine", "directionOfEvidenceProvided": "supports"}
        ],
    }
    validator["va-spec:Statement"].validate(stmt)


def test_evidence_line_nests_via_hasEvidenceItems():
    # EvidenceLine has no hasEvidenceLines; a subordinate Evidence Line is nested
    # among hasEvidenceItems (which accepts any InformationEntity).
    ev_line = {
        "type": "EvidenceLine",
        "directionOfEvidenceProvided": "supports",
        "hasEvidenceItems": [
            {"type": "EvidenceLine", "directionOfEvidenceProvided": "supports"}
        ],
    }
    validator["va-spec:EvidenceLine"].validate(ev_line)


def test_open_base_still_enforces_required_triple():
    # Extensibility does not weaken the contract: subject/predicate/object remain
    # required on any Proposition (here 'predicate' is omitted).
    with pytest.raises(ValidationError):
        validator["va-spec:Proposition"].validate(
            {"type": "MyOrgProp", "subject": {"id": "x", "type": "G"}, "object": "ex:o"}
        )

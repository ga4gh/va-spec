"""Common data model"""
from enum import Enum, IntEnum
from typing import List, Optional, Union, Dict, Any, Type

from ga4gh.vrsatile.pydantic.vrs_models import CURIE
from ga4gh.vrsatile.pydantic.vrsatile_models import ValueObjectDescriptor, \
    GeneDescriptor, VariationDescriptor
from pydantic import BaseModel
from pydantic.types import StrictBool

from metakb.version import __version__, LAST_UPDATED


class SourceName(str, Enum):
    """Resources we import directly."""

    CIVIC = 'civic'
    MOA = 'moa'


class XrefSystem(str, Enum):
    """Define constraints for System in xrefs."""

    CLINVAR = 'clinvar'
    CLINGEN = 'caid'
    DB_SNP = 'dbsnp'
    NCBI = 'ncbigene'
    DISEASE_ONTOLOGY = 'do'


class SourcePrefix(str, Enum):
    """Define constraints for source prefixes."""

    PUBMED = 'pmid'
    ASCO = 'asco'


class NormalizerPrefix(str, Enum):
    """Define constraints for normalizer prefixes."""

    GENE = 'gene'


class PropositionType(str, Enum):
    """Define constraints for proposition type."""

    PREDICTIVE = 'therapeutic_response_proposition'
    DIAGNOSTIC = 'diagnostic_proposition'
    PROGNOSTIC = 'prognostic_proposition'
    PREDISPOSING = 'predisposition_proposition'
    FUNCTIONAL = 'functional_consequence_proposition'
    ONCOGENIC = 'oncogenicity_proposition'
    PATHOGENIC = 'pathogenicity_proposition'


class PredictivePredicate(str, Enum):
    """Define constraints for predictive predicate."""

    SENSITIVITY = 'predicts_sensitivity_to'
    RESISTANCE = 'predicts_resistance_to'


class DiagnosticPredicate(str, Enum):
    """Define constraints for diagnostic predicate."""

    POSITIVE = 'is_diagnostic_inclusion_criterion_for'
    NEGATIVE = 'is_diagnostic_exclusion_criterion_for'


class PrognosticPredicate(str, Enum):
    """Define constraints for prognostic predicate."""

    BETTER_OUTCOME = 'is_prognostic_of_better_outcome_for'
    POOR_OUTCOME = 'is_prognostic_of_worse_outcome_for'


class PathogenicPredicate(str, Enum):
    """Define constraints for the pathogenicity predicate."""

    UNCERTAIN_SIGNIFICANCE = 'is_of_uncertain_significance_for'
    PATHOGENIC = 'is_pathogenic_for'
    BENIGN = 'is_benign_for'


class FunctionalPredicate(str, Enum):
    """Define constraints for functional predicate."""

    GAIN_OF_FUNCTION = 'causes_gain_of_function_of'
    LOSS_OF_FUNCTION = 'causes_loss_of_function_of'
    UNALTERED_FUNCTION = 'does_not_change_function_of'
    NEOMORPHIC = 'causes_neomorphic_function_of'
    DOMINATE_NEGATIVE = 'causes_dominant_negative_function_of'


Predicate = Union[PredictivePredicate, DiagnosticPredicate,
                  PrognosticPredicate, PathogenicPredicate,
                  FunctionalPredicate]


class VariationOrigin(str, Enum):
    """Define constraints for variant origin."""

    SOMATIC = 'somatic'
    GERMLINE = 'germline'
    NOT_APPLICABLE = 'N/A'


class Direction(str, Enum):
    """Define constraints for evidence direction."""

    SUPPORTS = 'supports'
    DOES_NOT_SUPPORT = 'does_not_support'


class MoleculeContext(str, Enum):
    """Define constraints for types of molecule context."""

    GENOMIC = 'genomic'
    TRANSCRIPT = 'transcript'
    PROTEIN = 'protein'


class Proposition(BaseModel):
    """Define Proposition model."""

    id: CURIE
    type: PropositionType
    predicate: Predicate
    subject: CURIE  # vrs:Variation
    object_qualifier: CURIE  # vicc:Disease


class TherapeuticResponseProposition(Proposition):
    """Define therapeutic Response Proposition model"""

    type = PropositionType.PREDICTIVE
    predicate: PredictivePredicate
    object: CURIE  # vicc:Therapy

    class Config:
        """Configure examples."""

        @staticmethod
        def schema_extra(schema: Dict[str, Any],
                         model: Type['TherapeuticResponseProposition']) \
                -> None:
            """Configure OpenAPI schema"""
            if 'title' in schema.keys():
                schema.pop('title', None)
            for prop in schema.get('properties', {}).values():
                prop.pop('title', None)
            schema['example'] = {
                "id": "proposition:133",
                "type": "therapeutic_response_proposition",
                "predicate": "predicts_sensitivity_to",
                "subject": "ga4gh:VA.kgjrhgf84CEndyLjKdAO0RxN-e3pJjxA",
                "object_qualifier": "ncit:C2926",
                "object": "rxcui:1430438"
            }


class PrognosticProposition(Proposition):
    """Defines the Prognostic Proposition model."""

    type = PropositionType.PROGNOSTIC
    predicate: PrognosticPredicate


class DiagnosticProposition(Proposition):
    """Defines the Diagnostic Proposition model."""

    type = PropositionType.DIAGNOSTIC
    predicate: DiagnosticPredicate


class MethodID(IntEnum):
    """Create AssertionMethod id constants for harvested sources."""

    CIVIC_EID_SOP = 1
    CIVIC_AID_AMP_ASCO_CAP = 2
    CIVIC_AID_ACMG = 3
    MOA_ASSERTION_BIORXIV = 4


class Statement(BaseModel):
    """Define Statement model."""

    id: CURIE
    type = 'Statement'
    description: str
    direction: Optional[Direction]
    evidence_level: CURIE
    proposition: CURIE
    variation_origin: Optional[VariationOrigin]
    variation_descriptor: CURIE
    therapy_descriptor: Optional[CURIE]
    disease_descriptor: CURIE
    method: CURIE
    supported_by: List[CURIE]
    # contribution: str  TODO: After metakb first pass


class Document(BaseModel):
    """Define model for Source."""

    id: CURIE
    document_id: Optional[CURIE]
    label: str
    description: Optional[str]
    xrefs: Optional[List[CURIE]]
    type = 'Document'


class Date(BaseModel):
    """Define model for date."""

    year: int
    month: Optional[int]
    day: Optional[int]

    class Config:
        """Configure examples."""

        @staticmethod
        def schema_extra(schema: Dict[str, Any],
                         model: Type['StatementResponse']) -> None:
            """Configure OpenAPI schema"""
            if 'title' in schema.keys():
                schema.pop('title', None)
            for prop in schema.get('properties', {}).values():
                prop.pop('title', None)
            schema['example'] = {
                "year": 2019,
                "month": 11,
                "day": 29
            }


class Method(BaseModel):
    """Define model for methods used in evidence curation and classifications."""  # noqa: E501

    id: CURIE
    label: str
    url: str
    version: Date
    authors: str
    type = 'Method'


class Response(BaseModel):
    """Define the Response Model."""

    statements: List[Statement]
    propositions: List[Union[TherapeuticResponseProposition,
                             PrognosticProposition,
                             DiagnosticProposition]]
    variation_descriptors: List[VariationDescriptor]
    gene_descriptors: List[GeneDescriptor]
    therapy_descriptors: Optional[List[ValueObjectDescriptor]]
    disease_descriptors: List[ValueObjectDescriptor]
    methods: List[Method]
    documents: List[Document]


class StatementResponse(BaseModel):
    """Define Statement Response for Search Endpoint."""

    id: CURIE
    type = 'Statement'
    description: str
    direction: Optional[Direction]
    evidence_level: CURIE
    variation_origin: Optional[VariationOrigin]
    proposition: CURIE
    variation_descriptor: CURIE
    therapy_descriptor: Optional[CURIE]
    disease_descriptor: CURIE
    method: CURIE
    supported_by: List[CURIE]

    class Config:
        """Configure examples."""

        @staticmethod
        def schema_extra(schema: Dict[str, Any],
                         model: Type['StatementResponse']) -> None:
            """Configure OpenAPI schema"""
            if 'title' in schema.keys():
                schema.pop('title', None)
            for prop in schema.get('properties', {}).values():
                prop.pop('title', None)
            schema['example'] = {
                "id": "civic.eid:2997",
                "description": "Afatinib, an irreversible inhibitor of the ErbB family of tyrosine kinases has been approved in the US for the first-line treatment of patients with metastatic non-small-cell lung cancer (NSCLC) who have tumours with EGFR exon 19 deletions or exon 21 (L858R) substitution mutations as detected by a US FDA-approved test",  # noqa: E501
                "direction": "supports",
                "evidence_level": "civic.evidence_level:A",
                "variation_origin": "somatic",
                "proposition": "proposition:133",
                "variation_descriptor": "civic.vid:33",
                "therapy_descriptor": "civic.tid:146",
                "disease_descriptor": "civic.did:8",
                "method": "method:001",
                "supported_by": [
                    "pmid:23982599"
                ],
                "type": "Statement"
            }


class NestedStatementResponse(BaseModel):
    """Define Statement Response for Search Endpoint."""

    id: CURIE
    type = 'Statement'
    description: str
    direction: Optional[Direction]
    evidence_level: CURIE
    variation_origin: Optional[VariationOrigin]
    proposition: Union[TherapeuticResponseProposition,
                       PrognosticProposition,
                       DiagnosticProposition]
    variation_descriptor: VariationDescriptor
    therapy_descriptor: Optional[ValueObjectDescriptor]
    disease_descriptor: ValueObjectDescriptor
    method: Method
    supported_by: List[Union[Document, CURIE]]

    class Config:
        """Configure examples."""

        @staticmethod
        def schema_extra(schema: Dict[str, Any],
                         model: Type['NestedStatementResponse']) -> None:
            """Configure OpenAPI schema"""
            if 'title' in schema.keys():
                schema.pop('title', None)
            for prop in schema.get('properties', {}).values():
                prop.pop('title', None)
            schema['example'] = {
                "id": "civic.eid:2997",
                "description": "Afatinib, an irreversible inhibitor of the ErbB family of tyrosine kinases has been approved in the US for the first-line treatment of patients with metastatic non-small-cell lung cancer (NSCLC) who have tumours with EGFR exon 19 deletions or exon 21 (L858R) substitution mutations as detected by a US FDA-approved test",  # noqa: E501
                "direction": "supports",
                "evidence_level": "civic.evidence_level:A",
                "variation_origin": "somatic",
                "proposition": {
                    "id": "proposition:133",
                    "type": "therapeutic_response_proposition",
                    "predicate": "predicts_sensitivity_to",
                    "subject": "ga4gh:VA.kgjrhgf84CEndyLjKdAO0RxN-e3pJjxA",
                    "object_qualifier": "ncit:C2926",
                    "object": "rxcui:1430438"
                },
                "variation_descriptor": {
                    "id": "civic.vid:33",
                    "type": "VariationDescriptor",
                    "label": "L858R",
                    "description": "EGFR L858R has long been recognized as a functionally significant mutation in cancer, and is one of the most prevalent single mutations in lung cancer. Best described in non-small cell lung cancer (NSCLC), the mutation seems to confer sensitivity to first and second generation TKI's like gefitinib and neratinib. NSCLC patients with this mutation treated with TKI's show increased overall and progression-free survival, as compared to chemotherapy alone. Third generation TKI's are currently in clinical trials that specifically focus on mutant forms of EGFR, a few of which have shown efficacy in treating patients that failed to respond to earlier generation TKI therapies.",  # noqa: E501
                    "xrefs": [
                        "clinvar:376280",
                        "clinvar:16609",
                        "clinvar:376282",
                        "caid:CA126713",
                        "dbsnp:121434568"
                    ],
                    "alternate_labels": [
                        "LEU858ARG"
                    ],
                    "extensions": [
                        {
                            "type": "Extension",
                            "name": "civic_representative_coordinate",
                            "value": {
                                "chromosome": "7",
                                "start": 55259515,
                                "stop": 55259515,
                                "reference_bases": "T",
                                "variant_bases": "G",
                                "representative_transcript":
                                    "ENST00000275493.2",
                                "ensembl_version": 75,
                                "reference_build": "GRCh37"
                            }
                        },
                        {
                            "type": "Extension",
                            "name": "civic_actionability_score",
                            "value": 375
                        }
                    ],
                    "variation_id":
                        "ga4gh:VA.kgjrhgf84CEndyLjKdAO0RxN-e3pJjxA",
                    "variation": {
                        "_id": "ga4gh:VA.kgjrhgf84CEndyLjKdAO0RxN-e3pJjxA",
                        "type": "Allele",
                        "location": {
                            "_id": "ga4gh:VSL.Sfs_3PlVEYp9BxBsHsFfU1tvhfDq361f",  # noqa: E501
                            "type": "SequenceLocation",
                            "sequence_id":
                                "ga4gh:SQ.vyo55F6mA6n2LgN4cagcdRzOuh38V4mE",
                            "interval": {
                                "type": "SequenceInterval",
                                "start": {
                                    "type": "Number",
                                    "value": 857
                                },
                                "end": {
                                    "type": "Number",
                                    "value": 858
                                }
                            }
                        },
                        "state": {
                            "type": "LiteralSequenceExpression",
                            "sequence": "R"
                        }
                    },
                    "structural_type": "SO:0001583",
                    "expressions": [
                        {
                            "type": "Expression",
                            "syntax": "hgvs.g",
                            "value": "NC_000007.13:g.55259515T>G"
                        },
                        {
                            "type": "Expression",
                            "syntax": "hgvs.p",
                            "value": "NP_005219.2:p.Leu858Arg"
                        },
                        {
                            "type": "Expression",
                            "syntax": "hgvs.c",
                            "value": "NM_005228.4:c.2573T>G"
                        },
                        {
                            "type": "Expression",
                            "syntax": "hgvs.c",
                            "value": "ENST00000275493.2:c.2573T>G"
                        }
                    ],
                    "gene_context": {
                        "id": "civic.gid:19",
                        "type": "GeneDescriptor",
                        "label": "EGFR",
                        "description": "EGFR is widely recognized for its importance in cancer. Amplification and mutations have been shown to be driving events in many cancer types. Its role in non-small cell lung cancer, glioblastoma and basal-like breast cancers has spurred many research and drug development efforts. Tyrosine kinase inhibitors have shown efficacy in EGFR amplfied tumors, most notably gefitinib and erlotinib. Mutations in EGFR have been shown to confer resistance to these drugs, particularly the variant T790M, which has been functionally characterized as a resistance marker for both of these drugs. The later generation TKI's have seen some success in treating these resistant cases, and targeted sequencing of the EGFR locus has become a common practice in treatment of non-small cell lung cancer. \nOverproduction of ligands is another possible mechanism of activation of EGFR. ERBB ligands include EGF, TGF-a, AREG, EPG, BTC, HB-EGF, EPR and NRG1-4 (for detailed information please refer to the respective ligand section).",  # noqa: E501
                        "xrefs": [
                            "ncbigene:1956"
                        ],
                        "alternate_labels": [
                            "ERRP",
                            "EGFR",
                            "mENA",
                            "PIG61",
                            "NISBD2",
                            "HER1",
                            "ERBB1",
                            "ERBB"
                        ],
                        "gene_id": "hgnc:3236"
                    }
                },
                "therapy_descriptor": {
                    "id": "civic.tid:146",
                    "type": "TherapyDescriptor",
                    "label": "Afatinib",
                    "xrefs": [
                        "ncit:C66940"
                    ],
                    "alternate_labels": [
                        "BIBW2992",
                        "BIBW 2992",
                        "(2e)-N-(4-(3-Chloro-4-Fluoroanilino)-7-(((3s)-Oxolan-3-yl)Oxy)Quinoxazolin-6-yl)-4-(Dimethylamino)But-2-Enamide"  # noqa: E501
                    ],
                    "therapy_id": "rxcui:1430438"
                },
                "disease_descriptor": {
                    "id": "civic.did:8",
                    "type": "DiseaseDescriptor",
                    "label": "Lung Non-small Cell Carcinoma",
                    "xrefs": [
                        "DOID:3908"
                    ],
                    "disease_id": "ncit:C2926"
                },
                "method": {
                    "id": "method:001",
                    "label": "Standard operating procedure for curation and clinical interpretation of variants in cancer",  # noqa: E501
                    "url": "https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-019-0687-x",  # noqa: E501
                    "version": {
                        "year": 2019,
                        "month": 11,
                        "day": 29
                    },
                    "authors":
                        "Danos, A.M., Krysiak, K., Barnell, E.K. et al.",
                    "type": "Method"
                },
                "supported_by": [
                    {
                        "id": "pmid:23982599",
                        "label": "Dungo et al., 2013, Drugs",
                        "description": "Afatinib: first global approval.",
                        "type": "Document"
                    }
                ],
                "type": "Statement"
            }


class SearchQuery(BaseModel):
    """Queries for the Search Endpoint."""

    variation: Optional[str]
    disease: Optional[str]
    therapy: Optional[str]
    gene: Optional[str]
    statement_id: Optional[str]
    detail: StrictBool

    class Config:
        """Configure examples."""

        @staticmethod
        def schema_extra(schema: Dict[str, Any],
                         model: Type['SearchQuery']) -> None:
            """Configure OpenAPI schema"""
            if 'title' in schema.keys():
                schema.pop('title', None)
            for prop in schema.get('properties', {}).values():
                prop.pop('title', None)
            schema['example'] = {
                "variation": "NP_005219.2:p.Leu858Arg",
                "disease": "Lung Non-small Cell Carcinoma",
                "therapy": "Afatinib",
                "statement_id": "civic.eid:2997",
                "detail": False
            }


class SearchStatementsQuery(BaseModel):
    """Queries for the Search Endpoint."""

    variation: Optional[str]
    disease: Optional[str]
    therapy: Optional[str]
    gene: Optional[str]
    statement_id: Optional[str]

    class Config:
        """Configure examples."""

        @staticmethod
        def schema_extra(schema: Dict[str, Any],
                         model: Type['SearchStatementsQuery']) -> None:
            """Configure OpenAPI schema"""
            if 'title' in schema.keys():
                schema.pop('title', None)
            for prop in schema.get('properties', {}).values():
                prop.pop('title', None)
            schema['example'] = {
                "variation": "NP_005219.2:p.Leu858Arg",
                "disease": "Lung Non-small Cell Carcinoma",
                "therapy": "Afatinib",
                "statement_id": "civic.eid:2997"
            }


class Matches(BaseModel):
    """Statements and Propositions that match the queried parameters."""

    statements: List[str]
    propositions: List[str]

    class Config:
        """Configure examples."""

        @staticmethod
        def schema_extra(schema: Dict[str, Any],
                         model: Type['Matches']) -> None:
            """Configure OpenAPI schema"""
            if 'title' in schema.keys():
                schema.pop('title', None)
            for prop in schema.get('properties', {}).values():
                prop.pop('title', None)
            schema['example'] = {
                "statements": ["civic.eid:2997"],
                "propositions": ["proposition:133"]
            }


class ServiceMeta(BaseModel):
    """Metadata for MetaKB service."""

    name = "metakb"
    version = __version__
    last_updated = LAST_UPDATED
    url = "https://github.com/cancervariants/metakb"

    class Config:
        """Configure schema example."""

        @staticmethod
        def schema_extra(schema: Dict[str, Any],
                         model: Type["ServiceMeta"]) -> None:
            """Configure OpenAPI schema"""
            if "title" in schema.keys():
                schema.pop("title", None)
            for prop in schema.get("properties", {}).values():
                prop.pop("title", None)
            schema["example"] = {
                "name": "metakb",
                "version": "1.1.0-alpha.4",
                "last_updated": "2021-12-16",
                "url": "https://github.com/cancervariants/metakb"
            }


class SearchService(BaseModel):
    """Define model for Search Endpoint Response."""

    query: SearchQuery
    warnings: Optional[List[str]]
    matches: Matches
    statements: Optional[List[StatementResponse]]
    propositions: Optional[List[Union[TherapeuticResponseProposition,
                                      DiagnosticProposition,
                                      PrognosticProposition]]]
    variation_descriptors: Optional[List[VariationDescriptor]]
    gene_descriptors: Optional[List[GeneDescriptor]]
    therapy_descriptors: Optional[List[ValueObjectDescriptor]]
    disease_descriptors: Optional[List[ValueObjectDescriptor]]
    methods: Optional[List[Method]]
    documents: Optional[List[Document]]
    service_meta_: ServiceMeta

    class Config:
        """Configure examples."""

        @staticmethod
        def schema_extra(schema: Dict[str, Any],
                         model: Type['SearchService']) -> None:
            """Configure OpenAPI schema"""
            if 'title' in schema.keys():
                schema.pop('title', None)
            for prop in schema.get('properties', {}).values():
                prop.pop('title', None)
            schema['example'] = {
                "query": {
                    "variation": "EGFR L858R",
                    "disease": "Lung Non-small Cell Carcinoma",
                    "therapy": "Afatinib",
                    "statement_id": "civic.eid:2997",
                    "detail": False
                },
                "warnings": [],
                "matches": {
                    "statements": ["civic.eid:2997"],
                    "propositions": ["proposition:109"]
                },
                "statements": [
                    {
                        "id": "civic.eid:2997",
                        "description": "Afatinib, an irreversible inhibitor of the ErbB family of tyrosine kinases has been approved in the US for the first-line treatment of patients with metastatic non-small-cell lung cancer (NSCLC) who have tumours with EGFR exon 19 deletions or exon 21 (L858R) substitution mutations as detected by a US FDA-approved test",  # noqa: E501
                        "direction": "supports",
                        "evidence_level": "civic.evidence_level:A",
                        "variation_origin": "somatic",
                        "proposition": "proposition:133",
                        "variation_descriptor": "civic.vid:33",
                        "therapy_descriptor": "civic.tid:146",
                        "disease_descriptor": "civic.did:8",
                        "method": "method:001",
                        "supported_by": [
                            "pmid:23982599"
                        ],
                        "type": "Statement"
                    }
                ],
                "propositions": [
                    {
                        "id": "proposition:133",
                        "type": "therapeutic_response_proposition",
                        "predicate": "predicts_sensitivity_to",
                        "subject": "ga4gh:VA.kgjrhgf84CEndyLjKdAO0RxN-e3pJjxA",
                        "object_qualifier": "ncit:C2926",
                        "object": "rxcui:1430438"
                    }
                ],
                "service_meta_": {
                    "name": "metakb",
                    "version": "1.1.0-alpha.4",
                    "last_updated": "2021-12-16",
                    "url": "https://github.com/cancervariants/metakb"
                }
            }


class SearchIDService(BaseModel):
    """Define model for Search by ID Endpoint Response."""

    query: str
    warnings: Optional[List[str]]
    statement: Optional[StatementResponse]
    proposition: Optional[Union[TherapeuticResponseProposition,
                                DiagnosticProposition,
                                PrognosticProposition]]
    variation_descriptor: Optional[VariationDescriptor]
    gene_descriptor: Optional[GeneDescriptor]
    therapy_descriptor: Optional[ValueObjectDescriptor]
    disease_descriptor: Optional[ValueObjectDescriptor]
    document: Optional[Document]
    method: Optional[Method]
    service_meta_: ServiceMeta

    class Config:
        """Configure examples."""

        @staticmethod
        def schema_extra(schema: Dict[str, Any],
                         model: Type['SearchIDService']) -> None:
            """Configure OpenAPI schema"""
            if 'title' in schema.keys():
                schema.pop('title', None)
            for prop in schema.get('properties', {}).values():
                prop.pop('title', None)
            schema['example'] = {
                "query": {
                    "node_id": "civic.vid:33"
                },
                "warnings": [],
                "matches": {
                    "node": "civic.vid:33"
                },
                "variation_descriptors": [
                    {
                        "id": "civic.vid:33",
                        "type": "VariationDescriptor",
                        "label": "L858R",
                        "description": "EGFR L858R has long been recognized "
                                       "as a functionally significant "
                                       "mutation in cancer, and is one of "
                                       "he most prevalent single mutations in"
                                       " lung cancer. Best described in "
                                       "non-small cell lung cancer (NSCLC), "
                                       "the mutation seems to confer "
                                       "sensitivity to first and second "
                                       "generation TKI's like gefitinib and"
                                       " neratinib. NSCLC patients with this"
                                       " mutation treated with TKI's show "
                                       "increased overall and "
                                       "progression-free survival, as "
                                       "compared to chemotherapy alone. "
                                       "Third generation TKI's are currently"
                                       " in clinical trials that specifically"
                                       " focus on mutant forms of EGFR, a few"
                                       " of which have shown efficacy in "
                                       "treating patients that failed to "
                                       "respond to earlier generation "
                                       "TKI therapies.",
                        "value_id": "ga4gh:VA.WyOqFMhc8aOnMFgdY0uM7nSLNqxVPAiR",  # noqa: E501
                        "value": {
                            "location": {
                                "interval": {
                                    "end": 858,
                                    "start": 857,
                                    "type": "SimpleInterval"
                                },
                                "sequence_id": "ga4gh:SQ.vyo55F6mA6n2LgN4cagcdRzOuh38V4mE",  # noqa: E501
                                "type": "SequenceLocation"
                            },
                            "state": {
                                "sequence": "R",
                                "type": "SequenceState"
                            },
                            "type": "Allele"
                        },
                        "xrefs": [
                            "clinvar:376280",
                            "clinvar:16609",
                            "clinvar:376282",
                            "caid:CA126713",
                            "dbsnp:121434568"
                        ],
                        "alternate_labels": [
                            "LEU858ARG"
                        ],
                        "extensions": [
                            {
                                "name": "civic_representative_coordinate",
                                "value": {
                                    "chromosome": "7",
                                    "start": 55259515,
                                    "stop": 55259515,
                                    "reference_bases": "T",
                                    "variant_bases": "G",
                                    "representative_transcript": "ENST00000275493.2",  # noqa: E501
                                    "ensembl_version": 75,
                                    "reference_build": "GRCh37"
                                },
                                "type": "Extension"
                            },
                            {
                                "name": "civic_actionability_score",
                                "value": "352.5",
                                "type": "Extension"
                            }
                        ],
                        "structural_type": "SO:0001583",
                        "expressions": [
                            {
                                "syntax": "hgvs.g",
                                "value": "NC_000007.13:g.55259515T>G",
                                "type": "Expression"
                            },
                            {
                                "syntax": "hgvs.p",
                                "value": "NP_005219.2:p.Leu858Arg",
                                "type": "Expression"
                            },
                            {
                                "syntax": "hgvs.c",
                                "value": "NM_005228.4:c.2573T>G",
                                "type": "Expression"
                            },
                            {
                                "syntax": "hgvs.c",
                                "value": "ENST00000275493.2:c.2573T>G",
                                "type": "Expression"
                            }
                        ],
                        "gene_context": "civic.gid:19"
                    }
                ],
                "service_meta_": {
                    "name": "metakb",
                    "version": "1.1.0-alpha.4",
                    "last_updated": "2021-12-16",
                    "url": "https://github.com/cancervariants/metakb"
                }
            }


class SearchStatementsService(BaseModel):
    """Define model for Search Statements Endpoint Response."""

    query: SearchStatementsQuery
    warnings: Optional[List[str]]
    matches: Matches
    statements: Optional[List[NestedStatementResponse]]
    service_meta_: ServiceMeta

    class Config:
        """Configure examples."""

        @staticmethod
        def schema_extra(schema: Dict[str, Any],
                         model: Type['SearchStatementsService']) -> None:
            """Configure OpenAPI schema"""
            if 'title' in schema.keys():
                schema.pop('title', None)
            for prop in schema.get('properties', {}).values():
                prop.pop('title', None)
            schema['example'] = {
                "query": {
                    "variation": "EGFR L858R",
                    "disease": "Lung Non-small Cell Carcinoma",
                    "therapy": "Afatinib",
                    "statement_id": "civic.eid:2997"
                },
                "warnings": [],
                "matches": {
                    "statements": ["civic.eid:2997"],
                    "propositions": ["proposition:109"]
                },
                "statements": [
                    {
                        "id": "civic.eid:2997",
                        "description": "Afatinib, an irreversible inhibitor of the ErbB family of tyrosine kinases has been approved in the US for the first-line treatment of patients with metastatic non-small-cell lung cancer (NSCLC) who have tumours with EGFR exon 19 deletions or exon 21 (L858R) substitution mutations as detected by a US FDA-approved test",  # noqa: E501
                        "direction": "supports",
                        "evidence_level": "civic.evidence_level:A",
                        "variation_origin": "somatic",
                        "proposition": {
                            "id": "proposition:133",
                            "type": "therapeutic_response_proposition",
                            "predicate": "predicts_sensitivity_to",
                            "subject": "ga4gh:VA.kgjrhgf84CEndyLjKdAO0RxN-e3pJjxA",    # noqa: E501
                            "object_qualifier": "ncit:C2926",
                            "object": "rxcui:1430438"
                        },
                        "variation_descriptor": {
                            "id": "civic.vid:33",
                            "type": "VariationDescriptor",
                            "label": "L858R",
                            "description": "EGFR L858R has long been recognized as a functionally significant mutation in cancer, and is one of the most prevalent single mutations in lung cancer. Best described in non-small cell lung cancer (NSCLC), the mutation seems to confer sensitivity to first and second generation TKI's like gefitinib and neratinib. NSCLC patients with this mutation treated with TKI's show increased overall and progression-free survival, as compared to chemotherapy alone. Third generation TKI's are currently in clinical trials that specifically focus on mutant forms of EGFR, a few of which have shown efficacy in treating patients that failed to respond to earlier generation TKI therapies.",  # noqa: E501
                            "xrefs": [
                                "clinvar:376280",
                                "clinvar:16609",
                                "clinvar:376282",
                                "caid:CA126713",
                                "dbsnp:121434568"
                            ],
                            "alternate_labels": [
                                "LEU858ARG"
                            ],
                            "extensions": [
                                {
                                    "type": "Extension",
                                    "name": "civic_representative_coordinate",
                                    "value": {
                                        "chromosome": "7",
                                        "start": 55259515,
                                        "stop": 55259515,
                                        "reference_bases": "T",
                                        "variant_bases": "G",
                                        "representative_transcript":
                                            "ENST00000275493.2",
                                        "ensembl_version": 75,
                                        "reference_build": "GRCh37"
                                    }
                                },
                                {
                                    "type": "Extension",
                                    "name": "civic_actionability_score",
                                    "value": 375
                                }
                            ],
                            "variation_id":
                                "ga4gh:VA.kgjrhgf84CEndyLjKdAO0RxN-e3pJjxA",
                            "variation": {
                                "_id": "ga4gh:VA.kgjrhgf84CEndyLjKdAO0RxN-e3pJjxA",  # noqa: E501
                                "type": "Allele",
                                "location": {
                                    "_id": "ga4gh:VSL.Sfs_3PlVEYp9BxBsHsFfU1tvhfDq361f",  # noqa: E501
                                    "type": "SequenceLocation",
                                    "sequence_id": "ga4gh:SQ.vyo55F6mA6n2LgN4cagcdRzOuh38V4mE",  # noqa: E501
                                    "interval": {
                                        "type": "SequenceInterval",
                                        "start": {
                                            "type": "Number",
                                            "value": 857
                                        },
                                        "end": {
                                            "type": "Number",
                                            "value": 858
                                        }
                                    }
                                },
                                "state": {
                                    "type": "LiteralSequenceExpression",
                                    "sequence": "R"
                                }
                            },
                            "structural_type": "SO:0001583",
                            "expressions": [
                                {
                                    "type": "Expression",
                                    "syntax": "hgvs.g",
                                    "value": "NC_000007.13:g.55259515T>G"
                                },
                                {
                                    "type": "Expression",
                                    "syntax": "hgvs.p",
                                    "value": "NP_005219.2:p.Leu858Arg"
                                },
                                {
                                    "type": "Expression",
                                    "syntax": "hgvs.c",
                                    "value": "NM_005228.4:c.2573T>G"
                                },
                                {
                                    "type": "Expression",
                                    "syntax": "hgvs.c",
                                    "value": "ENST00000275493.2:c.2573T>G"
                                }
                            ],
                            "gene_context": {
                                "id": "civic.gid:19",
                                "type": "GeneDescriptor",
                                "label": "EGFR",
                                "description": "EGFR is widely recognized for its importance in cancer. Amplification and mutations have been shown to be driving events in many cancer types. Its role in non-small cell lung cancer, glioblastoma and basal-like breast cancers has spurred many research and drug development efforts. Tyrosine kinase inhibitors have shown efficacy in EGFR amplfied tumors, most notably gefitinib and erlotinib. Mutations in EGFR have been shown to confer resistance to these drugs, particularly the variant T790M, which has been functionally characterized as a resistance marker for both of these drugs. The later generation TKI's have seen some success in treating these resistant cases, and targeted sequencing of the EGFR locus has become a common practice in treatment of non-small cell lung cancer. \nOverproduction of ligands is another possible mechanism of activation of EGFR. ERBB ligands include EGF, TGF-a, AREG, EPG, BTC, HB-EGF, EPR and NRG1-4 (for detailed information please refer to the respective ligand section).",  # noqa: E501
                                "xrefs": [
                                    "ncbigene:1956"
                                ],
                                "alternate_labels": [
                                    "ERRP",
                                    "EGFR",
                                    "mENA",
                                    "PIG61",
                                    "NISBD2",
                                    "HER1",
                                    "ERBB1",
                                    "ERBB"
                                ],
                                "gene_id": "hgnc:3236"
                            }
                        },
                        "therapy_descriptor": {
                            "id": "civic.tid:146",
                            "type": "TherapyDescriptor",
                            "label": "Afatinib",
                            "xrefs": [
                                "ncit:C66940"
                            ],
                            "alternate_labels": [
                                "BIBW2992",
                                "BIBW 2992",
                                "(2e)-N-(4-(3-Chloro-4-Fluoroanilino)-7-(((3s)-Oxolan-3-yl)Oxy)Quinoxazolin-6-yl)-4-(Dimethylamino)But-2-Enamide"  # noqa: E501
                            ],
                            "therapy_id": "rxcui:1430438"
                        },
                        "disease_descriptor": {
                            "id": "civic.did:8",
                            "type": "DiseaseDescriptor",
                            "label": "Lung Non-small Cell Carcinoma",
                            "xrefs": [
                                "DOID:3908"
                            ],
                            "disease_id": "ncit:C2926"
                        },
                        "method": {
                            "id": "method:001",
                            "label": "Standard operating procedure for curation and clinical interpretation of variants in cancer",  # noqa: E501
                            "url": "https://genomemedicine.biomedcentral.com/articles/10.1186/s13073-019-0687-x",  # noqa: E501
                            "version": {
                                "year": 2019,
                                "month": 11,
                                "day": 29
                            },
                            "authors": "Danos, A.M., Krysiak, K., Barnell, E.K. et al.",  # noqa: E501
                            "type": "Method"
                        },
                        "supported_by": [
                            {
                                "id": "pmid:23982599",
                                "label": "Dungo et al., 2013, Drugs",
                                "description": "Afatinib: first global approval.",  # noqa: E501
                                "type": "Document"
                            }
                        ],
                        "type": "Statement"
                    }
                ],
                "service_meta_": {
                    "name": "metakb",
                    "version": "1.1.0-alpha.4",
                    "last_updated": "2021-12-16",
                    "url": "https://github.com/cancervariants/metakb"
                }
            }

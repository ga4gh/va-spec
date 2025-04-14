.. _ccv-2022-profiles:

CCV 2022 Aligned Profiles
@@@@@@@@@@@@@@@@@@@@@@@@@


The following profiles align with terminology and curation conventions from the `ClinGen/CGC/VICC (CCV) 2022 Oncogenicity Interpretation Guidelines <https://pubmed.ncbi.nlm.nih.gov/35101336/>`_

These initial profiles were developed to support the following implementations and use cases: 

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: 30 70

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: 30 70

   *  - Implementer
      - Use Case
   *  - VICC MetaKB
      - Using VA-Spec models to structure oncogenicity classifications and evidence in its community-facing data exchange APIs.
   *  - ClinVar Submission Utility
      - Uses VA-Spec as input format for submission tools that send variant classifications and evidence from CIViC to the ClinVar database via its API.

The number and coverage of these profiles will grow as these implementations expand their scope, and additional adopters bring new use cases to the spec. 

Links to Source YAML and JSON Schema artifacts are provided following the description of each profile below.

.. _variant-oncogenicity-statement-ccv-2022:

Variant Oncogenicity Statement (CCV 2022)
#########################################

.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A Statement describing the oncogenicity of a variant, i.e. the role it plays in contributing to cancer tumorigenesis.

**Information Model**

This profile applies the following **constraints** on top of the core :ref:`Statement<Statement>` class definition:

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: 20 7 20 7 46


   *  - Field
      - Flags
      - Type
      - Limits
      - Description
   *  - proposition
      -
      - :ref:`variant-oncogenicity-proposition`
      - 1..1
      - A proposition about the oncogenicity of a varaint, the validity of which is assessed and reported by the Statement. A Statement can put forth the proposition as being true, false, or uncertain, and may provide an assessment of the level of confidence/evidence supporting this claim.
   *  - strength
      -
      - :ref:`MappableConcept` (nested enum: likely | definitive)
      - 0..1
      - A term used to report the strength of a Proposition's assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be). The indicated enumeration is bound to the 'code' field in the Coding object nested inside the MappableConcept.
   *  - classification
      -
      - :ref:`MappableConcept`  (nested enum: oncogenic | likely oncogenic | benign | likely benign | VUS)
      - 0..1
      - A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's Proposition, in terms of a classification of its subject. The indicated enumeration is bound to the 'code' field in the Coding object nested inside the MappableConcept.

**Artifacts**

 - |oncogenicity_study_statement_source_yaml|
 - |oncogenicity_study_statement_json_schema|

-----

.. _variant-oncogenicity-evidence-line-ccv-2022:

Variant Oncogenicity Evidence Line (CCV 2022)
##############################################

.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

An Evidence Line that describes how a specific type of information was interpreted as evidence for or againtst a variant's oncogenicity. In the CCV Framework, evidence is assessed by determining if a specific criterion (e.g. 'OM2') with a default strength (e.g. 'moderate') is 'met' or 'not met', and in some cases adjusting the default strength based on the quality and abundance of evidence.

**Information Model**

This profile applies the following **constraints** on top of the core :ref:`Evidence Line<EvidenceLine>` class definition:

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: 20 7 20 7 46

   *  - Field
      - Flags
      - Type
      - Limits
      - Description
   *  - targetProposition
      -
      - :ref:`variant-oncogenicity-proposition`
      - 0..1
      - A Variant Oncoogenicity Proposition against which a specific type of evidence was assessed, to determine the strength and direction of support this evidence provides for or against the proposition's validity.
   *  - directionOfEvidenceProvided
      -
      - string (enum: supports | disputes | none )
      - 1..1
      - The direction of support that the Evidence Line is determined to provide toward its target Proposition (supports, disputes, neutral). For CCV-based assessments, if a oncogenicity criterion is 'met' in the Evidence Line the direction is 'supports', if a benignity criterion is 'met' the direction is 'disputes', and if a criteria is 'not met' the direction is 'none'.
   *  - strengthOfEvidenceProvided
      -
      - :ref:`MappableConcept` (nested enum: stand alone | very strong | strong | moderate | supporting)
      - 0..1
      - The strength of support that an Evidence Line is determined to provide for or against the proposed oncogenicity of the assessed variant. Strength is evaluated relative to the direction indicated by the 'directionOfEvidenceProvided' attribute, and captured using a MappableConcept, whose nested 'code' field is bound to an enumerated set of values. Conditional requirement: if `directionOfEvidenceProvided` is either 'supports' or 'disputes', then this attribute is required. If it is 'none', then this attribute is not allowed.
   *  - specifiedBy
      -
      - :ref:`Method`
      - 0..1
      - The guidelines or rubrics followed in interpreting evidence, to determine the strength and direction of support that it provides for or against a variant's oncogenicity. While the CCV Criteria themselves provide minimal guidance, typically a more detailed, gene- or cancer- specific rubric is followed to determine if a given criterion was met, and how strongly.
   *  - methodType
      -
      -  string (enum: OVS1 | OS1 | OS2 | OS3 | OM1 | OM2 | OM3 | OM4 | OP1 | OP2 | OP3 | OP4 | SBVS1 | SBS1 | SBS2 | SBP1 | SBP2)
      - 1..1
      - A term representing the type of method used to assess evidence for or against the oncogenicity of a variant. Method type is reported as the CCV Code that defines criteria against which evidence is assessed to determine if it supports oncogenicity or benignity of a variant.
   *  - evidenceOutcome
      -
      - :ref:`MappableConcept` (nested enum, examples: OS2 | OS2_moderate | OS2_not_met | SBS2 | SBS2_moderate | SBS2_not_met)
      - 0..1
      - The evidence outcome provides a single string that summarizes 'directionOfEvidenceProvided' and 'strengthOfEvidenceProvided' assessments, along with the specific CCV criterion used in these assessments. Rules for constructing this string are as follows, and enforced by a regex constraint: (1) If a criterion is met and its default strength is not altered, the outcome is simply the criterion code (e.g. 'OM2' when the OM2 criteria is met with moderate strength); (2) If a criterion is met and its default strength is altered, the outcome is the criterion code plus the altered strength value (e.g. 'OS2_moderate' when OS2 is met with an adjusted moderate strength); (3) If a criterion is not met, the outcome is the criterion code plus the string 'not_met' (e.g. 'OS2_not_met').


**Artifacts**

 - |oncogenicity_functional_impact_evidence_line_source_yaml|
 - |oncogenicity_functional_impact_evidence_line_json_schema|

.. _acmg-2015-profiles:

ACMG 2015 Aligned Profiles
@@@@@@@@@@@@@@@@@@@@@@@@@@

The following profiles align with terminology and curation conventions from the `ACMG 2015 Pathogenicity Interpretation Guidelines <https://pubmed.ncbi.nlm.nih.gov/25741868>`_.

These initial profiles were developed to support the following implementations and use cases: 

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: 30 70

   *  - Implementer
      - Use Case
   *  - ClinVar GKS
      - Will use VA-Spec to represent GKS-based representations of the ClinVar XML records, and exchange this data across various ClinGen data systems
   *  - MAVE DB
      - Will use VA-Spec as a format to send multiplex-assay based functional impact data, classifications, and evidence interpretations to external platforms where they can be used to support pathogenicity and oncogenicity interpretation.

The breadth and coverage of these early profiles will grow as these impleentations expand their scope, and additional implementers bring new use cases to the spec. 

Profiles are :ref:`authored<profile-authoring-mechanisms>` , and described below, as ACMG-based constraints on top of a core :ref:`Statement<Statement>` and :ref:`Evidence Line<EvidenceLine>` class definitions. 

.. _variant-pathogenicity-statement-acmg-2015:

Variant Pathogenicity Statement (ACMG 2015)
###########################################

.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A Statement describing the role of a variant in causing an inherited condition.

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
      - :ref:`variant-pathogenicity-proposition`
      - 1..1
      - A proposition about the pathogenicity of a varaint, the validity of which is assessed and reported by the Statement. A Statement can put forth the proposition as being true, false, or uncertain, and may provide an assessment of the level of confidence/evidence supporting this claim.
   *  - strength
      -
      - :ref:`MappableConcept` (nested enum: likely | definitive)
      - 0..1
      - A term used to report the strength of a Proposition's assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be). The indicated enumeration is bound to the 'code' field in the Coding object nested inside the MappableConcept.
   *  - classification
      -
      - :ref:`MappableConcept`  (nested enum: pathogenic | likely pathogenic | benign | likely benign | uncertain significance)
      - 0..1
      - A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's Proposition, in terms of a classification of its subject. The indicated enumeration is bound to the 'code' field in the Coding object nested inside the MappableConcept.


**Artifacts**
 - |pathogenicity_statement_source_yaml|
 - |pathogenicity_statement_json_schema|

-----

.. _variant-pathogenicity-evidence-line-acmg-2015:

Variant Pathogenicity Evidence Line (ACMG 2015)
###############################################

.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

An Evidence Line that describes how a specific type of information was interpreted as evidence for or againtst a variant's pathogenicity. In the ACMG Framework, evidence is assessed by determining if a specific criterion (e.g. 'PM2') with a default strength (e.g. 'moderate') is 'met' or 'not met', and in some cases adjusting the default strength based on the quality and abundance of evidence.

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
      - :ref:`variant-pathogenicity-proposition`
      - 0..1
      - A Variant Pathogenicity Proposition against which a specific type of evidence was assessed, to determine the strength and direction of support this evidence provides for or against the proposition's validity.
   *  - directionOfEvidenceProvided
      -
      - string (enum: supports | disputes | none)
      - 1..1
      - The direction of support that the Evidence Line is determined to provide toward its target Proposition (supports, disputes, neutral). For ACMG-based assessments, if a pathogenicity criterion is 'met' in the Evidence Line the direction is 'supports', if a benignity criterion is 'met' the direction is 'disputes',  and if a criteria is 'not met' the direction is 'none'.
   *  - strengthOfEvidenceProvided
      -
      - :ref:`MappableConcept` (nested enum: stand alone | very strong | strong | moderate | supporting)
      - 0..1
      - The strength of support that an Evidence Line is determined to provide for or against the proposed pathogenicity of the assessed variant. Strength is evaluated relative to the direction indicated by the 'directionOfEvidenceProvided' attribute, and captured using a MappableConcept, whose nested 'code' field is bound to an enumerated set of values. Conditional requirement: if  `directionOfEvidenceProvided` is either 'supports' or 'disputes', then this attribute is required. If it is 'none', then this attribute is not allowed.
   *  - specifiedBy
      -
      - :ref:`Method`
      - 0..1
      - The guidelines or rubrics followed in interpreting evidence, to determine the strength and direction of support that it provides for or against a variant's pathogenicity. While the ACMG Criteria themselves provide minimal guidance, typically a more detailed, disease- or gene- specific rubric is followed to determine if a given criterion was met, and how strongly (e.g. the ClinGen Hearing Loss Expert Panel guidelines for ACMG interpretations).
   *  - methodType
      -
      - string (enum: PVS1 | PS1 | PS2 | PS3 | PS4 | PM1 | PM2 | PM3 | PM4 | PM5 | PM6 | PP1 | PP2 | PP3 | PP4 | PP5 | BA1 | BS1 | BS2 | BS3 | BS4 | BP1 | BP2 | BP3 | BP4 | BP5 | BP6 | BP7)
      - 1..1
      -  A term representing the type of method used to assess evidence for or against the pathogenicity of a variant. Method type is reported as the ACMG Code that defines criteria against which evidence is assessed to determine if it supports pathogenicity or benignity of a variant.
   *  - evidenceOutcome
      -
      - :ref:`MappableConcept` (nested enum, examples: PS3 | PS3_moderate | PS3_not_met | BP6 | BP6_strong | BS3_not_met)
      - 0..1
      - The evidence outcome provides a single string that summarizes 'directionOfEvidenceProvided' and 'strengthOfEvidenceProvided' assessments, along with the specific ACMG criterion used in these assessments. Rules for constructing this string are as follows, and enforced by a regex constraint: (1) If a criterion is met and its default strength is not altered, the outcome is simply the criterion code (e.g. 'PM2' when the PM2 criteria is met with moderate strength);  (2) If a criterion is met and its default strength is altered, the outcome is the criterion code plus the altered strength value (e.g. 'PS3_moderate' when PS3 is met with an adjusted moderate strength); (3)  If a criterion is not met, the outcome is the criterion code plus the string 'not_met' (e.g. 'PS3_not_met').


**Artifacts**

 - |pathogenicity_functional_impact_evidence_line_source_yaml|
 - |pathogenicity_functional_impact_evidence_line_json_schema|

.. _aac-2017-profiles:

AAC 2017 Aligned Profiles
!!!!!!!!!!!!!!!!!!!!!!!!!

The following profiles align with terminology and curation conventions from the `2017 AMP/ASCO/CAP (AAC) Clinical Variant Interpretation Guidelines <https://pubmed.ncbi.nlm.nih.gov/27993330/>`_.

These initial profiles were developed to support the following implementations and use cases: 

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: 30 70

   *  - Implementer
      - Use Case
   *  - VICC MetaKB
      - Using VA-Spec models to structure diagnostic, prognostic, and therapeutic response variant classifications and evidence in its community-facing data exchange APIs.
   *  - ClinVar Submission Utility
      - Uses VA-Spec as input format for submission tools that send variant classifications and evidence from CIViC to the ClinVar database via its API.

The number and coverage of these profiles will grow as these implementations expand their scope, and additional adopters bring new use cases to the spec. 

.. _variant-therapeutic-response-statement-aac-2017:

Variant Therapeutic Response Statement (AAC 2017)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A statement reporting whether a variant is associated with a therapeutic response (positive or negative).

**Information Model**

This profile applies the following **constraints** on top of the core :ref:`Statement<Statement>` class definition:

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto


   *  - Field
      - Flags
      - Type
      - Limits
      - Description
   *  - proposition
      -
      - :ref:`Variant Therapeutic Response Proposition <variant-therapeutic-response-proposition>`
      - 1..1
      - A proposition about the therapeutic response associated with a variant, in the context of a particular condition. The validity of this proposition, and the level of confidence/evidence supporting it, may be assessed and reported by the Statement.
   *  - strength
      -
      - :ref:`MappableConcept` (nested enum:  Level A | Level B | Level C | Level D)
      - 0..1
      - A term used to report the strength of a Proposition's assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be). The indicated enumeration is bound to the 'code' field in the Coding object nested inside the MappableConcept.
   *  - classification
      -
      - :ref:`MappableConcept`  (nested enum: Tier I | Tier II | Tier III | Tier IV)
      - 0..1
      - A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's Proposition, in terms of a classification of its subject. The indicated enumeration is bound to the 'code' field in the Coding object nested inside the MappableConcept.

**Artifacts**

 - |therapeutic_reponse_study_statement_source_yaml|
 - |therapeutic_reponse_study_statement_json_schema|

-----

.. _variant-diagnostic-statement-aac-2017:

Variant Diagnostic Statement (AAC 2017)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A statement reporting whether a variant is associated with a disease (a diagnostic inclusion criterion), or absence of a disease (diagnostic exclusion criterion).

**Information Model**

This profile applies the following **constraints** on top of the core :ref:`Statement<Statement>` class definition:

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Field
      - Flags
      - Type
      - Limits
      - Description
   *  - proposition
      -
      - :ref:`Variant Diagnostic Proposition <variant-diagnostic-proposition>`
      - 1..1
      - A proposition about a diagnostic association between a variant and condition. The validity of this proposition, and the level of confidence/evidence supporting it, may be assessed and reported by the Statement.
   *  - strength
      -
      - :ref:`MappableConcept` (nested enum:  Level A | Level B | Level C | Level D)
      - 0..1
      - A term used to report the strength of a Proposition's assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be). The indicated enumeration is bound to the 'code' field in the Coding object nested inside the MappableConcept.
   *  - classification
      -
      - :ref:`MappableConcept` (nested enum:  Level A | Level B | Level C | Level D)
      - 0..1
      - A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's Proposition, in terms of a classification of its subject. The indicated enumeration is bound to the 'code' field in the Coding object nested inside the MappableConcept.

**Artifacts**

 - |diagnostic_study_statement_source_yaml|
 - |diagnostic_study_statement_json_schema|

-----

.. _variant-prognostic-statement-aac-2017:

Variant Prognostic Statement (AAC 2017)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A statement reporting whether a variant is associated with a disease prognosis.

**Information Model**

This profile applies the following **constraints** on top of the core :ref:`Statement<Statement>` class definition:

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Field
      - Flags
      - Type
      - Limits
      - Description
   *  - proposition
      -
      - :ref:`Variant Prognostic Proposition <variant-prognostic-proposition>`
      - 1..1
      - A proposition about a prognostic association between a variant and condition. The validity of this proposition, and the level of confidence/evidence supporting it, may be assessed and reported by the Statement.
   *  - strength
      -
      - :ref:`MappableConcept` (nested enum:  Level A | Level B | Level C | Level D)
      - 0..1
      - A term used to report the strength of a Proposition's assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be). The indicated enumeration is bound to the 'code' field in the Coding object nested inside the MappableConcept.
   *  - classification
      -
      - :ref:`MappableConcept` (nested enum:  Level A | Level B | Level C | Level D)
      - 0..1
      - A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's Proposition, in terms of a classification of its subject. The indicated enumeration is bound to the 'code' field in the Coding object nested inside the MappableConcept.

**Artifacts**

 - |prognostic_study_statement_source_yaml|
 - |prognostic_study_statement_json_schema|

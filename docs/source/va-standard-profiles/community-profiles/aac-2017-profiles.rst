.. _aac-2017-profiles:

AMP/ASCO/CAP 2017 Aligned Profiles
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

The following profiles align with terminology and curation conventions from the `2017 AMP/ASCO/CAP Clinical Variant Interpretation Guidelines <https://pubmed.ncbi.nlm.nih.gov/27993330/>`_.

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

.. _variant-clinical-significance-statement-aac-2017:

Variant Clinical Significance Statement
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include::  ../../def/va-spec.aac-2017/VariantClinicalSignificanceStatement.rst

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
      - :ref:`Variant Clinical Significance Proposition<clinical-significance-proposition>`
      - 1..1
      - A proposition about the clinical significance of a variant with respect to a condition. The validity of this proposition, and the level of confidence/evidence supporting it, may be assessed and reported by the Statement.
   *  - strength
      -
      - :ref:`MappableConcept` (nested enum:  strong | potential)
      - 0..1
      - A term used to report the strength of a Proposition's assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be). The indicated enumeration is bound to the 'code' field in the Coding object nested inside the MappableConcept.
   *  - classification
      -
      - :ref:`MappableConcept`  (nested enum: tier i | tier ii | tier iii | tier iv)
      - 0..1
      - A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's Proposition, in terms of a classification of its subject. The indicated enumeration is bound to the 'code' field in the Coding object nested inside the MappableConcept. If `tier i` or `tier ii`, then a `PrognosticEvidenceLine`, `DiagnosticEvidenceLine`, or `TherapeuticEvidenceLine` MUST be used for any evidence lines (see Artifacts below for more information).

**Artifacts**

 - |variant_clinical_significance_statement_source_yaml|
 - |variant_clinical_significance_statement_json_schema|

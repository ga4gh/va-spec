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

VariantClinicalSignificanceStatement
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

.. include::  ../../def/va-spec.aac-2017/VariantClinicalSignificanceStatement.rst

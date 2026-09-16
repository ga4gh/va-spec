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

The number and coverage of these profiles will grow as these implementations expand their scope, and additional adopters bring new use cases to the spec.

.. _variant-pathogenicity-statement-acmg-2015:
.. _VariantPathogenicityStatement:

Variant Pathogenicity Statement (ACMG 2015)
###########################################

.. include::  ../../def/va-spec.acmg-2015/VariantPathogenicityStatement.rst

**Artifacts**
 - |pathogenicity_statement_source_yaml|
 - |pathogenicity_statement_json_schema|

-----

.. _variant-pathogenicity-evidence-line-acmg-2015:
.. _VariantPathogenicityEvidenceLine:

Variant Pathogenicity Evidence Line (ACMG 2015)
###############################################

.. include::  ../../def/va-spec.acmg-2015/VariantPathogenicityEvidenceLine.rst

**Artifacts**

 - |pathogenicity_evidence_line_source_yaml|
 - |pathogenicity_evidence_line_json_schema|

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

   *  - Implementer
      - Use Case
   *  - VICC MetaKB
      - Using VA-Spec models to structure oncogenicity classifications and evidence in its community-facing data exchange APIs.
   *  - ClinVar Submission Utility
      - Uses VA-Spec as input format for submission tools that send variant classifications and evidence from CIViC to the ClinVar database via its API.

The number and coverage of these profiles will grow as these implementations expand their scope, and additional adopters bring new use cases to the spec.

.. _variant-oncogenicity-statement-ccv-2022:
.. _VariantOncogenicityStatement:

Variant Oncogenicity Statement (CCV 2022)
#########################################

.. include::  ../../def/va-spec.ccv-2022/VariantOncogenicityStatement.rst

**Artifacts**

 - |oncogenicity_study_statement_source_yaml|
 - |oncogenicity_study_statement_json_schema|

-----

.. _variant-oncogenicity-evidence-line-ccv-2022:
.. _VariantOncogenicityEvidenceLine:

Variant Oncogenicity Evidence Line (CCV 2022)
##############################################

.. include::  ../../def/va-spec.ccv-2022/VariantOncogenicityEvidenceLine.rst

**Artifacts**

 - |oncogenicity_evidence_line_source_yaml|
 - |oncogenicity_evidence_line_json_schema|

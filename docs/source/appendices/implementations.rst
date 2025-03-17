.. _implementations:

Implementations
!!!!!!!!!!!!!!!

The following implementations are a work in progress as they are built on pre-release versions
of the VA-Spec. They are expected to be updated as the VA-Spec is finalized.


.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: 25 25 50

   *  - Name
      - Link
      - Description
   *  - VA Spec Python
      - `GA4GH VA-Spec Python Repository <https://github.com/ga4gh/va-spec-python>`_
      - The reference implementation for VA-Spec, this python package provides tools for generation and validation of VA-Spec objects.
   *  - VICC MetaKB
      - `Cancer Variants API v2 (Dev) <https://dev-search.cancervariants.org/api/v2>`_
      - The VICC Meta-Knowledgebase (MetaKB) v2 is currently under development as a knowledge integration engine that works across germline and somatic variant evidence. It represents genomic knowledge statements using the VA-Spec v1.0 March pre-release.
   *  - ClinVar Submission Utility
      - `ClinVar This Repository <https://github.com/clingen-data-model/clinvar-this>`_
      - This fork of the clinvar-this library uses GKS-formatted data submissions as input for sharing of evidence to the ClinVar database via its API. This is being used by the VICC Driver Project to share assertion data from the CIViC platform with ClinVar.
   *  -  ClinVar GKS
      - `ClinGen ClinVar GKS Repository <https://github.com/clingen-data-model/clinvar-gks>`_
      - Repository for the ClinGen ClinVar GKS pipeline (coming soon), which is a GKS-formatted version of the ClinVar database. This repository is used to generate the ClinVar GKS from the ClinVar XML data. A pre-release version of ClinVar in GKS format from Nov 2024 is available for download

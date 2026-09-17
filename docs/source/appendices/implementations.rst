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
      - `Online MetaKB UI <https://pediatric.metakb.org/>`_
      - The VICC Meta-Knowledgebase (MetaKB) v2 is currently under development as a knowledge integration engine that works across germline and somatic variant evidence. It represents genomic knowledge statements using the VA-Spec v1.0 March pre-release.
   *  - ClinVar Submission Utility
      - `ClinVar This Repository <https://github.com/clingen-data-model/clinvar-this>`_
      - This fork of the clinvar-this library uses GKM-formatted data submissions as input for sharing of evidence to the ClinVar database via its API. This is being used by the VICC Driver Project to share assertion data from the CIViC platform with ClinVar.
   *  -  ClinVar-GKM
      - `ClinGen ClinVar-GKM website <https://dataexchange.clinicalgenome.org/clinvar-gkm/>`_
      - Provides a standardized, machine-readable representation of ClinVar release data using the GKM schema set (VRS, Cat-VRS, and VA-Spec) -- normalizing variant identifiers, representing categorical variants via Cat-VRS, and capturing classification statements as VA-Spec representations. Actively maintained, with monthly full releases and weekly delta updates published in sync with ClinVar's own release schedule; the current v1 release covers variations, submitted classifications (SCVs), aggregated classifications (VCVs), and condition-level classifications (RCVs), with functional data submissions and case-level observations planned for future versions. See the `ClinGen ClinVar-GKM Repository <https://github.com/clingen-data-model/clinvar-gkm>`_ for the pipeline that generates it from ClinVar's XML data.

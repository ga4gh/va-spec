.. _community-profile-sets:

Community Profile Sets
!!!!!!!!!!!!!!!!!!!!!!

Many **VA Standard Profiles** are aligned with the terminologies and curation conventions defined in established community guidelines for generating variant knowledge.

**VA Community Profile Sets** are collections of VA Standard Profiles that all align with a particular guideline, and can be used together by implementers who wish to follow the terminological and curation conventions of a community in how they represent their data.

For example, profiles in the **ACMG-2015 Community Profile Set** define enumerations based on ACMG criterion codes (``PS3``, ``BS3``), criterion assessment outcomes (``met``, ``not met``), evidence strengths (``strong``, ``supporting``, ``moderate``), and classification outcomes (``pathogenic``, ``likely pathogenic``, ``benign``, ``likely benign``, ``VUS``), in constraining the values of specific attributes to align with this guideline.

Version 1 of the VA-Spec includes the three Community Profile Sets described below. At present these contain only a few profiles needed for ClinGen's and VICC's initial small-scale implementations. The number of profiles in each set will grow as these adopters expand the scope of their implementations, and new adopters provide additional use cases and requirements.


.. _acmg-2015:

ACMG-2015 Community Profile Set
###############################

A set of profiles defined to align with terminology and conventions from the American College of Medical Genetics and Genomics (ACMG) 2015 guidelines for interpretation of sequence **variant pathogenicity**.

**Community Guideline:**

 - `American College of Medical Genetics and Genomics 2015 Pathogenicity Interpretation Guidelines <https://pubmed.ncbi.nlm.nih.gov/25741868>`_

**Included Profiles**:

  - :ref:`Variant Pathogenicity Statement (ACMG 2015)<variant-pathogenicity-statement-acmg-2015>`
  - :ref:`Experimental Variant Pathogenicity Functional Impact Evidence Line (ACMG 2015)<experimental-variant-pathogenicity-functional-impact-evidence-line-acmg-2015>`
  - :ref:`Variant Pathogenicity Proposition<variant-pathogenicity-proposition>`

**Implementation Notes:**

This Profile Set supports data generated using ACMG-based guidelines or terminologies.

 - The **Statement** profile in this set can represent final pathogenicity classifications of a variant.
 - The **Evidence Line** profile can describe how functional data is interpreted as evidence for these classifications.
 - The **Proposition** profile itself does not define any ACMG-specific constraints, but is used to build the **Statement** and **Evidence Line** structures that do.

As additional ACMG-based Evidence Line profiles are created to describe interpretation of different evidence types, or Study Result profiles created to represent the foundational data used as evidence, these will be added to this community profile set.


.. _ccv-2022:

CCV-2022 Community Profile Set
##############################

A set of profiles defined to align with terminology and conventions from the Clinical Genome Resource (ClinGen), Cancer Genomics Consortium (CGC), and Variant Interpretation for Cancer Consortium (VICC) 2022 community guidelines for interpretation of **variant oncogenicity**.

**Community Guideline:**

 - `ClinGen/CGC/VICC (CCV) 2022 oncogenicity interpretation guidelines <https://pubmed.ncbi.nlm.nih.gov/35101336/>`_

**Included Profiles**:
 - :ref:`Variant Oncogenicity Statement (CCV 2022)<variant-oncogenicity-statement-ccv-2022>`
 - :ref:`Experimental Variant Oncogenicity Functional Impact Evidence Line (CCV 2022)<experimental-variant-oncogenicity-functional-impact-evidence-line-ccv-2022>`
 - :ref:`Variant Oncogenicity Proposition<variant-oncogenicity-proposition>`

**Implementation Notes:**

This Profile Set includes VA Standard Profiles that support data generated using CCV-based oncogenicity guidelines or terminologies.

 - The **Statement** profile can represent final oncogenicity classifications of a variant.
 - The **Evidence Line** profile can describe how functional data is interpreted as evidence for these classifications.
 - The **Proposition** profile itself does not define any CCV-specific constraints, but is used to build **Statement** and **Evidence Line** structures that do.

As additional CCV-based Evidence Line profiles are created to describe interpretation of different evidence types, or Study Result profiles created to represent the foundational data used as evidence, these will be added to this community profile set.


.. _aac-2017:

AMP/ASCO/CAP 2017 Community Profile Set
#######################################

A set of profiles defined to align with terminology and conventions from the Association for Molecular Pathology (AMP), American Society of Clinical Oncology (ASCO), and College of American Pathologists (CAP) 2017 guidelines for **clinical significance interpretation** of sequence variants in cancer.

**Community Guideline:**

 - `AMP/ASCO/CAP 2017 clinical interpretation guidelines <https://pubmed.ncbi.nlm.nih.gov/27993330/>`_

**Included Profiles**:

  - :ref:`Variant Clinical Significance Statement<variant-clinical-significance-statement-aac-2017>`
  - :ref:`Variant Therapeutic Response Proposition<variant-therapeutic-response-proposition>`
  - :ref:`Variant Diagnostic Proposition<variant-diagnostic-proposition>`
  - :ref:`Variant Prognostic Proposition<variant-prognostic-proposition>`

**Implementation Notes:**

This Profile Set includes VA Standard Profiles that support data generated using AMP/ASCO/CAP-based interpretation guidelines or terminologies.

 - The **Statement** profiles can represent final different types of clinical classifications of a variant.
 - The **Proposition** profiles themselves do not define any AMP/ASCO/CAP-specific constraints, but are used to build the **Statement** structures that do.

As any new AMP/ASCO/CAP-based profiles are created to support emerging use cases, these will be added to this community profile set.

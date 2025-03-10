.. _community-profile-sets:

Community Profile Sets
!!!!!!!!!!!!!!!!!!!!!!

Many **VA Standard Profiles** are aligned with the terminologies and curation conventions defined in standard community guidelines for generating variant knowledge. 

**VA Community Profile Sets** are collections of Standard Profiles that all align with a particular guidleine, and can be used together by implementers who wish to follow this standard in the strucutre and semantics of their data. 

For example, profiles in the **ACMG-2015 Community Profile Set** use ACMG's criterion codes (e.g. ``PS3``, ``BS3``), criterion assessment outcomes (``met``, ``not met``), evidence strengths (e.g. ``strong``, ``supporting``, ``moderate``), and classification outcomes (e.g. ``pathogenic``, ``likely pathogenic``, ``benign``, ``likely benign``, ``VUS``) in enumerations that constrain the values of specific attributes.

Version 1 of the VA-Spec includes the Community Profile Sets described below. At present each set includes only a few profiles as needed to support ClinGen's and VICC's initial small-scale implementations.   


.. _acmg-2015:

ACMG-2015 Community Profile Set
###############################

A set of profiles defined to align with terminology and conventions from the American College of Medical Genetics and Genomics (ACMG) 2015 guidelines for interpretation of sequence variant pathogenicity.

**Community Guideline:** 
 
 - `American College of Medical Genetics and Genomics 2015 Pathogenicity Interpretation Guidelines <https://pubmed.ncbi.nlm.nih.gov/25741868>`_

**Included Profiles**:

  - :ref:`Variant Pathogenicity Statement (ACMG 2015)<variant-pathogenicity-statement-acmg-2015>`
  - :ref:`Experimental Variant Pathogenicity Functional Impact Evidence Line (ACMG 2015)<experimental-variant-pathogenicity-functional-impact-evidence-line-acmg-2015>`

**Implementation Notes:**

 - This Profile Set supports data generated using ACMG-based guidelines or terminologies. 
 - The **Statement** profile can represent final classifications of a variant, and the **Evidence Line** profile can describe how functional data is interpreted as evidence for these classifications. 
 - As additional ACMG-based Evidence Line profiles are created to describe interpretation of different evidence types, or Study Result profiles created to represent the foundational data used as evidence, these will be added to this community profile set. 


.. _ccv-2022:

CCV-2022 Community Profile Set
##############################

A set of profiles defined to align with terminology and conventions from the Clinical Genome Resource (ClinGen), Cancer Genomics Consortium (CGC),and Variant Interpretation for Cancer Consortium (VICC) 2022 community guidelines for cancer variant interpretation. 

**Community Guideline:**  

 - `ClinGen/CGC/VICC (CCV) 2022 oncogenicity interpretation guidelines <https://clinicalgenome.org/docs/standards-for-the-classification-of-pathogenicity-of-somatic-variants-in-cancer-oncogenicity-joint-recommendations-of-clinical/>`_

**Included Profiles**:
 - :ref:`Variant Oncogenicity Statement (CCV 2022)<variant-oncogenicity-statement-ccv-2022>`
 - :ref:`Experimental Variant Oncogenicity Functional Impact Evidence Line (CCV 2022)<experimental-variant-oncogenicity-functional-impact-evidence-line-ccv-2022>`

**Implementation Notes:**
 - This Profile Set includes VA Standard Profiles that support data generated using CCV-based oncogenicity guidelines or terminologies. 
 - The **Statement** profile can represent final classifications of a variant, and the **Evidence Line** profile can describe how functional data is interpreted as evidence for these classifications. 
 - As additional CCV-based Evidence Line profiles are created to describe interpretation of different evidence types, or Study Result profiles created to represent the foundational data used as evidence, these will be added to this community profile set. 


.. _aac-2017:

AAC-2017 Community Profile Set
###############################

A set of profiles defined to align with terminology and conventions from the Association for Molecular Pathology (AMP), American Society of Clinical Oncology (ASCO), and College of American Pathologists (CAP) 2017 guidelines for the interpretation and reporting of sequence variants in cancer. 

**Community Guideline:**  
 
 - `AMP/ASCO/CAP (AAC) 2017 clinical interpretation guidleines <https://pubmed.ncbi.nlm.nih.gov/27993330/>`_

**Included Profiles**:

  - :ref:`Variant Therapeutic Response Statement (AAC 2017)<variant-therapeutic-response-statement-aac-2017>`
  - :ref:`Variant Diagnostic Statement (AAC 2017)<variant-diagnostic-statement-aac-2017>`
  - :ref:`Variant Prognostic Statement (AAC 2017)<variant-prognostic-statement-aac-2017>`

**Implementation Notes:**
 - This Profile Set includes VA Standard Profiles that support data generated using AAC-based interpretation guidelines or terminologies.
 - As new AAC-based Evidence Line profiles are created to describe interpretation of different evidence types, or Study Result profiles created to represent the foundational data used as evidence, these will be added to this community profile set. 

.. _community-profile-sets:

Community Profile Sets
!!!!!!!!!!!!!!!!!!!!!!

Many **VA Standard Profiles** are aligned with the curation and terminological conventions of an established community guideline for generating variant knowledge. 

**VA Community Profile Sets** are collections of standard profiles that all align with a given guidleine, and can be used together by implementers who wish to follow this standard in defining the strucutre and semantics of their data. 

For example, the **ACMG-2015 Community Profile Set** includes standard Statement and Evidence Line profiles that support representation of the ACMG-based variant interpretation process, and use ACMG-based terminology in constraining certain data (e.g. evidence strength terms, interpretation criterion codes).

Version 1 of the VA-Spec includes the following Community Profile Sets below

  - **ACMG-2015**: supports the American College of Medical Genetics and Genomics 2015 pathogenicity interpretation guidelines
  - **CCV-2022**: supports the ClinGen/CGC/VICC 2022 oncogenicity interpretation guidelines
  - **AAC-2017**: supports the AMP/ASCO/CAP 2017 clinical interpretation guidleines 


.. _acmg-2015:

ACMG-2015 Community Profile Set
###############################

**Community Guideline:** `American College of Medical Genetics and Genomics 2015 Pathogenicity Interpretation Guidelines <https://pubmed.ncbi.nlm.nih.gov/27993330/>`_

**Included Profiles**:

  - :ref:`Variant Pathogenicity Statement (ACMG 2015)<variant-pathogenicity-statement-acmg-2015>`
  - :ref:`Experimental Variant Pathogenicity Functional Impact Evidence Line (ACMG 2015)<experimental-variant-pathogenicity-functional-impact-evidence-line-acmg-2015>`

**Implementation Notes:**

  - This Profile Set supports representation data generated using ACMG-based guidelines or terminologies.
  - The **Statement** profile can represent final classifications of a variant, and the **Evidence Line** profile can describe how functional data is interpreted as evidence for these classifications. 
  - As additional ACMG-based Evidence Line profiles are created to describe interpretation of different evidence types, or Study Result profiles created to represent the foundational data used as evidence, these will be added to this community profile set. 


.. _ccv-2022:

CCV-2022 Community Profile Set
##############################

This Profile Set includes VA standard Profiles that support representation data generated using CCV-based oncogenicity guidelines or terminologies.

 #. :ref:`Variant Oncogenicity Statement (CCV 2022)<variant-oncogenicity-statement-ccv-2022>`
 #. :ref:`Experimental Variant Oncogenicity Functional Impact Evidence Line (CCV 2022)<experimental-variant-oncogenicity-functional-impact-evidence-line-ccv-2022>`

Here, the **Variant Oncogenicity Statement** profile can represent final classifications of a variant, and the **Experimental Variant Oncogenicity Functional Impact Evidence Line** profile can describe how functional data is interpreted as evidence for these classifications. 

As additional CCV-based Evidence Line profiles are created to describe interpretation of different evidence types, or Study Result profiles created to represent the foundational data used as evidence, these will be added to this community profile set. 


.. _aac-2017:

AAC-2017 Community Profile Set
###############################
https://pubmed.ncbi.nlm.nih.gov/25741868/
This Profile Set includes VA standard Profiles that support representation data generated using AAC-based interpretation guidelines or terminologies.

 #. :ref:`Variant Therapeutic Response Statement (AAC 2017)<variant-therapeutic-response-statement-aac-2017>`
 #. :ref:`Variant Diagnostic Statement (AAC 2017)<variant-diagnostic-statement-aac-2017>`
 #. :ref:`Variant Prognostic Statement (AAC 2017)<variant-prognostic-statement-aac-2017>`

As new AAC-based Evidence Line profiles are created to describe interpretation of different evidence types, or Study Result profiles created to represent the foundational data used as evidence, these will be added to this community profile set. 

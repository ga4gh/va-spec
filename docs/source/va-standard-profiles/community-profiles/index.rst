.. _community-profiles:

Community Profiles
!!!!!!!!!!!!!!!!!!

Version 1 of the VA-Spec includes **Statement** and **Evidence Line** Community Profiles aligned with three established variant interpretation guidelines:

 - the `ACMG 2015 Pathogenicity Interpretation Guidelines <https://pubmed.ncbi.nlm.nih.gov/25741868/>`_
 - the `ClinGen/CGC/VICC (CCV) 2022 Oncogenicity Interpretation Guidelines <https://pubmed.ncbi.nlm.nih.gov/35101336/>`_
 - the `AMP/ASCO/CAP (AAC) Guidelines for Clinical Interpretation of Genetic Variants <https://pubmed.ncbi.nlm.nih.gov/27993330>`_

These Community Profiles layer additional constraints on top of core class definitions to enforce alignment with terminology conventions of a specific community guideline. For example, ACMG-based profiles incorporate ACMG terminology into enuemrated value sets bound to core :ref:`Statement<Statement>` and :ref:`Evidence Line<EvidenceLine>` attributes, including:

- ACMG criterion codes (``PS3``, ``BS3``)
- ACMG criterion assessment outcomes (``met``, ``not met``)
- ACMG evidence strengths (``strong``, ``supporting``, ``moderate``)
- ACMG classification outcomes (``pathogenic``, ``likely pathogenic``, ``benign``, ``likely benign``, ``VUS``)

See :ref:`here <acmg-variant-pathogencity-statement-example>` for a simple data example of an ACMG-aligned Variant Pathogenicity Statement.

See :ref:`here <profile-authoring-mechanisms>` for a description of how constraints in Community Pofiles are authored.

-----

**Index:**

.. toctree::
   :maxdepth: 4
   :titlesonly:

   acmg-2015-profiles
   ccv-2022-profiles
   aac-2017-profiles

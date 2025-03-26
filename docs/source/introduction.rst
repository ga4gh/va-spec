.. _introduction:

Introduction
!!!!!!!!!!!!


Overview
########

The GA4GH Variant Annotation Specification (VA-Spec) defines a set of schema for representing different types of knowledge about genetic variants, to provide a common format for exchange between data systems. Each schema is built as a "profile" that extends a common, domain-agnostic :ref:`VA Core Model <va-core-model>`. The initial v1 release of the VA-Spec is focused on supporting specific types of variant knowledge exchanged by implementing Driver Projects and organizational members, including `ClinGen <https://clinicalgenome.org/>`_, `VICC <https://cancervariants.org/index.html>`_, and the `Atlas of  Variant Effects Alliance <https://www.varianteffect.org/>`_. The specification includes machine-readable JSON Schema specifications that support sharing and validation within and across these projects, along with a python reference implementation. In defining its models, VA-Spec builds on several more foundational standards, including the `SEPIO Model <https://github.com/sepio-framework/sepio-linkml>`_, and GA4GH `VRS <https://vrs.ga4gh.org/en/latest/index.html>`_  and `Cat-VRS <https://cat-vrs.readthedocs.io/en/latest/index.html>`_ schema. Future VA-Spec releases will include a modeling framework to support community-based authoring of profiles for new knowledge types and use cases.


Components
##########

The v1 release of VA-Spec includes the following components:

#. :ref:`A Foundational VA Core Model <va-core-model>`: A domain-agnostic model for describing knowledge of any kind, and the evidence and provenance supporting it. *The Core Model establishes a shared understanding of fundamental terms, concepts, and modeling patterns - and provides a foundation on which 'Standard VA Profiles' are built*.

#. :ref:`VA Profiles <va-profiles>`: A set of models built as specializations of core Statement, Study Result, and Evidence Line classes, each supporting a specific type of knowledge about genetic variation (e.g. this :ref:`Pathogenicity Statement Profile <variant-pathogenicity-statement>`). *These profiles are provided as machine-readable json schema, as common formats for representation and exchange of data by the GA4GH community*.

#. :ref:`A Python Reference Implementation <reference-implementation>`:  Code libraries that demonstrate the creation and validation compliant data using VA Profiles. *These resources provide a working example of code that can be adopted and/or extended by adopters*.

Use Cases and Applications
##########################

Currently, tools and systems that annotate variants with knowledge about their clinical or functional significance lack a consistent and unified exchange model, leading to challenges in data sharing and integration across platforms. The VA-Spec aims to address this gap by offering a comprehensive and extensible schema to support genomic data interpretation in research and clinical contexts.

As an exchange format, VA-Spec schema serve to provide a common structure to use in passing interoperable data between distinct systems. They are not designed to support search, analysis, and persistent storage applications - which will likely require other models from which data would be transformed into VA-Spec compliant forms for purposes of interoperable exchange. 

In this role, VA-Spec is intended to complement other GA4GH exchange formats such as `VRS <https://vrs.ga4gh.org/en/latest/index.html>`_  and `Cat-VRS <https://cat-vrs.readthedocs.io/en/latest/index.html>`_, which support interoperable representation of the variation concepts tha are the subjects of variant annotations.

Application use cases for the VA-Spec as a representation and exchange foramt include:
 - **Data integration across genomic knowledgebases**: Supporting consistent representation of variant-related knowledge in public genomic knowledgebases (e.g., ClinVar, OncoKB) and repositories hosting more foundational data and study results (e.g., gnomAD, MaveDB), enabling easier cross-referencing and data sharing.
 - **Evidence aggregation in curation and interpretation platforms**:  Facilitate import of diverse, standardized evidence from knowledgebases to support variant classification in research (e.g. ClinGen, CIViC) and clinical (e.g. Epic) contexts.
 - **Interoperable modules for use with other standards**: Providing models for functional and clinical annotations that can be embedded within other schemas and tools, such as Beacon, Phenopackets, and FHIR - to ensure cohesive and comprehensive data exchange across systems.

The table below describes some specific contexts in which VA-Spec supports these use cases, by facilitating the interoperable exchange of variant knowledge and evidence.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: 20 40 40

   *  - Project
      - Description
      - Implementation Status

   *  - ClinVar Submission Utility
      - Uses VA-Spec formatted data as input for tools that submit variant pathogenicity knowledge and evidence to the ClinVar database via its API.  
      - Active implementation used by the VICC Driver Project to share assertion data from the CIViC platform with ClinVar.


   *  - ClinVar GKS
      - Will use VA-Spec to represent GKS-based representations of the ClinVar XML records, and exchange this data across various ClinGen data systems
      - Under development, with initial implementation in ClinGen Data pipelines planned for 2025 to support variant pathogenicity statements

   *  - VICC MetaKB
      - Using VA-Spec models to structure various types of clinical significance classifications and evidence in its community-facing data exchange APIs
      - Active API implementation currently serving VA-Spec compliant data.

   *  - MAVE DB
      - Will use VA-Spec as a format in which to send multiplex-assay based functional impact data, classifications, and evidence interpretations to external curation platforms such as ClinGen and CIViC, where they will be used to support clinical variant interpretation.
      - Under development, with initial implementation planned for 2025.

   *  - Epic Variant Results & Tertiary Analysis
      - Will use VA-Spec as a format in which to receive varant knowledge from disparate sources including ClinVar and CIViC, which will be used to drive interpretation and clinical decision support in Epic.​
      - Under development, with initial implementation targeting variant pathogenicity and oncogenicity planned for 2025

More details about specific implementations of the VA-Spec can be found on the :ref:`Implementations <implementations>` page.


Scope and Development
#####################

VA-Spec takes an implementation-driven approach to development of the models it provides - releasing only models and elements that have been tested in real-world data systems. The initial release of the :ref:`VA Core Model<va-core-model>` contains a minimal subset of elements required to support early small-scale implementations led by ClinGen, VICC, and the Atlas of Variant Effects (AVE) Alliance.

:ref:`VA Profiles<va-profiles>` extend core :ref:`Statement<Statement>`, :ref:`Study Result<StudyResult>`, and :ref:`Evidence Line<EvidenceLine>` classes to support the specific types of knowledge captured (e.g. a variant pathogenicity), and community guidelines followed (e.g. the ACMG-2015 Guidelines) in implementing data systems. These three core classes are defined specifically to represent the levels at which curation tools and knowledgebases capture and report variant knowledge. Initial ClinGen, VICC, and AVE implementations required the profiles for the following types of variant knowledge in version 1 of the VA-Spec:

- **Statement Profiles** for Pathogenicity and Oncogenicity classifications, Therapeutic Response, Diagnostic, and Prognostic clinical associations, and Experimental Functional Impacts
- **Study Result Profiles** for Cohort Allele Frequency and Experimental Functioanl Impact analysis data.
- **Evidence Line Profiles** describing experimental Functional Impact evidence for Pathogenicity and Oncogenicity classifications.

Notably, various 'flavors' of profiles for a given knowledge type can be defined to align with different community guidelines and terminology standards. For example, v1 of the VA-Spec provides several of these :ref:`"Community Profiles"<community-profiles>`, which are aligned with :ref:`ACMG<acmg-2015-profiles>`, :ref:`CCV<ccv-2022-profiles>`, and :ref:`AAC<aac-2017-profiles>` guidelines in the domains of variant pathogenicity, oncogenicity, and clinical interpretation of somatic variants, respectively.

The initial, minimal profiles in VA-Spec v1.0  will expand along three axes as the specification evolves:

 - **Existing Profile Coverage**: the scope and size of existing profiles will grow as current implementations work to include more diverse and complex data from their sources, and new adopters bring additional data requirements and use cases. New elements to support this expansion will be pulled into VA-Spec as needed from the :ref:`SEPIO Core Information Model<what-is-sepio>`, on which VA-Spec models are based.
 - **New Base Profile Types**: the number of different profile types defined in the VA-Spec will expand, as driver projects with use cases for new knowledge types emerge (e.g. new profiles to Molecular Consequence, Evolutionary Conservation, or Phenotype Association knowledge)
 - **New Community Profiles**: new flavors of existing profiles that support the conventions and terminologies of different community guidelines will be created - e.g. separate Variant Pathogenicity profiles that support AMCG-2015 and the emerging update to these guidelines.

Importantly, the level of maturity of core and profile models, and the specific elements within each, are tracked according to the :ref:`GKS Maturity Model<gks-maturity-model>` - so adopters have a clear understanding of the stability and use of elements they employ in their systems.

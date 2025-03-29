.. _introduction:

Introduction
!!!!!!!!!!!!


Overview
########

Currently, tools and systems that annotate variants with knowledge about their clinical or functional significance lack a consistent and unified exchange model. This leads to challenges in data sharing and integration across platforms. The **GA4GH Variant Annotation Specification (VA-Spec)** aims to address this gap by offering a comprehensive and extensible schema to support genomic data interpretation in research and clinical contexts.

VA-Spec defines a set of schema for representing different types of knowledge about genetic variants, to provide a common format for exchange between data systems. Each schema is built as a :ref:`"Profile" <va-profiles>` that extends a common, domain-agnostic :ref:`VA Core Model <va-core-model>`. The initial v1 release of the VA-Spec includes the Profiles described :ref:`here <va-profiles>`, which support specific types of variant knowledge produced by implementing Driver Projects and organizational members, including `ClinGen <https://clinicalgenome.org/>`_, `VICC <https://cancervariants.org/index.html>`_, and the `Atlas of  Variant Effects Alliance <https://www.varianteffect.org/>`_. These Profiles are specified as **machine-readable JSON schema** that support sharing and validation within and across these projects, along with a **Python reference implementation**. 

In defining its models, VA-Spec adopts and builds on several more **foundational standards**, including the `SEPIO Model <https://github.com/sepio-framework/sepio-linkml>`_, and GA4GH `VRS <https://vrs.ga4gh.org/en/latest/index.html>`_  and `Cat-VRS <https://cat-vrs.readthedocs.io/en/latest/index.html>`_ schema. Future VA-Spec releases will include tighter integration with these upstream models, a larger set of Profiles with broader coverage, and a **modeling framework** to support community-based authoring of Profiles for new knowledge types and use cases.


Components
##########

The v1 release of VA-Spec includes the following components:

#. :ref:`A VA Core Model <va-core-model>`: A  foundational, domain-agnostic model for describing knowledge of any kind and the evidence and provenance supporting it. *The Core Model establishes a shared understanding of fundamental terms, concepts, and modeling patterns - and provides a foundation on which 'VA Profiles' for specific types of knowledge are built*.

#. :ref:`VA Profiles <va-profiles>`: A set of models built as specializations of core Statement, Study Result, and Evidence Line classes, each supporting a specific type of knowledge about genetic variation (e.g. this :ref:`Pathogenicity Statement Profile <variant-pathogenicity-statement>`). *These profiles are provided as machine-readable JSON Schema, as common formats for representation and exchange of data by the GA4GH community*.

#. :ref:`A Reference Implementation <reference-implementation>`:  Python code libraries that demonstrate the creation and validation compliant data using VA Profiles. *These resources provide a working example of code that can be adopted and/or extended by adopters*.

Use Cases and Implementations
#############################

As an exchange format, VA-Spec schema serve to provide a common structure to use in passing interoperable data between systems. VA models are not designed to support search, analysis, or persistent back end storage applications, but can be used or adapted for these purposes if desired.

General use cases for the VA-Spec as a data representation and exchange format include:

 - **Data integration across genomic knowledgebases**: Supporting consistent representation of variant-related knowledge in public genomic knowledgebases (e.g., ClinVar, OncoKB) and repositories hosting more foundational data and study results (e.g., gnomAD, MaveDB), enabling easier cross-referencing and data sharing.
 - **Evidence aggregation in curation and interpretation platforms**:  Facilitate import of diverse, standardized evidence from knowledgebases to support variant classification in research (e.g. ClinGen, CIViC) and clinical (e.g. Epic) contexts.
 - **Interoperable modules for use with other standards**: Providing models for functional and clinical annotations that can be embedded within other schemas and tools, such as Beacon, Phenopackets, and FHIR - to ensure cohesive and comprehensive data exchange across systems.

Specific implementations in which VA-Spec supports these use cases:

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: 20 40 40

   *  - Project
      - Description
      - Implementation Status
   *  - ClinVar Submission Utility
      - Uses VA-Spec as input format for submission tools that send variant pathogenicity classifications and evidence to the ClinVar database via its API.  
      - Active implementation used by the VICC Driver Project to share assertion data from the CIViC platform with ClinVar.
   *  - ClinVar GKS
      - Will use VA-Spec to represent GKS-based representations of the ClinVar XML records, and exchange this data across various ClinGen data systems
      - Under development, with initial implementation in ClinGen Data pipelines planned for 2025 to support variant pathogenicity statements
   *  - VICC MetaKB
      - Using VA-Spec models to structure various types of clinical significance classifications and evidence in its community-facing data exchange APIs
      - Active API implementation currently serving VA-Spec compliant data.
   *  - MAVE DB
      - Will use VA-Spec as a format to send multiplex-assay based functional impact data, classifications, and evidence interpretations to external curation platforms such as ClinGen and CIViC, where they will be used to support clinical variant interpretation.
      - Under development, with initial implementation planned for 2025.
   *  - Epic Variant Results & Tertiary Analysis
      - Will use VA-Spec as a format in which to receive variant knowledge from disparate sources including ClinVar and CIViC, which will be used to drive interpretation and clinical decision support in Epic.​
      - Under development, with initial implementation targeting variant pathogenicity and oncogenicity planned for 2025

More details about specific implementations of the VA-Spec can be found on the :ref:`Implementations <implementations>` page.


Scope and Development
#####################

VA-Spec takes an implementation-driven development approach - releasing only schema that have been tested in real-world data systems.  Each :ref:`VA Profile <va-profiles>` released in v1.0 of the specification has been applied in at least two of the implementations described above. And each class released in the foundational :ref:`VA Core Model <va-core-model>` includes only attributes that have been used or specialized in a released or developing Profile. Annotation of elements in the Core Model and Profiles with maturity tags based on the :ref:`GKS Maturity Model<gks-maturity-model>` ensures that adopters have a clear understanding of the stability and use of models they employ in their systems.

While this approach limits the scope of the initial VA-Spec release, it ensures that all content has proven utility in actual implementation settings. Note however that the :ref:`SEPIO Information Model <sepio-framework>`, from which the VA Core Model was derived, contains a broader set of elements that may support data not covered by current VA-Spec. These SEPIO elements can be incorporated into the VA Core Model as needed to support emerging data and use cases.

We anticipate that over time, the minimal Profiles included in VA-Spec 1.0 will expand in different ways:

- **Broader Coverage of Existing Profiles**: the scope of existing profiles will expand as current implementations start to include more data from their sources, and new adopters bring additional data types and use cases.
- **Addition of New Base Profile Types**: the number and types of profiles defined in the VA-Spec will expand, as new projects and use cases emerge (e.g. new base profiles to Molecular Consequence, Evolutionary Conservation, or Phenotype Association Propositions)
- **Addition of New Community Profiles**: new flavors of existing community profiles that support alternate community guidelines in a given domain may be created - e.g. separate Variant Pathogenicity profiles that support AMCG-2015 and the forthcoming update to these guidelines.




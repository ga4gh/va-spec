.. _introduction:

Introduction
!!!!!!!!!!!!


Overview
########

The GA4GH Variant Annotation Specification (VA-Spec) defines a set of standard schema to represent different types of knowledge about genetic variants. Each schema is built as a "profile" that extends a common, domain-agnostic :ref:`VA Core Model <va-core-model>`. The initial v1 release of the VA-Spec is focused on supporting specific types of variant knowledge provided by implementing Driver Projects and organizational members, including `ClinGen <https://clinicalgenome.org/>`_, `VICC <https://cancervariants.org/index.html>`_, and the `Atlas of  Variant Effects Alliance <https://www.varianteffect.org/>`_. The specification includes machine-readable JSON Schema specifications that support sharing and validation within and across these projects, along with a python reference implementation. In defining its models, VA-Spec builds on several more foundational standards, including the `SEPIO Model <https://github.com/sepio-framework/sepio-linkml>`_, and GA4GH `VRS <https://vrs.ga4gh.org/en/latest/index.html>`_  and `Cat-VRS <https://cat-vrs.readthedocs.io/en/latest/index.html>`_ schema. Future VA-Spec releases will include a modeling framework to support community-based authoring of profiles for new knowledge types and use cases.


Components
##########

The v1 release of VA-Spec includes the following components:

#. :ref:`A Foundational VA Core Model <va-core-model>`: A domain-agnostic model for describing knowledge of any kind, and the evidence and provenance supporting it. *The Core Model establishes a shared understanding of fundamental terms, concepts, and modeling patterns - and provides a foundation on which 'Standard VA Profiles' are built*.

#. :ref:`VA Profiles <va-profiles>`: A set of models built as specializations of core Statement, Study Result, and Evidence Line classes, each supporting a specific types of knowledge about genetic variation (e.g. this :ref:`Pathogenicity Statement Profile <variant-pathogenicity-statement>`). *These profiles are provided as machine-readable json schema, as recommended standards for validation and exchange of data by the GA4GH community*.

#. :ref:`A Python Reference Implementation <reference-implementation>`:  Code libraries that demonstrate the creation, validation, and exchange of compliant data using VA Profiles. *These resources provide a working example of code that can be adopted and/or extended by adopters*.


Readers may wish to review this :ref:`annotated data example <variant-pathogenicity-statement-example>`, to explore an end product of the VA-Spec, before diving in to the full documentation.

Scope and Development
#####################

VA-Spec takes an implementation-driven approach to development of the models it provides - releasing only models and elements that have been tested in real-world data systems. The initial release of the :ref:`VA Core Model<va-core-model>` contains a minimal subset of elements required to support early small-scale implementations led by ClinGen, VICC, and the Atlas of Variant Effects (AVE) Alliance.

:ref:`VA Profiles<va-profiles>` extend core :ref:`Statement<Statement>`, :ref:`Study Result<StudyResult>`, and :ref:`Evidence Line<EvidenceLine>` classes to support the specific types of knowledge captured (e.g. a variant pathogenicity), and community guidelines followed (e.g. the ACMG-2015 Guidelines) in implementing data systems. These three core classes are defined specifically to represent the levels at which curation tools and knowledgebases capture and report variant knowledge. Initial ClinGen, VICC, and AVE implementations required profiles to support the following types of variant-related knowledge:

**Statements**
   - Variant Pathogenicity
   - Variant Oncogenicity
   - Variant Diagnostic Associations
   - Variant Prognostic Associations
   - Variant Therapeutic Response Associations
   - Experimental Variant Functional Impacts

**Study Results**
   - Cohort Allele Frequency Data
   - Experimental Variant Functional Impact Data

**Evidence Line Profiles**
   - Variant Functional Impact Evidence for Pathogenicity
   - Variant Functional Impact Evidence for Oncogenicity

Notably, various 'flavors' of profiles for a given knowledge type can be defined to align with different community guidelines and terminology standards. For example, v1 of the VA-Spec provides several of these :ref:`"Community Profiles"<community-profiles>`, which are aligned with :ref:`ACMG<acmg-2015-profiles>`, :ref:`CCV<ccv-2022-profiles>`, and :ref:`AAC<aac-2017-profiles>` guidelines in the domains of variant pathogenicity, oncogenicity, and clinical interpretation of somatic variants, respectively.

The initial, minimal profiles in VA-Spec v1.0  will expand along three axes as the specification evolves:

 - **Existing Profile Coverage**: the scope and size of existing profiles will grow as current implementations work to include more diverse and complex data from their sources, and new adopters bring additional data requirements and use cases. New elements to support this expansion will be pulled into VA-Spec as needed from the :ref:`SEPIO Core Information Model<what-is-sepio>`, on which VA-Spec models are based.
 - **New Base Profile Types**: the number of different profile types defined in the VA-Spec will expand, as driver projects with use cases for new knowledge types emerge (e.g. new profiles to Molecular Consequence, Evolutionary Conservation, or Phenotype Association knowledge)
 - **New Community Profiles**: new flavors of existing profiles that support the conventions and terminologies of different community guidelines will be created - e.g. separate Variant Pathogenicity profiles that support AMCG-2015 and the emerging update to these guidelines.

Importantly, the level of maturity of core and profile models, and the specific elements within each, are tracked according to the :ref:`GKS Maturity Model<gks-maturity-model>` - so adopters have a clear understanding of the stability and use of elements they employ in their systems.

Community implementers are the engine that will drive this expansion - as VA models are only released after testing in real-world data systems. We strongly encourage community engagement through a variety of channels and mechanism, as described :ref:`here<how-to-contribute>`.  And the :ref:`Getting Started Guide<getting-started>` will walk newcomers through initial steps they can take to understand how the VA-Spec can support their data representation needs.

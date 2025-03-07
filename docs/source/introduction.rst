.. _introduction:

Introduction
!!!!!!!!!!!!


Overview
########

The GA4GH Variant Annotation Specification (VA-Spec) defines a set of standard schema to represent different types of knowledge about genetic variants. Each schema is built as a "profile" that extends a common, domain-agnostic :ref:`VA Core Model <va-core-model>`. The initial v1 release of the VA-Spec is focused on supporting specific types of variant knowledge provided by implementing Driver Projects and organizational members, including `ClinGen <https://clinicalgenome.org/>`_, `VICC <https://cancervariants.org/index.html>`_, and the `Atlas of  Variant Effects Alliance <https://www.varianteffect.org/>`_. The specification includes machine-readable JSON Schema specifications that support sharing and validation between these projects, along with a python reference implementation. It build on several more foundational standards, including the `SEPIO Model <https://github.com/sepio-framework/sepio-linkml>`_, and GA4GH `VRS <https://vrs.ga4gh.org/en/latest/index.html>`_  and `Cat-VRS <https://cat-vrs.readthedocs.io/en/latest/index.html>`_ schema. Future VA-Spec releases will include a modeling framework to support community-based authoring of profiles for new knowledge types and use cases. 


Components
##########

The v1 release of VA-Spec includes the following components:

#. :ref:`A Foundational VA Core Model <va-core-model>`: A domain-agnostic model for describing knowledge of any kind, and the evidence and provenance supporting it. The Core-IM establishes a shared understanding of fundamental terms, concepts, and modeling patterns - and provides a foundation on which 'Standard VA Profiles' are built*.  

#. :ref:`VA Standard Profiles <va-standard-profiles>`: A set of models built as Profiles of core Statement or Study Result classes, each supporting a specific types of knowledge about genetic variation (e.g. this :ref:`Pathogenicity Statement Profile <variant-pathogenicity-statement>`). *These models are provided as machine-readable json schema, as shared standards for validation and exchange of data by the GA4GH community*.

#. :ref:`Community Profile Sets <community-profile-sets>`:  Collections of standard profiles that all align with an established community guidleine for variant knowledge creation. *These can be used together by implementers who wish to follow this standard in defining the strucutre and semantics of their data*. 

#. :ref:`A Python Reference Implementation <reference-implementation>`:  Code libraries that demonstrate the creation, validation, and exchange of compliant data using GA4GH Profiles. *These resources provide a working example of code that can be adopted and/or extended by adopters*.


Readers may wish to review this :ref:`annotated data example <variant-pathogenicity-statement-example>`, to explore an end product of the VA-Spec, before diving in to the full documentation. 

Development & Implementation
############################


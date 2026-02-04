.. _design-decisions:

Design Decisions
!!!!!!!!!!!!!!!!

Definition of 'Variant Annotation'
##################################
To appreciate modeling and development choices made for the VA-Spec, it helps to understand how we define and distinguish the elements that comprise a Variant Annotation.

**Definition**:  “A **structured data object** that holds a **central statement of knowledge** about a **genetic variation**, along with **evidence and provenance metadata** supporting it.

  - **‘structured data object’**: an organized, computable representation of knowledge, in any format or syntax.
  - **‘central statement of knowledge’**: the single primary statement about a genetic variation is at the core of an annotation.
  - **‘genetic variation’**: defined broadly to cover sequence changes, epigenetic modifications, or alterations in gene expression or location.
  - **‘evidence and provenance metadata’**: describes how the central knowledge statement was generated, including when, by whom, and using what methods and evidence information.

The VA-Spec model was  defined to *explicitly represent* and *clearly distinguish* these key types of information within a Variant Annotation - so that users can appreciate the significance and utility of the knowledge they provide.

Scope of Variant Knowledge Supported
####################################

The VA-Spec supports statements of knowledge about the **biological** and **clinical** significance of these different types of variants, but leaves those
reporting **case-level observations** about a variant to other standards (e.g. Phenopackets, HL7-Clinical Genomics IM, FHIR)

 - **Biological Knowledge Statements**  ``IN-SCOPE``: e.g. Molecular Consequence, Functional Impact, Population Frequency, Relative Location, Evolutionary Conservation
 - **Clinical Knowledge Statements**  ``IN-SCOPE``: e.g. Pathogenicity Classification, Therapeutic Response Classification, Diagnostic Classification, Prognostic Classification, Phenotypic Feature Association
 - **Case-Level Knowledge Statement**  ``OUT-OF-SCOPE``:  e.g. observation of a variant in a patient, disease causality of an observed variant in a patient, origin of an observed variant in a patient, clonality of a variant in a patient - these kinds of information are not covered by the VA-Spec.

Explicit Statement Semantics
############################

In the VA data, each assertion of knowledge about a variant is captured in a self-contained ``Statement`` object. Statements put forth a Proposition that expresses some possible fact about the world, and may provide an assessment of this proposition's validity (i.e. how likely it is to be true or false based on evaluated evidence). The semantics of this possible fact are captured in a ``Proposition`` object, using ``subject``, ``predicate``, ``object``, and optional ``qualifier`` attributes (**SPOQ**). An assessment of the Proposition's  validity can optionally be captured using ``direction``, ``strength``, and/or ``score`` attributes (**DS**).  See :ref:`here <Statement>` for more.

Organization of variant knowledge into discrete Statement objects allows clear and precise tracking of the evidence and provenance that supports each. And as modular, self-contained structures, they can be re-used in different contexts in an annotation - as the primary statement being made, or a piece of evidence supporting such a statement. Finally, the consistent structured representation of semantics across all Statement types provides a framework for human and computational agents to identify what is being asserted as true, and what is accessory or supporting information.

.. _use-of-propositions:

Use of Propositions
###################

As noted above, **Proposition** objects are used to encapsulate the "SPOQ" semantics of possible facts that are asserted or evaluated in Statements, and against which evidence is evaluated in Evidence Lines.  The ``type`` of a given Statement or Evidence Line object is not directly declared in the data, but instead inferred from the ``type`` of the Proposition is holds. This avoids the need to create parallel hierarchies of Statement and Proposition types.

This design pattern also provides re-usable Proposition objects that can be referenced and re-used in these contexts (see :ref:`example here <proposition-utility-example>`). This can avoid the need to duplicate SPOQ semantics in the data across Statements and Evidence Lines with the same proposition.  Proposition objects may also provide a focal point for aggregating evidence across different Statements and Evidence Lines that all assess the same proposition - to provide a comprehensive view of the support for or against this possible fact, or help identify undiscovered evidence that may be used to reach a conclusive interpretation of a variant of uncertain significance.

A trade-off of this design decision is the deeper nesting structure that results in the data itself, and more complicated deserialization logic needed to determine what type of Statement is being parsed.


Domain Entity Representation
############################

Domain Entities are the real world concepts in the domain of discourse that variant annotation data is about - e.g. **Genetic Variation**, and the **Conditions**, **Therapies**, or **Genes** to which they are related. They are considered to represent general types or concepts (e.g. the disease 'Lung Cancer’), as opposed to particular instances of these concepts (‘patient X’s manifestation of lung cancer’).

The VA-Spec does not define detailed models for representing such domain entities - as this is the remit of other standards development organizations.

Where suitable standards exist they are incorporated into the VA-Spec - as we have done with the `VRS <https://vrs.ga4gh.org/en/latest/index.html>`_ and `CatVRS <https://cat-vrs.readthedocs.io/en/latest/index.html>`_ models for representing genetic variation.

Version 1 of the VA-Spec represents all other Domain Entity types using a simple :ref:`IRI Reference <iriReference>`, or a :ref:`Mappable Concept <mappable-concept>` which bundles an established code for the entity with metadata and mappings for the code and code system. Where there is a need to represent collections of more than one Domain Entity, classes are defined to capture these as sets of Mappable Concepts (e.g. ``ConditionSet``, ``Therapy Group``). More information and examples of Domain Entity representation can be found :ref:`here <domain-entities>`.

.. _profile-authoring-mechanisms:

Profile Authoring Mechanisms
############################

In version 1.0 of the VA-Spec, we distinguish between two categories of profiles, whose specifications which employ distinct authoring mechanisms:

 **VA Base Profiles**:

  - Specialize generic VA core classes for a particular type of knowledge, through formal definition of concrete subclasses.
  - This approach relies on bespoke `Metaschema Processor (MSP) tooling <https://github.com/ga4gh/gks-metaschema>`_ with functions to craft subclass definitions, and associated tooling to derive formal json schema from them.
  - This Base Profiling approach is used to create :ref:`Proposition Profiles<proposition-profiles>` and :ref:`Study Result Profiles<study-result-profiles>`, which can be used/referenced within Statement and Evidence Line profiles.

 **Community Profiles**:

  - Layer additional constraints on top of VA core classes to enforce alignment with terminology conventions of a specific community guideline (e.g. ACMG 2015).
  - These constraints are defined using a native json schema composition approach, which does not result in creation of concrete subclasses for each profile.
  - This approach is used to define :ref:`Statement<Statement>` and :ref:`Evidence Line<EvidenceLine>` profiles - which incorporate Propositions to specify the possible fact they assert to be true or evaluate evidence against, respectively.

This design decision was made to minimize the number of classes in the model while providing flexibility to specialize core models for diverse domains and community guidelines.  It also leverages the JSON Schema language which is widely used and familiar to most developers.

For more information and technical guidance around how these types of profiles are authored and used, see the :ref:`Developer Guide <developer-guide>` section.

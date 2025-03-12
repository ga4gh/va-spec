.. _design-decisions:

Design Decisions
!!!!!!!!!!!!!!!!

Definition of 'Variant Annotation'
###########################
To appreciate modeling and development choices made for the VA-Spec, it helps to understand how we define and distinguish the elements that comprise a Variant Annotation.
	
**Definition**:  “A **structured data object** that holds a **central statement of knowledge** about a **genetic variation**, along with **evidence and provenance metadata** supporting it.

  - **‘structured data object’**: an organized, computable representation of knowledge, in any format or syntax.
  - **‘central statement of knowledge’**: the single primary statement about a genetic variation is at the core of an annotation.
  - **‘genetic variation’**: defined broadly to cover sequence changes, epigenetic modifications, or alterations in gene expression or location. 
  - **‘evidence and provenance metadata’**: describes how the central knowledge statement was generated, including when, by whom, and using what methods and evidence information.

The VA-Spec model was  defined to *explicitly represent* and *clearly distinguish* these key types of information within a Variant Annotation - so that users can appreciate the significance and utility of the knowledge they provide.

Scope of Variant Knowledge Supported 
################################

The VA-Spec supports statements of knowledge about the **biological** and **clinical** significance of these different types of variants, but leaves those
reporting **case-level observations** about a variant to other standards (e.g. Phenopackets, HL7-Clinical Genomics IM, FHIR)

 - **Biological Knowledge Statements**  ``IN-SCOPE``: e.g. Molecular Consequence, Functional Impact, Population Frequency, Relative Location, Evolutionary Conservation
 - **Clinical Knowledge Statements**  ``IN-SCOPE``: e.g. Pathogenicity Classification, Therapeutic Response Classification, Diagnostic Classification, Prognostic Classification, Phenotypic Feature Association
 - **Case-Level Knowledge Statement**  ``OUT-OF-SCOPE``:  e.g. observation of a variant in a patient, disease causality of an observed variant in a patient, origin of an observed variant in a patient, clonality of a variant in a patient - these kinds of information are not covered by the VA-Spec.

Explicit Statement Semantics
############################

In the VA data, each assertion of knowledge about a variant is captured in a self-contained ``Statement`` object. Statements put forth a Proposition that expresses some possible fact about the world, and may provide an assessment of this proposition's validity (i.e. how likely it is to be true or false based on evaluated evidence). The semantics of this possible fact are captured in a ``Proposition`` object, using ``subject``, ``predicate``, ``object``, and optional ``qualifier`` attributes (**SPOQ**). An assessment of the Proposition's  validity can optionally be captured using ``direction``, ``strength``, and/or ``score`` attributes (**DS**).  See `here <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/entities/information-entities/statement.html>`_ for more.

Organization of variant knowledge into discrete Statement objects allows clear and precise tracking of the evidence and provenance that supports each. And as modular, self-contained structures, they can be re-used in different contexts in an annotation - as the primary statement being made, or a piece of evidence supporting such a statement. Finally, the consistent structured representation of semantics across all Statement types provides a framework for human and computational agents to identify what is being asserted as true, and what is accessory or supporting information.

Use of Propositions
###################

As noted above, **Proposition** objects are used to encapsulate the "SPOQ" semantics of possible facts that are asserted or evaluated in Statements, and against which evidence is evaluated in Evidence Lines.  The ``type`` of a given Statement or Evidence Line object is not directly declared in the data, but instead inferred from the ``type`` of the Proposition is holds. 

This design pattern provides re-usable Proposition objects that can be referenced and re-used in these contexts, so the model does not need to duplicate the definition of SPOQ semantics for different types of variant knowledge, or create parallel hierarchies of Statement and Proposition types. Proposition objects also provides an anchor around which all evidence around a given possible fact can be aggregated, across many possible Statements and Evidence Lines that use a given proposition - for a more comprehensive view of the support for or against this possible fact. 

A trade-off of this design decision is the deeper nesting structure that results in the data itself, and more complicated deserialization logic needed to determine what type of Statement is being parsed. 


Domain Entity Representation
############################

Domain Entities are the real world concepts in the domain of discourse that variant annotation data is about - e.g. **Genetic Variation**, and the **Conditions**, **Therapies**, or **Genes** to which they are related. They are considered to represent general types or concepts (e.g. the disease 'Lung Cancer’), as opposed to particular instances of these concepts (‘patient X’s manifestation of lung cancer’).

The VA-Spec does not define detailed models for representing such domain entities - as this is the remit of other standards development organizations. 

Where suitable standards exist they are incorporated into the VA-Spec - as we have done with the `VRS <https://vrs.ga4gh.org/en/latest/index.html>`_ and `CatVRS <https://cat-vrs.readthedocs.io/en/latest/index.html>`_ models for representing genetic variation. 

Version 1 of the VA-Spec represents all other Domain Entity types using a simple :ref:`IRI Reference <iriReference>`, or a :ref:`Mappable Concept <mappable-concept>` which bundles an established code for the entity with metadata and mappings for the code and code system. Where there is a need to represent collections of more than one Domain Entity, classes are defined to capture these as sets of Mappable Concepts (e.g. ``ConditionSet``, ``Therapy Group``). More information and examples of Domain Entity representation can be found `here <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/domain-entities.html>`_.


Profiling Approach
##################



Profile Authoring Mechanisms
############################

At present, VA-Spec uses two distinct mechanisms for authoring specializations of Core Model Classes for representing specific types of Varaint knowledge (i.e. 'VA Profiles').
 #. A `Metaschema Processor (MSP)-based approach <https://github.com/ga4gh/gks-metaschema>`_ that special MSP functions like `inherits` and `extends` - and requires MSP tooling derive concrete subclasses of parent core classes. This mechanism is used for authoring 'Base Profiles' for Propositions and Study Results, which can be used/referenced within Statement and Evidence Line profiles.
 #. A `JSON Schema composition-based approach <https://json-schema.org/understanding-json-schema/reference/combining>`_ that uses the ``allOf`` keyword to extend core class definitions with additional constraints. This mechanism is used for authoring 'Community Profiles' for Statements and Evidence Lines, which constrain the values of certain attributes to align with terminologies and conventions from established community standards such as the ACMG-2015 Interpretation Guidelines. For more, see `here <https://va-ga4gh.readthedocs.io/en/latest/community-profile-sets/index.html>`_. 

This design decision was largely guided by the technical environment under which we had to implement the initial profiling process, and limitations this imposed. Metashcema Processor tooling, while not specifically suited to support profiling operations, were available and used in other GKS standards. And JSON Schema is a widely used language familiar to most developers, that has built in support for profiling tasks.

We recognize that this patchwork approach is not ideal, and plan to evolve toward a more consistent profile authoring mechanism with integrated tooling support for community development (see :ref:`Future Plans <link-ml-profile-authoring-support>`).

Intorduction
!!!!!!!!!!!!

The Variant Annotation Specification (VA-Spec) provides standard models for unambiguous representation of knowledge about molecular variation, along with supporting evidence and provenance information.

 * It defines a `set of information models <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html>`_ to represent different kinds of statements made about variants - built as distinct **"profiles"** that extend a common `core information model <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/index.html>`_. 
 * It provides machine-readable `json-schema specifications <https://github.com/ga4gh/va-spec/tree/1.x/schema/profiles/json>`_ of these models, to enable sharing and validation of data through APIs and other exchange mechanisms. 
 * It offers a `modeling framework <https://github.com/ga4gh/va-spec/blob/1.x/docs/source/implementation-guidance.rst#profiling-methodology>`_ through which implementers can build profiles for **new statement types**, or **extend existing profiles** with additional features. 
 * It is based on the `SEPIO Modeling Framework <https://sepio-framework.github.io/sepio-linkml/about/>`_ - applying SEPIO's established models, conventions, and profiling methodology to produce these resources.

This document provides an **high-level introduction to VA-Spec principles, models, and processes**, and links out to separate pages for additional details. 

For a hands on experience with VA-Spec data, see the simple Variant Pathogenicity Statement example here (TO DO).

Definitions and Scope
######################

Below we define foundational concepts and outline the scope of what the VA-Spec was created to support - as a basis for understanding the models it provides, the data to which it can be applied. 

Variant
*******
Variants are the subjects of `Annotations <https://va-ga4gh.readthedocs.io/en/stable/overview.html#annotation>`_ that the VA-Spec was built to support. 

**Definition**: alternative forms of a genetic sequence, or of its molecular manifestation in a biological system. (Also referred to as a 'molecular variations'). 

  Covers *sequence variations* in a genome, transcript, or protein.
 * **simple** (SNV, indels) or **complex** (inversions, repeat regions) sequence changes
 * **continuous** (allele) or **discontinuous** (translocations) regions
 * **in cis** (haplotypes) or **in trans** (genotypes) sets of variant regions

  Covers *post-sequence* variations in the state of a program that unfolds 'downstream' of sequence 
 * changes in **expression level** or **location** of a gene product (e.g. decreased cytosolic expression)
 * changes in **post-translational modification** of proteins (e.g. increased PEST domain phosphorylation)
 * changes in **epigenetic alterations** of a gene or region (e.g. increased enhancer methylation)

  Covers different levels of **'represenational specificity'** at which these variations can be described
 * **Discrete Variation**:  specific instances of a sequence variation in a specified context (reference, location, state - even if incompletely known). e.g. the NC_000019.9:g.45411941T>C genomic allele (`link <https://gnomad.broadinstitute.org/variant/19-45411941-T-C>`_)
 * **Expansion Sets**: sets of Discrete Variation instances that are related via lift-over, or projection functions (or combinations thereof). e.g. the set of discrete varaints in ClinGen 'canonical allele' CA127512 (`link <http://reg.clinicalgenome.org/redmine/projects/registry/genboree_registry/by_caid?caid=CA127512>`_)
 * **Categorical Variation**: rule-based classes of variation defined by specific membership criteria.  e.g. ‘deletions spanning EGFR exon 4’ (`link <https://civicdb.org/variants/252/summary>`_), ‘TSC1 loss-of-function muts.’ (`link <https://civicdb.org/variants/125/summary>`_)

The VA-Spec uses the `GA4GH Variant Representation Specification (VRS) <https://vrs.ga4gh.org/en/stable/index.html>`_ as a standard for identifying and representing these different forms of molecular variation.

Annotation
**********

**Definition**:  “A **structured data object** that holds a **central statement of knowledge** about a **molecular variation**, along with **evidence and provenance metadata** supporting it.

 * **‘structured data object’**: an organized, computable representation of knowledge, in any format or syntax.
 * **‘central statement of knowledge’**: the single primary statement about a molecular variation is at the core of an annotation.
 * **‘molecular variation’**: defined broadly to cover sequence changes, epigenetic modifications, or alterations in gene expression or location (see `Variant`_). 
 * **‘evidence and provenance metadata’**: describes how the central knowledge statement was generated, including when, by whom, and using what methods and evidence information.

The VA-Spec model was  defined to *explcitly represent* and *clearly distinguish* these key types of information within a Variant Annotation - so that users can appreciate the significance and utility of the knowledge they provide.


Variant Annotation Types
************************
The VA-Spec supports annotation statements about the **biological** and **clinical** significance of a variant, but leaves thoae reporting **case-level observations** about a variant to other standards (e.g. Phenopackets, HL7-Clinical Genomics IM, FHIR)

 * **Biological Variant Statements** (*in-scope*): Molecular Consequence, Functional Impact, Population Frequency, Relative Location, Evolutionary Conservation
 * **Clinical Knolwedge Statements** (*in-scope*): Pathogenicity Classification, Therapeutic Response Classification, Diagnostic Classification, Prognostic Classification, Phenotypic Feature Association
 * **Case-Level Knowledge Statement** (*out-of-scope*):  observation of a variant in a patient, disease causality of an observed variant in a patient, origin of an observed variant in a patient, clonality of a variant in a patient.


Modeling Foundations
####################

The VA-Spec was built on top of the `SEPIO Modeling Framework <https://sepio-framework.github.io/sepio-linkml/about/>`_ - adopting its established models, conventions, and profiling methodology to produce standard models for the GA4GH community. The SEPIO framework provides a domain-agnostic **Core Information Model (Core-IM)** and **Profiling Methodology** that can be used to define schema for specific kinds of Statements, and the specific kinds of evidence and provenance information that support them. For example, the VA-Spec has applied the framework to define 'Variant Pathogenicity Statement' and 'Variant Therapeutic Response Statement' profiles, among others found `here <https://va-ga4gh.readthedocs.io/en/stable/standard-profiles/index.html>`_. 

The SEPIO Core Information Model
********************************
The foundational SEPIO Core-IM is a doamin-agnostic model for describing the scientific knowledge assertions of any kind. As shown in Figure XXX, each knowledge assertion is captured in a self-contained ``Statement`` object, where the semantics of what is asserted to be true is explicitly structured in terms of a subject, predicate, object, and qualifier(s). Organization of variant knowledge into discrete Statement objects allows clear and precise tracking of the evidence and provenance that supports each.

.. _sepio-class-diagram-w-statement:

.. figure:: images/sepio-class-diagram-w-statement.PNG

   Statement-Centric SEPIO Data Strucutres 

   **Legend** (A) Explicit Statement Semantics (B) SEPIO Data Strucutre:  The central axis of SEPIO data structures is rooted at a **Statement** object (aka 'Assertion') - 
   which may be linked to one or more **Evidence Lines** representing disctrete arguments for or against it. 
   Each Evidence Line may then be linked to one or more pieces of information used as evidence (i.e. **Evidence Items**) 
   contributing to such an argument. Surrounding the central axis are classes that describe the provenance of these
   core artifacts, including **Contributions** made to them by **Agents**, **Activities** performed in doing so, **Methods**
   that specify their creation, and **Documents** that describe them. This core structure allows precise tracking of provenance
   at the level of a Statement and each supporting Evidence Lines and Items.


test 
test 


.. note::  While the majority of applications are focused on representing knowledge **Statements**, SEPIO data structures can be built
           around other classes as their central focus. For exapmle, implementations have defined profiles focused on describing and
           tracking the provenance of **Evidence Line** or **Study Reuslt** objects, where the same modeling patterns and principles are applied (see here).

The SEPIO Profiling Methodology
*******************************
In practice, application of SEPIO to represent actual data requires a 'Profiling' process, in which the gneeric Core-IM is specialized represent specific Statement types. For example, Figure XXX shows how the Core-IM could be specialized into profiles for Variant Pathogenicity, Molecular Consequence, and Therapeutic Response Statements. Note that these profiles exhibit very different levels of complexity, to support the specific evidence and provenance requirements for each type of Statement.   

FIGURE:

Legend: 


Profiling tasks may include:
 * Selecting a subset of classes and attributes needed to represent the Statement/use case of interest (e.g. a data creator may decide not to bring the ``Statement.hasEvidenceLines`` or the ``Evidence Line`` class into their profile).
 * Defining domain-specific subtypes of general purpose Core IM classes (e.g. ``Statement`` -> ``VariantPathogenicityStatement``).
 * Specializing certain attributes to capture domain-specific information (e.g. ``Statement.qualifier`` -> ``VariantPathogenicityStatement.alleleoriginQualifier``).
 * Defining or importing classes representing domain entities that a specific type of Statement is about (e.g. classes to represent a ``Variation``, ``Gene``, ``Disease``).
 * Constraining values of generic Core IM attributes to take specific domain entities or data types as values (e.g. restricting the ``VariantPathogenicityStatement.subject`` field to only take ‘Variation’ instances).
 * Defining domain-specific value sets that get bound to attributes taking coded values (e.g. binding ``VariantPathogenicityStatement.alleleoriginQualifier`` to take only `allele_origin terms <https://www.ebi.ac.uk/ols4/ontologies/geno/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGENO_0000877>`_ from the GENO Ontology)


Profiling tasks may include:
 * selecting a subset of classes and attributes needed to represent the Statement/use case of interest
     * e.g. a data creator may decide not to bring the ``Statement.hasEvidenceLines`` or the ``Evidence Line` class into their profile
 * defining domain-specific subtypes of general purpose Core IM classes
     * e.g. ``Statement`` -> ``VariantPathogenicityStatement``
 * specializing certain attributes to capture domain-specific information
     * e.g. ``Statement.qualifier`` -> ``VariantPathogenicityStatement.alleleoriginQualifier``
 * defining or importing classes representing domain entities that a specific type of Statement is about 
     * e.g. classes to represent a ``Variation``, ``Gene``, ``Disease``
 * constraining values of generic Core IM attributes to take specific domain entities or data types as values
     * e.g. restricting the ``VariantPathogenicityStatement.subject`` field to only take ‘Variation’ instances
 * defining domain-specific value sets that get bound to attributes taking coded values
     * e.g. binding ``VariantPathogenicityStatement.alleleoriginQualifier`` to take only `allele_origin <https://www.ebi.ac.uk/ols4/ontologies/geno/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGENO_0000877>`_ terms from the GENO Ontology

The Profiles that result from this process represent custom, domain-specific information models that can be implemented as formal schema for a particular use case or application.  




.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Profiling Task
      - Example
   *  - Select a subset of classes and attributes needed to represent the Statement/use case of interest 
      - Implementers may choose not to use the``Evidence Line` class and related attributes in their profile.
   *  - Define domain-specific subtypes of general purpose Core IM classes 
      - Specialize ``Statement`` -> ``VariantPathogenicityStatement``
   *  - Specialize attributes to capture domain-specific information
      - Specialize ``Statement.qualifier`` -> ``VariantPathogenicityStatement.alleleoriginQualifier``
   *  - Define or import classes for domain entities that profiles Statements are about
      - For a Variant Pathogencity Statement profile, classes to represent the subject ``Variation`` and object ``Disease`` 
   *  - Constrain values of Core IM attributes to take specific domain entities or data types as values
      - Restricting the ``VariantPathogenicityStatement.subject`` field to only take ‘Variation’ instances
   *  - Define value sets that get bound to attributes taking coded values
      - Binding ``VariantPathogenicityStatement.alleleoriginQualifier`` to take only `allele_origin terms from the GENO Ontology <https://www.ebi.ac.uk/ols4/ontologies/geno/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGENO_0000877>`_). 












Figure XXX illulstrates coneptually how such 'Profiles' can be  dervied for representing variant knowledge, including a Variant Pathogenicity Statements, Molecular Consequence Statements, and Therapeutic REsponse Statements




specializaton of its generic elements for a particular domain or application, through a process called 'Profiling'



Implementation of the SEPIO model requires specialization of its general purpose elements with domain-specific features adn constraints, to generate ‘VA Profiles’. Profiles are domain- or application- specific data models that constrain the core information model, and can extend it to support custom schema for a particular use case.  The VA-Spec provides a Profiling Methodology to guide adopters in this process (which is not unlike the FHIR Profiling paradigm widely used in the clinical data domain).  A developing draft of this methodology can be found here.  Work is ongoing to refine and formalize this with template and tooling support. 



is used to extend this generic core model with of domain-specific content, to derive custom schema for representing specific types of Statemetns and supporting evidence and provenance.
It defines 
Figure XXX illulstrates coneptually how such 'Profiles' can be  dervied for representing variant knowledge, including a Variant Pathogenicity Statements, Molecular Consequence Statements, and Therapeutic REsponse Statements
LEgend: 




For more information,  see . . . .



VA-Spec Implementation of the SEPIO Framework
*********************************************

Implementations extend this generic core model with of domain-specific content, to create custom schema called ‘SEPIO Profiles’


VA-Spec as a SEPIO Implementation


The VA Core IM was developed as a subset of of this full SEPIO model, where comprehensive requriemetns analysis acorss driver project and use cases helped identity a sthe classes and attributes used ot seed the inidial VA model.




The framework provides value in the following ways

\A standard won't get used if not expressive enough to capture detail/nuance required for some use cases, or if it imposes too complex a model for simpler use cases.
We need to balance the need for flexibility and extensibility, with goal of interoperability and accessibility.
To keep pace with community needs and leverage community resources, we should allow for distributed development of models for any type of Annotation (e.g. gene/sequence annotation).
One way to support this is to ground the specification in a common domain-agnostic foundational model that can be extended to address the specific needs of different VA types, data sources, and use cases.

Diversity of types, levels of complexity, and use cases for evidence and provenance across knowledge domains and application means there is no ‘one-size-fits-all’ solution
A framework that allows custom models built on a common semantic foundation can provide a base level of understanding and interoperability, without restricting expressivity.
While this approach may not always support out-of-the-box interoperability across all communities of use, it can significantly lower barriers to aggregating, harmonizing, and operating across disparate data.


The ultimate product of the VA-Spec is a set of `standard models <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html>`_ for representing diverse types of variant knowledge.




accommodates the diverse type of knwoledge and the diverse requrieemtns regarding tyep and level of detail for E/P








**Contents**
 * `Definitions and Scope`_
 * `Modeling Principles and Framework`_



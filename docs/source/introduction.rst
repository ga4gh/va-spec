Introduction
!!!!!!!!!!!!

``PREREQUISITES``: None

Reliable exchange of knowledge about molecular variation between clinicians, researchers, and testing laboratories is required to maximize the personal, public, research, and clinical value of genomic information. This knowledge is typically exchanged as `Variant Annotations <https://va-ga4gh.readthedocs.io/en/latest/faq.html#what-is-a-variant-annotation>`_ - structured data objects that holds a **central statement of knowledge** about a **molecular variation**, along with **evidence and provenance metadata** supporting its interpretation and use. 

The **GA4GH Variant Annotation Specification (VA-Spec)** was developed by a partnership among national information resource providers and major public initiatives — as an open specification to standardize the exchange of such variation knowledge. It was built as a `SEPIO-based modeling framework <https://va-ga4gh.readthedocs.io/en/latest/faq.html#what-is-the-sepio-framework>`_ that supports implementation-driven development of standard models for specific VA Statement types. It leverages the GA4GH `VRS <https://vrs.ga4gh.org/en/latest/index.html>`_ and `Cat-VRS <https://github.com/ga4gh/cat-vrs?tab=readme-ov-file>`_ specifications to represent `diverse kinds of molecular variation <https://va-ga4gh.readthedocs.io/en/latest/faq.html#what-types-of-variants-are-supported>`_ as annotation subjects. And it supports `diverse kinds of biological and clinical variant knowledge <https://va-ga4gh.readthedocs.io/en/latest/faq.html#what-kinds-of-variant-knowledge-are-supported>`_, leaving case-level variant information to other standards. 

VA Framework Components
#######################

The VA-Spec modeling framework is comprised of the following components:

#. `A Foundational 'GKS Core Information Model' <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/index.html>`_ (Core-IM): A domain-agnostic model for describing knowledge statements of any kind, and the evidence and provenance supporting them. This model, which is based on the SEPIO Core-IM, establishes a shared understanding of fundamental terms, concepts, and modeling patterns - and provides a foundation on which standard 'profiles' for specific types of statements about molecular variation are built.  

#. `Standard VA Profiles <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html>`_: A set of models built as 'Profiles' of the Statement or Study Result classes in the Core-IM, each supporting a specific types of knowledge about molecular variation (e.g. a `Variant Pathogenicity Statement <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/statement-profiles.html#variant-pathogenicity-statement>`_) profile. These models are provided in machine-readable json schema, as shared standards for validation and exchange of data by the GA4GH community. 

#. `A Profiling Methodology <https://va-ga4gh.readthedocs.io/en/latest/modeling-framework.html>`_:  A set of defined processes, conventions, and tooling support to guide VA and community developers in executing the profiling process. This approach allows adopters to  build profiles for new statement types, or extend existing profiles - supporting an implementation-driven approach to VA standards development.

#. `A Python Reference Implementation <https://va-ga4gh.readthedocs.io/en/latest/reference-implementation.html>`_:  Code libraries that demonstrate the creation, validation, and exchange of compliant data using GA4GH Profiles. These resources provide a working example of code that can be adopted and/or extended by adopters. ``COMING SOON``

This modeling framework has allowed for implementation-driven development that reduces bottlenecks imposed by centralized approaches, leverages the expertise of diverse adopters, and delivers schema that have proven out in working applications.

VA Standard Development and Dependencies
########################################
While development of `VA Standard Profiles <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html>`_ is grounded in foundational SEPIO and GKS core models, it is ultimately driven by bottom-up implementation requirements. Accordingly, development tasks unfold across a stack of interdependent models and specifications, as described below. 

.. _va-model-dependencies:

.. figure:: images/va-model-dependencies.png

   VA Ecosystem Models and Dependencies

   **Legend** A hierarchy of models and standards support generation of the Standard Profile Schema that are the final product of the VA-Specification. Arrows on the left describe ``PROCESSES`` through which downstream models are generated from more foundational ones. Arrows on the right    describe the propagation of requirements from implementation models to inform upstream Core-IM expansion and refinement. The format of each model (e.g. 'YAML', 'JSON') is indicated by icons on each.

Below we describe each model in this ecosystem and how it is generated, using ClinGen's definition of a simple Variant Pathogenicity Statement Profile to support ClinVar SCV data as an example. 
|

**1. The SEPIO Core-IM** provides foundational representation of domain-agnostic concepts describing the knowledge generation process, and artifacts it produces, and relationships between them. It is part of a larger modeling Framework that includes a Profiling Methodology for deriving models specialized for particular types of Statements reporting variant *knowledge*, or Study Results reporting created *related collections of variant data*. It is written in a yaml format and not formalized as a json schema, as it is not intended to be directly implemented in data. More information can be found `here <https://va-ga4gh.readthedocs.io/en/latest/faq.html#what-is-the-sepio-framework>`_. 
|

**2. The GKS Core-IM** is the basis for the profiling process that generates Statement or Study Result profiles for specific types of variant annotations. The VA Team ``EXTRACT`` a hand-selected subset of the SEPIO Core-IM, chosen specifically to support profiles drafted by early Driver Project implementations of the VA-Spec, for inclusion in the GKS core model.

.. _core-im-from-sepio:

.. figure:: images/core-im-from-sepio.png

   Extraction of the Core-IM from the SEPIO Model

   **Legend** Classes and attributes needed for ClinGen's Variant Pathogneicity Profile are identified and extracted into the GKS Core-IM subset (which will include additional elements needed to support other implementation profiles being created by other Driver Projects such as VICC and MAVEdb)

**3. GKS Domain Entity Models** represent the biological and clinical entities that Variant Annotations are about, and serve as subjects, objects, and qualifiers of VA Statements (Genes, Conditions, Therapeutic Procedures). These classes ``EXTEND`` the GKS Core-IM to support VA Profile definitions. 

.. _domain-entities-from-core-im:

.. figure:: images/domain-entities-from-core-im.png

   Extension of Core-IM with Domain Entity Classes

   **Legend** The **Variant Pathogenicity Profile** requires representations of **Variations** that serve as the subjects of these statements, **Conditions** that serve as the objects, and **Genes** which may provide qualifying context.  Variations adopt the `GA4GH VRS specification <https://vrs.ga4gh.org/en/latest/index.html>`_. Minimal draft models for a Gene class and a small hierarchy of Condition classes are defined and submitted to the GKS-Commons specification, where they are available for broader re-use in other Profiles. 

**4. VA Standard Profile IMs** define the structure and semantics of the Standard Models that will be used by the GA4GH community. Separate yaml-based are defined for different kinds of VA Statements and Study Results. Profile definition is implementation-driven, beginning Draft Implementation Profiles which **select** and ``SPECIALIZE`` elements from the GKS Core-IM with profile-specific constraints, based on the needs of a particular application. 

.. _standard-profile-from-core-im:

.. figure:: images/standard-profile-from-core-im.png

   Profiling of the Core-IM into a Draft Variant Pathogenicity Statement Profile

   **Legend** A draft of a Variant Pathogenicity Statement Profile is created through the profiling process whereby elements needed to support the ClinVar data and ClinGen's implementation requirements. GKS Core_IM elements usedin the profile are hihglighted in ``RED``. Examples of specializations are shown in BLUE in the zoomed Variant Pathogenicity Statement class, including definition of this Statement subclass itself, binding of *subject* and *object* attributes to specific Domain Entity classes, definition of a specific *qualifier* class to capture gene context, and definition and binding of the *predicate* attribute to a specific enumeration of permissible values. 

**5. VA Standard Profile JSON Schema** are the final, machine readable products of the VA modeling framework, intended for implementation in working data systems.  They ``FORMALIZE`` the yaml-based Standard Profile IMs, through the automated transformation to JSON schema by GKS Metaschema Processor tools. 

.. _schema-from-yaml-profile:

.. figure:: images/schema-from-yaml-profile.png

   Formalization of YAML Source profiles into JSON Schema specifications 

   **Legend** A JSON Schema specification of the Standard Variant Pathogenicity Statement Profile are automatically derived from source YAML by GKS Metaschema Processor Tools

**Implementation Schema** are concrete schema that are actually implemented in data systems. When Driver Projects ``IMPLEMENT`` a Standard JSON schema, they may use it as is, translate it into different schema languages (eg. graphql, ShEX), and/or refine it with application-specific additions to support local implementation needs. Such local changes break from the VA Standard, which requires data to be transformed back to compliant form for sharing over GA4GH APIs.

.. _implementation-from-standard-profile:

.. figure:: images/implementation-from-standard-profile.png

   Implementation of Standard JSON Schema with System-Specific Changes

   **Legend** ClinGen systems may translate the standard **JSON schema** into a **GraphQL** specification, and may make a handful of application-specific changes (red) to meet local system needs (e.g. flattening classes and adding a few new custom properties).

While the SEPIO and GKS Core models are the basis for deriving downstream Standard Profiles, the evolution of these foundational core models is driven by bottom-up requirements arising from implementation models for working data applications. These requirements flow upstream to inform extension or refinement of the GKS Core-IM, and ultimately the SEPIO Core-IM - ensuring tight alignment across these models, and adherence to core modeling principles they espouse. 


Establishing and Evolving VA Standards
######################################
As noted, VA Standard development is implementation-driven, beginning with the definition of a Draft Implementation Profile to meet the needs of a particular driver project application. Emergence of a consensus Standard Profile requires negotiation across developers of SEPIO, VA, and Implementation models, through the following processes:

**Align and Refine Models**

While aspiring to use the SEPIO and GKS Core IMs, Draft Implementation Models may include features that are not consistent with these foundational models. Once an initial implementation profile is drafted, implementers work with the VA Team to identify such inconsistencies, and refine data models to bring them into alignment. This may involve reworking the implementation profile to more fully adopt Core-IM modeling patterns, or adding new features to core models to support requirements surfaced by the implementation profile. Notably, any implementation-specific features not ultimately supported by the GKS Core-IM can be captured in a compliant way by using the `Extension <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/data-types.html#extension>`_ element.

**Publish as a GA4GH Standard Profile**

Once alignment is complete, a draft of the Standard Profile is circulated for community review. Concerns and feedback are discussed and resolved, and any final changes are propagated to the relevant models. The model is then published as an official VA Standard Profile for a particular Statement or Study Result type.

**Evolve Profile to Support New Requirements**

A given Standard Profile will evolve as existing implementations expand coverage to new data types, or new implementations provide novel requirements to support their use case. For example, the Variant Pathogenicity Profile will evolve as ClinGen expands the ClinVar data it wants the profile to cover, and as other Driver Projects such AGHA/Shariant adopt the standard and need it to support their implementation. 

Implementing the VA-Spec
########################

The VA Modeling Framework offers many modes for engaging with the VA-Specification. Some users will want to **adopt established standard profiles out-of-the-box**, others may want to **extend or refine an existing standard profile** for their use case, while others may want to **develop entirely new profiles for additional types of Statements**.

The Quick Start Guide provides more information on these **modes of use**, and a **decision tree** to help adopters identify their best entry point into the VA Framework. And the `Profiling Methodology guide <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_ explains in detail the specific tasks and conventions involved in building VA Profiles.  

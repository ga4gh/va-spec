.. _developer-guide:

Developer Guide
!!!!!!!!!!!!!!!

Documentation in previous sections aims to provide a more conceptual and academic understanding of the VA-Spec - describing its content, modeling principles, and utility for a diverse community of potential adopters.

While a conceptual understanding of the specification is important for a technical audience as well, here we provide guidance to support data engineers who will be defining VA schema and implementing them in data exchange systems.

.. _base-vs-community-profiling:

Base vs Community Profiles
##########################

An important technical detail that is important for applying the VA-Spec is the distinction between what we call 'Base' and 'Community' Profiles.

**Base Profiles**:

- These are :ref:`Proposition <proposition-profiles>` and :ref:`Study Result <study-result-profiles>` profiles authored as formal subclasses of core classes in the va-core-source-yaml file.
- As detailed below, this mechanism for profile authoring allows for the kinds of attribute extension and addition that are needed in these Profile types (e.g. to specialize Proposition ``subject`` and ``object`` attributes, and create specific Proposition qualifiers and StudyResult data items)
- Proposition profile classes are used/referenced within Statement and Evidence Line 'Community' profiles - which are defined using a different mechanism. Here, the formal type of the Proposition is definitional for inferring the type of Statement or Evidence Line they support.

**Community Profiles**:

- These are :ref:`Statement <community-profiles>` and :ref:`Study Result <community-profiles>` profiles authored using a JSON Schema composition approach that layers constraints on top of VA core classes to enforce alignment with terminology conventions of a specific community guideline (e.g. ACMG 2015).
- Community profiles are specified in separate files, within directories that group profiles aligning with a particular community guideline (e.g. ACMG-2015, or AAC-2022)
- These Statement and Evidence Line profiles are subschema, not formal subclasses, of their parent core class, and they do not get a specialized ``type``.  As noted above, their type must be inferred from that of Proposition they employ to specify the possible fact they assert or evaluate evidence against, respectively.


.. _profile-authoring-mechanisms:

Profile Authoring Mechanisms
############################

Version 1.0 of the VA-Spec relies on two distinct mechanisms for authoring these different categories of Profiles.

.. _inheritance-based-profiling:

**Mechanism 1: Inheritance-Based Profiling** (for authoring "Base" Profiles)

- **Description**: Specializes generic VA core classes for a particular type of knowledge, through formal definition of concrete subclasses.
- **Mechanism**: Relies on bespoke `GKS Metaschema Processor <https://github.com/ga4gh/gks-metaschema>`_  *inherits* and *extends* functions, and requisite tooling, to implement class inheritance and attribute extension which are not natively supported by JSON Schema.
- **Application**: Used in authoring "Base Profiles" for  :ref:`Propositions <proposition-profiles>` and :ref:`Study Results <study-result-profiles>`, which can be used/referenced within Statement and Evidence Line profiles.
- **Rationale**: Allows for the types of attribute extension and addition that are applied in these Base Profiles (e.g. to specialize Proposition ``subject`` and ``object`` attributes, and create specific Proposition qualifiers and StudyResult data items)

 **Inheritance-Based Profiling Example**:

.. code-block:: yaml

  # From the source yaml file where the Variant Pathogenicity Proposition Base Profile is authored

  VariantPathogenicityProposition:
    inherits: ClinicalVariantProposition           # MSP inherits keyword
    maturity: trial use
    type: object
    description: A proposition describing the role of a variant in causing a heritable condition.
    properties:
      objectCondition:
        extends: object                            # MSP extends keyword
        oneOf:
          - $ref: Condition
          - $refCurie: gks.core:iriReference
        description: The :ref:`Condition` for which the variant impact is stated.
      penetranceQualifier:                         # Addition of new qualifier attribute
        $refCurie: gks.core:MappableConcept
        description: Reports the penetrance of the pathogenic effect...

.. _composition-based-profiling:

**Mechanism 2: Composition-Based Profiling** (for authoring "Community" Profiles)

- **Description**:  Defines subschema that layer additional constraints on top of VA core attributes to refine the values they are able to take.
- **Mechanism**:  Relies on schema composition using the native JSON Schema ``allOf`` keyword, which does not result in creation of concrete subclasses for each profile.
- **Application**: Used in authoring "Community Profiles" that add guideline-specific constraints on core :ref:`Statement <variant-pathogenicity-statement-acmg-2015>` and :ref:`Evidence Line <experimental-variant-pathogenicity-functional-impact-evidence-line-acmg-2015>` classes, which can leverage base Proposition profiles to represent semantics of the possible fact they assert or evaluate evidence against, respectively.
- **Rationale**: Allows implementers to define simple constraints for Statement and Evidence Line profiles in a way that does not require running bespoke MSP tooling

 **Composition-Based Profiling Example**:

.. code-block:: yaml

  # From the source yaml file where the Variant Pathogenicity Statement AMCG 2015 Community Profile is authored

  VariantPathogenicityStatement:
    description: A Statement describing the role of a variant in causing an inherited condition.
    # JSON Schema 'allOf' keyword used for schema composition
    allOf:
    - $ref: "/ga4gh/schema/va-spec/1.0.0-ballot.2025-03.2/base/json/Statement"
    # list of property definitions that further constrain attributes in the base Statement class
    - properties:
        # A constraint on the Statement.proposition attribute requiring it to take a VariantPathogenicityProposition
        proposition:
          $ref: "/ga4gh/schema/va-spec/1.0.0-ballot.2025-03.2/base/json/VariantPathogenicityProposition"
          description: A proposition about the pathogenicity of a variant, the validity of which is assessed and reported by the Statement.
        # A constraint on the code field nested within a MappableConcept that requires the 'strength' attribute to take specific values.
        strength:
          description: The strength of support that an ACMG 2015 Variant Pathogenicity statement is determined to provide for or against the proposed pathogenicity of the assessed variant.
          properties:
            primaryCoding:
              code:
                enum:
                  - definitive
                  - likely
              system:
                const: ACMG Guidelines, 2015


.. _custom-profile-development:

Custom Profile Development
##########################

Representation of a particular type of **Statement** or **Evidence Line** using the VA-Spec does not always require a VA Profile to be specifically defined for it.

Custom Profiles are Statement or Evidence Line profiles that are created de novo, to support a specific implementation use case where data cannot be made to conform to a particular guideline-based Community Profile .

This section describes why these are useful, and how to create them.

**Why they are useful:**

* The Statement and Evidence Line :ref:`Community Profiles <community-profiles>` included in version 1.0 of the VA-Spec are there to support data providers pursuing strict alignment with a particular community guidelines.
* Implementers who do not seek such alignment can build their own schema for Statements or Evidence Lines to report on any of the knowledge types specified in VA :ref:`Base Proposition profiles<proposition-profiles>`.
* For example, a project that aims to represent some of the messier data in ClinVar where values for key fields bound to ACMG-specific enuemrations in the exsitng :ref:`Variant Pathogenicity Statement profile <variant-pathogenicity-statement-acmg-2015>` - and doesn't want to use :ref:`Extensions <Extension>` to capture this data - can define a custom Pathogenicity Statement Profile from core Statement and Evidence Line classes that applies constraints specific to its data.

**The process is relatively straightforward:**

#. Starting with the core :ref:`Statement<Statement` class
#. Bind its ``proposition`` attribute to the :ref:`VariantPathogenicityProposition <variant-pathogenicity-proposition>`base profile class
#. Use other base Statement attributes and core classes to represent additional information about the Statement (e.g. strength, classification, methods, etc) - defining additional constraints or enuemrations as desired using the :ref:`Composition-Based Profiling Mechanism <composition-based-profiling>` described above.

This :ref:`simple data example <custom-varaint-pathogenicity-statement-example>` illustrates application of this approach to create a custom, non-ACMG-compliant representation of a pathogenicity statement.







VA Profile Development
######################

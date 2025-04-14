.. _developer-guide:

Developer Guide
!!!!!!!!!!!!!!!

Preceding documentation provides a more conceptual understanding of the VA-Spec for a broad audience - covering its content, modeling principles, and general utility. Here we provide guidance to support modelers and data engineers who will be authoring VA Profiles, or implementing them in data exchange systems.

.. _profile-authoring-mechanisms:

Authoring Base vs Community Profiles
#####################################

Here we build on this :ref:`conceptual overview of the Profiling Approach <profiles>`, to describe the technical mechanisms used to define profile specilaizations. Version 1.0 of the VA-Spec makes a formal distinction between **'Base'** and **'Community'** Profiles, and relies on **distinct mechanisms** for authoring them.

.. _inheritance-based-profiling:

**Inheritance-Based Authoring of Base Profiles**:

- **Description**: Specializes generic VA core classes for a particular type of knowledge, through formal definition of concrete subclasses.
- **Mechanism**: Relies on bespoke `GKS Metaschema Processor <https://github.com/ga4gh/gks-metaschema>`_  *inherits* and *extends* functions, and requisite tooling, to implement class inheritance and attribute extension which are not natively supported by JSON Schema.
- **Application**: Used in authoring "Base Profiles" for  :ref:`Propositions <proposition-profiles>` and :ref:`Study Results <study-result-profiles>`, which can be used/referenced within Statement and Evidence Line profiles.
- **Rationale**: Allows for the types of attribute extension and addition that are applied in these Base Profiles (e.g. to specialize Proposition ``subject`` and ``object`` attributes, and create specific Proposition qualifiers and StudyResult data items)
- **Example**:

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

**JSON Schema Composition-Based Authoring of Community Profiles**:

- **Description**:  Defines subschema that layer additional constraints on top of VA core attributes to refine the values they are able to take.
- **Mechanism**:  Relies on schema composition using the native JSON Schema ``allOf`` keyword, which does not result in creation of concrete subclasses for each profile. Source files are organized in directories based on the community guideline they enforce (e.g. ACMG-2015, or AAC-2022).
- **Application**: Used in authoring "Community Profiles" that add guideline-specific constraints on core :ref:`Statement <variant-pathogenicity-statement-acmg-2015>` and :ref:`Evidence Line <evidence-line-acmg-2015>` classes, which embed corresponding base Proposition profiles to represent semantics of the possible fact they assert or evaluate evidence against, respectively.
- **Rationale**: Allows implementers to define simple constraints for Statement and Evidence Line profiles in a way that does not require running bespoke Metaschema Processor tooling.
- **Example**:

.. code-block:: yaml

  # From the source yaml file where the Variant Pathogenicity Statement AMCG 2015 Community Profile is authored

  VariantPathogenicityStatement:
    description: A Statement describing the role of a variant in causing an inherited condition.
    # JSON Schema 'allOf' keyword used for schema composition
    allOf:
    - $ref: "/ga4gh/schema/va-spec/1.0.0-ballot.2025-03.4/base/json/Statement"
    # list of property definitions that further constrain attributes in the base Statement class
    - properties:
        # A constraint on the Statement.proposition attribute requiring it to take a VariantPathogenicityProposition
        proposition:
          $ref: "/ga4gh/schema/va-spec/1.0.0-ballot.2025-03.4/base/json/VariantPathogenicityProposition"
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

Custom Profiles are Statement or Evidence Line models that are defined de novo, to support a specific implementation use case where data cannot be made to conform to a particular guideline-based Community Profile.

This section describes why these are useful, and how to create them.

**Why they are useful:**

* The Statement and Evidence Line :ref:`Community Profiles <community-profiles>` included in version 1.0 of the VA-Spec are there to support data providers pursuing strict alignment with a particular community guidelines.
* Implementers who do not seek such alignment can build their own schema for Statements or Evidence Lines to report on any of the knowledge types specified in VA :ref:`Base Proposition profiles<proposition-profiles>`.
* For example, a project that aims to represent some of the messier data in ClinVar where values for key fields bound to ACMG-specific enumerations in the exisitng :ref:`Variant Pathogenicity Statement profile <variant-pathogenicity-statement-acmg-2015>` - and doesn't want to use :ref:`Extensions <Extension>` to capture this data - can define a custom Pathogenicity Statement Profile from core Statement and Evidence Line classes that applies constraints specific to its data.

**The process is straightforward** - e.g. to create a custom Statement profile for pathogenicity classification data not based strictly aligned with ACMG terminology:

#. Start with the core :ref:`Statement<Statement>` class
#. Bind its ``proposition`` attribute to the :ref:`VariantPathogenicityProposition <variant-pathogenicity-proposition>`base profile class
#. Use other core Statement attributes and related core classes to represent additional information about the Statement (e.g. strength, classification, methods, etc) - defining additional constraints or enumerations as desired using the :ref:`Composition-Based Profiling Mechanism <composition-based-profiling>` described above.

This :ref:`simple data example <custom-variant-pathogenicity-statement-example>` illustrates application of this approach to create a custom, non-ACMG-compliant representation of a pathogenicity statement.







VA Profile Development
######################

.. _developer-guide:

Developer Guide
!!!!!!!!!!!!!!!

The preceding documentation provides a more conceptual understanding of the VA-Spec for a broad audience - covering its content, modeling principles, and general utility. This section provides more technical guidance to support modelers and data engineers who will be authoring VA Profiles, or implementing them in data exchange systems.

.. _profile-definition-mechanisms:

Profile Definition Mechanisms
#############################

We have :Ref:`previously described <va-profiles>` two categories of profiles in the VA-Spec, which are authored using different mechanisms:

 #. **Base Profiles**: use a **subclassing mechanism** to define **Proposition** and **Study Result** profiles as VA base classes.
 #. **Community Profiles**: use a **schema-composition mechanism** to define **Statement** and **Evidence Line** profiles as constraints on top of core class definitions.

For **Proposition** and **Study Result** Base Profiles, a subclassing mechanism is required to rename and add additional attributes - including qualifier and data item fields used to collect domain-specific information in these profiles

For **Statements** and **Evidence Lines**, any domain-specificity is specified in the **Propositions** these objects encapsulate, so there is no need to define formal subclasses here. However, VA-Spec includes **Community Profiles** of these classes that constrain certain attribute values to align with the conventions of a particular community guideline - and here `schema composition <https://json-schema.org/understanding-json-schema/reference/combining>`_ is sufficient to define these restrictions. This approach to profile definition reduces the number of classes that need to be created, managed, and parsed when creating and validating VA data.

The diagrams below illustrate where subclass- and composition-based mechanisms are applied to define each profile included in the VA-Spec. Top to bottom, the increasingly dark colors reflect the increasing domain-specificity of the models.

------


.. image:: /images/core-model-classes-mechanism.png


The **Core Data Model** consists of the domain-agnostic classes above. **Concrete** classes can be used to capture data directly. **Abstract** classes must first be 'specialized' through subclassing. Note that some classes in the model are imported from gks-core, vrs, and cat-vrs models, as indicated by annotations in green which indicate the GKS specification in which each is defined.


-------

.. image:: /images/base-profiles-mechanism.png

The **Proposition** and **Study Result** Base Profiles above are defined using a subclassing mechanism, creating formal "VA Base Classes" that extend the Core Data Model. The specific syntax for this authoring mechanism leverages features outside the native JSON Schema language, as illustrated in the Proposition profile example :ref:`here <subclass-based-profiling-syntax>`.

-------

.. image:: /images/community-profiles-mechanism.png

The **Statement** and **Evidence Line** profiles above are defined as "Schema Compositions" using a constraint-based mechanism. These profiles represent *sub-schema*, rather than *sub-classes* in the VA Model. The domain-specificity of these profiles is defined in the **Proposition** profiles they encapsulate, as diagrammed.  Constraints may be added to restrict certain attributes to align with terminological conventions of a particular community guideline (e.g. ACMG-2015, AAC-2017, CCV-2022). The specific syntax for this authoring mechanism is illustrated in the Statement profile example :ref:`here <composition-based-profiling-syntax>`.

------

Finally, this :ref:`diagrammed data example <acmg-variant-pathogenicity-statement-example-with-evidence-diagram>` provides a nice visualization of how Core Model classes and profiles defined using these different mechanisms are used together to represent real data. Styling conventions in the diagram indicate the type of model that specifies each object in the example (Core Class, Base Profile, Community Profile).

-------

.. _profile-authoring-syntax:

Authoring Base vs Community Profiles
#####################################

Here we describe the technical mechanism and syntax used to define VA Profiles. As noted, version 1.0 of the VA-Spec makes a formal distinction between **Base** and **Community** Profiles, and relies on **distinct mechanisms** for authoring them.

.. _subclass-based-profiling:

**Subclass-Based Authoring of Base Profiles**:

- **Mechanism**: Specializes generic VA core classes for a particular type of knowledge, through formal definition of concrete subclasses.
- **Syntax**: Relies on `GKS Metaschema Processor <https://github.com/ga4gh/gks-metaschema>`_  ``inherits`` and ``extends`` keywords and requisite tooling to implement class inheritance and attribute extension which are not natively supported by JSON Schema.
- **Application**: Used in authoring "Base Profiles" for  :ref:`Propositions <proposition-profiles>` and :ref:`Study Results <study-result-profiles>`, which can be used/referenced within Statement and Evidence Line profiles.
- **Rationale**: Allows for the types of attribute extension and addition that are applied in these Base Profiles (e.g. to specialize Proposition ``subject`` and ``object`` attributes, and create specific Proposition qualifiers and StudyResult data items)
- **Example**:

.. _subclass-based-profiling-syntax:

.. code-block:: yaml

  # Syntax from the source yaml file where the Variant Pathogenicity Proposition Base Profile is authored

  VariantPathogenicityProposition:
    inherits: GeneticContextVariantProposition     # MSP inherits keyword
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

**Schema Composition-Based Authoring of Community Profiles**:

- **Mechanism**:  Defines subschema that layer additional constraints on top of VA core attributes to refine the values they are able to take.
- **Syntax**:  Relies on schema composition using the native JSON Schema ``allOf`` keyword, which does not result in creation of concrete subclasses for each profile. Source files are organized in directories based on the community guideline they enforce (e.g. ACMG-2015, or AAC-2022).
- **Application**: Used in authoring "Community Profiles" that add guideline-specific constraints on core :ref:`Statement <variant-pathogenicity-statement-acmg-2015>` and :ref:`Evidence Line <variant-pathogenicity-evidence-line-acmg-2015>` classes, which embed corresponding base Proposition profiles to represent semantics of the possible fact they assert or evaluate evidence against, respectively.
- **Rationale**: Allows implementers to define simple constraints for Statement and Evidence Line profiles in a way that does not require running custom Metaschema Processor tooling.
- **Example**:

.. _composition-based-profiling-syntax:

.. code-block:: yaml

  # Syntax from the source yaml file where the AMCG 2015 Variant Pathogenicity Statement Community Profile is authored

  VariantPathogenicityStatement:
    description: A Statement describing the role of a variant in causing an inherited condition.
    # JSON Schema 'allOf' keyword used for schema composition
    allOf:
    - $ref: "/ga4gh/schema/va-spec/1.0.0/base/json/Statement"
    # list of property definitions that further constrain attributes in the base Statement class
    - properties:
        # A constraint on the Statement.proposition attribute requiring it to take a VariantPathogenicityProposition
        proposition:
          $ref: "/ga4gh/schema/va-spec/1.0.0/base/json/VariantPathogenicityProposition"
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

------

.. _custom-profile-development:

Custom Profile Development
##########################

Representation of a particular type of **Statement** or **Evidence Line** using the VA-Spec does not always require a VA Profile to be specifically defined for it.

Custom Profiles are Statement or Evidence Line models that are defined de novo, to support a specific implementation use case where data cannot be made to conform to a particular guideline-based Community Profile.

This section describes why these are useful, and how to create them.

**Why they are useful:**

* The Statement and Evidence Line :ref:`Community Profiles <community-profiles>` included in version 1.0 of the VA-Spec are there to support data providers pursuing strict alignment with a particular community guidelines.
* Implementers who do not seek such alignment can build their own schema for Statements or Evidence Lines to report on any of the knowledge types specified in VA :ref:`Base Proposition profiles<proposition-profiles>`.
* For example, a project that aims to represent some of the messier data in ClinVar where values for key fields bound to ACMG-specific enumerations in the existing :ref:`Variant Pathogenicity Statement profile <variant-pathogenicity-statement-acmg-2015>` - and doesn't want to use :ref:`Extensions <Extension>` to capture this data - can define a custom Pathogenicity Statement Profile from core Statement and Evidence Line classes that applies constraints specific to its data.

**The process is straightforward** - e.g. to create a custom Statement profile for pathogenicity classification data not based strictly aligned with ACMG terminology:

#. Start with the core :ref:`Statement<Statement>` class
#. Bind its ``proposition`` attribute to the :ref:`VariantPathogenicityProposition <variant-pathogenicity-proposition>` base profile class
#. Use other core Statement attributes and related core classes to represent additional information about the Statement (e.g. strength, classification, methods, etc) - defining additional constraints or enumerations as desired using the :ref:`Composition-Based Profiling Mechanism <composition-based-profiling>` described above.
#. Use the base Statement reference implementation to create and validate compliant data.

This :ref:`simple data example <custom-variant-pathogenicity-statement-example>` illustrates application of this approach to create a custom, non-ACMG-compliant representation of a pathogenicity statement.

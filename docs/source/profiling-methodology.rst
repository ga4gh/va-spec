.. _profiling-methodology:

Profiling Methodology
!!!!!!!!!!!!!!!!!!!!!


**Overview**

In practice, the schema used to represent actual data are 'profiles' which constrain and/or extend core Statement, Study Result, and Evidence Line classes to support a specific type of variant knowledge. 

The VA-Spec defines a **Profiling Methodology** which specifies the types of specializations and extensions that are permitted. 

The diagram below illustrates the types of specializations defined in authoring a Variant Pathogenicity Proposition and Statement profile, based here on terminological conventions of the ACMG Variant Interpretation Guidelines. 

.. _profiling-methodology

.. figure:: images/profiling-methodology.png

    Profiling specializations defined in Variant Pathogenicity profiles.

   (A) Core Proposition and Statement classes and a subset of their attributes. (B) ACMG-based Variant Pathogenicity and Statement profiles derived from these core classes, with specializations highlighted in green. The actual VA-Spec v1.0 schema for these profiles are :ref:`here <variant-pathogenicity-proposition>` and :ref:`here <variant-pathogenicity-statement-acmg-2015>`. 


**Profiling operations supported by the methodology, and illustrated in the example above, include:**

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Profiling Operation
      - Example
   *  - Defining domain-specific subtypes of general purpose Core IM classes
      - Specialization of ``Proposition`` -> ``VariantPathogenicityProposition``
   *  - Defining attributes to capture domain-specific information
      -  Statement qualifiers ``geneContextQualifier`` and ``alleleoriginQualifier``
   *  - Define or import classes for domain entities that profiles are about
      - The Variant Pathogenicity Proposition profile, uses ``MolecularVariation`` and ``CategoricalVariation`` classes imported from VRS and CatVRS, and a ``Condition`` class defined in VA-Spec
   *  - Constrain values of core attributes to take specific types as values
      - Restricting the ``VariantPathogenicityStatement.object`` field to take a ``Condition`` as its value
   *  - Define value sets and binding them to attributes taking coded values.
      - Restricting nested fields in the MappableConcept object taken by ``VariantPathogenicityStatement.classification`` to a set of enumerated values based on ACMG Guideline temrinology.
   *  - Refining cardinality of select attributes 
      - Making ``Statement.classification`` a required field in the ACMG Varint Variant Pathogenicity Statement.


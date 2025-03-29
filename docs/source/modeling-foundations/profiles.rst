.. _profiles:

Profiles
!!!!!!!!

.. important::  This overview is meant to provide a **conceptual** understanding of how profiling works. The **technical** details behind how profiles are specified and used are described in the :ref:`Developer Guide <developer-guide>` section.

Profiling Tasks
###############

As noted, the VA-Spec provides Profiles for :ref:`Statement <Statement>`, :ref:`Study Result <StudyResult>`, and :ref:`Evidence Line <EvidenceLine>` representation that specialize these core classes to support a specific type of variant knowledge.

The profiling approach defined in v1.0 of the VA-Spec informally describe the types of constraints and extensions that are permitted in authoring profiles. The table below describes the specific tasks supported in this profiling approach.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  -      Profiling Task
      -            Example
   *  - Define domain-specific subtypes of general purpose Core Model classes
      - Specialization of ``Proposition`` into ``VariantPathogenicityProposition``
   *  - Define new attributes to capture domain-specific information
      -  The Statement qualifiers ``geneContextQualifier`` and ``alleleoriginQualifier``
   *  - Define or import classes for domain entities that profiles are about
      - The ``VariantPathogenicityProposition`` profile uses ``MolecularVariation`` and ``CategoricalVariation`` classes imported from VRS and CatVRS, and a ``Condition`` class defined in the VA-Spec itself.
   *  - Constrain values of core attributes to take specific types as values
      - Restricting the ``VariantPathogenicityStatement.object`` field to take a ``Condition`` as its value
   *  - Define value sets and binding them to select attributes.
      - Restricting nested fields in the MappableConcept object taken by ``VariantPathogenicityStatement.classification`` to a set of enumerated values based on ACMG Guideline temrinology.
   *  - Refine cardinality of select attributes
      - Making ``Statement.classification`` a required field in the ACMG Variant Pathogenicity Statement.

Future versions of the specification will include a more formal specification and tooling support for executing these tasks and validating they were performed correctly.

Profiling Example
#################

The diagram below illustrates at a conceptual level some of the profiling steps applied to the core Statement and Proposition classes, to create models supporting ACMG-based Variant Pathogneicity Statements.

.. _profiling-methodology

.. figure:: ../images/profiling-methodology.png

   ACMG-based Variant Pathogenicity Profiles.

   (**A**) Core Proposition and Statement classes, showing a subset of their attributes. (**B**) ACMG-based Variant Pathogenicity profiles derived from these core classes, with profiling specializations in green. Text in curly braces are enumerations, which in some cases are nested inside fields of a MappableConcept. The actual VA-Spec v1.0 schema for these profiles are :ref:`here <variant-pathogenicity-proposition>` and :ref:`here <variant-pathogenicity-statement-acmg-2015>`.

This :ref:`simple data example <acmg-variant-pathogenicity-statement-example>` illustrates application of these profiles to structure a Pathogenicity Statement.

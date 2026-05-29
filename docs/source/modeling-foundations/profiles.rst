.. _profiles:

Profiles
!!!!!!!!

.. important::  This overview is meant to provide a **conceptual** understanding of how profiling works. The **technical** details behind how profiles are specified and used are described in the :ref:`Developer Guide <developer-guide>` section.

Profiling Tasks
###############

As noted, the VA-Spec provides :ref:`Statement <Statement>`, :ref:`Study Result <StudyResult>`, :ref:`Evidence Line <EvidenceLine>`, and :ref:`Proposition <Proposition>` Profiles that specialize these core classes to support a specific domain of variant knowledge (e.g. pathogenicity), and/or support conventions of a particular community guideline (e.g. ACMG-2015).

The table below describes the different profiling tasks supported in v1.0 of the VA-Spec, with examples based on definition of ACMG-aligned Variant Pathogenicity profiles. These are illustrated graphically in the figure that follows.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: 40 60

   *  -      Profiling Task
      -            Example
   *  - Define a domain- or community-specific version of a Core Model class
      - Specialization of the ``Proposition`` class to create the ``VariantPathogenicityProposition`` profile
   *  - Import and reference classes for domain entities that variant knowledge is about
      - The ``VariantPathogenicityProposition`` profile uses ``MolecularVariation`` and ``CategoricalVariation`` classes imported from VRS and CatVRS, and a minimal ``Condition`` class defined in the VA-Spec itself.
   *  - Constrain attributes to take a more specific type of value (possible renaming them in the process)
      - The ``VariantPathogenicityProposition`` profile renames the ``object`` attribute  to ``objectCondition``, and restricts it to take a ``Condition`` as its value
   *  - Define value sets and binding them to select attributes.
      - The ``ACMG 2015 Variant Pathogenicity Statement`` profile restricts its ``classification`` attribute to take values based on ACMG 2015 criterion codes and terminology.
   *  - Define a new attribute to capture domain-specific information in a profiled class
      - The ``VariantPathogenicityProposition`` profile defines ``geneContextQualifier`` and ``alleleOriginQualifier`` attributes.
   *  - Refine cardinality of select attributes
      - The ``ACMG 2015 Variant Pathogenicity Statement`` profile makes ``Statement.classification`` a required field.

Profiling Example
#################

The diagram below illustrates at a conceptual level some of the profiling steps applied to the core Statement and Proposition classes, to create models supporting ACMG-based Variant Pathogenicity Statements.

.. _profiling-methodology:

.. figure:: ../images/profiling-methodology.png

   ACMG-based Variant Pathogenicity Profiles.

   (**A**) Core Proposition and Statement classes, showing a subset of their attributes. (**B**) ACMG-based Variant Pathogenicity profiles derived from these core classes, with profiling specializations in green. Text in curly braces are enumerations, which in some cases are nested inside fields of a MappableConcept. The actual VA-Spec v1.0 schema for these profiles are :ref:`here <variant-pathogenicity-proposition>` and :ref:`here <variant-pathogenicity-statement-acmg-2015>`.

This :ref:`data example <acmg-variant-pathogenicity-statement-example>` illustrates application of these two profiles to represent a simple Variant Pathogenicity Statement.

Future versions of the VA-Spec will include a more formal specification and tooling support for executing these tasks and validating they were performed correctly.

.. _Statement:

Statement
!!!!!!!!!


.. include::  ../../../def/va-spec/Statement.rst

----------

Data Structure
##############

:ref:`Statements <Statement>` represent *assertions* or *assessments* of general knowledge about a variant - e.g. an *assertion* that *'HRAS:c.173C>T is pathogenic for Costello Syndrome*, or an *assessment* that there is presently only moderate evidence supporting this possible fact.

In VA-Spec, the :ref:`Statement <Statement>` class and its :ref:`profiles <community-profiles>` can support the general data structure below.

.. statement-proposition-data-structure:

.. figure:: ../../../images/statement-proposition-data-structure.png
   :width: 700

   Statement Data Structure

   **Legend** A class-level view of the Statement-based structures supported in VA-Spec data. Italicized text in each class exemplify the kind of information each may capture, here in the case of a Variant Pathogenicity Statement supported by Population Allele Frequency evidence.

In this structure:

* A **Statement** roots a central axis where it is linked, via ``hasEvidenceLines``, to zero or more nested **Statements** serving as **Evidence Lines** - discrete arguments for or against it.
* Each Evidence Line may in turn be linked, via ``hasEvidenceItems``, to zero or more pieces of information (e.g. **Study Results**) that were used to build its evidence-based argument.
* The **Proposition** contained in the Statement object encapsulates a structured representation of the possible fact that the Statement may assert or assess (e.g. that *'HRAS:c.173C>T is causal for Costello Syndrome'*). Unless otherwise stated, this is the same proposition against which evidence is assessed in supporting Evidence Lines.
* Surrounding this central axis are classes that describe the provenance of the central artifacts, including **Contributions** made to them by **Agents**, **Activities** performed in doing so, **Methods** that specify their creation, and **Documents** that describe them.

A data example illustrating this structure for a Variant Pathogenicity Statement can be found :ref:`here <acmg-variant-pathogenicity-statement-example-with-evidence>`.

---------

Implementation Guidance
#######################

1. Statement and Proposition Semantics
======================================

Statements put forth a Proposition that expresses some possible fact about the world, and may provide an assessment of this proposition's validity (e.g. a level of confidence that it is true, or indicator of the overall strength of evidence supporting it). The semantics of the Proposition are captured in  ``subject``, ``predicate``, ``object``, and optional ``qualifier`` attributes (**SPOQ**). An assessment of the Proposition's validity can be captured using ``direction``, ``strength``, and/or ``score`` attributes (**DS**).

* The ``direction`` attribute is used to indicate whether the Statement's Proposition is **supported** by the agent's assessment (when evidence favors its validity), is **disputed** by the agent's assessment (when evidence argues against its validity), or remains **neutral** (when conflicting or insufficient evidence exists to assert one direction or the other). Values come from an enumerated set of strings defined in the model {'supports', 'disputes', 'neutral'}.

* The ``strength`` attribute is used to report the strength of this assessment in the direction indicated. Strength can be framed as a **level of confidence** that the Proposition is true or false, or as a **strength of evidence** that supports or disputes it - depending on what  values of this attribute are used (e.g. 'high confidence', 'low confidence', etc. if confidence level is being assessed, or 'strong evidence', 'weak evidence', etc. if evidence strength is being assessed). ALternatively, data providers can choose values that don't commit to one or the other if they don't want to make the distinction (e.g. 'high' vs 'medium' vs 'low').

* The ``score`` attribute serves the same purpose as ``strength``, but allows for a quantitative assessment based on a numerical score, and can be used in addition to or as an alternative to the '`strength`' attribute.

This **'SPOQ-DS'** Proposition pattern is used to explicitly represent the semantics of the central piece of knowledge reported in any Statement, which is supported by evidence and provenance information captured in other Statement attributes.


2. Statements as Evidence Lines
===============================

The core model does not define a separate ``EvidenceLine`` class. A discrete, evidence-based argument for or against a Proposition is simply another **Statement**, attached to the Statement it argues about via ``hasEvidenceLines``. A Statement in that role uses the same attributes as any other:

* ``proposition`` holds the possible fact the evidence is assessed against. It may be omitted when it would merely repeat the ``proposition`` of the Statement it supports.
* ``hasEvidenceItems`` holds the information that was assessed - a :ref:`Statement <Statement>`, :ref:`Study Result <StudyResult>`, :ref:`Data Item <DataItem>`, or an IRI reference to one of these.
* ``direction``, ``strength`` and/or ``score`` report the outcome of that assessment, and ``outcome`` summarizes it in a single community-familiar term.

See the :ref:`Evidence Line <EvidenceLine>` page for when to use this pattern rather than citing evidence items directly, how deeply to nest it, and how broadly to scope each argument.


3. Use of the ``Proposition.qualifier`` Attribute:
==================================================

* This attribute allows representation of more complex, n-ary statements that may not be accommodated by a simple subject-predicate-object (SPO) triple. For example, if an SPO triple asserts that 'Variant X' - predicts sensitivity to - 'Treatment Y', a qualifier can be used to indicate that this applies in the context of a particular 'Disease Z'.
* Qualifiers can also add information that quantifies aspects of a Statement's Proposition - e.g.  an SPO triple reporting that a 'Variant X'- causes - 'Phenotype Y', can be quantified with frequency/penetrance information that indicates the percentage of carriers in which the phenotype manifests. Proposition profiles may define more than one qualifier, as needed to capture different types of qualifying information.
* The Core model specifies use of a key-value 'Qualifier' object to capture the meaning and value of each type of qualifying information relevant for a given type of Proposition. But in practice, profiles for specific Proposition types may choose to define one or more specializations of the generic 'qualifier' property as named attributes. This makes the data more succinct and parsable, and allows specific constraints to be applied and validated for different qualifiers.
* For example, a VariantPathogenicityProposition profile may define a named ``alleleOriginQualifier`` attribute that is required, and a named ``geneContextQualifier`` attribute that is optional - both of which conceptually specialize the Core ``qualifier`` property. Under this approach, the core ``qualifier`` acts as a placeholder to seed such specializations, but is not used directly in Proposition profiles.
* In practice, the core ``qualifier`` attribute SHOULD be conceptually extended in Proposition profiles to indicate specific types of qualifying information that is being provided (e.g.``diseaseContextQualifier``, or ``penetranceQualifier``). The ``qualifier`` attribute in the core model acts as a placeholder to seed such specializations, but it, or the ``Qualifier`` class, SHOULD NOT be used directly in a Proposition profile.

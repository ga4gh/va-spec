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

.. raw:: html

   <iframe src="../../../_static/diagrams/statement-evidence-example.html" style="width:100%; height:750px; border:0;" title="Statement, Proposition, and Evidence worked example"></iframe>

**Legend** A class-level view of the Statement-based structures supported in VA-Spec data, including the classes that describe provenance (Proposition, Method, Contribution, Document) and evidence (Evidence Line, Study Result, Data Item).

In this structure:

* A **Statement** roots a central axis where it is linked, via ``hasEvidenceLines``, to zero or more :ref:`Evidence Lines <EvidenceLine>` - discrete arguments for or against it - and/or, via ``hasEvidence``, directly to any information used as evidence.
* Each Evidence Line may in turn be linked, via ``hasEvidenceItems``, to zero or more pieces of information (e.g. **Study Results**) that were used to build its evidence-based argument.
* The **Proposition** contained in the Statement object encapsulates a structured representation of the possible fact that the Statement may assert or assess (e.g. that *'HRAS:c.173C>T is causal for Costello Syndrome'*). Unless otherwise stated, this is the same proposition against which evidence is assessed in supporting Evidence Lines.
* Surrounding this central axis are classes that describe the provenance of the central artifacts, including **Contributions** made to them by **Agents**, **Methods** that specify their creation, and **Documents** that describe them.

A data example illustrating this structure for a Variant Pathogenicity Statement can be found :ref:`here <acmg-variant-pathogenicity-statement-example-with-evidence>`.

---------

Implementation Guidance
#######################

1. Statement and Proposition Semantics
======================================

Statements put forth a Proposition that expresses some possible fact about the world, and may provide an assessment of this proposition's validity (e.g. a level of confidence that it is true, or indicator of the overall strength of evidence supporting it). The semantics of the Proposition are captured in ``subject``, ``predicate``, and ``object`` attributes, plus optional, type-specific qualifiers (**SPOQ**; see the guidance on qualifiers below). An assessment of the Proposition's validity can be captured using ``direction``, ``strength``, and/or ``score`` attributes (**DS**).

* The ``direction`` attribute is used to indicate whether the Statement's Proposition is **supported** by the agent's assessment (when evidence favors its validity), is **disputed** by the agent's assessment (when evidence argues against its validity), or remains **neutral** (when conflicting or insufficient evidence exists to assert one direction or the other). Values come from an enumerated set of strings defined in the model {'supports', 'disputes', 'neutral'}.

* The ``strength`` attribute is used to report the strength of this assessment in the direction indicated. Strength can be framed as a **level of confidence** that the Proposition is true or false, or as a **strength of evidence** that supports or disputes it - depending on what  values of this attribute are used (e.g. 'high confidence', 'low confidence', etc. if confidence level is being assessed, or 'strong evidence', 'weak evidence', etc. if evidence strength is being assessed). ALternatively, data providers can choose values that don't commit to one or the other if they don't want to make the distinction (e.g. 'high' vs 'medium' vs 'low').

* The ``score`` attribute serves the same purpose as ``strength``, but allows for a quantitative assessment based on a numerical score, and can be used in addition to or as an alternative to the '`strength`' attribute.

This **'SPOQ-DS'** Proposition pattern is used to explicitly represent the semantics of the central piece of knowledge reported in any Statement, which is supported by evidence and provenance information captured in other Statement attributes.


2. Attaching Evidence to a Statement
====================================

A Statement can cite the evidence behind its assessment in two complementary ways:

* ``hasEvidence`` links the Statement directly to any information used as evidence - a :ref:`Study Result <StudyResult>`, :ref:`Data Item <DataItem>`, prior :ref:`Statement <Statement>`, :ref:`Evidence Line <EvidenceLine>`, or an IRI reference to any :ref:`Information Entity <InformationEntity>`. Use this when the data simply records *that* some information was used as evidence.
* ``hasEvidenceLines`` links the Statement to one or more :ref:`Evidence Lines <EvidenceLine>` - discrete, scored, directional arguments (each with its own ``targetProposition``, ``directionOfEvidenceProvided``, ``strengthOfEvidenceProvided``, and ``evidenceOutcome``) built from the information they assessed. Use this when the data captures *how* information was interpreted and scored as an argument.

See the :ref:`Evidence Line <EvidenceLine>` page for when to use a structured Evidence Line rather than citing evidence directly, how deeply Evidence Lines nest, and how broadly to scope each argument.


3. Use of Qualifiers (the "Q" in SPOQ):
==================================================

* Qualifiers let a Proposition represent more complex, n-ary claims that a simple subject-predicate-object (SPO) triple cannot capture on its own. For example, where an SPO triple asserts that 'Variant X' - predicts sensitivity to - 'Treatment Y', a qualifier can restrict that claim to the context of a particular 'Disease Z'. Qualifiers can also *quantify* a claim - e.g. an SPO triple reporting that 'Variant X' - causes - 'Phenotype Y' can carry penetrance information indicating the percentage of carriers in which the phenotype manifests.
* The **Q** in **SPOQ** is conceptual, not a physical attribute. The core :ref:`Proposition` class does **not** define a ``qualifier`` property, and there is no ``Qualifier`` class - so no Proposition instance ever carries a field literally named ``qualifier``. Qualifiers come into being only when a concrete Proposition subclass is formally defined and declares them.
* When a Proposition type defines qualifiers, each one is declared as its own **named attribute** using the ``xxxQualifier`` convention, where ``xxx`` names the kind of qualifying information it carries (e.g. ``geneContextQualifier``, ``alleleOriginQualifier``, ``conditionQualifier``, ``penetranceQualifier``). Declaring each qualifier as a distinct named attribute keeps the data succinct and parsable, and lets the schema apply and validate constraints specific to that qualifier.
* A single Proposition type may define more than one qualifier, and each may be required or optional according to that type's definition. For example, :ref:`VariantPathogenicityProposition` defines ``geneContextQualifier``, ``alleleOriginQualifier``, ``penetranceQualifier``, and ``modeOfInheritanceQualifier`` (all optional), while :ref:`VariantTherapeuticResponseProposition` defines ``geneContextQualifier`` and ``alleleOriginQualifier`` (optional) together with a required ``conditionQualifier``.

.. _Proposition:

Proposition
!!!!!!!!!!!

.. include::  ../../def/va-spec/Proposition.rst

-----

**Implementation Guidance:**

**1. Structuring Proposition Semantics:**

Propositions are abstract representations of possible facts about a domain of discourse, e.g. *"NM_005343.4:c.173C>T causes Costello Syndrome"*. The semantics of a Proposition are captured in ``subject``, ``predicate``, ``object``, and optional ``qualifier`` attributes (SPOQ). Proposition profiles constrain the types of values that can be captured in these SPO attributes, and may define any number of specialized qualifier attributes that extend the SPO "triple" with additional detail or context.  For example, if an SPO triple asserts that *"NM_005343.4:c.173C>T is causal for Costello Syndrome"*, a ``geneContextQualifier`` can be used to indicate that its effect on the HRAS gene mediates this causal relationship, and an ``alleleOriginQualifier`` can be used to indicate that the fact holds specifically for variants of 'germline' origin:

.. code-block:: yaml

  # Note that values in this example are reported in shorthand form for human readability.
  # In actual VA-Spec data, many values would be wrapped in complex data type structures such as MappabeConcepts.

  subject: NM_005343.4:c.173C>T
  predicate: isCausalFor
  object: Costello Syndrome
  geneContextQualifier: HRAS
  alleleOriginQualifier: germline



-----

**2. Proposition Utility:**

A proposition itself makes no claim as to whether the sentiment it expresses is true or not - its job is simply to convey the sharable meaning of a possible fact in a structured data object. Such propositions can then be referenced and reused by **Statements** and **Evidence Lines**, which make assertions about them. Specifically:

 - **Statements** may report that a proposition was asserted by a particular agent to be true or false, or may report the overall strength of confidence or evidence supporting or disputing a proposition for which a definitive assertion cannot yet be made. Such Statements are based on the agent's interpretation of evidence as providing discrete argument(s) for or against the proposition.
 - **Evidence Lines** are used to represent each such discrete evidence-based argument. They report that a particular collection of  information (evidence items) was assessed and scored as evidence to support or dispute some target proposition.  It is typically through the assessment of several distinct Evidence Lines that a particular Proposition is ultimately asserted to be true or false in a Statement.

-----

.. _proposition-utility-example:

**3. Proposition Example**

Variant pathogenicity classifications based on the 2015 ACMG Interpretation guidelines are a nice example of how a single proposition such as *"NM_005343.4:c.173C>T is causal for Costello Syndrome"* can be used in Evidence Lines and Statements. This proposition may first be used as a **target** against which data is interpreted to build Evidence Lines, according to specific evaluation criteria (e.g. PM2 for allele frequency data, PM1 for functional impact data). As Evidence Lines supporting this proposition accumulate, it may subsequently be used in a **Statement** where it is asserted as true to classify the variant as 'pathogenic'.

The example below illustrates how such a scenario may be represented using the VA-Spec - illustrating the use of the same ``Proposition001`` in two Evidence Lines and a Variant Pathogenicity Statement.

.. code-block:: yaml

 # Note that values in this example are reported in shorthand form for human readability.
 # In actual VA-Spec data, many values would be wrapped in complex data type structures such as MappabeConcepts.

   # As a target proposition in an EvidenceLine based on functional impact data, created at t0 by Curator 1
   id: EvidenceLine001
   type: EvidenceLine
   targetProposition:
     - id: VarPathProposition001
       type: VariantPathogenicityProposition
       subjectVariant: NM_005343.4:c.173C>T:c.173C>T
       predicate: isCausalFor
       objectConditon: Costello Syndrome
       geneContextQualifier: HRAS
   evidenceItems: FunctionalImpactStudyResult001       # full StudyResult object omitted for space
   directionOfEvidenceProvided: supports
   strengthOfEvidenceProvided: moderate
   specifiedBy: PM1

   # As a target proposition in an EvidenceLine based on cohort allele frequency data, created at t1 by Curator 2
   id: EvidenceLine002
   type: EvidenceLine
   targetProposition: VarPathProposition001    # no need to duplicate an inlined representation, as this Proposition is already defiend in the message.
   evidenceItems: AlleleCohortFrequencyStudyResult001   # full StudyResult object omitted for space
   directionOfEvidenceProvided: supports
   strengthOfEvidenceProvided: moderate
   specifiedBy: PM2

   # As an asserted proposition in a VariantPathogenicityStatement, created at t2 by Curator 3 who puts forth the proposition as true and classifies the variant as 'pathogenic' based on the Evidence Lines above
   id: Statement001
   type: Statement
   proposition: VarPathProposition001          # no need to duplicate an inlined representation, as this Proposition is already defiend in the message.
   direction: supports
   strength: definitive
   classification: pathogenic
   hasEvidenceLines
     - EvidenceLine001
     - EvidenceLine002
   specifiedBy: 2015 ACMG Variant Interpretation Guidelines

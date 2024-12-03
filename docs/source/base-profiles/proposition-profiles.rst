.. _proposition-profiles:

Proposition Profiles
!!!!!!!!!!!!!!!!!!!!

**Proposition Utility**
	
Propositions are abstract representations of possible facts about a domain of discourse, e.g. *"HRAS:c.173C>T causes Costello Syndrome"*.  A proposition itself makes no claim as to whether the sentiment it expresses is true or not - its job is simply to convey the sharable meaning of a possible fact in a structured data object.  

Such propositions can then be referenced and reused by **Statements** and **Evidence Lines**, which make assertions about them. Specifically:

 - **Statements** may report that a proposition was asserted by a particular agent to be true or false, or may report the overall strength of confidence or evidence supporting or disputing a proposition for which a definitive assertion cannot yet be made. Such Statements are based on the agent's interpretation of evidence as providing discrete argument(s) for or against the proposition. 
 - **Evidence Lines** are used to represent each such discrete evidence-based argument. They report that a particular collection of  information (evidence items) was assessed and scored as evidence to support or dispute some target proposition.  It is typically through the assessment of several distinct Evidence Lines that a particular Proposition is ultimately asserted to be true or false in a Statement. 

Variant pathogenicity classifications based on the 2015 ACMG Interpretation guidelines are a nice example of how a single proposition such as *"HRAS:c.173C>T is causal for Costello Syndrome"* can be used in Evidence Lines and Statements. This proposition may first be used as a **target** against which data is interpreted to build Evidence Lines, according to specific evaluation criteria (e.g. PM2 for allele frequency data, PM1 for functional impact data). As Evidence Lines supporting this proposition accumulate, it may subsequently be used in a **Statement** where it is asserted as true to classify the variant as 'pathogenic'.

The structured example below illustrates how such a scenario may be represented using the VA-Spec (note that values are provided in shorthand syntax for human redability, and are not fully VA-Spec compliant). 

.. code-block:: yaml

 # Use of a proposition in Evidence Lines and a Variant Pathogenicity Statement 

   # As a target proposition in an EvidenceLine based on functional impact data, created at t0 by curator X
   id: EvidenceLine001
   type: EvidenceLine
   targetProposition:
     - id: VarPathProposition001
       type: VariantPathogenicityProposition
       subjectVariant: HRAS:c.173C>T
       predicate: isCausalFor
       objectConditon: Costello Syndrome
   evidenceItems:
     - id: FunctionalImpactStudyResult001     # strudy result details omitted for space
   directionOfEvidenceProvided: supports
   strengthOfEvidenceProvided: moderate
   specifiedBy: PM1

   # As a target proposition in an EvidenceLine based on cohort allele frequency data, created at t1 by curator Y
   id: EvidenceLine002
   type: EvidenceLine
   targetProposition:
     - id: VarPathProposition001
       type: VariantPathogenicityProposition
       subjectVariant: HRAS:c.173C>T
       predicate: isCausalFor
       objectConditon: Costello Syndrome
   evidenceItems:
     - id:alleleCohortFrequencyStudyResult001     # study result details omitted for space
   directionOfEvidenceProvided: supports
   strengthOfEvidenceProvided: moderate
   specifiedBy: PM2

   # As an asserted proposition in a VariantPathogenicityStatement, created at t2 by curator Z who puts forth the proposition as true and classifies the variant as 'pathogenic' based on the Evidence Lines above
   id: Statement001
   type: Statement
   proposition:
     - id: VarPathProposition001
       type: VariantPathogenicityProposition
       subjectVariant: HRAS:c.173C>T
       predicate: isCausalFor
       objectConditon: Costello Syndrome
   direction: supports
   strength: definitive
   classification: pathogenic
   hasEvidenceLines
     - EvidenceLine001
     - EvidenceLine002
   specifiedBy: 2015 ACMG Variant Interpretation Guidelines
	
**Proposition Profiles**
	
Proposition Profiles are defined as specializations of the core ``Proposition`` class, to explicitly represent particular types of possible facts that may be true in a domain of discourse. In the example abpve, a ``VariantPathogenicityProposition`` profile defines a model for describing causal relationships between genetic variants and specific diseases. Providing explicit and detailed representations of such propositions is critical for reporting and understanding exactly what a VA ``Statement`` may assert, or a VA ``Evidence Line`` may assess and score evidence against. 

The semantics of a Proposition are captured in ``subject``, ``predicate``, ``object``, and optional ``qualifier`` attributes (SPOQ). Proposition profiles constrain the types of values that can be captured in these SPO attributes, and may define any number of specialized qualifier attributes that extend the SPO "triple" with additional detail or context.  For example, if an SPO triple asserts that *"VariantX - is causal for - DiseaseY"*, a ``geneContextQualifier`` can be used to indicate a specific GeenZ as mediating this causal relationship, and an ``alleleOriginQualifier`` can be used to indicate that the fact holds specifically for variants of germline origin:

.. code-block:: yaml

  subject: VariantX
  predicate: isCausalFor
  object: DiseaseY
  geneContextQualifier: GeneZ
  alleleOriginQualifier: germline
	
Proposition profiles defined in this way are used within the context of generic ``Statement`` or ``EvidenceLine`` classes from the core model, to provide domain specific semantics for the respective assessments that these core classes provide. This avoids the need to profile/specialize ``Statement`` or ``EvidenceLine`` classes for many use cases.  However, these classes may be profiled as needed to add community specific constraints on direct attributes of the Statement or Evidence Line classes (see :ref: `Community Profiles <community-profiles>`).

---------

Below are the **Base Proposition Profiles** currently defined as part of the VA-Spec, and available for adoption or extension by Driver Project implementations. **JSON Schema** for each Profile can be found `here <https://github.com/ga4gh/va-spec/tree/mbrush-ballot-doc-proposition-updates/schema/va-spec/base/json>`_. 

.. _variant-pathogenicity-proposition-profile:

Variant Pathogenicity Proposition
#################################

.. include::  ../def/va-spec/VariantPathogenicityProposition.rst

Variant Oncogenicity Proposition
#################################

.. include::  ../def/va-spec/VariantOncogenicityStudyProposition.rst

Variant Therapeutic Response Proposition
########################################

.. include::  ../def/va-spec/VariantTherapeuticResponseStudyProposition.rst

.. _variant-diagnostic-statement-profile:

Variant Diagnostic Proposition
##############################

.. include::  ../def/va-spec/VariantDiagnosticStudyProposition.rst

Variant Prognostic Proposition
##############################

.. include::  ../def/va-spec/VariantPrognosticStudyProposition.rst


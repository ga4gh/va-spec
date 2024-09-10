.. _Statement:

Statement
!!!!!!!!!


.. include::  ../../../../../schema/core-im/def/Statement.rst



Implementation Guidance
#######################

**Statement:**

 * Statement objects are used to report primary assertions of knowledge at the core of a Varaint Annotation, along with evidence and provenance information. Every Statement puts forth a 'proposition' - a possible fact it assesses or reports to be true.  The semantics of this proposition are explicitly captured using 'subject', 'predicate', and 'object' attributes, and optional 'qualifier' slot(s).
 * The model supports two "modes of use" for Statements, which differ in what they say about their proposition, and can be distinguished by whether 'direction' and 'strength' or 'score' attributes are populated. 
 * In **"Assertion Mode"** a Statement simply reports an SPOQ proposition to be true (e.g. that "BRCA2 c.8023A>G is pathogenic for Breast Cancer"), and 'direction', 'strength', and 'score' attributes are not populated.  Thos mode is used by project reporting conclusive assertions about a domain of discourse, but not providing confidence or evidence level assessments.
 * In **"Proposition Assessment Mode"** a Statement describes the overall state of evidence and/or confidence surrounding the SPOQ proposition - which may or may not be true. The 'direction' and 'strength' or 'score' attributes are populated, which allows for Statements to report that "there is very strong evidence supporting the proposition that 'BRCA2 c.8023A>G is pathogenic for Breast Cancer'", or "we have high confidence that the proposition 'BRCA2 c.8023A>G is pathogenic for Breast Cancer' is false").  This mode is used in curation projects to track the evolving state of support for propositions of interest, as curators continue to collect evidence and work toward a conclusive assertion.   

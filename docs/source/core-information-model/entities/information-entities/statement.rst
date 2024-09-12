.. _Statement:

Statement
!!!!!!!!!


.. include::  ../../../../../schema/core-im/def/Statement.rst



**Implementation Guidance**

Statements put forth a Proposition that expresses some possible fact about the world, and may provide an assessment of this proposition's validity (i.e. how likely it is to be true or false based on evaluated evidence). The semantics of the Proposition are captured in the ``subject``, ``predicate``, ``object``, and optional ``qualifier`` attributes. An assessment of the Proposition's  validity can be captured using ``direction``, ``strength``, and ``score`` attributes. 

* The ``direction`` attribute is used to indicate whether the Statement's Proposition is **supported** by the agent's assessment (when evidence favors its validity), is **disputed** by the agent's assessment (when evidence argues against its validity), or remains **neutral** (when conflicting or insufficient evidence exists to assert one direction or the other). (Enumerated values = 'supports', 'disputes', 'neutral').

* The ``strength`` attribute is used to report the strength of this assessment in the direction indicated. Strength can be framed as a **level of confidence** that the Proposition is true or false, or as a **level of evidence** that supports or disputes it. Data creators can define the permissible values for the ``strength`` attribute to indicate which of these facets is being assessed (e.g. 'high confidence' vs 'low confidence', or 'strong evidence' vs 'weak evidence') - or they can choose values that don't commit to one or the other if they don't want to make the distinction (e.g. 'high' vs 'medium' vs 'low').

* The ``score`` attribute serves the same purpose as 'strength', but allows for a quantitative assessment based on a numerical score.


The model supports two "modes of use" for Statements, which differ in what they say about their proposition, and can be distinguished by whether ``direction`` and ``strength`` or ``score`` attributes are populated. 

* In **"Assertion Mode"** a Statement simply reports an SPOQ proposition to be true (e.g. that "BRCA2 c.8023A>G is pathogenic for Breast Cancer"), and ``direction``, ``strength``, and ``score`` attributes are not populated.  This mode is used by project reporting conclusive assertions about a domain of discourse, but not providing confidence or evidence level assessments.

* In **"Proposition Assessment Mode"** a Statement describes the overall state of evidence and/or confidence surrounding the SPOQ proposition - which may or may not be true. The ``direction`` and ``strength`` or ``score`` attributes are populated, which allows for Statements to report that "there is very strong evidence supporting the proposition that 'BRCA2 c.8023A>G is pathogenic for Breast Cancer'", or "we have high confidence that the proposition 'BRCA2 c.8023A>G is pathogenic for Breast Cancer' is false").  This mode is used in curation projects to track the evolving state of support for propositions of interest, as curators continue to collect evidence and work toward a conclusive assertion.   

.. _custom-variant-pathogenicity-statement-example:

Custom Variant Pathogenicity Statement Example
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

**Building Custom Statement Models:**
  
* Representation of a particular type of **Statement** or **Evidence Line** using the VA-Spec does not always require a Profile to be specifically defined for it.
* The :ref:`Statement and Evidence Line Community Profiles <community-profiles>` included in version 1.0 of the VA-Spec are there to support data providers pusuing strict alignment with a particular community guidelines.
* Implementers who do not seek such alignment can build their own schema for Statements or Evidence Lines to report on any of the knowledge types specified in VA :ref:`Base Proposition profiles<proposition-profiles>`.
* For example, starting with the core Statement<Statement> class, simply bind its ``proposition`` attribute to the relevant Proposition base profile, and the permissive core Statement attributes will not impose community-specific constraints around representation of additional information about the Statement (e.g. strength, provenance, source documents, etc).
  
**Example Description:**

 * The example below represents the same ClinVar-based Variant Pathogenicity Statement as in this `simple test fixtures example <https://github.com/ga4gh/va-spec/blob/1.0.0-ballot.2025-03/tests/fixtures/VA-ClinVar-SCV-Example-001.yaml>`_, but does not coform to the :ref:`ACMG 2015 Community Profile<variant-pathogenicity-statement-acmg-2015>` for this statement type. 
 * Instead, the schema uses the core :ref:`Statement<Statement>` class with in a base :ref:`Variant Pathogenicity Proposition <variant-pathogenicity-proposition>`, and the looser constraints on the core class to allow use of the implementers preferred vocabularies for capturing things like Statement ``strength`` and ``classification``. 
 * Annotations in the example point out where the implementers preferred codes are used instead of ACMG-based terms. 

**Data**:

.. code-block:: yaml

 SCV000778434.1:
  id: SCV000778434.1
  type: Statement               
  proposition:                 # a Proposition object captures the possible fact assessed by the Statement, using a subject, predicate, object, qualifier (SPOQ) semantic modeling pattern.
    id: ex:Proposition001      # the proposition here is that "NM_004700.4:c.803CCT[1] is causal for AD nonsyndromic hearing loss 2A"
    type: VariantPathogenicityProposition 
    subjectVariant: clinvar/208366    # 'subjectVariant' specializes the VA Core 'subject' attribute, and holds a CatVRS 'Categorical Variant' whose full representtion is not shown here. 
    predicate: isCausalFor     # the predicate for this Statement profile is fixed at 'isCausalFor' 
    objectCondition:           # 'objectCondition' specialilzes the VA Core 'object' attribute.
      id: clinvar.trait/939    # this is a MappableConcept object that represents the Condition, using names/codes from existing code systems
      conceptType: Disease
      name: Autosomal dominant nonsyndromic hearing loss 2A    # the name for the concept as assigned by the data provider
      primaryCoding:           # holds a Coding object, where the concept is defined in the 'code' or 'name' field  
        code: C2677637         # the code from the MedGen terminology for AD nonsyndromic hearing loss 2A
        system: https://www.ncbi.nlm.nih.gov/medgen/
        iris:
          - http://identifiers.org/medgen/C2677637
    penetranceQualifier:       # holds a MappableConcept that reports qualifying penetrance information about the object condition (here, that the statement holds for high penetrance AD hearing loss)
      primaryCoding:
        code: high 
        system: ga4gh-gks-term:pathogenicity-penetrance-qualifier   # code system here is a locally defined placeholder, until we formalize terminological standards for use in the VA-Spec 
      name: high
  direction: supports          # an enumerated string that indicates the Statement 'supports' the Proposition as true
  strength:                    # holds a MappableConcept reporting that confidence/evidence for this stated support
    primaryCoding:
      code: established        # the code here based on a term used in the implementers preferred guidelines or application (as opposed to ACMG terminolgoical conventions)  
      system: Implementer System 1
  classification:              # holds a MappableConcept reporting the final classification of the subject variant to be 'disease-causing'     
    primaryCoding:
      code: disease-causing    # the code here based on a term used in the implementers preferred guidelines or application (as opposed to ACMG terminolgoical conventions) 
      system: ACMG Guidelines, 2015
  contributions:               # a list of Contribution objects, each describing how an agent contributed to the Statement
    - type: Contribution
      contributor:             # reports who made this contribution
        id: clinvar.submitter/500139
        type: Agent
        name: ClinVar Staff, National Center for Biotechnology Information (NCBI)
      activityType:            # reports the type of contribution that was made (here an evaluation activity)
        name: evaluated
      date: '2015-08-20'       # reports when this contribution was performed     
    - type: Contribution
      contributor:
        id: clinvar.submitter/500139
        type: Agent
        name: ClinVar Staff, National Center for Biotechnology Information (NCBI)
      activityType:
        name: submitted
      date: '2018-06-12'
  specifiedBy:                 # holds a Method object describing the implementers guidelines and terminology for recording the knowledge reported in the Statement 
    type: Method
    reportedIn:                # a document that describes the Method (this is all we are given about this Method in the source data)
      type: Document
      name: Alternate Guidelines and Terminology for Variant Pathogenicity Classification

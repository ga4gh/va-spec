.. _variant-pathogenicity-statement-simple:

Variant Pathogenicity Statement, Simple
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

**Description:**

* The Pathogenicity Statement data below adds instructive annotations to this `simple test fixtures example <https://github.com/ga4gh/va-spec/blob/1.0.0-ballot.2025-03/tests/fixtures/VA-ClinVar-SCV-Example-001.yaml>`_ from ClinGen's "ClinVar-GKS" implementation of the :ref:`Variant Pathogenicity Statement (ACMG 2015) Profile <variant-pathogenicity-statement-acmg-2015>`.
* The annotations are intended to help readers better understand the structure, semantics, and utility of VA-Spec models.
* The example itself covers a subset of data from the `ClinVar SCV000778434.1 record <https://www.ncbi.nlm.nih.gov/clinvar/RCV000656422.10/>`_ - which reports that *"the KCNQ4 variant NM_004700.4:c.803CCT[1] is pathogenic for Autosomal dominant nonsyndromic hearing loss 2A"*. 
* Note that it omits full representations of the ``CategoricalVariation`` that is the subject of the Statement - as this is a large structure that is the remit of the `CatVRS specification <https://github.com/ga4gh/cat-vrs>`_.

**Data**:

.. code-block:: yaml

 SCV000778434.1:
  id: SCV000778434.1
  type: Statement              # Formal type in the model is 'Statement', but the data aligns with the "Variant Pathogenicity Statement (ACMG 2015)" Community Profile.  
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
      code: definitive         # the code here is a term based on language used in the ACMG guidleines, as ACMG does not provide a formal code system for this 
      system: ACMG Guidelines, 2015
  classification:              # holds a MappableConcept reporting the final ACMG classification of the subject variant  to be 'pathogneic'      
    primaryCoding:
      code: pathogenic         # the code here is a term based on language in the ACMG guidelines, as ACMG does not provide a formal code system for this 
      system: ACMG Guidelines, 2015
  contributions:               # a list of Contribution objects, each describing how an agent contributed to the Statement
    - type: Contribution
      contributor:             # reports who made this contribution
        id: clinvar.submitter/500139
        type: Agent
        name: ClinVar Staff, National Center for Biotechnology Information (NCBI)
      activityType:            # reports the type of contribution that was made (here an evaluation activity)
        name: evaluated
        mappings:
          - coding:
              code: cg000011
              system: https://dataexchange.clinicalgenome.org/codes/
            relation: exactMatch
      date: '2015-08-20'       # reports when this contribution was performed     
    - type: Contribution
      contributor:
        id: clinvar.submitter/500139
        type: Agent
        name: ClinVar Staff, National Center for Biotechnology Information (NCBI)
      activityType:
        name: submitted
        mappings:
          - coding:
              code: cg000010
              system: https://dataexchange.clinicalgenome.org/codes/
            relation: exactMatch
      date: '2018-06-12'
  specifiedBy:                 # holds a Method object describing guidelines followed in generating the knowledge reported in the Statement 
    type: Method
    reportedIn:                # a document that describes the Method (this is all we are given about this Method in the source data)
      type: Document
      pmid: 25741868
      name: ACMG Guidelines, 2015

.. _acmg-variant-pathogenicity-statement-example-with-evidence:

ACMG Variant Pathogenicity Statement Example (with Evidence)
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

**Description:**

The data below builds on the simple ClinVar-GKM example described :ref:`here <acmg-variant-pathogenicity-statement-example>`, embellishing its base ClinVar record with additional evidence to demonstrate richer structures the :ref:`Variant Pathogenicity Statement (ACMG 2015) profile <variant-pathogenicity-statement-acmg-2015>` can support.

Specifically, it stitches together several simpler **Statement**, **Study Result**, and **Evidence Line** data examples from the `test fixtures directory <https://github.com/ga4gh/va-spec/tree/1.0.0/tests/fixtures>`_, to reveal how these objects can be combined to build the rich evidence and provenance structure below.

.. variant-pathogenicity-statement-with-evidence:

.. figure:: ../images/variant-pathogenicity-statement-with-evidence.png

   High Level Structure of the Data Example

   **Legend**: A root Pathogenicity Statement is supported by Evidence Lines based on a Cohort Allele Frequency Study Result from `gnomAD <https://gnomad.broadinstitute.org/>`_, and a Functional Impact Statement from `MAVE DB <https://mavedb.org/>`_, which itself is supported by a Functional Impact Study Result. Boxes represent objects comprising the central axis of the data, with italicized text indicating what each object reports to be true.

Such structures can represent the full details of how evidence is interpreted to build up support for higher order assertions of variant knowledge  - e.g. here how functional data from a study result supports a study-specific
conclusion about the functional impact of a variant, which is interpreted as 'strong' evidence 'supporting' for the variant's possible pathogenicity, and assessed as one argument supporting an ACMG-based pathogenicity
classification of the variant.

A few additional notes about this example:

* Comments in the yaml are provided to help readers better understand the structure, semantics, and utility of the data in the example.
* Some identifiers not present in the source test fixture data were created for purposes of identifying and cross-referencing objects in this aggregate example (these are all prefixed with the string 'ex:').
* Note that the variant subject of each Statement and Study Result objects is reported as the same, generic variation for simplicity (ex:Variant001). In reality these objects may describe subtly different variants that all map to each other in some way (e.g. a protein-level variant in the Functional Impact objects, a genomic-level variant in the Allele Frequency objects, and a Categorical Variant that covers both of these contextual variants in the Pathogenicity Statement and its direct Evidence Lines). Nuances around how variant subjects of Statements and those described by supporting evidence is a separate and complex topic addressed :ref:`here <variant-congruence>`.
* The example omits full representations of these `VRS <https://github.com/ga4gh/vrs>`_ and `CatVRS <https://github.com/ga4gh/cat-vrs>`_ Variation objects - as these are large structures that are the remit of other GKM Specifications.

**Data**:

.. note:: Comments in the example below will be easier to view in the |acmg_pathogenicity_statement_with_evidence_example_source_yaml|, which affords the option of a wider browser window.
   We recommend opening this example side-by-side with the figure above, and tracking how the data reflects the diagrammed structure and semantics.

.. code-block:: yaml

 ex.Statement001:              # Based on the ClinVar record SCV000778434.1
  id: ex:Statement001
  type: Statement              # Formal type in the model is 'Statement', but the data aligns with the "Variant Pathogenicity Statement (ACMG 2015)" Community Profile.
  proposition:                 # a Proposition object captures the possible fact assessed by the Statement, using a subject, predicate, object, qualifier (SPOQ) semantic modeling pattern.
    id: ex:Proposition001      # the proposition here is that "NM_004700.4:c.803CCT[1] is causal for AD nonsyndromic hearing loss 2A"
    type: VariantPathogenicityProposition
    subject: ex:Variant001    # the 'subject' of the Proposition, narrowed to a variant. The full representation of the NM_004700.4:c.803CCT[1] KCNQ4 variant is not included.
    predicate: isCausalFor           # the predicate for this Statement profile is fixed at 'isCausalFor'
    object:                 # the 'object' of the Proposition, narrowed to a Condition.
      id: clinvar.trait/939    # this is a MappableConcept object that represents the Condition, using names/codes from existing code systems
      type: MappableConcept
      conceptType: Disease
      name: Autosomal dominant nonsyndromic hearing loss 2A    # the name for the concept as assigned by the data provider
      primaryCoding:           # holds a Coding object, where the concept is defined in the 'code' or 'name' field
        code: C2677637         # the code from the MedGen terminology for AD nonsyndromic hearing loss 2A
        system: https://www.ncbi.nlm.nih.gov/medgen/
        iris:
          - http://identifiers.org/medgen/C2677637
    penetranceQualifier:       # holds a MappableConcept that reports qualifying penetrance information about the object condition (here, that the statement holds for high penetrance AD hearing loss)
      type: MappableConcept
      primaryCoding:
        code: high
        system: ga4gh-gkm-term:pathogenicity-penetrance-qualifier   # code system here is a locally defined placeholder, until we formalize terminological standards for use in the VA-Spec
      name: high
  direction: supports          # an enumerated string that indicates the Statement 'supports' the Proposition as true
  strength:                    # holds a MappableConcept reporting that confidence/evidence for this stated support
    type: MappableConcept
    primaryCoding:
      code: definitive         # the code here is a term based on language used in the ACMG guidelines, as ACMG does not provide a formal code system for this
      system: ACMG Guidelines, 2015
  outcome:                      # holds a MappableConcept reporting the final ACMG classification of the subject variant  to be 'pathogenic'
    type: MappableConcept
    primaryCoding:
      code: pathogenic         # the code here is a term based on language in the ACMG guidelines, as ACMG does not provide a formal code system for this
      system: ACMG Guidelines, 2015
  contributions:               # a list of Contribution objects, each describing how an agent contributed to the Statement
    - type: Contribution
      contributor:             # reports who made this contribution
        id: clinvar.submitter/500139
        type: Agent
        name: ClinVar Staff, National Center for Biotechnology Information (NCBI)
      activityType: evaluated  # a string naming the type of contribution that was made (here an evaluation activity)
      date: '2015-08-20'       # reports when this contribution was performed
    - type: Contribution
      contributor:
        id: clinvar.submitter/500139
        type: Agent
        name: ClinVar Staff, National Center for Biotechnology Information (NCBI)
      activityType: submitted
      date: '2018-06-12'
  specifiedBy:                 # holds a Method object describing guidelines followed in generating the knowledge reported in the Statement
    type: Method
    name: ClinGen Hearing Loss Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines
    reportedIn:                # a document that describes the Method
      type: Document
      urls:
        - https://clinicalgenome.org/docs/clingen-hearing-loss-expert-panel-specifications-to-the-acmg-amp-variant-interpretation-guidelines/
  hasEvidenceLines:            # holds EvidenceLine objects describing how difference types of evidence was interpreted to support the root Statement
  - id: ex:EvidenceLine001     # an Evidence Line based on cohort allele frequency data from gnomAD (https://gnomad.broadinstitute.org/)
    type: Statement            # uses the core Statement class as its type, but validated against the VariantPathogenicityEvidenceLine Profile
    proposition: ex:Proposition001     # the possible fact against which evidence information is assessed in this EvidenceLine (typically, as here, this is the same proposition as asserted in the root Statement it supports)
    hasEvidenceItems:          # the information interpreted as evidence in building this Evidence Line
    - id: ex:StudyResult001    # here, the evidence consists of a single StudyResult, which collects several allele frequency data items about the 1-10120-T-G allele.
      type: CohortAlleleFrequencyStudyResult
      name: Overall Cohort Allele Frequency for 1-40819444_40819446-del
      focus: ex:Variant001  # the KCNQ4 variant that data included in this Result are about (the full representation of the variant is not included)
      alleleFrequency: 0
      focusCount: 0      # three specific data items produced by the analysis are collected in this StudyResult (focus allele frequency, focus allele count, and locus allele count)
      locusCount: 34086
      sourceDataSet:           # the gnomAD dataset from which the data included in this Result were pulled.
        id: gnomad4.1.0
        type: DataSet
        name: gnomAD v4.1.0
        version: 4.1.0
      cohort:                  # a description of the cohort within the gnomad dataset interrogated in the analysis (here, the full gnomad population)
        id: ALL
        name: Overall
        type: StudyGroup
      specifiedBy:             # holds a Method object describing protocols and guidelines followed in generating the data reported in the Study Result
        type: Method
        name: gnomAD methods
        reportedIn:            # a document that describes the Method (this is all we are given about this Method in the source data)
          type: Document
          name: gnomAD help documentation
          urls:
            - "https://gnomad.broadinstitute.org/help"
    direction: supports   # reports that the frequency evidence 'supports' the target proposition (as opposed to disputing it)
    strength:
      type: MappableConcept
      primaryCoding:
        code: moderate        # reports that this supporting evidence is of 'moderate' strength
        system: ACMG Guidelines, 2015
    outcome:          # holds a single term summarizing evidence direction and strength assessments, using community-specific vocabulary ...
      type: MappableConcept
      primaryCoding:
        code: PM2             # ... here, that the ACMG PM2 criterion was met. Because PM2 was met at its default 'moderate' strength,
        system: ACMG Guidelines, 2015    # the bare criterion code is used (a code like 'PM2_supporting' would signal an adjusted strength,
      name: ACMG 2015 PM2 Criterion Met  # and 'PM2_not_met' that the criterion was assessed but not met).
    specifiedBy:              # holds a Method object describing guidelines followed in generating the evidence assessment in this Evidence Line
      type: Method
      methodType: population_data_assessment   # names the kind of evidence assessed; constrains which ACMG codes the 'outcome' may use
      name: ClinGen Hearing Loss Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines
      reportedIn:             # a document that describes the Method (this is all we are given about this Method in the source data)
        type: Document
        urls:
          - https://clinicalgenome.org/docs/clingen-hearing-loss-expert-panel-specifications-to-the-acmg-amp-variant-interpretation-guidelines/
    contributions:            # holds descriptions of contributions to this Evidence Line
      - type: Contribution
        contributor:
          id: curator001
          type: Agent
        activityType: evidence evaluation
        date: '2018-03-11'
  - id: ex:EvidenceLine002               # an Evidence Line based on functional impact data about the variant from MAVE (https://mavedb.org/)
    type: Statement                      # uses the core Statement class as its type, but validated against the VariantPathogenicityEvidenceLine Profile
    proposition: ex:Proposition001
    hasEvidenceItems:
      - id: ex:Statement002              # here the evidence item is another Statement about the functional impact of the variant
        type: Statement
        proposition:
          type: ExperimentalVariantFunctionalImpactProposition
          subject: ex:Variant001  # the full representation of the variant subject of this Statement is not included
          predicate: impactsFunctionOf   # the predicate for this type of Statement is fixed at 'impactsFunctionOf'
          object:         # holds a MappableConcept object that represents the Gene impacted by the variant, using names/codes from existing code systems
            id: clinvar-gene:9132
            type: MappableConcept
            conceptType: Gene
            primaryCoding:
              code: ncbigene:9132
              system: https://identifiers.org/ncbigene
              iris:
                - https://identifiers.org/ncbigene:9132
            name: KCNQ4
          experimentalContextQualifier:      # this qualifier is able to take a custom, data provider-defined object to describe the experiment in which the reported impact was determined. A condensed example is shown here, but an real and complete example can be found in the Exp-Var-Func-Impact-Statement-01.yaml test fixtures file.
            title: KCNQ4 VAMP Seq Expt 001
            description: Multiplex assessment of KCNQ4 protein variant abundance by massively parallel sequencing
            phenotypicAssay: flow cytometry
            modelSystem: immortalized human cells
            variantLibrarySystem: oligo-directed mutagenic PCR
            profilingStrategy: barcode sequencing
            sequencingReadType: single-segment (short read)
        direction: supports           # indicates that the Statement supports the assessed impact Proposition above (i.e. says that the subject Variant does impact the function of the object Gene)
        outcome:                      # summarizes the Statement in terms of a final classification of the variant, using a term familiar in the community of use.
          type: MappableConcept
          primaryCoding:
            code: abnormal            # indicates the variant version of the gene has abnormal function (consistent with the 'impactsFunctionOf' proposition being 'supported')
            system: ga4gh-gkm-term:experimental-var-func-impact-classification
        specifiedBy:                  # a Method followed to produce the Statement, which is described by the publication indicated below
          type: Method
          methodType: variant interpretation guideline   # 'methodType' is a plain string
          reportedIn:
            type: Document
            pmid: '29785012'
        hasEvidenceLines:
        - id: EvidenceLine003
          type: Statement
          direction: supports  # indicates that EvidenceLine003 based on a Functional Impact Study Result 'supports' the Functional Impact Statement
          specifiedBy:          # a Method followed in assessing the direction and strength of evidence provided by the Functional Impact StudyResult for the Functional Impact Statement
            type: Method
            name: MAVE bayesian threshold probability method 001
            reportedIn:
              type: Document
              urls:
                - "https://mavedb.org/score-sets/urn:mavedb:00000013-a-1"
          hasEvidenceItems:             # a Study Result that captures the experimental data and scores on which the Functional Impact Statement was based.
            - id: ex:StudyResult002     # the evidence in this case is data captured in a Functional Impact Study Result
              type: ExperimentalVariantFunctionalImpactStudyResult
              focus: ex:Variant001   # the KCNQ4 variant that data are about (a full representation of the variant is not included)
              functionalImpactScore: 1.29395467005388        # this is the only data item included right now in this StudyResult
              specifiedBy:
                type: Method
                methodType: Experimental protocol
                reportedIn:
                  type: Document
                  pmid: '29785012'
              sourceDataSet:
                type: DataSet
                name: variant effect data set
                license:
                  type: MappableConcept
                  primaryCoding:
                    code: CC0
                    system: https://spdx.org/licenses/
                    iris:
                      - https://spdx.org/licenses/CC0-1.0.html
                reportedIn:
                  type: Document
                  urls:
                    - "https://mavedb.org/score-sets/urn:mavedb:00000013-a-1"
    direction: supports   # indicates that EvidenceLine002 based on a Functional Impact Statement 'supports' the root Pathogenicity Statement
    strength:
      type: MappableConcept
      primaryCoding:
        code: strong                      # indicates that this line of evidence provides 'strong' support for the variant's Pathogencity
        system: ACMG Guidelines, 2015
    outcome:
      type: MappableConcept
      primaryCoding:
        code: PS3                         # the ACMG PS3 criterion was met at its default 'strong' strength
        system: ACMG Guidelines, 2015
      name: ACMG 2015 PS3 Criterion Met
    specifiedBy:          # holds a Method object describing guidelines followed in assessing the evidence provided by the Functional Impact Statement for the root Pathogenicity Statement
      type: Method
      methodType: functional_data_assessment
      name: ClinGen Hearing Loss Expert Panel Specifications to the ACMG/AMP Variant Interpretation Guidelines
      reportedIn:
        type: Document
        urls:
          - https://clinicalgenome.org/docs/clingen-hearing-loss-expert-panel-specifications-to-the-acmg-amp-variant-interpretation-guidelines/
    contributions:
      - type: Contribution
        contributor:
          id: curator002       # the curator who assessed functional impact statement as evidence for pathogenicity
          type: Agent
        activityType: evidence evaluation
        date: '2018-04-03'
  extensions:      # holds Extension objects which allow data providers to define key-value pairs for capturing additional info not supported by the VA model.
  - name: clinvarMethodCategory   # here, Extensions are used to report clinvar-specific values that the data provider does not want to lose
    value: literature only
  - name: clinvarReviewStatus
    value: no assertion criteria provided
  - name: clinvarSubmittedClassification
    value: Pathogenic

------

.. _acmg-variant-pathogenicity-statement-example-with-evidence-diagram:

**Detailed Diagram**:

The diagram shows a subset of data from the full json example. It provides a more detailed data structure overview that highlights encapsulation of **Propositions** in **Statements** and **Evidence Lines** and the use of the same set of Core Model classes (**Method**, **Document**, **Contribution**, **Agent**) to capture provenance information about all primary knowledge artifacts.

It also highlights the kind of schema that specifies each objects in the data - illustrating how **Core Model Classes**, **Base Profiles**, and **Community Profiles**  that rely on :ref:`different authoring mechanisms <profile-definition-mechanisms>` are used together in a structured data representation.

.. raw:: html

   <iframe src="../_static/diagrams/acmg-statement-with-evidence-example.html" style="width:100%; height:760px; border:0;" title="Detailed Data Example"></iframe>

**Legend**: Diagrammatic representation of this same general structure -- a root Statement, its first Evidence Line, and that Evidence Line's Study Result -- populated with a different real ClinGen classification (see the diagram's own caption) rather than the json example above, to keep this page anchored to two independently-sourced real examples instead of one. Each box's class name is the specific profile class actually used (``VariantPathogenicityStatement``, ``VariantPathogenicityEvidenceLine``, ``CohortAlleleFrequencyStudyResult``), with its formal base class as a ``«...»`` stereotype above the name. The root Statement (solid box) and the Evidence Line (dashed box, per this skill's "same class in a different role" convention) share the same ``«Statement»`` stereotype -- both are, formally, the same underlying **Statement** class playing different structural roles, and their ``type`` is always literally ``"Statement"`` regardless of role. The Study Result's ``«StudyResult»`` stereotype instead reflects its own community/base-profile-specific ``type``. To fit the data into this form and make it human readable, syntactic shortcuts were taken to simplify values normally wrapped in complex data structures like MappableConcepts and Codings.

A key thing to note in the example is that, because Base Profiles are defined as formal subclasses, these objects have a specific ``type``  that reflects this (e.g. ``CohortAlleleFrequencyStudyResult``). But because Community Profiles are defined using schema composition, the formal ``type`` of these objects is that of the Core Model class on which they are built (e.g. ``Statement`` for statement profiles, or ``EvidenceLine`` for evidence-line profiles).

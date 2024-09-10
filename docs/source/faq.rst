FAQ
!!!

  
What is a Variant Annotation?
#############################
To appreciate modeling and development choices made for the VA-Spec, it helps to understand
how we define and think about the content of a Variant Annotation.

  .. definition:: Normalizing objects is STRONGLY RECOMMENDED for
               interoperability. While normalization is not strictly
               required, automated validation mechanisms are
               anticipated that will likely disqualify Variation that
               is not normalized. See :ref:`should-normalize` for
               a rationale.


text . . . 
  
  
.. important:: Normalizing objects is STRONGLY RECOMMENDED for
              interoperability. While normalization is not strictly
              required, automated validation mechanisms are
              anticipated that will likely disqualify Variation that
              is not normalized. See :ref:`should-normalize` for
              a rationale.
  
**Definition**:  “A **structured data object** that holds a **central statement of knowledge** about a **molecular variation**, along with **evidence and provenance metadata** supporting it.

 * **‘structured data object’**: an organized, computable representation of knowledge, in any format or syntax.
 * **‘central statement of knowledge’**: the single primary statement about a molecular variation is at the core of an annotation.
 * **‘molecular variation’**: defined broadly to cover sequence changes, epigenetic modifications, or alterations in gene expression or location (see `Variant`_). 
 * **‘evidence and provenance metadata’**: describes how the central knowledge statement was generated, including when, by whom, and using what methods and evidence information.

The VA-Spec model was  defined to *explcitly represent* and *clearly distinguish* these key types of information within a Variant Annotation - so that users can appreciate the significance and utility of the knowledge they provide.

  
What types of variants are covered by the VA-spec?
##################################################
  
Variants are the subjects of the knowledge statements that the VA-Spec was built to support. We define the notion of 'variant' broadly
to cover the diversity of targets annotated with knowledge in variant curtaion efforts and knowledgebases.

**Definition**: alternative forms of a genetic sequence, or of its molecular manifestation in a biological system. (Also referred to as a 'molecular variations'). 

Covers *sequence variations* in a genome, transcript, or protein.
 * **simple** (SNV, indels) or **complex** (inversions, repeat regions) sequence changes
 * **continuous** (allele) or **discontinuous** (translocations) regions
 * **in cis** (haplotypes) or **in trans** (genotypes) sets of variant regions

Covers *post-sequence* variations in the state of a program that unfolds 'downstream' of sequence 
 * changes in **expression level** or **location** of a gene product (e.g. decreased cytosolic expression)
 * changes in **post-translational modification** of proteins (e.g. increased PEST domain phosphorylation)
 * changes in **epigenetic alterations** of a gene or region (e.g. increased enhancer methylation)

Covers different levels of **'represenational specificity'** at which these variations can be described
 * **Discrete Variation**:  specific instances of a sequence variation in a specified context (reference, location, state - even if incompletely known). e.g. the NC_000019.9:g.45411941T>C genomic allele (`link <https://gnomad.broadinstitute.org/variant/19-45411941-T-C>`_)
 * **Expansion Sets**: sets of Discrete Variation instances that are related via lift-over, or projection functions (or combinations thereof). e.g. the set of discrete varaints in ClinGen 'canonical allele' CA127512 (`link <http://reg.clinicalgenome.org/redmine/projects/registry/genboree_registry/by_caid?caid=CA127512>`_)
 * **Categorical Variation**: rule-based classes of variation defined by specific membership criteria.  e.g. ‘deletions spanning EGFR exon 4’ (`link <https://civicdb.org/variants/252/summary>`_), ‘TSC1 loss-of-function muts.’ (`link <https://civicdb.org/variants/125/summary>`_)

The VA-Spec uses the `GA4GH Variant Representation Specification (VRS) <https://vrs.ga4gh.org/en/stable/index.html>`_ as a standard for identifying and representing these different forms of molecular variation.
  
  
What types of variant knowledge are covered by the VA-Spec?
###########################################################
The VA-Spec supports annotation statements about the **biological** and **clinical** significance of a variant, but leaves those
reporting **case-level observations** about a variant to other standards (e.g. Phenopackets, HL7-Clinical Genomics IM, FHIR)

 * **Biological Variant Statements** (*in-scope*): Molecular Consequence, Functional Impact, Population Frequency, Relative Location, Evolutionary Conservation
 * **Clinical Knolwedge Statements** (*in-scope*): Pathogenicity Classification, Therapeutic Response Classification, Diagnostic Classification, Prognostic Classification, Phenotypic Feature Association
 * **Case-Level Knowledge Statement** (*out-of-scope*):  observation of a variant in a patient, disease causality of an observed variant in a patient, origin of an observed variant in a patient, clonality of a variant in a patient.


What is the SEPIO framework?
#############################

  
  
How does the VA Spec build on the SEPIO framework?
##################################################

  
  
Why was the VA-Spec built as a modeling framework? 
##################################################

How does implementation led dev work / lead to standards?

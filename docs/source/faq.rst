FAQ
!!!

  
What is a Variant Annotation?
#############################
To appreciate modeling and development choices made for the VA-Spec, it helps to understand how we define and distinguish the elements that comprise a Variant Annotation.

**Definition**:  
   “A **structured data object** that holds a **central statement of knowledge** about a **molecular variation**, along with **evidence and provenance metadata** supporting it.

     * **‘structured data object’**: an organized, computable representation of knowledge, in any format or syntax.
     * **‘central statement of knowledge’**: the single primary statement about a molecular variation is at the core of an annotation.
     * **‘molecular variation’**: defined broadly to cover sequence changes, epigenetic modifications, or alterations in gene expression or location (see `What types of variants are supported?`_). 
     * **‘evidence and provenance metadata’**: describes how the central knowledge statement was generated, including when, by whom, and using what methods and evidence information.

The VA-Spec model was  defined to *explcitly represent* and *clearly distinguish* these key types of information within a Variant Annotation - so that users can appreciate the significance and utility of the knowledge they provide.
  
What types of variants are supported?
#####################################
  
Variants are the subjects of the knowledge statements that the VA-Spec was built to support. We define the notion of 'variant' broadly
to cover the diversity of variation concepts that are annotated with knowledge in different curtaion efforts and knowledgebases. 

**Variant Definition**: Alternative forms of a genetic sequence, or of its molecular manifestation in a biological system (also referred to as a 'molecular variations'). 
This definition covers:

    **Sequence variations** in a genome, transcript, or protein.
     * **simple** (SNV, indels) or **complex** (inversions, repeat regions) sequence changes
     * **continuous** (allele) or **discontinuous** (translocations) regions
     * **in cis** (haplotypes) or **in trans** (genotypes) sets of variant regions

    **Non-sequence** variations in the state of a program that unfolds 'downstream' of sequence 
     * changes in **expression level** or **location** of a gene product
           e.g. decreased cytosolic expression of the MYOD1 gene
     * changes in **post-translational modification** of proteins 
           e.g. increased PEST domain phosphorylation of the GADD34 gene
     * changes in **epigenetic alterations** of a gene or region
           e.g. increased AKT1 enhancer methylation

    Different levels of **'represenational specificity'** at which these variations can be described
     * **Discrete Variation**:  specific instances of a sequence variation in a specified context (reference, location, state - even if incompletely known). 
            e.g. the NC_000019.9:g.45411941T>C genomic allele (`link <https://gnomad.broadinstitute.org/variant/19-45411941-T-C>`_)
     * **Canonical Variation**: sets of Discrete Variation instances that are related via lift-over, or projection functions (or combinations thereof). 
            e.g. the set of discrete varaints in ClinGen 'canonical allele' CA127512 (`link <http://reg.clinicalgenome.org/redmine/projects/registry/genboree_registry/by_caid?caid=CA127512>`_)
     * **Categorical Variation**: rule-based classes of variation defined by specific membership criteria.  
            e.g. ‘deletions spanning EGFR exon 4’ (`link <https://civicdb.org/variants/252/summary>`_), ‘TSC1 loss-of-function muts.’ (`link <https://civicdb.org/variants/125/summary>`_)

The VA-Spec adopts the GA4GH `VRS <https://vrs.ga4gh.org/en/latest/index.html>`_ and `Cat-VRS <https://github.com/ga4gh/cat-vrs?tab=readme-ov-file>`_ specifications to support representation of these diverse kinds of molecular variation.

What kinds of variant knowledge are supported?
##############################################

The VA-Spec supports statements of knowledge about the **biological** and **clinical** significance of these different types of variants, but leaves those
reporting **case-level observations** about a variant to other standards (e.g. Phenopackets, HL7-Clinical Genomics IM, FHIR)

 * **Biological Knolwedge Statements**  ``IN-SCOPE``: e.g. Molecular Consequence, Functional Impact, Population Frequency, Relative Location, Evolutionary Conservation
 * **Clinical Knolwedge Statements**  ``IN-SCOPE``: e.g. Pathogenicity Classification, Therapeutic Response Classification, Diagnostic Classification, Prognostic Classification, Phenotypic Feature Association
 * **Case-Level Knowledge Statement**  ``OUT-OF-SCOPE``:  e.g. observation of a variant in a patient, disease causality of an observed variant in a patient, origin of an observed variant in a patient, clonality of a variant in a patient - these kinds of information are not covered by the VA-Spec.


What is the SEPIO framework?
#############################
The SEPIO Modeling Framework is a suite of models, methods, and tools to enable the creation of interoperable schema for representing scientific assertions, and the evidence and provenance supporting them. SEPIO was first developed as an ontology by the Monarch Initiative to support standardized RDF representations of evidence and provenance across integrated genotype-phenotype datasets (the Scientific Evidence and Provenance Information Ontology). The ontological model has since been abstracted into a generic Core Information Model (IM) that can be implemented in any language or format. 
The Core IM is domain-agnostic, and able to represent assertions and their evidence and provenance of any kind.  Application of SEPIO to a specific data set or use case requires defining a ‘Profile’ that extends/customizes the generic core model for a specific domain or application.

The components of the SEPIO Framework include: 

#. **A Domain Analysis Model (DAM)**: an informal description of the domain we are modeling (scientific assertions and their evidence/provenance)
#. **A Core Information Model (IM)**:  defines data structures that can represent information about this domain (for any type of assertion and evidence).
#. **A 'Profiling' Methodology**:  Implementations extend the core model with domain-specific content to define a “SEPIO Profile” - a custom schema for a particular application or use case.
#. **Ontology Support**: An ontological representation of the core model that can be used if desired to produce linked data with ontology-based semantics.

The framework approach addresses challenges posed by the diversity of types, levels of complexity, and use cases for evidence and provenance across knowledge domains and application - which means there is no ‘one-size-fits-all’ solution. The framework allows custom models built on a common semantic foundation can provide a base level of understanding and interoperability, without restricting expressivity. While this approach may not always support out-of-the-box interoperability across all communities of use, it can significantly lower barriers to aggregating, harmonizing, and operating across disparate data.

See the `SEPIO Framework website <https://sepio-framework.github.io/sepio-linkml/about/>`_ for more information about this foundational standard on which the VA Specification is built. 

How does the VA Spec use the SEPIO framework?
#############################################

coming soon . . . 

  
Why was the VA-Spec built as a modeling framework? 
##################################################

coming soon . . . 

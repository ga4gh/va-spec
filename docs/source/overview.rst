Overview
!!!!!!!!

The Variant Annotation Specification (VA-Spec) provides standard models for unambiguous representation of knowledge about molecular variation, along with supporting evidence and provenance information.

 * It defines a **set of information models** to represent different kinds of statements made about variants - built as discrete **profiles** that extend a common **core information model**. 
 * It provides machine-readable **json-schema specifications** of these models, to enable sharing and validation of data through APIs and other exchange mechanisms. 
 * It offers a **modeling framework** through which implementers can build profiles for **new statement types**, or **extend existing profiles** with additional features. 
 * It uses the `SEPIO Modeling Framework <https://sepio-framework.github.io/sepio-linkml/about/>`_ to produce these resources - applying SEPIO's established models, conventions, and profiling methodology.

This document provides an high-level introduction of VA-Spec **principles**, **models**, and **processes**, and links out to separate pages for additional details. For a hands on experience with va-spec data, see the simple **Variant Pathogenicity Statement example** here (TO DO).

Definitions and Scope
######################

Variant
*******
**Definition**: alternative forms of a genetic sequence, or its molecular manifestation in a biological system.  aka 'molecular variation'.

Covers variation in the *sequence* of a genome, transcript, or protein.
 * **simple** (SNV, indels) or **complex** (inversions, repeat regions) sequence changes
 * **continuous** (allele) or **discontinuous** (translocations) regions
 * **in cis** (haplotypes) or **in trans** (genotypes) sets of variant regions

Covers *post-sequence* variations in the state of a genetic program that unfolds 'downstream' of sequence 
 * variation in **expression level** or **location** of a gene product (e.g. decreased cytosolic expression)
 * variation in **post-translational modification** of proteins (e.g. increased PEST domain phosphorylation)
 * variation in **epigenetic alterations** of a gene or region (e.g. increased enhancer  methylation)

Covers different levels of 'represenational specificity' of these forms of variation
 * **Discrete Variation**:  precise instances of sequence variation in a specified context (reference, location, state - even if incompletely known). e.g. the NC_000019.9:g.45411941T>C genomic allele (`link <https://gnomad.broadinstitute.org/variant/19-45411941-T-C>`_), the APOE ɛ2/ɛ3 genotype (`link <https://www.snpedia.com/index.php/Gs269>`_)
 * **Expansion Sets**: sets of Discrete Variation instances that are related via lift-over, or projection functions (or combinations thereof). e.g. ClinGen 'canonical allele' CA127512 (`link <http://reg.clinicalgenome.org/redmine/projects/registry/genboree_registry/by_caid?caid=CA127512>`_), with members {NC_000019.10:g.44908684T>C, NC_000019.9:g.45411941T>C, NM_000041.3:c.388T>C NP_000032.1:p.Cys130Arg, ... }  
 * **Categorical Variation**: rule-based classes of variation defined by specific membership criteria.  e.g. ‘deletions spanning EGFR exon 4’ (`link <https://civicdb.org/variants/252/summary>`_), ‘TSC1 loss-of-function muts.’ (`link <https://civicdb.org/variants/125/summary>`_)

*For more on variant types and representation, see the `GA4GH VRS specification <https://vrs.ga4gh.org/en/stable/index.html>`_*

Annotation
**********
**Definition**:  “A **structured data object** that holds a **central statement of knowledge** about a **molecular variation**, along with **metadata** supporting its interpretation and use.
 * **‘structured data object’**: an organized, computable representation of knowledge (in any format or syntax)
 * **‘central statement of knowledge’**: the single primary statement about a molecular variation is at the core of an annotation
 * **‘molecular variation’**: defined broadly to cover sequence changes, epigenetic modifications, or  alterations in gene expression/amount (see `Variant`_). 
 * **‘metadata’**:  may include evidence and provenance for the primary statement, and additional information that helps the user appreciate the significance and utility of this knowledge

VA-Spec Scope
*************
**Definition**: The VA-Spec supports diverse types of **biological** and **clinical** variant knowledge, but leaves **case-level observations** to other standards (e.g. Phenopackets, HL7-Clinical Genomics IM, FHIR)

Examples of in-scope Statements:
 * **Biological Statements**: Molecular Consequence, Functional Impact, Population Frequency, Relative Location, Evolutionary Conservation
 * **Clinical Statements**: Pathogenicity Classification, Therapeutic Response Classification, Diagnostic Classification, Prognostic Classification, Phenotypic Feature Association

Examples of out-of-scope Statements:
 * **Case-Level Statements**:  observation of a variant in a patient, disease causality of an observed variant in a patient, origin of an observed variant in a patient, clonality of a variant in a patient.


Modeling Principles and Framework
#################################

. . . text






**Contents**
 * `Definitions and Scope`_
 * `Modeling Principles and Framework`_



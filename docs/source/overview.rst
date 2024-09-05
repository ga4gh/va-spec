Overview
!!!!!!!!

The **Variant Annotation Specification (VA-Spec)** provides standard models for flexible and unambiguous representation of knowledge about molecular variation, along with supporting evidence and provenance information - to support exchange through GA4GH APIs and other data sharing mechanisms. 

Definitions and Scope:
######################


Variant
********
**Definition**: alternative forms of a genetic sequence, or its molecular manifestation in a biological system.  aka 'molecular variation'.

Covers variation in the *sequence* of a genome, transcript, or protein.
 * **simple** (SNV, indels) or **complex** (inversions, repeat regions) sequence changes
 * **continuous** (allele) or **discontinuous** (translocations) regions
 * **in cis** (haplotypes) or **in trans** (genotypes) sets of variant regions

Covers *post-sequence* variations in the state of a genetic program that unfolds 'downstream' of sequence 
 * variation in **expression level** or **location* of a gene product (e.g. decreased cytosolic expression)
 * variation in **post-translational modification** of proteins (e.g. increased PEST domain phosphorylation)
 * variation in **epigenetic alterations** of a gene or region (e.g. increased enhancer  methylation)

Covers different levels of 'represenational specificity' of these forms of variation
 * **Discrete Variation**:  precise instances of sequence variation in a specified context (reference, location, state - even if incompletely known). e.g. the NC_000019.9:g.45411941T>C genomic allele (`link <https://gnomad.broadinstitute.org/variant/19-45411941-T-C>`_), the APOE ɛ2/ɛ3 genotype (`link <https://www.snpedia.com/index.php/Gs269>`_)
 * **Expansion Sets**: sets of Discrete Variation instances that are related via lift-over, or projection functions (or combinations thereof). e.g. ClinGen 'canonical allele' CA127512 (`link <http://reg.clinicalgenome.org/redmine/projects/registry/genboree_registry/by_caid?caid=CA127512>`_), wiwth members {NC_000019.10:g.44908684T>C, NC_000019.9:g.45411941T>C, NM_000041.3:c.388T>C NP_000032.1:p.Cys130Arg, ... }  
 * **Categorical Variation**: rule-based classes of variation defined by specific membership criteria.  e.g. ‘deletions spanning EGFR exon 4’ `link <https://civicdb.org/variants/252/summary>`_), ‘TSC1 loss-of-function muts.’ (`link <https://civicdb.org/variants/125/summary>`_)

**For more on variant types and representation, see the `GA4GH VRS specification <https://vrs.ga4gh.org/en/stable/index.html>`_

Annotation
********
**Definition**: 


Covers variation in the *sequence* of a genome, transcript, or protein.
 * **simple** (SNV, indels) or **complex** (inversions, repeat regions) sequence changes
 * **continuous** (allele) or **discontinuous** (translocations) regions
 * **in cis** (haplotypes) or **in trans** (genotypes) sets of variant regions

Covers *post-sequence* variations in the state of a genetic program that unfolds 'downstream' of sequence 
 * variation in **expression level** or **location* of a gene product (e.g. decreased cytosolic expression)
 * variation in **post-translational modification** of proteins (e.g. increased PEST domain phosphorylation)
 * variation in **epigenetic alterations** of a gene or region (e.g. increased enhancer  methylation)

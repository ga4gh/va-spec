Overview
!!!!!!!!

The **Variant Annotation Specification (VA-Spec)** provides standard models for flexible and unambiguous representation of knowledge about molecular variation, along with supporting evidence and provenance information - to support exchange through GA4GH APIs and other data sharing mechanisms. 

Definitions and Scope:
######################


Variant
********
**Definition**: alternative forms of a genetic sequence, or its molecular manifestation in a biological system.  aka 'molecular variation'.

Covers variation in the *sequence* of a genome, transcript, or protein.
 * simple (SNV, indels) or complex (inversions, repeat regions) sequence changes
 * continuous (allele) or discontinuous (translocations) regions
 * in cis (haplotypes) or in trans (genotypes)  sets of variant regions

Covers *post-sequence* variations in the state of a genetic program that unfolds 'downstream' of sequence 
 * variation in expression level or location of a gene (e.g. decreased cytosolic expression)
 * variation in post-translational modification of proteins (e.g. increased phosphorylation)
 * variation in epigenetic alteration/state of a gene/region (e.g. increased methylation)






#. **VARIANT**: alternative forms of a genetic sequence, or its molecular manifestation in a biological system.  aka 'molecular variation'.

    * Sequence Variant -  changes in the sequence of a genome, transcript, or protein.
        * simple (e.g. SNV, indels) or complex (inversions, repeat regions) sequence changes
        * continuous (allele) or discontinuous (translocations) regions
        * in cis (e.g. haplotypes) or in trans (e.g. genotypes)  sets of variant regions

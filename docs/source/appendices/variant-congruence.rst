.. _variant-congruence

Variant Congruence
!!!!!!!!!!!!!!!!!!

This concerns the notion that the variant subject of a Statement's Proposition may be appear to be different than variants described in Evidence Items or Evidence Lines that support it. This is because different databases may attach knowledge to variants defined in different reference contexts, on different molecule types, or at different levels of specificity - but variation across these levels of representation can map to each other and share a common genetic basis or biological characteristic that is the true subject of a knowledge statement.

For example, Pathogenicity Statements often report knowledge about a `Categorical Variant <https://cat-vrs.readthedocs.io/en/latest/introduction.html>`_ such as *BRAF V600E*, while an Experimental Functional Impact Study Result supporting it may describe a discrete **protein-level variant** such as *NP_004324.2:p.Val600Glu*, and a Cohort Allele Frequency Study Result supporting it may describe a discrete **genomic-level variant** such as *NC_000007.13:g.140453136A>T* - both of which are covered by the definition of the *BRAF V600E* Categorical Variant.

The computational foundations of the `VRS <https://github.com/ga4gh/vrs>`_ and `CatVRS <https://github.com/ga4gh/cat-vrs>`_ specifications are designed to enable mappings between discrete variants defined on different references contexts or molecule types, and mappings from discrete variation to broader Categorical Variant concepts to which they 'belong'. This is essential for aggregating evidence attached to related variation defined at different levels of specificity - as illustrated in :ref:`this scenario <acmg-variant-pathogenicity-statement-example-with-evidence>` where data about the frequency of discrete alleles defined in a genomic context, and functional data about discrete variants defined in a protein context, are assembled and interpreted as evidence for the pathogenicity classification of a broader categorical variation.

For more on this challenge and solutions, explore the `VRS <https://vrs.ga4gh.org/en/stable/introduction.html>`_ and `Cat-VRS <https://cat-vrs.readthedocs.io/en/latest/introduction.html>`_ documentation.

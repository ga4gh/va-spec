.. _variant-congruence

Variant Congruence
!!!!!!!!!!!!!!!!!!

This concerns the notion that the variant subject of a Statement's Proposition may be specified on different molecule types, or at different levels of granularity, than variants described in Evidence Items or Evidence Lines that support it. 

For example, Pathogenicity Statements often report knowledge about a **Categorical Variant**, while an Experimental Functional Impact Study Result supporting it may describe a discrete **protein-level variant** (e.g. *KCNQ4 p.Ser269del*), and a Cohort Allele Frequency Study Result supporting it may describe a discrete **genomic-level variant** (e.g. *chr1-40819438-TCTC-T*) - both of which are covered by the definition of the aforementioned Categorical Variant. 

The computational basis of CatVRS and VRS variant specifications are defined to enable mappings between such discrete variants and a broader Categorical Variant concept, and support tools that can identify and link evidence based on discrete variants related under a Categorical Variant definition. Considerations, approaches, and tooling in this area are the remit of the `VRS <https://github.com/ga4gh/vrs>`_ and `CatVRS <https://github.com/ga4gh/cat-vrs>`_ specifications. 

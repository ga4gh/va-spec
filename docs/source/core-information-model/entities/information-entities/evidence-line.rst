.. _EvidenceLine:

Evidence Line
!!!!!!!!!!!!!

.. include::  ../../../../../schema/core-im/def/EvidenceLine.rst  

**IMPLEMENTATION GUIDANCE**

**1. Meaning and Utility of Evidence Lines**

* Evidence Lines are used to capture one or more pieces of information (i.e. **evidence items**) that are assessed together as an argument for or against some **target proposition** - and report the **direction** (supports or disputes) and **strength** (e.g. strong, moderate, weak) that the argument is determined to make. 
* For example, the allele count and frequency calculations for the BRCA2 c.8023A>G variant in the ExAC database are evidence items that may be collectively assessed to build an EvidenceLine making argument of **moderate strength** that **supports** a target proposition that the variant is pathogenic for Breast Cancer. 

.. image:: images/evidence-line-semantics.png
  :width: 700

* In an EvidenceLine instance, the `targetProposition` attribute captures the 'possible fact' that the evidence is assessed against. The `evidenceItems` attribute the information assessed as evidence. And the `directionOfEvidenceProvided` and `strengthOfEvidenceProvided` attributes report the outcome of this assessment - whether the evidence line supports or disputes the target proposition, and how strongly. Additional attributes allow provenance information about the evidence assessment process to be captured (who did it, when, using what guidelines, etc). 

**2. Evidence Line Scope**

* Evidence Lines are flexible with respect to the granularity of arguments they support, and the scope of evidence items they can collectively assess. 
* Narrow scoping will bucket available evidence into many, fine-grained Evidence Lines that make the most atomic independently meaningful arguments possible. The ACMG Variant Pathogenicity Interpretation Guidelines are an example of a fairly fine-grained evidence interpretation framework. 
* Broader scoping approaches may organize the same available evidence into fewer Evidence Lines that build and assess less atomic arguments based on a wider and more diverse set of evidence items.  For example, CIViC curators assess the strength and direction of evidence items at the level of *all information reported in a publication for a specific study* - which can encompass many different results and evidence types that under more fine-grained interpretation approaches might be split apart and assessed as separate lines of evidence. 
* This CIViC EID5682 record (https://civicdb.org/evidence/5682/summary) is a clear example of this. We see here that CIViC evidence assessments are performed at the level of all results reported in PMID:23143947 - which would captured as a single Evidence Line that assigns a strength (level C) and direction (supports) to the collective argument made by this evidence.  However, as detailed in the free-text summary of this EID, the more fine-grained ACMG framework breaks out and separately assess two arguments here - one based on criterion PP1 (disease co-segregation evidence), and one based on criterion PP4 (highly specific gene-phenotype information) - which a finer-grained representation would capture as two distinct Evidence Lines.   
* This example illustrates the flexible scope of Evidence Lines to fit different curation processes- where ACMG-based curation might assess evidence at a finer-grained level that would support a larger number of more atomic Evidence Lines, while CIViC curators might assess the same evidence all together in a single, more broadly-scoped Evidence Line - in virtue of its being reported in the same publication.

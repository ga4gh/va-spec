.. _StudyResult:

Study Result
!!!!!!!!!!!!

.. include::  ../../../def/va-spec/StudyResult.rst

---------

**DATA STRUCTURE**

In VA-Spec, the :ref:`Study Result <StudyResult>` class and its :ref:`profiles <study-result-profiles>` can support the general data structure below.

.. core-im-study-result-data-structure:

.. figure:: ../../../images/study-result-data-structure.png

   Study Result Data Structure

   **Legend** A class-level view of the Study Result-based structures supported in VA-Spec data. Italicized text in each class exemplify the kind of information each may capture - here in the case of a Cohort Allele Frequency Study Result reporting data from the gnomAD dataset about a particular variant.

In this structure:

* A **Study Result** and the data items it holds can be linked to the larger **Data Set** from which they came, and a description of the **Study Group** from which the data was collected.
* Note that no **Proposition** object is used here, because Study Results represent more foundational data, and do not assert or assess evidence for possible facts about the domain.
* As with Statements and Evidence Lines, surrounding classes can be used to describe the provenance of the Study Result and its data items.

A data example illustrating this structure for a Study Result interpreted as evidence for a Variant Pathogenicity Statement can be found :ref:`here <acmg-variant-pathogenicity-statement-example-with-evidence>`.

------------

**IMPLEMENTATION GUIDANCE**

**1. Study Result Utility**

 * StudyResults provide a useful way to capture a subset of items from a study dataset that are used as evidence in generating higher order knowledge assertions about the entity that is the focus of the study result.
 * For example, consider the comprehensive allele frequency dataset provided by gnomAD, which covers millions of variants. A curator looking to assess the pathogenicity of a particular variant might create a StudyResult object to capture a subset of data related to this focus allele, including  its count, frequency, homozygous frequency, along with metadata concerning the shared provenance or quality of this data. The StudyResult could then be references as a piece of evidence used to inform the focus alleles final pathogenicity classification.
 * Study Results are typically used to define subsets of data from larger high throughput analyses or clinical study data sets. But a StudyResult might be used to organize the data from a simple, small scale bench experiment - e.g. a western blot analysis of protein expression, or an in vitro binding assay focused on a single protein.  Even such small 'studies' can generate multiple data items and metadata, and a StudyResult object can be used to collect all or some of these data points pertinent to a particular focus into an organized structure.


**2. Use of the** ``StudyResult.dataItems`` **attribute:**

* The model specifies use of a key-value based ``DataItem`` object to capture the meaning and value of each type of data item captured in a given StudyResult. But in practice, profiles for specific StudyResult types may choose to define one or more specializations of the generic ``dataItems`` attribute as named attributes. This makes the data more succinct and parsable, and allows specific constraints to be applied and validated for different data items.
* For example, a **CohortAlleleFrequencyStudyResult** profile may define a named ``focusAlleleFrequency`` attribute that is required, and a named ``focusAlleleCount`` attribute that is optional - both of which conceptually specialize the gkm-core ``dataItems'`` property. Under this approach, the core ``dataItems`` attribute acts as a placeholder to seed such specializations, but is not used directly in StudyResult profiles.

.. _StudyResult:

Study Result
!!!!!!!!!!!!

.. include::  ../../../../../schema/core-im/def/StudyResult.rst


**STUDY RESULT DATA STRUCTURE**

Many users of the VA-Spec provide curated collections of data about a particular variant from a particular study or analysis, as opposed to higher order assertions of knowledge. The :ref:`Study Result <StudyResult>` class is defined to support this use case.

Like the Statement class, it roots a larger data structure supporting clear and precise tracking of the evidence and provenance information.

.. core-im-study-result-data-structure:

.. figure:: ../../../images/core-im-study-result-data-structure.png

   Study Result Data Structure

   **Legend** A class-level view of the Study Result-based structures that manifest in VA-Spec data. Italicized text under class names illustrate the kind of information each class may report in the case of a Cohort Allele Frequency study Result reporting data from the gnomAD dataset about a particular variant.

In this structure:
 * A **Study Result** is linked to the set of **Data Items** it collects about the focus variant.
 * The **Data Items** can be linked to the larger **Data Set** or sets from which it came,
 * The **Study Result** and **Data Set** can be linked to a description of the **Study Group** from which the data was collected.
 * As with Statements, clear and precise provenance information about the Study Result, Data Items, and Data Set can be captured in supporting **Method**, **Document**, **Contribution**, **Agent**, and **Activity** objects.


**IMPLEMETNATION GUIDANCE**

1. StudyResults provide a useful way to capture a subset of items from a study dataset that are used as evidence in generating higher order knowledge assertions about the entity that is the focus of the study result. 

* For example, consider the comprehensive allele frequency dataset provided by gnomAD, which covers millions of variants. A curator looking to assess the pathogenicity of a particular variant might create a StudyResult object to capture a subset of data related to this focus allele, including  its count, frequency, homozygous frequency, along with metadata concerning the shared provenance or quality of this data. The StudyResult could then be references as a piece of evidence used to inform the focus alleles final pathogenicity classification. 
* Note that Study Results are typically used to define subsets of data from larger high throughput analyses or clinical study data sets. But a StudyResult might be used to organize the data from a simple, small scale bench experiment - e.g. a western blot analysis of protein expression, or an in vitro binding assay focused on a single protein.  Even such small 'studies' can generate multiple data items and metadata, and a StudyResult object can be used to collect all or some of these data points pertinent to a particular focus into an organized structure.


2. Use of the ``StudyResult.dataItems`` attribute:

* The model specifies use of a key-value based ``DataItem`` object to capture the meaning and value of each type of data item captured in a given StudyResult. But in practice, profiles for specific StudyResult types may choose to define one or more specializations of the generic ``dataItems`` attribute as named attributes. This makes the data more succinct and parsable, and allows specific constraints to be applied and validated for different data items. 
* For example, a **CohortAlleleFrequencyStudyResult** profile may define a named ``focusAlleleFrequency`` attribute that is required, and a named ``focusAlleleCount`` attribute that is optional - both of which conceptually specialize the core-im ``dataItems'`` property. Under this approach, the core ``dataItems`` attribute acts as a placeholder to seed such specializations, but is not used directly in StudyResult profiles. 

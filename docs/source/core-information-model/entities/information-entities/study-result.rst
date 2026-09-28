.. _StudyResult:

Study Result
!!!!!!!!!!!!

.. include::  ../../../def/va-spec/StudyResult.rst

---------

**DATA STRUCTURE**

In VA-Spec, the :ref:`Study Result <StudyResult>` class and its :ref:`profiles <study-result-profiles>` can support the general data structure below.

.. core-im-study-result-data-structure:

.. raw:: html

   <iframe src="../../../_static/diagrams/study-result-example.html" style="width:100%; height:550px; border:0;" title="Study Result worked example"></iframe>

**Legend** A class-level view of the Study Result-based structures supported in VA-Spec data, filled in with illustrative example data for a gnomAD population-frequency result.

In this structure:

* A **Study Result** and the data items it holds can be linked to the larger **Data Set** from which they came.
* Some profiles narrow **focus** and add their own dedicated group fields -- e.g. a Cohort Allele Frequency Study Result's ``cohort`` attribute, which references the **Study Group** the data was collected from. This is not part of the base **Study Result** class itself.
* Note that no **Proposition** object is used here, because Study Results represent more foundational data, and do not assert or assess evidence for possible facts about the domain.
* As with Statements and Evidence Lines, surrounding classes can be used to describe the provenance of the Study Result and its data items.

A data example illustrating this structure for a Study Result interpreted as evidence for a Variant Pathogenicity Statement can be found :ref:`here <acmg-variant-pathogenicity-statement-example-with-evidence>`.

------------

**IMPLEMENTATION GUIDANCE**

**1. Study Result Utility**

 * StudyResults provide a useful way to capture a subset of items from a study dataset that are used as evidence in generating higher order knowledge assertions about the entity that is the focus of the study result.
 * For example, consider the comprehensive allele frequency dataset provided by gnomAD, which covers millions of variants. A curator looking to assess the pathogenicity of a particular variant might create a StudyResult object to capture a subset of data related to this focus allele, including  its count, frequency, homozygous frequency, along with metadata concerning the shared provenance or quality of this data. The StudyResult could then be references as a piece of evidence used to inform the focus alleles final pathogenicity classification.
 * Study Results are typically used to define subsets of data from larger high throughput analyses or clinical study data sets. But a StudyResult might be used to organize the data from a simple, small scale bench experiment - e.g. a western blot analysis of protein expression, or an in vitro binding assay focused on a single protein.  Even such small 'studies' can generate multiple data items and metadata, and a StudyResult object can be used to collect all or some of these data points pertinent to a particular focus into an organized structure.


**2. Capturing the data items in a StudyResult:**

* The core ``StudyResult`` class does not define a generic array attribute to hold the individual data items it collects. Instead, profiles for specific StudyResult types define their own data-type-specific named attributes to capture this information (e.g. ``focusAlleleCount``, ``focusAlleleFrequency``, and ``locusAlleleCount`` in a :ref:`CohortAlleleFrequencyStudyResult`). This makes the data more succinct and parsable, and allows specific constraints to be applied and validated for different data items.
* For information that does not fit a profile's named attributes, the core class provides two open ``object`` attributes (both at *draft* maturity): ``ancillaryResults``, for custom fields capturing additional results derived from the primary data items (e.g. a ``grpMaxFAF95`` calculation in a Cohort Allele Frequency Study Result), and ``qualityMeasures``, for custom fields describing the quality or provenance of those primary data items (e.g. a sequencing coverage metric).

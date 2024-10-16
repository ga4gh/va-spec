.. _study-result-profiles:


Study Result Profiles
!!!!!!!!!!!!!!!!!!!!!

In the **GKS-Core-IM**, the ``StudyResult`` class (:ref:`link <StudyResult>`) is used to capture collections of data about a single variant from a particular study or analysis (e.g. from the gnomAD allele frequency dataset) - and provide provenance information and other supporting metadata.

**Study Result Profiles** are defined as specializations of this Core-IM ``StudyResult`` class, to provide a concrete schema for representing a particular type of data from a variant study or analysis (e.g. cohort allele frequency data.

Below are the **Standard Study Result Profiles** currently defined as part of the VA-Spec, and available for adoption or extension by implementations.

Cohort Allele Frequency Study Result
####################################


.. include::  ../../../schema/profiles/def/CohortAlleleFrequencyStudyResult.rst


Assay Variant Effect Measurement Study Result
#############################################

.. include::  ../../../schema/profiles/def/AssayVariantEffectMeasurementStudyResult.rst

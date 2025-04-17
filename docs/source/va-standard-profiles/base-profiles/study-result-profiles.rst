.. _study-result-profiles:

Study Result Profiles
!!!!!!!!!!!!!!!!!!!!!

**Study Results** represent collections of data items about a single variant from a particular study or analysis (e.g. `1-55051215-G-GA (GRCh38) <https://gnomad.broadinstitute.org/variant/1-55051215-G-GA?dataset=gnomad_r4>`_ from the gnomAD allele frequency dataset) - along with provenance and other supporting metadata.

**Study Result Profiles** are defined as concrete subclasses of the Core :ref:`Study Result<StudyResult>` class - each tailored to represent data from a particular type of study or analysis.

Below are the Study Result Profiles currently defined as part of the VA-Spec, and available for adoption or extension by implementations.

.. _cohort-allele-frequency-study-result:

Cohort Allele Frequency Study Result
####################################


.. include::  ../../def/va-spec/CohortAlleleFrequencyStudyResult.rst

**Use Cases and Implementations**

This Study Result profile was defined to support `gnomAD <https://gnomad.broadinstitute.org/>`_ data in an early implementation for the `GREGoR consortium <https://gregorconsortium.org/>`_. It proivides a format to represent and share the diverse types of allele frequency data, quality measures, and derived ancillary results this resource provides. The model may be generalized in the future to support broader use cases, as new requirements and implementers emerge.



.. _experimental-variant-functional-impact-study-result:

Experimental Variant Functional Impact Study Result
###################################################

.. include::  ../../def/va-spec/ExperimentalVariantFunctionalImpactStudyResult.rst

**Use Cases and Implementations**

This Study Result profile was defined to support an early `MAVE-DB <https://www.mavedb.org/>`_ implementation of the VA-Spec, as a format to represent high-throughput, quantitative multiplex-assay based functional impact data. This is a very unique type of assay and functional impact data, and the model may be generalized in the future to support broader use cases, as new requirements and implementers emerge.

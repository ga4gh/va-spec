.. _study-result-profiles:

Study Result Profiles
!!!!!!!!!!!!!!!!!!!!!

Study Results are used to represent collections of data items about a single variant from a particular study or analysis (e.g. `1-55051215-G-GA (GRCh38)<https://gnomad.broadinstitute.org/variant/1-55051215-G-GA?dataset=gnomad_r4>`_from the gnomAD allele frequency dataset) - along with provenance and other supporting metadata. 

Study Result Profiles are defined as specialized subclasses of the Core :ref:`Study Result<StudyResult>` class - each tailored to represent data from a particular type of study or analysis. 

Below are the Study Result Profiles currently defined as part of the VA-Spec, and available for adoption or extension by implementations.

.. _cohort-allele-frequency-study-result:

Cohort Allele Frequency Study Result
####################################


.. include::  ../../def/va-spec/CohortAlleleFrequencyStudyResult.rst


.. _experimental-variant-functional-impact-study-result:

Experimental Variant Functional Impact Study Result
###################################################

.. include::  ../../def/va-spec/ExperimentalVariantFunctionalImpactStudyResult.rst

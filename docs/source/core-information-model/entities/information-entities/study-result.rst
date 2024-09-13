.. _StudyResult:

Study Result
!!!!!!!!!!!!

.. include::  ../../../../../schema/core-im/def/StudyResult.rst

**Implementation Guidance**



The ``dataItems`` attribute:

* The model specifies use of a key-value based ``DataItem`` object to capture the meaning and value of each type of data item captured in a given StudyResult. But in practice, profiles for specific StudyResult types may choose to define one or more specializations of the generic ``dataItems`` attribute as named attributes. 
* This makes the data more succinct and parsable, and allows specific constraints to be applied and validated for different data items. For example, a **PopulaitonAlleleFrequencyStudyResult** profile may define a named ``focusAlleleFrequency`` attribute that is required, and a named ``focusAlleleCount`` attribute that is optional - both of which conceptually specialize the core-im ``dataItems'`` property. Under this approach, the core ``dataItems`` attribute acts as a placeholder to seed such specializations, but is not used directly in StudyResult profiles. 

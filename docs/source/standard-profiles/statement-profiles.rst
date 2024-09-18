.. _statement-profiles:

Statement Profiles
!!!!!!!!!!!!!!!!!!

In the **GKS-Core-IM**, each discrete assertion of knowledge is captured in a self-contained ``Statement`` object which roots a `data structure <https://va-ga4gh.readthedocs.io/en/latest/modeling-foundations.html#core-im-statement-structure>`_ supporting rich and flexible descriptions of the evidence and provenance supporting this knowledge.

**Statement Profiles** are defined as specializations of this Core-IM ``Statement`` class, to provide a concrete schema for representing a particular type of Variant knowledge (e.g. variant pathogenicity classifications).

Below are the **Standard Statement Profiles** currently defined as part of the VA-Spec, and available for adoption or extension by Driver Project implementations.

Variant Pathogenicity Statement
###############################

An example of data structured using this Standard Profile can be found `here <https://va-ga4gh.readthedocs.io/en/stable/examples/variant-pathogenicity-statement.html>`_.

.. include::  ../../../schema/profiles/def/VariantPathogenicityStatement.rst


Variant Oncogenicity Statement
##############################

.. include::  ../../../schema/profiles/def/VariantOncogenicityStudyStatement.rst


Variant Therapeutic Response Study Statement
#############################################

.. include::  ../../../schema/profiles/def/VariantTherapeuticResponseStudyStatement.rst


Variant Diagnostic Study Statement
##################################

.. include::  ../../../schema/profiles/def/VariantDiagnosticStudyStatement.rst


Variant Prognostic Study Statement
##################################

.. include::  ../../../schema/profiles/def/VariantPrognosticStudyStatement.rst


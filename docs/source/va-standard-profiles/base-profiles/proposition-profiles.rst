.. _proposition-profiles:

Proposition Profiles
!!!!!!!!!!!!!!!!!!!!

Proposition Profiles are defined as specializations of the core ``Proposition`` class, to explicitly represent particular types of possible facts that may be true in a domain of discourse. For example, the :ref:`VariantPathogenicityProposition<variant-pathogenicity-proposition-profile>` profile defines a model for describing causal relationships between genetic variants and specific diseases.

Such Propositions are used within the context of generic ``Statement`` or ``EvidenceLine`` classes from the core model, to provide domain specific semantics for the respective assessments that these core classes provide (e.g. in the :ref:`example here<proposition-utility-example>`). This avoids the need to define Statement or Evidence Line profiles for many use cases. (The VA-Spec only defines Statement or Evidence Line profiles profiles to support strict alignment with terminological conventions of a particular community guideline, e.g. the :Ref:`ACMG 2015 Variant Pathogenicity Statement<variant-pathogenicity-statement-acmg-2015>` profile).

Below are the **VA Standard Proposition Profiles** currently defined as part of the VA-Spec, and available for adoption or extension by implementations.


.. _variant-pathogenicity-proposition:

Variant Pathogenicity Proposition
#################################

.. include::  ../../def/va-spec/VariantPathogenicityProposition.rst

.. _variant-oncogenicity-proposition:

Variant Oncogenicity Proposition
#################################

.. include::  ../../def/va-spec/VariantOncogenicityProposition.rst

.. _variant-therapeutic-response-proposition:

Variant Therapeutic Response Proposition
########################################

.. include::  ../../def/va-spec/VariantTherapeuticResponseProposition.rst

.. _variant-diagnostic-proposition:

Variant Diagnostic Proposition
##############################

.. include::  ../../def/va-spec/VariantDiagnosticProposition.rst

.. _variant-prognostic-proposition:

Variant Prognostic Proposition
##############################

.. include::  ../../def/va-spec/VariantPrognosticProposition.rst

.. _experimental-variant-functional-impact-proposition:

Experimental Variant Functional Impact Proposition
##################################################

.. include::  ../../def/va-spec/ExperimentalVariantFunctionalImpactProposition.rst

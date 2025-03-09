.. _statement-profiles:

Statement Profiles
!!!!!!!!!!!!!!!!!!

Statement Profiles specialize the core ``Statement`` class to support a specific type of knowledge. The Statement profiles included in v1 of the VA-Spec are named and defined to align with curation and terminological conventions of established community guidelines in a given knowledge domain - such as the `ACMG 2015 Variant Interpretation Guidelines <https://pubmed.ncbi.nlm.nih.gov/27993330/>`_ for pathogenicity classifications, or the `AMP/ASCO/CAP (AAC) Guidleines <https://pubmed.ncbi.nlm.nih.gov/25741868/>`_ for clinical interpretation of genetic variants. 

.. _variant-pathogenicity-statement-acmg-2015:

Variant Pathogenicity Statement (ACMG 2015)
###########################################

.. note:: This data class is at a **draft** maturity level and may \
    change in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Artifacts**
 - `Source YAML <https://github.com/ga4gh/va-spec/blob/1.0-docs-refactor/schema/va-spec/acmg-2015/pathogenicity-statement-profile-source.yaml>`_
 - `JSON Schema <https://github.com/ga4gh/va-spec/blob/1.0-docs-refactor/schema/va-spec/acmg-2015/json/VariantPathogenicityStatement>`_

**Computational Definition**
A Statement describing the role of a variant in causing an inherited condition. 
The structure and certain attribute constraints in this profile are defined to align with 
curation and terminological conventions of the ACMG 2015 Variant Interpretation Guidelines.

**Information Model**
Some Variant Pathogenicity Statement attributes are inherited from  :ref:`Statement` and :ref:`InformationEntity`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Field
      - Flags
      - Type
      - Limits
      - Description
   *  - id
      - 
      - string
      - 0..1
      - The 'logical' identifier of the Entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - name
      - 
      - string
      - 0..1
      - A primary name for the entity.
   *  - description
      - 
      - string
      - 0..1
      - A free-text description of the Entity.
   *  - aliases
      - 
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - string
      - 0..m
      - Alternative name(s) for the Entity.
   *  - extensions
      - 
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - specifiedBy
      - 
      - :ref:`Method` | :ref:`iriReference`
      - 0..1
      - A specification that describes all or part of the process that led to creation of the Information Entity
   *  - contributions
      - 
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Contribution`
      - 0..m
      - Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
   *  - reportedIn
      - 
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Document` | :ref:`iriReference`
      - 0..m
      - A document in which the the Information Entity is reported.
   *  - type
      - 
      - string
      - 1..1
      - MUST be "Statement".
   *  - proposition
      - 
      - :ref:`Variant Pathogenicity Proposition`
      - 1..1
      - A proposition about the pathogenicity of a varaint, the validity of which is assessed and reported by the Statement. A Statement can put forth the proposition as being true, false, or uncertain, and may provide an assessment of the level of confidence/evidence supporting this claim. 
   *  - direction
      - 
      - string
      - 1..1
      - A term indicating whether the Statement supports, disputes, or remains neutral w.r.t. the validity of the Proposition it evaluates.
   *  - strength
      - 
      - :ref:`MappableConcept`
      - 0..1
      - A term used to report the strength of a Proposition's assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be).  Implementers may choose to frame a strength assessment in terms of how *confident* an agent is that the Proposition is true or false, or in terms of the *strength of all evidence* they believe supports or disputes it.
   *  - score
      - 
                        .. raw:: html

                            <span style="background-color: #D3D3D3; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Draft Maturity Level">D</span>
      - number
      - 0..1
      - A quantitative score that indicates the strength of a Proposition's assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be). Depending on its implementation, a score may reflect how *confident* that agent is that the Proposition is true or false, or the *strength of evidence* they believe supports or disputes it. Instructions for how to interpret the menaing of a given score may be gleaned from the method or document referenced in 'specifiedBy' attribute. 
   *  - classification
      - 
      - :ref:`MappableConcept`
      - 0..1
      - A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's Proposition, in terms of a classification of its subject.
   *  - hasEvidenceLines
      - 
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`EvidenceLine` | :ref:`iriReference`
      - 0..m
      - An evidence-based argument that supports or disputes the validity of the proposition that a Statement assesses or puts forth as true. The strength and direction of this argument (whether it supports or disputes the proposition, and how strongly) is based on an interpretation of one or more pieces of information as evidence (i.e. 'Evidence Items).


.. _variant-oncogenicity-statement-ccv-2022:

Variant Oncogenicity Statement (CCV 2022)
#########################################

.. note:: This data class is at a **draft** maturity level and may \
    change in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**


**Information Model**

.. _variant-therapeutic-response-statement-aac-2017:

Variant Therapeutic Response Statement (AAC 2017)
#################################################

.. note:: This data class is at a **draft** maturity level and may \
    change in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**


**Information Model**

.. _variant-diagnostic-statement-aac-2017:

Variant Diagnostic Statement (AAC 2017)
#######################################

.. note:: This data class is at a **draft** maturity level and may \
    change in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**


**Information Model**

.. _variant-prognostic-statement-aac-2017:

Variant Prognostic Statement (AAC 2017)
#######################################

.. note:: This data class is at a **draft** maturity level and may \
    change in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**


**Information Model**

.. _experimental-variant-functional-impact-statement:

Experimental Variant Functional Impact Statement
################################################

.. note::  A VA Standard Profile for this type of Statement is not explicitly defined in the VA-Spec, \
    because there are no established community guidelines or terminologies in this domain to guide \
    additional constraints on the values of core Statement attributes. Instead, implementations such as \
    the Atals of Variant Effects use the generic core ``Statement`` class and constrain its \
    ``proposition`` attribute to take an ``Experimental Variant Functional Impact Proposition``, then \
    apply any additional constraints over other core attruibutes to define an implementation schema for \
    this type of Statement. See `here <https://github.com/ga4gh/va-spec/blob/1.0-docs-refactor/tests/fixtures/Exp-Var-Func-Impact-Statement-01.yaml>`_ for a data example. 

.. _acmg-2015-profiles:

ACMG 2015 Aligned Profiles
@@@@@@@@@@@@@@@@@@@@@@@@@@

The following profiles align with terminology and curation conventions from the `ACMG 2015 Pathogenicity Interpretation Guidelines <https://pubmed.ncbi.nlm.nih.gov/25741868>`_ 

.. _variant-pathogenicity-statement-acmg-2015:

Variant Pathogenicity Statement (ACMG 2015)
###########################################

.. note:: This data class is at a **draft** maturity level and may \
    change in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A Statement describing the role of a variant in causing an inherited condition.
The structure and certain attribute constraints in this profile are defined to align with
curation and terminological conventions of the ACMG 2015 Variant Interpretation Guidelines.

**Information Model**

This profile applies the following constraints on top of the core :ref:`Statement<Statement>` class definition:

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
   *  - proposition
      -
      - :ref:`Variant Pathogenicity Proposition`
      - 1..1
      - A proposition about the pathogenicity of a varaint, the validity of which is assessed and reported by the Statement. A Statement can put forth the proposition as being true, false, or uncertain, and may provide an assessment of the level of confidence/evidence supporting this claim.
   *  - strength
      -
      - :ref:`MappableConcept` (nested enum: 'likely' | 'definitive')
      - 0..1
      - A term used to report the strength of a Proposition's assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be). The indicated enumeration is bound to the 'code' field in the Coding object nested inside the MappableConcept. 
   *  - classification
      -
      - :ref:`MappableConcept`  (nested enum: 'pathogenic' | 'likely pathogenic' | 'benign' | 'likely benign' | 'VUS')
      - 0..1
      - A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's Proposition, in terms of a classification of its subject. The indicated enumeration is bound to the 'code' field in the Coding object nested inside the MappableConcept. 

**Artifacts**
 - `Source YAML <https://github.com/ga4gh/va-spec/blob/latest/schema/va-spec/acmg-2015/pathogenicity-statement-profile-source.yaml>`_
 - `JSON Schema <https://github.com/ga4gh/va-spec/blob/latest/schema/va-spec/acmg-2015/json/VariantPathogenicityStatement>`_

-----

.. _experimental-variant-pathogenicity-functional-impact-evidence-line-acmg-2015:

Experimental Variant Pathogenicity Functional Impact Evidence Line (ACMG 2015)
##############################################################################

.. note:: This data class is at a **draft** maturity level and may \
    change in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

An Evidence Line that describes how information about the functional impact of a variant on a gene or
gene product was interpreted as evidence for or against the variant's pathogenicity.
The structure and certain attribute constraints in this profile are defined to align with
curation and terminological conventions of the ACMG 2015 Variant Interpretation Guidelines.

**Information Model**

Some EvidenceLine attributes are inherited from :ref:`EvidenceLine` and :ref:`InformationEntity`.

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
      - The ACMG guidelines that were followed to interpret variant functional impact information as evidence for or against the assessed variant's pathogenicity.
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
      - MUST be "EvidenceLine".
   *  - targetProposition
      -
      - :ref:`VariantPathogenicityProposition`
      - 0..1
      - A Variant Pathogenicity Proposition against which functional impact information was assessed, in determining the strength and direction of support this information provides as evidence.
   *  - hasEvidenceItems
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`StudyResult` | :ref:`Statement` | :ref:`EvidenceLine` | :ref:`iriReference`
      - 0..m
      - An individual piece of information that was evaluated as evidence in building the argument represented by an Evidence Line.
   *  - directionOfEvidenceProvided
      -
      - string (enum: 'supports' | 'disputes' | 'none')
      - 1..1
      - The direction of support that the Evidence Line is determined to provide toward its target Proposition.
   *  - strengthOfEvidenceProvided
      -
      - :ref:`MappableConcept` (nested enum: 'strong' | 'moderate' | 'supporting')
      - 0..1
      - The strength of support that an Evidence Line is determined to provide for or against the proposed pathogenicity of the assessed variant. Strength is evaluated relative to the direction indicated by the directionOfEvidenceProvided attribute. The indicated enumeration constrains the nested `MappableConcept.primaryCoding > Coding.code` attribute when capturing evidnece strength. *Conditional requirement*: if directionOfEvidenceProvided is either 'supports' or 'disputes', then this attribute is required. If it is 'none', then this attribute is not allowed.
   *  - scoreOfEvidenceProvided
      -
      - number
      - 0..1
      - A quantitative score indicating the strength of support that an Evidence Line is determined to provide for or against its target Proposition, evaluated relative to the direction indicated by the directionOfEvidenceProvided value.
   *  - evidenceOutcome
      -
      - :ref:`MappableConcept` (nested enum: PS3 | PS3_moderate | PS3_supporting | PS3_not_met | BS3 | BS3_moderate | BS3_supporting | BS3_not_met)
      - 0..1
      - A term summarizing the overall outcome of the evidence assessment represented by the Evidence Line, in terms of the direction and strength of support it provides for or against the target Proposition. The evidence outcome is a summary of the 'directionOfEvidenceProvided' and 'strengthOfEvidenceProvided' values, along with the specific ACMG criterion code used in these assessments. The indicated enumeration constrains the nested `MappableConcept.primaryCoding > Coding.code` attribute when capturing evidence outcomes. Note that if 'directionOfEvidenceProvided' is 'none', then the evidence outcome is 'not met' for the relevant criterion (e.g. 'PS3_not_met'). If 'directionOfEvidenceProvided' is 'supports' or 'disputes', then the outcome is 'met' for the relevant criterion, along with the strength of evidence provided. (e.g. 'PS3_moderate').

**Artifacts**
 - `Source YAML <https://github.com/ga4gh/va-spec/blob/latest/schema/va-spec/acmg-2015/pathogenicity-functional-impact-evidence-line-profile-source.yaml>`_
 - `JSON Schema <https://github.com/ga4gh/va-spec/blob/latest/schema/va-spec/acmg-2015/json/VariantPathogenicityFunctionalImpactEvidenceLine>`_

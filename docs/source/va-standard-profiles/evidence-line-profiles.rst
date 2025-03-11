.. _evidence-line-profiles:

Evidence Line Profiles
!!!!!!!!!!!!!!!!!!!!!!

Evidence Line Profiles specialize the core ``Evidence Line`` class to represent how specific types of information are interpreted as evidence for specific types of knowledge statements. The Evidence Line profiles included in v1 of the VA-Spec are named and defined to align with curation and terminological conventions of established community guidelines in a given knowledge domain - such as the `ACMG 2015 Variant Interpretation Guidelines <https://pubmed.ncbi.nlm.nih.gov/27993330/>`_ for pathogenicity classifications.

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


.. _experimental-variant-oncogenicity-functional-impact-evidence-line-ccv-2022:

Experimental Variant Oncogenicity Functional Impact Evidence Line (CCV 2022)
##############################################################################

.. note:: This data class is at a **draft** maturity level and may \
    change in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

An Evidence Line that describes how information about the functional impact of a variant on a gene or
gene product was interpreted as evidence for or against the variant's oncogenicity.
The structure and certain attribute constraints in this profile are defined to align with
curation and terminological conventions of the CCV 2022 interpretation guidelines.

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
      - :ref:`VariantOncogenicityProposition`
      - 0..1
      - A Variant Oncogenicity Proposition against which functional impact information was assessed, in determining the strength and direction of support this information provides as evidence.
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
      - :ref:`MappableConcept` (nested enum: OS2 | OS2_moderate | OS2_supporting | OS2_not_met | SBS2 | SBS2_moderate | SBS2_supporting | SBS2_not_met)
      - 0..1
      - A term summarizing the overall outcome of the evidence assessment represented by the Evidence Line, in terms of the direction and strength of support it provides for or against the target Proposition. The evidence outcome is a summary of the 'directionOfEvidenceProvided' and 'strengthOfEvidenceProvided' values, along with the specific CCV criterion code used in these assessments. The indicated enumeration constrains the nested `MappableConcept.primaryCoding > Coding.code` attribute when capturing evidence outcomes. Note that if 'directionOfEvidenceProvided' is 'none', then the evidence outcome is 'not met' for the relevant criterion (e.g. 'OS2_not_met'). If 'directionOfEvidenceProvided' is 'supports' or 'disputes', then the outcome is 'met' for the relevant criterion, along with the strength of evidence provided. (e.g. 'OS2_moderate').

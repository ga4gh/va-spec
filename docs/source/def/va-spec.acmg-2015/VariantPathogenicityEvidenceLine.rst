.. admonition:: Draft
    :class: warning

    May change significantly in future releases. See |maturity-model|.

**Computational Definition**

An Evidence Line that describes how a specific type of information was interpreted as evidence for or against a variant's pathogenicity. In the ACMG Framework, evidence is assessed by determining if a specific criterion (e.g. 'PM2') with a default strength (e.g. 'moderate') is 'met' or 'not met', and in some cases adjusting the default strength based on the quality and abundance of evidence.

**Information Model**


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
   *  - type
      -
      - string
      - 1..1
      - MUST be "EvidenceLine".
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
      - 1..1
      - The guidelines or rubrics followed in interpreting evidence, to determine the strength and direction of support that it provides for or against a variant's pathogenicity. While the ACMG Criteria themselves provide minimal guidance, typically a more detailed, disease- or gene- specific rubric is followed to determine if a given criterion was met, and how strongly (e.g. the ClinGen Hearing Loss Expert Panel guidelines for ACMG interpretations).
   *  - contributions
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Ordered">&#8595;</span>
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
   *  - targetProposition
      -
      - :ref:`VariantPathogenicityProposition` | :ref:`iriReference`
      - 0..1
      - A Variant Pathogenicity Proposition against which a specific type of evidence was assessed, to determine the strength and direction of support this evidence provides for or against the proposition's validity.
   *  - hasEvidenceItems
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`InformationEntity` | :ref:`iriReference`
      - 0..m
      - An individual piece of information that was evaluated as evidence in building the argument represented by an Evidence Line.
   *  - directionOfEvidenceProvided
      -
      - string
      - 1..1
      - The direction of support that the Evidence Line is determined to provide toward its target Proposition (supports, disputes, neutral)
   *  - strengthOfEvidenceProvided
      -
      - :ref:`MappableConcept` | :ref:`iriReference`
      - 0..1
      - The strength of support that an Evidence Line is determined to provide for or against the proposed pathogenicity of the assessed variant. Strength is evaluated relative to the direction indicated by the 'direction' attribute, and captured using a MappableConcept, whose nested 'code' field is bound to an enumerated set of values. Conditional requirement: if `direction` is either 'supports' or 'disputes', then this attribute is required. If it is 'neutral', then this attribute is not allowed.
   *  - scoreOfEvidenceProvided
      -
      - number
      - 0..1
      - A quantitative score indicating the strength of support that an Evidence Line is determined to provide for or against its target Proposition, evaluated relative to the direction indicated by the directionOfEvidenceProvided value.
   *  - evidenceOutcome
      -
      - :ref:`MappableConcept` | :ref:`iriReference`
      - 0..1
      - The evidence outcome provides a single string that summarizes 'direction' and 'strength' assessments, along with the specific ACMG criterion used in these assessments. Rules for constructing this string are as follows, and enforced by a regex constraint: (1) If a criterion is met and its default strength is not altered, the outcome is simply the criterion code (e.g. 'PM2' when the PM2 criteria is met with moderate strength); (2) If a criterion is met and its default strength is altered, the outcome is the criterion code plus the altered strength value (e.g. 'PS3_moderate' when PS3 is met with an adjusted moderate strength); (3)  If a specific criterion was assessed but not met, the outcome is the criterion code plus '_not_met' (e.g. 'PS3_not_met'); (4)  If the criteria associated with the 'methodType' were assessed, but none were met, the outcome is 'no_criteria_met'.

**Additional Constraints**

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - If property...
      - has value...
      - then property...
      - must...
   *  - *directionOfEvidenceProvided*
      - one of: **supports**, **disputes**
      - *strengthOfEvidenceProvided*
      - be provided
   *  - *specifiedBy.methodType*
      - **population_data_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|(BA1|BS1|PM2)(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **case_control_enrichment_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|(BS2|PM4)(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **null_variant_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|PVS1(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **same_amino_acid_change_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|PS1(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **mutational_hot_spot_and_functional_domain_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|PM1(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **protein_length_change_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|(PM4|BP3)(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **novel_missense_position_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|PM5(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **variant_spectrum_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|(PP2|BP1)(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **in_silico_functional_impact_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|(PP3|BP4)(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **predicted_silent_variant_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|BP7(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **functional_data_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|(PS3|BS3)(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **segregation_data_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|(PP1|BS4)(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **de_novo_occurrence_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|(PS2|PM6)(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **cis_trans_variant_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|(PM3|BP2)(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **reputable_source_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|(PP5|BP6)(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **phenotype_gene_specificity_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|PP4(_.+)?)$**
   *  - *specifiedBy.methodType*
      - **alternative_cause_assessment**
      - *evidenceOutcome.primaryCoding.code*
      - match the pattern **^(?:no_criteria_met|BP5(_.+)?)$**

If *evidenceOutcome.primaryCoding.code* must match the pattern **^(?:no_criteria_met|(?:[A-Z]+[0-9]+)_not_met)$**, then:

* *directionOfEvidenceProvided* must be: **neutral**


**Composes:** :ref:`EvidenceLine`

**Used in:** :ref:`VariantPathogenicityStatement`

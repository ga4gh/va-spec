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
      - :ref:`VariantPathogenicityProposition`
      - 0..1
      - A Variant Pathogenicity Proposition against which a specific type of evidence was assessed, to determine the strength and direction of support this evidence provides for or against the proposition's validity.
   *  - hasEvidenceItems
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`InformationEntity` | :ref:`iriReference`
      - 0..m
      - An individual piece of information that was evaluated as evidence in building the argument represented by an Evidence Line.
   *  - hasEvidenceLines
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`EvidenceLine` | :ref:`iriReference`
      - 0..m
      - A subordinate evidence-based argument that supports or disputes the validity of this Evidence Line's target Proposition. The strength and direction of this argument (whether it supports or disputes the proposition, and how strongly) is based on an interpretation of one or more pieces of information as evidence (i.e. 'Evidence Items').
   *  - directionOfEvidenceProvided
      -
      - string
      - 1..1
      - The direction of support that the Evidence Line is determined to provide toward its target Proposition (supports, disputes, neutral). For ACMG-based assessments, if a pathogenicity criterion is 'met' in the Evidence Line the direction is 'supports', if a benignity criterion is 'met' the direction is 'disputes', and if a criteria is 'not met' the direction is 'none'.
   *  - strengthOfEvidenceProvided
      -
      - :ref:`MappableConcept`
      - 0..1
      - The strength of support that an Evidence Line is determined to provide for or against the proposed pathogenicity of the assessed variant. Strength is evaluated relative to the direction indicated by the 'directionOfEvidenceProvided' attribute, and captured using a MappableConcept, whose nested 'code' field is bound to an enumerated set of values. Conditional requirement: if `directionOfEvidenceProvided` is either 'supports' or 'disputes', then this attribute is required. If it is 'none', then this attribute is not allowed.
   *  - qualityOfEvidenceProvided
      -
                        .. raw:: html

                            <span style="background-color: #D3D3D3; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Draft Maturity Level">D</span>
      - :ref:`MappableConcept`
      - 0..1
      - A term used to report the quality of the assessment of a Proposition taking into consideration the reliability of the method, the contributor's self-reporting of the rigor of the evaluation, and the overall robustness of the supporting or disputing evidence. This is useful when there is a consistent policy and authority that manages and a governing framework for evaluating the quality of evidence. Also known as trust rating, review status or ranking.
   *  - scoreOfEvidenceProvided
      -
      - number
      - 0..1
      - A quantitative score indicating the strength of support that an Evidence Line is determined to provide for or against its target Proposition, evaluated relative to the direction indicated by the directionOfEvidenceProvided value.
   *  - evidenceOutcome
      -
      - :ref:`MappableConcept`
      - 0..1
      - The evidence outcome provides a single string that summarizes 'directionOfEvidenceProvided' and 'strengthOfEvidenceProvided' assessments, along with the specific ACMG criterion used in these assessments. Rules for constructing this string are as follows, and enforced by a regex constraint: (1) If a criterion is met and its default strength is not altered, the outcome is simply the criterion code (e.g. 'PM2' when the PM2 criteria is met with moderate strength); (2) If a criterion is met and its default strength is altered, the outcome is the criterion code plus the altered strength value (e.g. 'PS3_moderate' when PS3 is met with an adjusted moderate strength); (3)  If a criterion is not met, the outcome is the criterion code plus the string 'not_met' (e.g. 'PS3_not_met').

**Conditional Constraints**

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - If property...
      - has value...
      - then property...
      - must...
   *  - ``directionOfEvidenceProvided``
      - one of: ``supports``, ``disputes``
      - ``strengthOfEvidenceProvided``
      - be provided
   *  - ``methodType``
      - ``Population Data Assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^(BA1|BS1|PM2)(_.+)?$``
   *  - ``methodType``
      - ``Case-Control Enrichment Assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^(BS2|PM4)(_.+)?$``
   *  - ``methodType``
      - ``Null variant assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^PVS1(_.+)?$``
   *  - ``methodType``
      - ``Same amino acid change assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^PS1(_.+)?$``
   *  - ``methodType``
      - ``Mutational hot spot and functional domain assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^PM1(_.+)?$``
   *  - ``methodType``
      - ``Protein length change assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^(PM4|BP3)(_.+)?$``
   *  - ``methodType``
      - ``Novel missense position assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^PM5(_.+)?$``
   *  - ``methodType``
      - ``Variant spectrum assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^(PP2|BP1)(_.+)?$``
   *  - ``methodType``
      - ``In silico functional impact assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^(PP3|BP4)(_.+)?$``
   *  - ``methodType``
      - ``Predicted silent variant assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^BP7(_.+)?$``
   *  - ``methodType``
      - ``Functional Data Assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^(PS3|BS3)(_.+)?$``
   *  - ``methodType``
      - ``Segregation Data Assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^(PP1|BS4)(_.+)?$``
   *  - ``methodType``
      - ``De Novo Data Assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^(PS2|PM6)(_.+)?$``
   *  - ``methodType``
      - ``Cis/trans variant assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^(PM3|BP2)(_.+)?$``
   *  - ``methodType``
      - ``Reputable Source Assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^(PP5|BP6)(_.+)?$``
   *  - ``methodType``
      - ``Phenotype-gene specificity assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^PP4(_.+)?$``
   *  - ``methodType``
      - ``Alternative cause assessment``
      - ``evidenceOutcome.primaryCoding.code``
      - match the pattern ``^BP5(_.+)?$``


**Composes:** :ref:`EvidenceLine`

**Used in:** :ref:`VariantPathogenicityStatement`

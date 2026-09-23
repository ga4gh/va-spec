.. admonition:: Draft
    :class: warning

    May change significantly in future releases. See |maturity-model|.

**Computational Definition**

Diagnostic statement for AMP/ASCO/CAP

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
      - 0..1
      - A specification that describes all or part of the process that led to creation of the Information Entity
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
      - :ref:`VariantDiagnosticProposition` | :ref:`iriReference`
      - 1..1
      - The possible fact against which evidence items contained in an Evidence Line were collectively evaluated, in determining the overall strength and direction of support they provide. For example, in an ACMG Guideline-based assessment of variant pathogenicity, the support provided by distinct lines of evidence are assessed against a target proposition that the variant is pathogenic for a specific disease.
   *  - hasEvidenceItems
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Statement` | :ref:`StudyResult` | :ref:`DataItem` | :ref:`iriReference`
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
      - The direction of support that the Evidence Line is determined to provide toward its target Proposition (supports, disputes, neutral)
   *  - strengthOfEvidenceProvided
      -
      - :ref:`MappableConcept` | :ref:`iriReference`
      - 0..1
      - The strength of support that an Evidence Line is determined to provide for or against its target Proposition, evaluated relative to the direction indicated by the directionOfEvidenceProvided value.
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
      - :ref:`MappableConcept` | :ref:`iriReference`
      - 0..1
      - A term summarizing the overall outcome of the evidence assessment represented by the Evidence Line, in terms of the direction and strength of support it provides for or against the target Proposition.

**Composes:** :ref:`AmpAscoCapEvidenceLine`

**Used in:** :ref:`VariantClinicalSignificanceStatement`

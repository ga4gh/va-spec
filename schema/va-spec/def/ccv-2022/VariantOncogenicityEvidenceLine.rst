.. admonition:: Draft
    :class: warning

    May change significantly in future releases. See |maturity-model|.

**Computational Definition**

An Evidence Line that describes how evidence for a variant was interpreted to determine if a specific CCV 2022 criterion code is met, and the strength that evidence this provides for or against the variant's oncogenicity. An Evidence Line that describes how a specific type of information was interpreted as evidence for or against a variant's oncogenicity. In the CCV Framework, evidence is assessed by determining if a specific criterion (e.g. 'OM2') with a default strength (e.g. 'moderate') is 'met' or 'not met', and in some cases adjusting the default strength based on the quality and abundance of evidence.

**Information Model**

This class refines :ref:`EvidenceLine`.

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
   *  - specifiedBy *(refined)*
      -
      - :ref:`Method` | :ref:`iriReference`
      - 1..1
      - The guidelines or rubrics followed in interpreting evidence, to determine the strength and direction of support that it provides for or against a variant's oncogenicity. While the CCV Criteria themselves provide minimal guidance, typically a more detailed, gene- or cancer- specific rubric is followed to determine if a given criterion was met, and how strongly.
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
   *  - targetProposition *(refined)*
      -
      - :ref:`VariantOncogenicityProposition`
      - 0..1
      - A Variant Oncogenicity Proposition against which a specific type of evidence was assessed, to determine the strength and direction of support this evidence provides for or against the proposition's validity.
   *  - hasEvidenceItems
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`StudyResult` | :ref:`Statement` | :ref:`EvidenceLine` | :ref:`iriReference`
      - 0..m
      - An individual piece of information that was evaluated as evidence in building the argument represented by an Evidence Line.
   *  - directionOfEvidenceProvided *(refined)*
      -
      - string
      - 1..1
      - The direction of support that the Evidence Line is determined to provide toward its target Proposition (supports, disputes, neutral). For CCV-based assessments, if a oncogenicity criterion is 'met' in the Evidence Line the direction is 'supports', if a benignity criterion is 'met' the direction is 'disputes', and if a criteria is 'not met' the direction is 'none'.
   *  - strengthOfEvidenceProvided *(refined)*
      -
      - :ref:`MappableConcept`
      - 0..1
      - The strength of support that an Evidence Line is determined to provide for or against the proposed oncogenicity of the assessed variant. Strength is evaluated relative to the direction indicated by the 'directionOfEvidenceProvided' attribute, and captured using a MappableConcept, whose nested 'code' field is bound to an enumerated set of values. Conditional requirement: if `directionOfEvidenceProvided` is either 'supports' or 'disputes', then this attribute is required. If it is 'none', then this attribute is not allowed.
   *  - scoreOfEvidenceProvided
      -
      - number
      - 0..1
      - A quantitative score indicating the strength of support that an Evidence Line is determined to provide for or against its target Proposition, evaluated relative to the direction indicated by the directionOfEvidenceProvided value.
   *  - evidenceOutcome *(refined)*
      -
      - :ref:`MappableConcept`
      - 0..1
      - The evidence outcome provides a single string that summarizes 'directionOfEvidenceProvided' and 'strengthOfEvidenceProvided' assessments, along with the specific CCV criterion used in these assessments. Rules for constructing this string are as follows, and enforced by a regex constraint: (1) If a criterion is met and its default strength is not altered, the outcome is simply the criterion code (e.g. 'OM2' when the OM2 criteria is met with moderate strength); (2) If a criterion is met and its default strength is altered, the outcome is the criterion code plus the altered strength value (e.g. 'OS2_moderate' when OS2 is met with an adjusted moderate strength); (3)  If a criterion is not met, the outcome is the criterion code plus the string 'not_met' (e.g. 'OS2_not_met').

**Used in:** :ref:`VariantOncogenicityStatement`

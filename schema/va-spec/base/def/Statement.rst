.. note:: This data class is at a **trial use** maturity level and may \
    change in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A claim of purported truth as made by a particular agent, on a particular occasion. Statements may be used to simply put forth a possible fact (i.e. a 'proposition') as true, or to provide a more nuanced assessment of the level of confidence or evidence supporting a particular proposition.

**Information Model**

Some Statement attributes are inherited from :ref:`InformationEntity`.

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
   *  - label
      - 
      - string
      - 0..1
      - A primary name for the entity.
   *  - description
      - 
      - string
      - 0..1
      - A free-text description of the Entity.
   *  - alternativeLabels
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
      - :ref:`Proposition`
      - 1..1
      - A possible fact that the Statement assesses or puts forth as true.
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
      - number
      - 0..1
      - A quantitative score that indicates the strength of a Proposition's assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be).  Depending on its implementation, a score may reflect how *confident* that agent is that the Proposition is true or false, or the *strength of evidence* they believe supports or disputes it.
   *  - classification
      - 
      - :ref:`MappableConcept`
      - 0..1
      - A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's proposition, in terms of a classification of its subject.
   *  - hasEvidenceLines
      - 
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`EvidenceLine`
      - 0..m
      - An evidence-based argument that supports or disputes the validity of the proposition that a Statement assesses or puts forth as true. The strength and direction of this argument (whether it supports or disputes the proposition, and how strongly) is based on an interpretation of one or more pieces of information as evidence (i.e. 'Evidence Items).

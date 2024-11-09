**Computational Definition**

A StudyResult that reports a functional impact score from a variant functional assay or study.

**Information Model**

Some ExperimentalVariantFunctionalImpactStudyResult attributes are inherited from :ref:`gks-core:StudyResult`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Field
      - Type
      - Limits
      - Description
   *  - id
      - string
      - 0..1
      - The 'logical' identifier of the Entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - label
      - string
      - 0..1
      - A primary name for the entity.
   *  - description
      - string
      - 0..1
      - A free-text description of the Entity.
   *  - alternativeLabels
      - string
      - 0..m
      - Alternative name(s) for the Entity.
   *  - extensions
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - contributions
      - :ref:`Contribution`
      - 0..m
      - Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
   *  - reportedIn
      - :ref:`Document` | :ref:`iriReference`
      - 0..m
      - A document in which the the Information Entity is reported.
   *  - dateAuthored
      - string
      - 0..1
      - Indicates when the information content expressed in the Information Entity was generated.
   *  - recordMetadata
      - :ref:`RecordMetadata`
      - 0..1
      - Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).
   *  - componentResult
      - :ref:`StudyResult`
      - 0..m
      - Another StudyResult comprised of data items about the same focus as its parent Result, but based on a more narrowly scoped analysis of the foundational data (e.g. an analysis based on data about a subset of the parent Results full study population) .
   *  - studyGroup
      - :ref:`StudyGroup`
      - 0..1
      - A description of a specific group or population of subjects interrogated in the ResearchStudy that produced the data captured in the StudyResult.
   *  - ancillaryResults
      - object
      - 0..1
      - 
   *  - qualityMeasures
      - object
      - 0..1
      - 
   *  - type
      - string
      - 1..1
      - MUST be "ExperimentalVariantFunctionalImpactStudyResult".
   *  - focusVariant
      - :ref:`MolecularVariation` | :ref:`iriReference`
      - 0..1
      - The genetic variant for which a functional impact score is generated.
   *  - functionalImpactScore
      - number
      - 0..1
      - The score of the variant impact measured in the assay or study.
   *  - specifiedBy
      - :ref:`Method` | :ref:`iriReference`
      - 0..1
      - The assay that was performed to generate the reported functional impact score.
   *  - sourceDataSet
      - :ref:`DataSet`
      - 0..m
      - The full data set that provided the reported the functional impact score. 

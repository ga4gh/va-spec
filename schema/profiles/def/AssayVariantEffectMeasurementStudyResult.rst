**Computational Definition**

A StudyResult that reports a variant effect score from a functional assay.

**Information Model**

Some AssayVariantEffectMeasurementStudyResult attributes are inherited from :ref:`gks.core-im:StudyResult`.

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
      - :ref:`Document` | :ref:`IRI`
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
      - MUST be "AssayVariantEffectMeasurementStudyResult".
   *  - focusVariant
      - :ref:`MolecularVariation` | :ref:`IRI`
      - 0..1
      - The human mapped representation of the variant that is the subject of the Statement.
   *  - score
      - number
      - 0..1
      - The score of the variant effect in the assay.
   *  - specifiedBy
      - :ref:`Method` | :ref:`IRI`
      - 0..1
      - The assay that was used to measure the variant effect with all the various properties
   *  - sourceDataSet
      - :ref:`DataSet`
      - 0..m
      - The full data set that this measurement is a part of

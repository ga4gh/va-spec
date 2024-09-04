**Computational Definition**

A StudyResult that reports measures related to the frequency of an Allele in a cohort

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
      - `Extension </ga4gh/schema/gks-common/1.x/data-types/json/Extension>`_
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - specifiedBy
      - `Method <../core-im/core.json#/$defs/Method>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 0..1
      - A specification that describes all or part of the process that led to creation of the Information Entity (e.g. a specific experimental protocol or data analysis specification that describe how data were generated, or an evidence interpretation guideline that describes steps taken to interpret data in making a variant pathogenicity classification).
   *  - contributions
      - `Contribution <../core-im/core.json#/$defs/Contribution>`_
      - 0..m
      - Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
   *  - dateAuthored
      - string
      - 0..1
      - Indicates when the information content expressed in the Information Entity was generated.
   *  - recordMetadata
      - `RecordMetadata <../core-im/core.json#/$defs/RecordMetadata>`_
      - 0..1
      - Provenance metadata about a specific concrete encoding/serialization of information (e.g. as a record in a specific data/knowledgebase, or an online digital resource) - as opposed to provenance about the abstract information content a record carries.
   *  - sourceDataSet
      - `DataSet <../core-im/core.json#/$defs/DataSet>`_
      - 0..m
      - A larger DataSet from which the content of the StudyResult was derived.
   *  - componentResult
      - `StudyResult <../core-im/core.json#/$defs/StudyResult>`_
      - 0..m
      - Another StudyResult comprised of data items about the same focus as its parent Result, but based on a more narrowly scoped analysis of the foundational data (e.g. an analysis based on data about a subset of the parent Results full study population) .
   *  - studyGroup
      - `StudyGroup <../core-im/core.json#/$defs/StudyGroup>`_
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
      - `MolecularVariation </ga4gh/schema/vrs/2.x/json/MolecularVariation>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 0..1
      - The human mapped representation of the variant that is the subject of the Statement.
   *  - score
      - number
      - 0..1
      - The score of the variant effect in the assay.
   *  - reportedIn
      - `Document <../core-im/core.json#/$defs/Document>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 1..m
      - The assay that was used to measure the variant effect with all the various properties

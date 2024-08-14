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
          - 1..1
          - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
       *  - label
          - string
          - 0..1
          - A primary name for the entity.
       *  - description
          - string
          - 0..1
          - A free-text description of the entity.
       *  - alternativeLabels
          - string
          - 0..m
          - Alternative name(s) for the Entity.
       *  - extensions
          - `Extension </ga4gh/schema/gks-common/1.x/data-types/json/Extension>`_
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - specifiedBy
          - `Method <../core-im/core.json#/$defs/Method>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
          - 0..1
          - A :ref:`Method` that describes all or part of the process through which the information was generated.
       *  - contributions
          - `Contribution <../core-im/core.json#/$defs/Contribution>`_
          - 0..m
          - A list of :ref:`Contribution` objects that describe the activities performed by agents upon this entity.
       *  - dateAuthored
          - string
          - 0..1
          - Indicates when the information content expressed in the Information Entity was generated.
       *  - recordMetadata
          - `RecordMetadata <../core-im/core.json#/$defs/RecordMetadata>`_
          - 0..1
          - Metadata that applies to a specific concrete record of information as encoded in a particular system.
       *  - sourceDataSet
          - `DataSet <../core-im/core.json#/$defs/DataSet>`_
          - 0..m
          - A larger Data Set from which the content of the Result was derived.
       *  - componentResult
          - `StudyResult <../core-im/core.json#/$defs/StudyResult>`_
          - 0..m
          - A Study Result comprised of data items about the same focus as its parent Result, but based on a analysis of a different subset of the data pertaining to that focus (e.g. data from analysis of a subset of the full Study Group).
       *  - studyGroup
          - `StudyGroup <../core-im/core.json#/$defs/StudyGroup>`_
          - 0..1
          - A structured description of specific population of subjects interrogated in the Research Study to produce the subset of data captured in the StudyResult.
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
       *  - isReportedIn
          - `Document <../core-im/core.json#/$defs/Document>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
          - 1..m
          - The assay that was used to measure the variant effect with all the various properties

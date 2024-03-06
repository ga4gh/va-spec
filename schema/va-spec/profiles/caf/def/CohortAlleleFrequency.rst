**Computational Definition**

A measure of the frequency of an Allele in a cohort.


    **Information Model**
    
Some CohortAlleleFrequency attributes are inherited from :ref:`va.core:InformationEntity`.

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
          - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
       *  - label
          - string
          - 0..1
          - A primary label for the entity.
       *  - description
          - string
          - 0..1
          - A free-text description of the entity.
       *  - extensions
          - `Extension <../../core-im/../../gks-common/core.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - type
          - string
          - 1..1
          - 
       *  - specifiedBy
          - `Method <../../core-im/core.json#/$defs/Method>`_ | `IRI <../../gks-common/core.json#/$defs/IRI>`_
          - 0..1
          - A :ref:`Method` that describes all or part of the process through which the information was generated.
       *  - contributions
          - `Contribution <../../core-im/core.json#/$defs/Contribution>`_
          - 0..m
          - 
       *  - isReportedIn
          - `Document <../../core-im/core.json#/$defs/Document>`_ | `IRI <../../gks-common/core.json#/$defs/IRI>`_
          - 0..m
          - A document in which the information content is expressed.
       *  - recordMetadata
          - None
          - 0..1
          - 
       *  - derivedFrom
          - object
          - 0..1
          - Information about the dataset from which the CohortAlleleFrequency was reported.
       *  - focusAllele
          - `Allele <../../../vrs/vrs.json#/$defs/Allele>`_ | string
          - 1..1
          - 
       *  - focusAlleleCount
          - integer
          - 1..1
          - 
       *  - locusAlleleCount
          - integer
          - 1..1
          - 
       *  - alleleFrequency
          - number
          - 1..1
          - 
       *  - cohort
          - object
          - 1..1
          - 
       *  - ancillaryResults
          - object
          - 0..1
          - 
       *  - qualityMeasures
          - object
          - 0..1
          - 
       *  - subcohortFrequency
          - :ref:`CohortAlleleFrequency`
          - 0..m
          - 

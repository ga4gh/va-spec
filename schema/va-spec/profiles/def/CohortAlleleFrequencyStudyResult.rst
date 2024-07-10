**Computational Definition**

A StudyResult that reports measures related to the frequency of an Allele in a cohort

    **Information Model**
    
Some CohortAlleleFrequencyStudyResult attributes are inherited from :ref:`va.core:StudyResult`.

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
          - `Extension <../core-im/../../gks-common/common.json#/$defs/Extension>`_
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - specifiedBy
          - `Method <../core-im/core.json#/$defs/Method>`_ | `IRI <../../gks-common/common-source.json#/$defs/IRI>`_
          - 0..1
          - A :ref:`Method` that describes all or part of the process through which the information was generated.
       *  - contributions
          - `Contribution <../core-im/core.json#/$defs/Contribution>`_
          - 0..m
          - A list of :ref:`Contribution` objects that describe the activities performed by agents upon this entity.
       *  - isReportedIn
          - `Document <../core-im/core.json#/$defs/Document>`_ | `IRI <../../gks-common/common-source.json#/$defs/IRI>`_
          - 0..m
          - A document in which the information content is expressed.
       *  - dateAuthored
          - string
          - 0..1
          - Indicates when the information content expressed in the Information Entity was generated.
       *  - recordMetadata
          - `RecordMetadata <../core-im/core.json#/$defs/RecordMetadata>`_
          - 0..1
          - Metadata that applies to a specific concrete record of information as encoded in a particular system.
       *  - dataItem
          - object
          - 0..1
          - An item of data that is included in the StudyResult because it pertains to the 'focus' of the result. This data can directly describe this 'focus' (e.g. the population frequency of an allele focus), or  represent metadata about how data about the 'focus' were generated (e.g the sequencing method used to  determine this allele frequency).
       *  - type
          - string
          - 1..1
          - MUST be "CohortAlleleFrequencyStudyResult".
       *  - sourceDataSet
          - `DataSet <../core-im/core.json#/$defs/DataSet>`_
          - 0..m
          - The dataset from which the CohortAlleleFrequencyStudyResult was reported.
       *  - focusAllele
          - `Allele <../../vrs/vrs.json#/$defs/Allele>`_ | string
          - 1..1
          - The specific subject or experimental unit in a Study that data in the StudyResult object is about. e.g. a particular variant in a population allele frequency dataset like ExAC or gnomAD.
       *  - focusAlleleCount
          - integer
          - 1..1
          - The number of occurrences of the focusAllele in the cohort.
       *  - locusAlleleCount
          - integer
          - 1..1
          - The number of occurrences of alleles at the locus in the cohort (count of all alleles at this locus, sometimes referred to as "allele number")
       *  - alleleFrequency
          - number
          - 1..1
          - The frequency of the focusAllele in the cohort.
       *  - cohortStudyGroup
          - `StudyGroup <../core-im/core.json#/$defs/StudyGroup>`_
          - 1..1
          - The cohort from which the frequency was derived.
       *  - ancillaryResults
          - object
          - 0..1
          - Ancillary results that may be associated with the CohortAlleleFrequency, providing additional context or information.               
       *  - subCohortFrequency
          - :ref:`CohortAlleleFrequencyStudyResult`
          - 0..m
          - A list of CohortAlleleFrequency objects describing subcohorts of the cohort currently being described. This creates a recursive relationship and subcohorts can be further subdivided into more subcohorts. This enables, for example, the description of different ancestry groups and sexes among those ancestry groups.                    

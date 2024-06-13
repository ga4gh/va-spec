**Computational Definition**

A collection of data items from a single study that are about a particular subject or experimental unit in the study, along with optional provenance information describing how these data items were generated. StudyResult objects provide a flexible and useful way to summarize a subset of data items from a larger study that are cited as evidence in curation workflows that generate higher order knowledge about a particular variant or other entity.

    **Information Model**
    
Some StudyResult attributes are inherited from :ref:`InformationEntity`.

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
          - A primary label for the entity.
       *  - description
          - string
          - 0..1
          - A free-text description of the entity.
       *  - extensions
          - `Extension <../../gks-common/common.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - type
          - string
          - 1..1
          - MUST be "InformationEntity".
       *  - specifiedBy
          - :ref:`Method` | `IRI <../../gks-common/common.json#/$defs/IRI>`_
          - 0..1
          - A :ref:`Method` that describes all or part of the process through which the information was generated.
       *  - contributions
          - :ref:`Contribution`
          - 0..m
          - A list of :ref:`Contribution` objects that describe the activities performed by agents upon this entity.
       *  - isReportedIn
          - :ref:`Document` | `IRI <../../gks-common/common.json#/$defs/IRI>`_
          - 0..m
          - A document in which the information content is expressed.
       *  - dateAuthored
          - string
          - 0..1
          - Indicates when the information content expressed in the Information Entity was generated.
       *  - recordMetadata
          - None
          - 0..1
          - Metadata that applies to a specific concrete record of information as encoded in a particular system.
       *  - focus
          - :ref:`Entity`
          - 0..1
          - The specific subject or experimental unit in a Study that data in the StudyResult object is about. e.g. a particular variant in a population allele frequency dataset like ExAC or gnomAD.
       *  - dataItems
          - :ref:`DataItem`
          - 0..m
          - A Data Item  that is included in the StudyResult because it pertains to the entity that is the 'focus'. This data can directly describe this focus, or represent metadata about data in the Result were generated.
       *  - sourceDataSet
          - {'$ref': '#/$defs/DataSet'}
          - 0..1
          - A larger Data Set from which the content of the Result was derived.
       *  - componentResult
          - :ref:`StudyResult`
          - 0..m
          - A Study Result comprised of data items about the same focus as its parent Result, but based on a analysis of a different subset of the data pertaining to that focus (e.g. data fron analysis of a subset of the full Study Group).
       *  - studyGroup
          - {'$ref': '#/$defs/StudyGroup'}
          - 0..1
          - A structured description of specific population of subjects interrogated in the Research Study to produce the subset of data captured in the StudyResult.

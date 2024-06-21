**Computational Definition**

A collection of related data items or records that are organized together in a common format or structure, to enable their computational manipulation as a unit.

    **Information Model**
    
Some DataSet attributes are inherited from :ref:`InformationEntity`.

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
       *  - derivedFrom
          - :ref:`InformationEntity`
          - 0..m
          - Another Information Entity from which this Information Entity is derived, in whole or in part.
       *  - recordMetadata
          - None
          - 0..1
          - Metadata that applies to a specific concrete record of information as encoded in a particular system.
       *  - subtype
          - `Coding <../../gks-common/common.json#/$defs/Coding>`_
          - 0..1
          - A specific type of data set the DataSet object represents (e.g. a clinical data set, a sequencing data set, a gene expression data set, a genome annotation data set)
       *  - releaseDate
          - string
          - 0..1
          - Indicates when a version of a Data Set was formally released.
       *  - version
          - string
          - 0..1
          - The version of the Data Set, as assigned by its creator.
       *  - license
          - string
          - 0..1
          - A license that dictates legal permissions for how the Data Set can be used - referenced by a URL where possible.

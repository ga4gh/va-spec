**Computational Definition**

An InformationEntity representing an individual piece of data, generated/acquired through methods  which reliably produce truthful information about something.

    **Information Model**
    
Some DataItem attributes are inherited from :ref:`InformationEntity`.

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
          - `Extension <../../gks-common/core.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - type
          - string
          - 1..1
          - Must be "DataItem"
       *  - specifiedBy
          - :ref:`Method` | `IRI <../../gks-common/core.json#/$defs/IRI>`_
          - 0..1
          - A :ref:`Method` that describes all or part of the process through which the information was generated.
       *  - contributions
          - :ref:`Contribution`
          - 0..m
          - 
       *  - isReportedIn
          - :ref:`Document` | `IRI <../../gks-common/core.json#/$defs/IRI>`_
          - 0..m
          - A document in which the information content is expressed.
       *  - recordMetadata
          - None
          - 0..1
          - 
       *  - subtype
          - `Coding <../../gks-common/core.json#/$defs/Coding>`_
          - 0..1
          - A specific type of data the DataItem object represents (e.g. a specimen count, a  patient weight, an allele frequency, a p-value, a confidence score)
       *  - value
          - string
          - 1..1
          - 
       *  - unit
          - {'$ref': '../../gks-common/core.json#/$defs/Coding'}
          - 0..1
          - 

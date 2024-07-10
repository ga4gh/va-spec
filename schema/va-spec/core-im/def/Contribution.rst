**Computational Definition**

An action taken by an agent in contributing to the creation, modification, assessment, or deprecation of a particular entity (e.g. a Statement, EvidenceLine, DataItem, Publication, etc.)

    **Information Model**
    
Some Contribution attributes are inherited from :ref:`Activity`.

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
          - `Extension <../../gks-common/common.json#/$defs/Extension>`_
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - subtype
          - {'$ref': '../../gks-common/common-source.json#/$defs/Coding'}
          - 0..1
          - A more specific type of activity that an Activity object may represent.
       *  - date
          - string
          - 0..1
          - The date that the Activity was completed. The date SHOULD be formatted as a date string in ISO format "YYYY-MM-DD".
       *  - specifiedBy
          - :ref:`Method`
          - 0..m
          - A method that was followed in performing an Activity, that describes how it was executed.
       *  - type
          - string
          - 1..1
          - MUST be "Contribution".
       *  - contributor
          - :ref:`Agent`
          - 1..1
          - The agent that made the contribution.
       *  - activityType
          - `Coding <../../gks-common/common-source.json#/$defs/Coding>`_
          - 0..1
          - SHOULD describe a concept descending from the Contributor Role Ontology.

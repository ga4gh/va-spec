**Computational Definition**

An action taken by an agent in contributing to the creation, modification, assessment, or deprecation of a particular entity (e.g. a Statement, EvidenceLine, DataItem, Publication, etc.)

    **Information Model**
    
Some Contribution attributes are inherited from :ref:`gks.common:Entity`.

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
          - 0..1
          - MUST be "Contribution".
       *  - contributor
          - :ref:`Agent`
          - 0..1
          - The agent that made the contribution.
       *  - date
          - string
          - 0..1
          - The date on which the contribution was made. The date SHOULD be formatted as a date string in ISO format "YYYY-MM-DD".
       *  - contributionMadeTo
          - :ref:`InformationEntity`
          - 0..1
          - The artifact toward which the contribution was made.
       *  - activity
          - `Coding <../../gks-common/common.json#/$defs/Coding>`_
          - 0..1
          - SHOULD describe a concept descending from the Contributor Role Ontology.

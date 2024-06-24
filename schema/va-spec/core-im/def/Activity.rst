**Computational Definition**

An action or set of actions performed by an agent, that occurs over a period of time. Activities may use, generate, modify, move, or destroy one or more entities.

    **Information Model**
    
Some Activity attributes are inherited from :ref:`gks.common:Entity`.

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
       *  - mappings
          - `ConceptMapping <../../gks-common/common.json#/$defs/ConceptMapping>`_
          - 0..m
          - A list of mappings to concepts in terminologies or code systems. Each mapping should include a coding and a relation.
       *  - extensions
          - `Extension <../../gks-common/common.json#/$defs/Extension>`_
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - subtype
          - {'$ref': '../../gks-common/common.json#/$defs/Coding'}
          - 0..1
          - A more specific type of activity that an Activity object may represent.
       *  - date
          - string
          - 0..1
          - The date (and possibly specific time) that the Activity was performed. If tracking time more precisely, use this attribute to capture when the activity completed.
       *  - performedBy
          - :ref:`Agent`
          - 0..m
          - An Agent who contributed to executing the Activity.
       *  - specifiedBy
          - :ref:`Method`
          - 0..m
          - A method that was followed in performing an Activity, that describes how it was executed.

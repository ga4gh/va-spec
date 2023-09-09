**Computational Definition**

A Statement (aka ‘Assertion’) represents a claim of purported truth as made by a particular agent,  on a particular occasion.

    **Information Model**
    
Some Statement attributes are inherited from :ref:`InformationEntity`.

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
          - `Extension <core.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - type
          - string
          - 1..1
          - 
       *  - specified_by
          - :ref:`Method` | `IRI <core.json#/$defs/IRI>`_
          - 0..1
          - A :ref:`Method` that describes all or part of the process through which the information was generated.
       *  - contributions
          - :ref:`Contribution`
          - 0..m
          - 
       *  - is_reported_in
          - :ref:`Document` | `IRI <core.json#/$defs/IRI>`_
          - 0..m
          - A document in which the information content is expressed.
       *  - record_metadata
          - `RecordMetadata <core.json#/$defs/RecordMetadata>`_
          - 0..1
          - 
       *  - subject
          - <undefined>
          - 1..1
          - The subject of the Statement.
       *  - predicate
          - string
          - 0..1
          - The predicate of the Statement.
       *  - object
          - <undefined>
          - 0..1
          - The object of the Statement.
       *  - qualifiers
          - <undefined>
          - 0..1
          - Additional, optional properties that may qualify the Statement.
       *  - direction
          - string
          - 1..1
          - The direction of this statement with respect to the statement predicate.
       *  - strength
          - `Coding <core.json#/$defs/Coding>`_ | `IRI <core.json#/$defs/IRI>`_
          - 0..1
          - A term indicating the overall strength of support for the Statement based on all evidence assessed.
       *  - conclusion
          - `Coding <core.json#/$defs/Coding>`_ | `IRI <core.json#/$defs/IRI>`_
          - 0..1
          - The conclusion associated with the statement.

**Computational Definition**

An InformationEntity representing an individual piece of data, generated/acquired through methods  which reliably produce truthful information about something.

**Information Model**

Some DataItem attributes are inherited from :ref:`Entity`.

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
   *  - type
      - string
      - 1..1
      - The schema class that is instantiated by the data object. Must be the name of a class from  the VA schema.
   *  - label
      - string
      - 0..1
      - 
   *  - extensions
      - `Extension <core.json#/$defs/Extension>`_
      - 0..m
      - 
   *  - description
      - string
      - 0..1
      - A free-text description of the InformationEntity.
   *  - confidence_level
      - `Coding <core.json#/$defs/Coding>`_
      - 0..1
      - A coded term describing the strength of support that the information the statement represents is true.
   *  - confidence_score
      - :ref:`DataItem`
      - 0..1
      - A quantitative score reflecting the degree of confidence that the information  the information entity represents is true.
   *  - method
      - :ref:`Method` | `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - A :ref:`Method` that describes all or part of the process through which the information was generated.
   *  - contributions
      - :ref:`Contribution`
      - 0..m
      - 
   *  - is_reported_in
      - :ref:`Document` | `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - A document in which the information content is expressed.
   *  - record_metadata
      - `RecordMetadata <core.json#/$defs/RecordMetadata>`_
      - 0..1
      - 
   *  - value
      - string
      - 1..1
      - The value of the data item
   *  - unit
      - {'$ref': 'core.json#/$defs/Coding'}
      - 0..1
      - 

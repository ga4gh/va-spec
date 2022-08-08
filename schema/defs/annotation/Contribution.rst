**Computational Definition**

The sum of all actions taken by a single agent in contributing to the creation, modification,  assessment, or deprecation of a particular entity (e.g. a Statement, EvidenceLine, DataItem,  Publication, etc.)

**Information Model**

Some Contribution attributes are inherited from :ref:`Entity`.

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
      - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
   *  - type
      - string
      - 1..1
      - MUST be "Contribution".
   *  - label
      - string
      - 0..1
      - 
   *  - extensions
      - `Extension <core.json#/$defs/Extension>`_
      - 0..m
      - 
   *  - agent
      - :ref:`Agent`
      - 0..1
      - 
   *  - date
      - string
      - 0..1
      - 
   *  - role
      - string
      - 0..1
      - 

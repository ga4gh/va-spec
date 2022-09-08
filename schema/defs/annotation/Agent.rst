**Computational Definition**

An autonomous actor (person, organization, or computational agent) that bears some form of responsibility for an activity taking place, for the existence of an entity, or for  another agent’s activity.

**Information Model**

Some Agent attributes are inherited from :ref:`Entity`.

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
      - MUST be "Agent".
   *  - label
      - string
      - 0..1
      - 
   *  - extensions
      - `Extension <core.json#/$defs/Extension>`_
      - 0..m
      - 
   *  - name
      - string
      - 0..1
      - 
   *  - subtype
      - `Coding <core.json#/$defs/Coding>`_
      - 0..1
      - A specific type of agent the Agent object represents (e.g. a person, organization,  software agent)

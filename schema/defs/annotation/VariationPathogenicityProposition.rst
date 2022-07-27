**Computational Definition**

More to come!

**Information Model**

Some VariationPathogenicityProposition attributes are inherited from :ref:`Entity`.

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
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system.
   *  - type
      - string
      - 1..1
      - MUST be "VariationPathogenicityProposition"
   *  - variation
      - `CategoricalVariation <catvars.json#/$defs/CategoricalVariation>`_
      - 0..1
      - The :ref:`ValueEntity` about which the Proposition is made.
   *  - association
      - string
      - 0..1
      - The relationship asserted to hold between the subject and the object of the  Proposition.
   *  - condition
      - `Condition <core.json#/$defs/Condition>`_
      - 0..1
      - A ValueEntity that is related to the subject of a Proposition via its predicate.

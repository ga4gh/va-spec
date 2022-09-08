**Computational Definition**

A proposition describing the role of a variation in causing or preventing a germline disease condition.

**Information Model**

Some VariationGermlinePathogenicityProposition attributes are inherited from :ref:`Entity`.

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
      - The 'logical' identifier of the entity in the system of record, and MUST be represented as a CURIE. This 'id' is unique within a given system, but may also refer to an 'id' for the shared concept in  another system (represented by namespace, accordingly).
   *  - type
      - string
      - 1..1
      - MUST be "VariationGermlinePathogenicityProposition"
   *  - subject
      - `Variation <vrs.json#/definitions/Variation>`_ | `CategoricalVariation <catvars.json#/$defs/CategoricalVariation>`_ | `CURIE <core.json#/$defs/CURIE>`_
      - 1..1
      - The `Variation` or `CategoricalVariation` about which the Proposition is made.
   *  - predicate
      - string
      - 1..1
      - The relationship asserted to hold between the variation (subject) and  the condition (object) of the Proposition.
   *  - object
      - `Condition <core.json#/$defs/Condition>`_ | `Disease <core.json#/$defs/Disease>`_ | `Phenotype <core.json#/$defs/Phenotype>`_
      - 1..1
      - A ValueEntity that is related to the subject of a Proposition via its predicate.

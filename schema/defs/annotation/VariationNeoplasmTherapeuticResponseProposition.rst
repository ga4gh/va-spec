**Computational Definition**

A :ref:`Proposition` describing the role of a variation in modulating the response of a neoplasm to one or more therapeutics.

**Information Model**

Some VariationNeoplasmTherapeuticResponseProposition attributes are inherited from :ref:`Entity`.

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
      - The schema class that is instantiated by the data object. Must be the name of a class from  the VA schema.
   *  - subject
      - `Variation <vrs.json#/definitions/Variation>`_ | `CategoricalVariation <catvars.json#/$defs/CategoricalVariation>`_ | `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - The `Variation` or `CategoricalVariation` about which the Proposition is made.
   *  - predicate
      - string
      - 0..1
      - The relationship asserted to hold between the subject and the object of the  Proposition.
   *  - object
      - `Therapeutic <core.json#/$defs/Therapeutic>`_ | `CombinationTherapeuticCollection <core.json#/$defs/CombinationTherapeuticCollection>`_ | `SubstituteTherapeuticCollection <core.json#/$defs/SubstituteTherapeuticCollection>`_
      - 0..1
      - The therapeutic(s) to which the neoplasm response is modulated in the presence of the `subject` variation.
   *  - neoplasm_type_qualifier
      - `Condition <core.json#/$defs/Condition>`_ | `Disease <core.json#/$defs/Disease>`_ | `Phenotype <core.json#/$defs/Phenotype>`_
      - 0..1
      - The neoplasm for which the presence of the indicated variation is relevant.

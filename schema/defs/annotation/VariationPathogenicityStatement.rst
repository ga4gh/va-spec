**Computational Definition**

A :ref:`Statement` describing the pathogenicity of a variation.

**Information Model**

Some VariationPathogenicityStatement attributes are inherited from :ref:`Entity`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description
   *  - _id
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system.
   *  - type
      - string
      - 1..1
      - MUST be "VariationPathogenicityStatement".
   *  - extensions
      - `Extension <core.json#/$defs/Extension>`_
      - 0..m
      - 
   *  - confidence_level
      - string
      - 0..1
      - A qualitative term describing the degree of confidence held by the creator of the information entity,  that the information it represents is true.
   *  - confidence_score
      - DataItem
      - 0..1
      - A quantitative score reflecting the degree of confidence held by the creator of the information  entity, that the information it represents is true.
   *  - target_proposition
      - :ref:`Proposition`
      - 0..1
      - The Proposition about which the Statement is made.
   *  - conclusion
      - string
      - 0..1
      - The conclusion drawn from the statement proposition, significance, confidence level, and/or  confidence score.
   *  - significance
      - string
      - 0..1
      - The significance of this statement with respect to the target proposition.
   *  - classification
      - string
      - 0..1
      - The conclusion drawn from the statement proposition, significance, confidence level, and/or  confidence score.

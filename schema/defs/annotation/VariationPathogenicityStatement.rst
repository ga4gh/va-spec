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
   *  - id
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..1
      - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system.
   *  - type
      - string
      - 1..1
      - MUST be "VariationPathogenicityStatement".
   *  - label
      - string
      - 0..1
      - 
   *  - extensions
      - `Extension <core.json#/$defs/Extension>`_
      - 0..m
      - 
   *  - record_metadata
      - `RecordMetadata <core.json#/$defs/RecordMetadata>`_
      - 0..1
      - 
   *  - description
      - string
      - 0..1
      - A free-text description of the InformationEntity.
   *  - confidence_level
      - string
      - 0..1
      - A qualitative term describing the degree of confidence held by the creator of the information entity,  that the information it represents is true.
   *  - confidence_score
      - :ref:`DataItem`
      - 0..1
      - A quantitative score reflecting the degree of confidence held by the creator of the information  entity, that the information it represents is true.
   *  - method
      - :ref:`Method`
      - 0..1
      - A :ref:`Method` that describes all or part of the process through which the information was generated.
   *  - contributions
      - :ref:`Contribution`
      - 0..m
      - 
   *  - significance
      - string
      - 0..1
      - The significance of this statement with respect to the target proposition.
   *  - condition_descriptor
      - `ConditionDescriptor <vod.json#/$defs/ConditionDescriptor>`_
      - 0..1
      - A descriptor characterizing the condition impacted by the variation.
   *  - variation_descriptor
      - `CategoricalVariationDescriptor <vod.json#/$defs/CategoricalVariationDescriptor>`_
      - 0..1
      - A descriptor characterizing the variation impacting the condition.
   *  - classification
      - `LabeledEntity <core.json#/$defs/LabeledEntity>`_
      - 0..1
      - The conclusion drawn from the statement proposition, significance, confidence level, and/or  confidence score.
   *  - target_proposition
      - :ref:`VariationPathogenicityProposition`
      - 0..1
      - The Proposition about which the Statement is made.

**Computational Definition**

A :ref:`Statement` describing the role of a variation in causing or protecting against a germline Condition.

**Information Model**

Some VariationGermlineConditionStatement attributes are inherited from :ref:`Entity`.

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
      - MUST be "VariationPathogenicityStatement".
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
   *  - strength
      - `Coding <core.json#/$defs/Coding>`_
      - 0..1
      - A coded term describing the strength of support that the information the statement represents is true.
   *  - confidence_score
      - :ref:`DataItem`
      - 0..1
      - A quantitative score reflecting the degree of confidence that the information  the information entity represents is true.
   *  - method
      - :ref:`Method`
      - 0..1
      - A :ref:`Method` that describes all or part of the process through which the information was generated.
   *  - contributions
      - :ref:`Contribution`
      - 0..m
      - 
   *  - is_reported_in
      - :ref:`Document`
      - 0..m
      - A document in which the information content is expressed.
   *  - record_metadata
      - `RecordMetadata <core.json#/$defs/RecordMetadata>`_
      - 0..1
      - 
   *  - direction
      - string
      - 0..1
      - The direction of this statement with respect to the target proposition.
   *  - subject_descriptor
      - `CategoricalVariationDescriptor <vod.json#/$defs/CategoricalVariationDescriptor>`_
      - 0..1
      - A descriptor characterizing the variation impacting the condition.
   *  - variation_origin
      - string
      - 0..1
      - A representation of whether the subject variation is inherited (germline) or acquired (somatic).
   *  - object_descriptor
      - `ConditionDescriptor <vod.json#/$defs/ConditionDescriptor>`_
      - 0..1
      - A descriptor characterizing the condition impacted by the variation.
   *  - classification
      - `Coding <core.json#/$defs/Coding>`_
      - 0..1
      - The conclusion drawn from the statement proposition, direction, strength, and/or  confidence score.
   *  - target_proposition
      - :ref:`VariationGermlineConditionProposition`
      - 0..1
      - The Proposition about which the Statement is made.

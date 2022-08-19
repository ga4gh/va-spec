**Computational Definition**

A :ref:`Statement` describing the role of a variation in modulating the response of a neoplasm to one or more therapeutics.

**Information Model**

Some VariationNeoplasmTherapeuticResponseStatement attributes are inherited from :ref:`Entity`.

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
   *  - strength
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
   *  - target_proposition
      - :ref:`Proposition`
      - 0..1
      - The Proposition about which the Statement is made.
   *  - conclusion
      - `Coding <core.json#/$defs/Coding>`_
      - 0..1
      - The conclusion drawn from the statement proposition, direction, strength, and/or  confidence score.
   *  - direction
      - string
      - 0..1
      - The direction of this statement with respect to the target proposition.
   *  - subject_descriptor
      - `CategoricalVariationDescriptor <vod.json#/definitions/CategoricalVariationDescriptor>`_
      - 0..1
      - A descriptor characterizing the variation impacting the condition.
   *  - variation_origin
      - string
      - 0..1
      - A representation of whether the subject variation is inherited (germline) or acquired (somatic).
   *  - neoplasm_type_descriptor
      - `ConditionDescriptor <vod.json#/definitions/ConditionDescriptor>`_
      - 0..1
      - A descriptor characterizing the neoplasm type for which the indicated variation is relevant.
   *  - object_descriptor
      - `TherapeuticDescriptor <vod.json#/definitions/TherapeuticDescriptor>`_ | `TherapeuticCollectionDescriptor <vod.json#/definitions/TherapeuticCollectionDescriptor>`_
      - 0..1
      - A descriptor characterizing the therapeutic(s) to which the neoplasm response is modulated in  the presence of the `subject` variation.

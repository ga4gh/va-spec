**Computational Definition**

An Evidence Line that describes the strength and direction of support provided by one or more  evidence items for or against the pathogenicity of a variant for a particular disease. 

**Information Model**

Some PathogenicityEvidenceLine attributes are inherited from :ref:`gks-core:EvidenceLine`.

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
      - The 'logical' identifier of the Entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - label
      - string
      - 0..1
      - A primary name for the entity.
   *  - description
      - string
      - 0..1
      - A free-text description of the Entity.
   *  - alternativeLabels
      - string
      - 0..m
      - Alternative name(s) for the Entity.
   *  - extensions
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - contributions
      - :ref:`Contribution`
      - 0..m
      - Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
   *  - reportedIn
      - :ref:`Document` | :ref:`iriReference`
      - 0..m
      - A document in which the the Information Entity is reported.
   *  - dateAuthored
      - string
      - 0..1
      - Indicates when the information content expressed in the Information Entity was generated.
   *  - derivedFrom
      - :ref:`InformationEntity`
      - 0..m
      - Another Information Entity from which this Information Entity is derived, in whole or in part.
   *  - recordMetadata
      - :ref:`RecordMetadata`
      - 0..1
      - Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).
   *  - scoreOfEvidenceProvided
      - number
      - 0..1
      - A quantitative score indicating the strength of support that an Evidence Line is determined to provide for or against its target Proposition, evaluated relative to the direction indicated by the directionOfEvidenceProvided value.
   *  - type
      - string
      - 1..1
      - MUST be "PathogenicityEvidenceLine".
   *  - hasEvidenceItems
      - :ref:`InformationEntity`
      - 0..m
      - An Information Entity that was assessed as evidence in determining the possible  pathogenicity of a variant (e.g. a Functional Impact Study Statement or Study Reuslt)
   *  - directionOfEvidenceProvided
      - string
      - 0..1
      - The direction of support that the Evidence Line is determined to provide for its target Variant Pathogenicity Proposition, based on assessment of its evidence items (i.e. does the  evidence line support or dispute the possible pathogenicity of the subject variant, or remain neutral)
   *  - strengthOfEvidenceProvided
      - string
      - 0..1
      - The strength of support that an Evidence Line is determined to provide for or against the pathogenicity of the assessed variant. Strength is evaluated relative to the direction indicated by the directionOfEvidenceProvided attribute.
   *  - targetProposition
      - :ref:`VariantPathogenicityProposition`
      - 0..1
      - The possible fact toward which the strength and direction of evidence provided by functional assay data was evaluated (here, a proposition that the assessed variant may be pathogenic for a particular disease).      
   *  - specifiedBy
      - :ref:`Method` | :ref:`iriReference`
      - 0..1
      - A method that specifies how evidence items used in the Evidence Line are to be evaluated and weighed as evidence for or against the pathogenicity of the assessed variant.

**Computational Definition**

A collection of individuals or specimens from the same taxonomic class, selected for analysis in a scientific  study based on their exhibiting one or more common characteristics  (e.g. ethnicity, race, country of origin,  clinical history, age, gender, geographic location, income, etc.)

    **Information Model**
    
Some StudyGroup attributes are inherited from :ref:`gks.core:Entity`.

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
       *  - label
          - string
          - 0..1
          - A primary label for the entity.
       *  - description
          - string
          - 0..1
          - A free-text description of the entity.
       *  - extensions
          - `Extension <../../gks-common/core.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - memberCount
          - integer
          - 0..1
          - the total number of individual members in the study group
       *  - isSubsetOf
          - :ref:`StudyGroup`
          - 0..m
          - A larger study group of which this study group represents a subset.
       *  - characteristics
          - :ref:`Characterisitc`
          - 0..m
          - A feature or characteristic shared by all members of the study group, and representing a criteria for  membership in the group.

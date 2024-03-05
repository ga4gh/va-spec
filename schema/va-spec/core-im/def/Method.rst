**Computational Definition**

A set of instructions that specify how to achieve some objective (e.g. experimental protocols,  curation guidelines, rule sets, etc.)

    **Information Model**
    
Some Method attributes are inherited from :ref:`gks.core:Entity`.

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
       *  - type
          - string
          - 0..1
          - MUST be "Method".
       *  - isReportedIn
          - `IRI <../../gks-common/core.json#/$defs/IRI>`_ | :ref:`Document`
          - 0..1
          - 
       *  - subtype
          - `Coding <../../gks-common/core.json#/$defs/Coding>`_
          - 0..1
          - A more specific type of entity the method represents (e.g. Variant Interpretation Guideline,  Experimental Protocol)

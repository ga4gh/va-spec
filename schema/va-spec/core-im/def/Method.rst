**Computational Definition**

A set of instructions that specify how to achieve some objective (e.g. experimental protocols, curation guidelines, rule sets, etc.)

    **Information Model**
    
Some Method attributes are inherited from :ref:`gks.common:Entity`.

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
          - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
       *  - label
          - string
          - 0..1
          - A primary name for the entity.
       *  - description
          - string
          - 0..1
          - A free-text description of the entity.
       *  - mappings
          - `ConceptMapping <../../gks-common/common.json#/$defs/ConceptMapping>`_
          - 0..m
          - A list of mappings to concepts in terminologies or code systems. Each mapping should include a coding and a relation.
       *  - extensions
          - `Extension <../../gks-common/common.json#/$defs/Extension>`_
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - type
          - string
          - 0..1
          - MUST be "Method".
       *  - isReportedIn
          - `IRI <../../gks-common/common.json#/$defs/IRI>`_ | :ref:`Document`
          - 0..1
          - 
       *  - subtype
          - `Coding <../../gks-common/common.json#/$defs/Coding>`_
          - 0..1
          - A more specific type of entity the method represents (e.g. Variant Interpretation Guideline, Experimental Protocol)
       *  - license
          - string
          - 0..1
          - A particular license that dictates legal permissions for how a published method (e.g. an experimental protocol, workflow specification, curation guideline) can be used.

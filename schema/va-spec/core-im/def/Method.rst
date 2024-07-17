**Computational Definition**

A set of instructions that specify how to achieve some objective (e.g. experimental protocols, curation guidelines, rule sets, etc.)

    **Information Model**
    
Some Method attributes are inherited from :ref:`InformationEntity`.

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
          - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is unique within a given system. The identified entity may have a different 'id' in a different system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
       *  - label
          - string
          - 0..1
          - A primary name for the entity.
       *  - description
          - string
          - 0..1
          - A free-text description of the entity.
       *  - alternativeLabels
          - string
          - 0..m
          - Alternative name(s) for the Entity.
       *  - extensions
          - `Extension <../../gks-common/common.json#/$defs/Extension>`_
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - specifiedBy
          - :ref:`Method` | `IRI <../../gks-common/common-source.json#/$defs/IRI>`_
          - 0..1
          - A :ref:`Method` that describes all or part of the process through which the information was generated.
       *  - contributions
          - :ref:`Contribution`
          - 0..m
          - A list of :ref:`Contribution` objects that describe the activities performed by agents upon this entity.
       *  - isReportedIn
          - `IRI <../../gks-common/common-source.json#/$defs/IRI>`_ | :ref:`Document`
          - 0..1
          - 
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
          - Metadata that applies to a specific concrete record of information as encoded in a particular system.
       *  - type
          - string
          - 1..1
          - MUST be "Method".
       *  - subtype
          - `Coding <../../gks-common/common-source.json#/$defs/Coding>`_
          - 0..1
          - A more specific type of entity the method represents (e.g. Variant Interpretation Guideline, Experimental Protocol)
       *  - license
          - string
          - 0..1
          - A particular license that dictates legal permissions for how a published method (e.g. an experimental protocol, workflow specification, curation guideline) can be used.          

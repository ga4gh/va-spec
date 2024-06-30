**Computational Definition**

InformationEntities are abstract (non-physical) entities that are about something (i.e. they carry information about things in the real world).

    **Information Model**
    
Some InformationEntity attributes are inherited from :ref:`gks.common:Entity`.

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
          - 1..1
          - MUST be "InformationEntity".
       *  - specifiedBy
          - :ref:`Method` | `IRI <../../gks-common/common.json#/$defs/IRI>`_
          - 0..1
          - A :ref:`Method` that describes all or part of the process through which the information was generated.
       *  - contributions
          - :ref:`Contribution`
          - 0..m
          - A list of :ref:`Contribution` objects that describe the activities performed by agents upon this entity.
       *  - isReportedIn
          - :ref:`Document` | `IRI <../../gks-common/common.json#/$defs/IRI>`_
          - 0..m
          - A document in which the information content is expressed.
       *  - dateAuthored
          - string
          - 0..1
          - Indicates when the information content expressed in the Information Entity was generated.
       *  - derivedFrom
          - :ref:`InformationEntity`
          - 0..m
          - Another Information Entity from which this Information Entity is derived, in whole or in part.
       *  - recordMetadata
          - None
          - 0..1
          - Metadata that applies to a specific concrete record of information as encoded in a particular system.

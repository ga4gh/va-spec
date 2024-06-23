**Computational Definition**

A discrete, independent argument relevant to the validity of the Proposition assessed or put forth as true in a Statement. This argument is based on an interpretation of one or more pieces of information as evidence (i.e. Evidence Items).

    **Information Model**
    
Some EvidenceLine attributes are inherited from :ref:`InformationEntity`.

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
       *  - targetProposition
          - :ref:`Proposition`
          - 0..1
          - The possible fact against which evidence items contained in an Evidence Line were collectively evaluated, in determining the overall strength and direction of support they provide. e.g. in an ACMG Guideline-based assessment of variant pathogenicity, the support provided by distinct lines of evidence are assessed against a target proposition that a variant is pathogenic for a specific disease.
       *  - evidenceItems
          - :ref:`InformationEntity`
          - 0..m
          - An individual piece of information that was evaluated as evidence in building the argument represented by an Evidence Line.
       *  - directionOfEvidenceProvided
          - string
          - 0..1
          - The direction of support that the Evidence Line is determined to provide toward its target Proposition (can be supporting, disputing, or neutral)
       *  - strengthOfEvidenceProvided
          - `Coding <../../gks-common/common.json#/$defs/Coding>`_ | `IRI <../../gks-common/common.json#/$defs/IRI>`_
          - 0..1
          - The strength of support that an Evidence Line is determined to provide for or against its target Proposition. Strength is evaluated in the direction indicated by the directionOfEvidenceProvided value.

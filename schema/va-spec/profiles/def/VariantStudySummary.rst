**Computational Definition**

A :ref:`Statement` summarizing evidence about the impact of a variant from one or more studies.

    **Information Model**
    
Some VariantStudySummary attributes are inherited from :ref:`VariantStatement`.

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
          - `Extension <../core-im/../../gks-core-im/core.json#/$defs/Extension>`_
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - type
          - string
          - 1..1
          - 
       *  - specifiedBy
          - `Method <../core-im/../../gks-core-im/core.json#/$defs/Method>`_ | `IRI <../core-im/../../gks-core-im/core.json#/$defs/IRI>`_
          - 0..1
          - A :ref:`Method` that describes all or part of the process through which the information was generated.
       *  - contributions
          - `Contribution <../core-im/../../gks-core-im/core.json#/$defs/Contribution>`_
          - 0..m
          - A list of :ref:`Contribution` objects that describe the activities performed by agents upon this entity.
       *  - dateAuthored
          - string
          - 0..1
          - Indicates when the information content expressed in the Information Entity was generated.
       *  - derivedFrom
          - `InformationEntity <../core-im/../../gks-core-im/core.json#/$defs/InformationEntity>`_
          - 0..m
          - Another Information Entity from which this Information Entity is derived, in whole or in part.
       *  - recordMetadata
          - #/$defs/RecordMetadata
          - 0..1
          - Metadata that applies to a specific concrete record of information as encoded in a particular system.
       *  - predicate
          - string
          - 0..1
          - The predicate of the Statement.
       *  - object
          - _Not Specified_
          - 0..1
          - The object of the Statement.
       *  - qualifiers
          - object
          - 0..1
          - Additional, optional properties that may qualify the Statement.
       *  - direction
          - string
          - 1..1
          - The direction of this Statement with respect to the predicate.
       *  - strength
          - `Coding <../../gks-core-im/core-im-source.yaml#/$defs/Coding>`_ | `IRI <../../gks-core-im/core-im-source.yaml#/$defs/IRI>`_
          - 0..1
          - The overall strength of support for the Statement based on all evidence assessed.
       *  - statementText
          - string
          - 0..1
          - A natural-language expression of what a structured Statement object asserts to be true. e.g. for a Variant Pathogenicity statement, "BRCA2 c.8023A>G is pathogenic for Breast Cancer", or "there is moderate evidence supporting the pathogenicity of BRCA2 c.8023A>G for Breast Cancer".
       *  - proposition
          - `Proposition <../core-im/core.json#/$defs/Proposition>`_
          - 0..1
          - A possible fact that the Statement assesses or puts forth as true. This attribute provides the option of encapsulating the structured semantics of the possible fact asserted or evaluated by a Statement in a separate 'Proposition' object - instead of using the subject, predicate, object, qualifier properties directly in the Statement object.
       *  - subjectClassification
          - `Coding <../../gks-core-im/core-im-source.yaml#/$defs/Coding>`_ | `IRI <../../gks-core-im/core-im-source.yaml#/$defs/IRI>`_
          - 0..1
          - A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's proposition, in terms of a classification of the Statement subject. Permissible values for this attribute are typically selected to be succinct and familiar in the target community of practice. e.g. 'likely pathogenic' in the domain of variant pathogenicity classification'.
       *  - hasEvidenceOfType
          - `Coding <../../gks-core-im/core-im-source.yaml#/$defs/Coding>`_
          - 0..m
          - A term describing a type of evidence used to assess the validity of Statement's proposition (e.g. 'sequence similarity evidence', 'in vitro assay evidence').
       *  - hasEvidenceLines
          - `EvidenceLine <../core-im/core.json#/$defs/EvidenceLine>`_
          - 0..m
          - A discrete, independent argument relevant to the validity of the Proposition assessed or put forth in the Statement. This argument is based on the interpretation of one or more pieces of information as evidence.
       *  - hasEvidence
          - `InformationEntity <../../gks-core-im/core-im-source.yaml#/$defs/InformationEntity>`_
          - 0..m
          - A piece of information that represents or contributes to an argument for or against the validity of the Proposition put forth in a Statement. This is a shortcut relation that links a Statement directly to a piece of evidence supporting it, bypassing the Evidence Line class when used data creators do not utilize an Evidence Line object.
       *  - variant
          - `Variation <../../vrs/vrs.json#/$defs/Variation>`_ | `CategoricalVariation <../../catvrs/catvrs.json#/$defs/CategoricalVariation>`_ | `IRI <../../gks-core-im/core-im.json#/$defs/IRI>`_
          - 1..1
          - A variant that is the subject of the Statement.
       *  - isReportedIn
          - `Document <../core-im/../../gks-core-im/core.json#/$defs/Document>`_ | `IRI <../core-im/../../gks-core-im/core.json#/$defs/IRI>`_
          - 1..m
          - A document in which the information content is expressed.

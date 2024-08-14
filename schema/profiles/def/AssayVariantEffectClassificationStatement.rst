**Computational Definition**

TODO @alanrubin will fill out a description

    **Information Model**
    
Some AssayVariantEffectClassificationStatement attributes are inherited from :ref:`gks.core-im:Statement`.

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
          - `Extension </ga4gh/schema/gks-common/1.x/data-types/json/Extension>`_
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - contributions
          - `Contribution <../core-im/core.json#/$defs/Contribution>`_
          - 0..m
          - A list of :ref:`Contribution` objects that describe the activities performed by agents upon this entity.
       *  - isReportedIn
          - `Document <../core-im/core.json#/$defs/Document>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
          - 0..m
          - A document in which the information content is expressed.
       *  - dateAuthored
          - string
          - 0..1
          - Indicates when the information content expressed in the Information Entity was generated.
       *  - derivedFrom
          - `InformationEntity <../core-im/core.json#/$defs/InformationEntity>`_
          - 0..m
          - Another Information Entity from which this Information Entity is derived, in whole or in part.
       *  - recordMetadata
          - `RecordMetadata <../core-im/core.json#/$defs/RecordMetadata>`_
          - 0..1
          - Metadata that applies to a specific concrete record of information as encoded in a particular system.
       *  - direction
          - string
          - 1..1
          - The direction of this Statement with respect to the predicate.
       *  - strength
          - `Coding </ga4gh/schema/gks-common/1.x/data-types/json/Coding>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
          - 0..1
          - A qualitative term indicating the overall strength of support for or against the Statement based on all evidence assessed.
       *  - score
          - number
          - 0..1
          - A quantitative score indicating the overall strength of support for or against the Statement based on all evidence assessed.
       *  - statementText
          - string
          - 0..1
          - A natural-language expression of what a structured Statement object asserts to be true. e.g. for a Variant Pathogenicity statement, "BRCA2 c.8023A>G is pathogenic for Breast Cancer", or "there is moderate evidence supporting the pathogenicity of BRCA2 c.8023A>G for Breast Cancer".
       *  - hasEvidenceOfType
          - `Coding </ga4gh/schema/gks-common/1.x/data-types/json/Coding>`_
          - 0..m
          - A term describing a type of evidence used to assess the validity of Statement's proposition (e.g. 'sequence similarity evidence', 'in vitro assay evidence').
       *  - hasEvidenceLines
          - `EvidenceLine <../core-im/core.json#/$defs/EvidenceLine>`_
          - 0..m
          - A discrete, independent argument relevant to the validity of the Proposition assessed or put forth in the Statement. This argument is based on the interpretation of one or more pieces of information as evidence. argument is based on the interpretation of one or more pieces of information as evidence.
       *  - hasEvidence
          - `InformationEntity <../core-im/core.json#/$defs/InformationEntity>`_
          - 0..m
          - A piece of information that represents or contributes to an argument for or against the validity of the Proposition put forth in a Statement. This is a shortcut relation that links a Statement directly to a piece of evidence supporting it, bypassing the Evidence Line class when used data creators do not utilize an Evidence Line object.
       *  - type
          - string
          - 1..1
          - MUST be "AssayVariantEffectClassificationStatement".
       *  - subjectVariant
          - `MolecularVariation </ga4gh/schema/vrs/2.x/json/MolecularVariation>`_ | `CategoricalVariation </ga4gh/schema/cat-vrs/1.x/json/CategoricalVariation>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
          - 1..1
          - A protein or genomic contextual or canonical molecular variant.
       *  - predicate
          - string
          - 1..1
          - The predicate of the Statement.
       *  - objectAssay
          - string | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_ | `Coding </ga4gh/schema/gks-common/1.x/data-types/json/Coding>`_
          - 1..1
          - The assay that is evaluated for the variant effect. (e.g growth in haploid cell culture protein stability in fluorescence assay)
       *  - subjectClassification
          - `Coding </ga4gh/schema/gks-common/1.x/data-types/json/Coding>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
          - 1..1
          - The classification of the variant effect in the assay.
       *  - specifiedBy
          - `Method <../core-im/core.json#/$defs/Method>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
          - 0..1
          - The method that specifies the classification of the variant effect in the assay.

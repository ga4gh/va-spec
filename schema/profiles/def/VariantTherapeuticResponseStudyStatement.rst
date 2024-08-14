**Computational Definition**

A study summarization describing the role of a variant in modulating the response of a neoplasm to drug administration or other therapeutic procedure.

**Information Model**

Some VariantTherapeuticResponseStudyStatement attributes are inherited from :ref:`gks.core-im:Statement`.

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
   *  - specifiedBy
      - `Method <../core-im/core.json#/$defs/Method>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 0..1
      - A :ref:`Method` that describes all or part of the process through which the information was generated.
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
   *  - subjectClassification
      - `Coding </ga4gh/schema/gks-common/1.x/data-types/json/Coding>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 0..1
      - A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's proposition, in terms of a classification of the Statement's subject. Permissible values for this attribute are typically selected to be succinct and familiar in the target community of practice. e.g.  'likely pathogenic' in the domain of variant pathogenicity classification'.
   *  - hasEvidenceLines
      - `EvidenceLine <../core-im/core.json#/$defs/EvidenceLine>`_
      - 0..m
      - A discrete, independent argument relevant to the validity of the Proposition assessed or put forth in the Statement. This argument is based on the interpretation of one or more pieces of information as evidence. argument is based on the interpretation of one or more pieces of information as evidence.
   *  - type
      - string
      - 1..1
      - MUST be "VariantTherapeuticResponseStudyStatement".
   *  - subjectVariant
      - `Variation </ga4gh/schema/vrs/2.x/json/Variation>`_ | `CategoricalVariation </ga4gh/schema/cat-vrs/1.x/json/CategoricalVariation>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 1..1
      - A variant that is the subject of the Statement.
   *  - predicate
      - string
      - 1..1
      - The predicate of the Statement.
   *  - objectTherapeutic
      - `TherapeuticProcedure </ga4gh/schema/gks-common/1.x/domain-entities/json/TherapeuticProcedure>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 1..1
      - A drug administration or other therapeutic procedure that the neoplasm is intended to respond to.
   *  - diseaseQualifier
      - `Condition </ga4gh/schema/gks-common/1.x/domain-entities/json/Condition>`_ | `IRI </ga4gh/schema/gks-common/1.x/data-types/json/IRI>`_
      - 1..1
      - Reports the disease context in which the variant's association with therapeutic sensitivity or resistance is evaluated. Note that this is a required qualifier in therapeutic response statements.
   *  - alleleOriginQualifier
      - string
      - 0..1
      - Reports whether the statement should be interpreted in the context of an inherited (germline) variant, an acquired (somatic) mutation, or both (combined).
   *  - allelePrevalenceQualifier
      - string
      - 0..1
      - Reports wWhether the statement should be interpreted in the context of the variant
 being rare or common.
   *  - geneContextQualifier
      - `Gene </ga4gh/schema/gks-common/1.x/domain-entities/json/Gene>`_
      - 0..1
      - Reports a gene impacted by the variant, which contributes to the therapeutic sensitivity or resistance reported in the Statement.


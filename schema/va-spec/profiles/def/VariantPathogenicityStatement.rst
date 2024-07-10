**Computational Definition**

A :ref:`VariantClassification` describing the role of a variant in causing an  inherited disorder.

    **Information Model**
    
Some VariantPathogenicityStatement attributes are inherited from :ref:`va.core:Statement`.

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
          - `Extension <../core-im/../../gks-common/common.json#/$defs/Extension>`_
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - specifiedBy
          - `Method <../core-im/core.json#/$defs/Method>`_ | `IRI <../../gks-common/common-source.json#/$defs/IRI>`_
          - 0..1
          - A :ref:`Method` that describes all or part of the process through which the information was generated.
       *  - contributions
          - `Contribution <../core-im/core.json#/$defs/Contribution>`_
          - 0..m
          - A list of :ref:`Contribution` objects that describe the activities performed by agents upon this entity.
       *  - isReportedIn
          - `Document <../core-im/core.json#/$defs/Document>`_ | `IRI <../../gks-common/common-source.json#/$defs/IRI>`_
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
          - `Coding <../../gks-common/common-source.json#/$defs/Coding>`_ | `IRI <../../gks-common/common-source.json#/$defs/IRI>`_
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
          - `Coding <../../gks-common/common-source.json#/$defs/Coding>`_ | `IRI <../../gks-common/common-source.json#/$defs/IRI>`_
          - 0..1
          - A single term or phrase summarizing the outcome of direction and strength assessments of a Statement's proposition, in terms of a classification of the Statement's subject. Permissible values for this attribute are typically selected to be succinct and familiar in the target community of practice. e.g. 'likely pathogenic' in the domain of variant pathogenicity classification'.
       *  - hasEvidenceOfType
          - `Coding <../../gks-common/common-source.json#/$defs/Coding>`_
          - 0..m
          - A term describing a type of evidence used to assess the validity of Statement's proposition (e.g. 'sequence similarity evidence', 'in vitro assay evidence').
       *  - hasEvidenceLines
          - `EvidenceLine <../core-im/core.json#/$defs/EvidenceLine>`_
          - 0..m
          - A discrete, independent argument relevant to the validity of the Proposition assessed or put forth in the Statement. This argument is based on the interpretation of one or more pieces of information as evidence.
       *  - hasEvidence
          - `InformationEntity <../core-im/core.json#/$defs/InformationEntity>`_
          - 0..m
          - A piece of information that represents or contributes to an argument for or against the validity of the Proposition put forth in a Statement. This is a shortcut relation that links a Statement directly to a piece of evidence supporting it, bypassing the Evidence Line class when used data creators do not utilize an Evidence Line object.
       *  - type
          - string
          - 1..1
          - MUST be "VariantPathogenicityStatement".
       *  - subjectVariant
          - `Variation <../../vrs/vrs.json#/$defs/Variation>`_ | `CategoricalVariation <../../catvrs/catvrs.json#/$defs/CategoricalVariation>`_ | `IRI <../../gks-common/common.json#/$defs/IRI>`_
          - 1..1
          - A variant that is the subject of the Statement.
       *  - predicate
          - string
          - 1..1
          - The predicate of the Statement.
       *  - objectCondition
          - `Condition <../../gks-domain-entities/domain-entities.json#/$defs/Condition>`_ | `IRI <../../gks-common/common.json#/$defs/IRI>`_
          - 1..1
          - The :ref:`Condition` for which the variant impact is stated.
       *  - penetranceQualifier
          - string
          - 0..1
          - Extends the statement to report the penetrance of the pathogenic effect - i.e. the extent  to which the variant impact is expressed by individuals carrying it as a measure of the  proportion of carriers exhibiting the condition.
       *  - modeOfInheritanceQualifier
          - string
          - 0..1
          - Reports a pattern of inheritance expected for the pathogenic effect of the variant. 
       *  - geneContextQualifier
          - `Gene <../../gks-domain-entities/domain-entities.json#/$defs/Gene>`_
          - 0..1
          - Reports the gene through which the pathogenic effect asserted for the variant is mediated  (i.e. it is the variant's impact on this gene that is responsible for causing the condition).

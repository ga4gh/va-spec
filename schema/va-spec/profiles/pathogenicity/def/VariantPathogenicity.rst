**Computational Definition**

A :ref:`VariantClassification` describing the role of a variant in causing an  inherited disorder.

    **Information Model**
    
Some VariantPathogenicity attributes are inherited from :ref:`va.core:VariantClassification`.

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
          - `Extension <../../core-im/../../gks-common/core.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - type
          - string
          - 1..1
          - MUST be "VariantPathogenicity".
       *  - specifiedBy
          - `Method <../../core-im/core.json#/$defs/Method>`_ | `IRI <../../gks-common/core.json#/$defs/IRI>`_
          - 0..1
          - A :ref:`Method` that describes all or part of the process through which the information was generated.
       *  - contributions
          - `Contribution <../../core-im/core.json#/$defs/Contribution>`_
          - 0..m
          - 
       *  - isReportedIn
          - `Document <../../core-im/core.json#/$defs/Document>`_ | `IRI <../../gks-common/core.json#/$defs/IRI>`_
          - 0..m
          - A document in which the information content is expressed.
       *  - dateAuthored
          - string
          - 0..1
          - Indicates when the information content expressed in the Information Entity was generated.
       *  - derivedFrom
          - `InformationEntity <../../core-im/core.json#/$defs/InformationEntity>`_
          - 0..m
          - Another Information Entity from which this Information Entity is derived, in whole or in part.
       *  - recordMetadata
          - None
          - 0..1
          - 
       *  - direction
          - string
          - 1..1
          - The direction of this Statement with respect to the predicate.
       *  - strength
          - `Coding <../../gks-common/core.json#/$defs/Coding>`_ | `IRI <../../gks-common/core.json#/$defs/IRI>`_
          - 0..1
          - The overall strength of support for the Statement based on all evidence assessed.
       *  - statementText
          - string
          - 0..1
          - A natural-language expression of what a structured Statement object asserts to be true.  e.g. for a Variant Pathgenicity statement, "BRCA2 c.8023A>G is pathogenic for Breast  Cancer", or "there is moderate evidence supporting the pathogenicity of BRCA2 c.8023A>G  for Breast Cancer".
       *  - proposition
          - `Proposition <../../core-im/core.json#/$defs/Proposition>`_
          - 0..1
          - A possible fact that the Statement assesses or puts forth as true. This attribute provides  the option of encapsulating the structured semantics of the possible fact asserted or  evaluated by a Statement in a separate 'Proposition' object - instead of using the subject,  predicate, object, qualifier properties directly in the Statement object.
       *  - hasEvidenceOfType
          - `Coding <../../gks-common/core.json#/$defs/Coding>`_
          - 0..m
          - A term describing a type of evidence used to assess the validity of Statement's proposition (e.g. 'sequence similarity evidence', 'in vitro assay evidence').    
       *  - hasEvidenceLines
          - `EvidenceLine <../../core-im/core.json#/$defs/EvidenceLine>`_
          - 0..m
          - A discrete, independent argument relevant to the validity of the Proposition assessed or  put forth in the Statement. This arguent is based on the interpretation of one or more  pieces of information as evidence.
       *  - hasEvidence
          - `InformationEntity <../../core-im/core.json#/$defs/InformationEntity>`_
          - 0..m
          - A piece of information that represents or contributes to an argument for or against the  validity of the Proposition put forth in a Statement. This is a shortcut relation that links  a Statement directly to a piece of evidnece supporting it, bypassing the Evidence Line class  when used data creators do not utilize an Evidence Line object.
       *  - variant
          - `Variation <../../vrs/vrs.json#/$defs/Variation>`_ | `CategoricalVariation <../../catvrs/catvrs.json#/$defs/CategoricalVariation>`_ | `IRI <../../gks-common/core.json#/$defs/IRI>`_
          - 1..1
          - A variant that is the subject of the Statement.
       *  - classification
          - `Coding <../../gks-common/core.json#/$defs/Coding>`_ | `IRI <../../gks-common/core.json#/$defs/IRI>`_
          - 1..1
          - A methodological, summary classification about the impact of a variant.
       *  - predicate
          - string
          - 0..1
          - The predicate of the Statement.
       *  - condition
          - `Condition <../../../gks-common/conditions.json#/$defs/Condition>`_ | `IRI <../../../gks-common/core.json#/$defs/IRI>`_
          - 1..1
          - The :ref:`Condition` for which the variant impact is stated.
       *  - qualifiers
          - object
          - 0..1
          - Additional, optional properties that may qualify the Statement.

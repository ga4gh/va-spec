**Computational Definition**

A measure of the frequency of an Allele in a cohort.

    **Information Model**
    
Some CohortAlleleFrequency attributes are inherited from :ref:`va.core:InformationEntity`.

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
          - `ConceptMapping <../core-im/../../gks-common/common.json#/$defs/ConceptMapping>`_
          - 0..m
          - A list of mappings to concepts in terminologies or code systems. Each mapping should include a coding and a relation.
       *  - extensions
          - `Extension <../core-im/../../gks-common/common.json#/$defs/Extension>`_
          - 0..m
          - A list of extensions to the entity. Extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.
       *  - type
          - string
          - 1..1
          - MUST be "InformationEntity".
       *  - specifiedBy
          - `Method <../core-im/core.json#/$defs/Method>`_ | `IRI <../../gks-common/common.json#/$defs/IRI>`_
          - 0..1
          - A :ref:`Method` that describes all or part of the process through which the information was generated.
       *  - contributions
          - `Contribution <../core-im/core.json#/$defs/Contribution>`_
          - 0..m
          - A list of :ref:`Contribution` objects that describe the activities performed by agents upon this entity.
       *  - isReportedIn
          - `Document <../core-im/core.json#/$defs/Document>`_ | `IRI <../../gks-common/common.json#/$defs/IRI>`_
          - 0..m
          - A document in which the information content is expressed.
       *  - dateAuthored
          - string
          - 0..1
          - Indicates when the information content expressed in the Information Entity was generated.
       *  - derivedFrom
          - object
          - 0..1
          - Information about the dataset from which the CohortAlleleFrequency was reported.
       *  - recordMetadata
          - None
          - 0..1
          - Metadata that applies to a specific concrete record of information as encoded in a particular system.
       *  - focusAllele
          - `Allele <../../vrs/vrs.json#/$defs/Allele>`_ | string
          - 1..1
          - The Allele for which the frequency is being reported.
       *  - focusAlleleCount
          - integer
          - 1..1
          - The number of occurrences of the focusAllele in the cohort.
       *  - locusAlleleCount
          - integer
          - 1..1
          - The number of occurrences of alleles at the locus in the cohort (count of all alleles at this locus, sometimes referred to as "allele number").
       *  - alleleFrequency
          - number
          - 1..1
          - The frequency of the focusAllele in the cohort.
       *  - cohort
          - object
          - 1..1
          - The cohort from which the frequency was derived.
       *  - ancillaryResults
          - object
          - 0..1
          - Ancillary results that may be associated with the CohortAlleleFrequency, providing additional context or information.
       *  - qualityMeasures
          - object
          - 0..1
          - Quality measures associated with the CohortAlleleFrequency and how it was derived, which may impact interpretation.
       *  - subcohortFrequency
          - :ref:`CohortAlleleFrequency`
          - 0..m
          - A list of CohortAlleleFrequency objects describing subcohorts of the cohort currently being described. This creates a recursive relationship and subcohorts can be further subdivided into more subcohorts. This enables, for example, the description of different ancestry groups and sexes among those ancestry groups.

.. admonition:: Draft
    :class: warning

    May change significantly in future releases. See |maturity-model|.

**Computational Definition**

An AnalysisResult that reports the output of a single in silico tool's analysis of a variant's functional impact, including any numeric score(s) and optional categorical interpretation.

**Information Model**

Some ComputationalVariantFunctionalImpactAnalysisResult attributes are inherited from :ref:`StudyResult`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Field
      - Flags
      - Type
      - Limits
      - Description
   *  - id
      -
      - string
      - 0..1
      - The 'logical' identifier of the Entity in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - type
      -
      - string
      - 1..1
      - MUST be "ComputationalVariantFunctionalImpactAnalysisResult".
   *  - name
      -
      - string
      - 0..1
      - A primary name for the entity.
   *  - description
      -
      - string
      - 0..1
      - A free-text description of the Entity.
   *  - aliases
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - string
      - 0..m
      - Alternative name(s) for the Entity.
   *  - extensions
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - specifiedBy
      -
      - :ref:`iriReference` | :ref:`Method`
      - 0..1
      - The in silico method or algorithm that was applied to generate the reported score(s).
   *  - contributions
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Ordered">&#8595;</span>
      - :ref:`Contribution`
      - 0..m
      - Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of this Information Entity.
   *  - reportedIn
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Document` | :ref:`iriReference`
      - 0..m
      - A document in which the the Information Entity is reported.
   *  - focus
      -
      - :ref:`iriReference` | :ref:`Allele` | :ref:`CategoricalVariant`
      - 1..1
      - The genetic variant for which the in silico analysis was performed.
   *  - sourceDataSet
      -
      - :ref:`DataSet`
      - 0..1
      - The dataset from which the in silico scores were retrieved or derived (e.g., an Ensembl VEP annotation dataset).
   *  - ancillaryResults
      -
                        .. raw:: html

                            <span style="background-color: #D3D3D3; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Draft Maturity Level">D</span>
      - object
      - 0..1
      - An object in which implementers can define custom fields to capture additional scores or outputs produced by the in silico tool beyond the primary score. For example, CADD reports both a raw score and a Phred-scaled score; the primary score field would hold one, and ancillaryResults would hold the other.
   *  - qualityMeasures
      -
                        .. raw:: html

                            <span style="background-color: #D3D3D3; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Draft Maturity Level">D</span>
      - object
      - 0..1
      - An object in which implementers can define custom fields to capture metadata about the quality/provenance of the primary data items captured in standard attributes in the main body of the Study Result. e.g. a sequencing coverage metric in a Cohort Allele Frequency Study Result.
   *  - transcriptVariationContext
      -
      - :ref:`iriReference` | :ref:`Allele`
      - 1..1
      - The transcript in the context of which the in silico analysis was performed.
   *  - impactScore
      -
      - number
      - 1..1
      - The primary numeric score produced by the in silico tool for this variant.
   *  - impactScoreType
      -
      - :ref:`iriReference` | :ref:`MappableConcept`
      - 0..1
      - A descriptor indicating what the score represents (e.g., 'SIFT impact score', 'CADD Phred-scaled impact score').
   *  - categoricalImpact
      -
      - :ref:`iriReference` | :ref:`MappableConcept`
      - 0..1
      - The categorical interpretation derived from the score by the in silico tool (e.g., 'tolerated', 'benign', 'pathogenic').
   *  - impactedFeatureType
      -
      - :ref:`iriReference` | :ref:`MappableConcept`
      - 0..1
      - A descriptor indicating the type of feature for which the focus variant has a predicted impact
   *  - impactedFeature
      -
      - :ref:`iriReference` | :ref:`MappableConcept`
      - 0..1
      - The specific feature for which the focus variant has a predicted impact

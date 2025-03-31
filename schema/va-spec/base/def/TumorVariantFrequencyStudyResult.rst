.. note:: This data class is at a **trial use** maturity level and may \
    change in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A Study Result that reports measures related to the frequency of an variant across different tumor types.

**Information Model**

Some TumorVariantFrequencyStudyResult attributes are inherited from :ref:`StudyResult`.

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
      - :ref:`Method` | :ref:`iriReference`
      - 0..1
      - A specification that describes all or part of the process that led to creation of the Information Entity
   *  - contributions
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Contribution`
      - 0..m
      - Specific actions taken by an Agent toward the creation, modification, validation, or deprecation of an Information Entity.
   *  - reportedIn
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Document` | :ref:`iriReference`
      - 0..m
      - A document in which the the Information Entity is reported.
   *  - ancillaryResults
      -
                        .. raw:: html

                            <span style="background-color: #D3D3D3; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Draft Maturity Level">D</span>
      - object
      - 0..1
      - An object in which implementers can define custom fields to capture additional results derived from analysis of primary data items captured in standard attributes in the main body of the Study Result. e.g. in a Cohort Allele Frequency Study Result, this maybe a grpMaxFAF95 calculation, or homozygote/heterozygote calls derived from analyzing raw allele count data.
   *  - qualityMeasures
      -
                        .. raw:: html

                            <span style="background-color: #D3D3D3; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Draft Maturity Level">D</span>
      - object
      - 0..1
      - An object in which implementers can define custom fields to capture metadata about the quality/provenance of the primary data items captured in standard attributes in the main body of the Study Result. e.g. a sequencing coverage metric in a Cohort Allele Frequency Study Result.
   *  - type
      -
      - string
      - 1..1
      - MUST be "TumorVariantFrequencyStudyResult".
   *  - sourceDataSet
      -
      - :ref:`DataSet`
      - 0..1
      - The dataset from which data in the Tumor Variant Frequency Study Result was taken.
   *  - focusVariant
      -
      - :ref:`Allele` | :ref:`iriReference` | :ref:`CategoricalVariant`
      - 1..1
      - The variant for which frequency data is reported in the Study Result
   *  - affectedTumorSamples
      -
      - integer
      - 1..1
      - The number of tumor samples that contain the focus variant
   *  - totalTumorSamples
      -
      - integer
      - 1..1
      - The total number of tumor samples included in the dataset
   *  - affectedFrequency
      -
      - number
      - 1..1
      - The frequency of tumor samples that include the focus variant.
   *  - sampleGroup
      -
      - :ref:`StudyGroup`
      - 1..1
      - The set of samples about which the frequency data was generated.
   *  - subGroupFrequency
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`TumorVariantFrequencyStudyResult`
      - 0..m
      - A list of Tumor Variant Frequency Study Result objects describing subsets of the sample group currently being described. Subgroups can be further subdivided into more subcohorts. This enables, for example, the description of frequency data within samples with a narrower categorical variant than the root focus variant, or samples with a specific tumors type

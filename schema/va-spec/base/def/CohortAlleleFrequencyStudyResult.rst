.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A StudyResult that reports measures related to the frequency of an Allele in a cohort

**Information Model**

Some CohortAlleleFrequencyStudyResult attributes are inherited from :ref:`va-spec:StudyResult`.

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
   *  - label
      - 
      - string
      - 0..1
      - A primary name for the entity.
   *  - description
      - 
      - string
      - 0..1
      - A free-text description of the Entity.
   *  - alternativeLabels
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
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Method` | :ref:`iriReference`
      - 0..m
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
   *  - dateAuthored
      - 
      - :ref:`datetime`
      - 0..1
      - Indicates when the information content expressed in the Information Entity was generated.
   *  - recordMetadata
      - 
      - :ref:`RecordMetadata`
      - 0..1
      - Provenance metadata about a specific concrete record of information as encoded/serialized in a particular data set or object (as opposed to provenance about the abstract information content the encoding carries).
   *  - ancillaryResults
      - 
                        .. raw:: html

                            <span style="background-color: #D3D3D3; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Draft Maturity Level">D</span>
      - object
      - 0..1
      - 
   *  - qualityMeasures
      - 
                        .. raw:: html

                            <span style="background-color: #D3D3D3; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Draft Maturity Level">D</span>
      - object
      - 0..1
      - 
   *  - type
      - 
      - string
      - 1..1
      - MUST be "CohortAlleleFrequencyStudyResult".
   *  - sourceDataSet
      - 
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`DataSet`
      - 0..m
      - The dataset from which the CohortAlleleFrequencyStudyResult was reported.
   *  - focusAllele
      - 
      - :ref:`Allele` | string
      - 1..1
      - The specific subject or experimental unit in a Study that data in the StudyResult object is about - e.g. a particular variant in a population allele frequency dataset like ExAC or gnomAD.
   *  - focusAlleleCount
      - 
      - integer
      - 1..1
      - The number of occurrences of the focusAllele in the cohort.
   *  - locusAlleleCount
      - 
      - integer
      - 1..1
      - The number of occurrences of all alleles at the locus in the cohort (sometimes referred to as "allele number")
   *  - focusAlleleFrequency
      - 
      - number
      - 1..1
      - The frequency of the focusAllele in the cohort.
   *  - cohort
      - 
      - :ref:`StudyGroup`
      - 1..1
      - The cohort from which the frequency was derived.
   *  - subCohortFrequency
      - 
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`CohortAlleleFrequencyStudyResult`
      - 0..m
      - A list of CohortAlleleFrequency objects describing subcohorts of the cohort currently being described. This creates a recursive relationship and subcohorts can be further subdivided into more subcohorts. This enables, for example, the description of different ancestry groups and sexes among those ancestry groups.

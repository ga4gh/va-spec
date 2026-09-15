.. admonition:: Trial Use
    :class: note

    May change in future releases. See |maturity-model|.

**Computational Definition**

The Extension class provides entities with a means to include additional attributes that are outside of the specified standard but needed by a given content provider or system implementer. These extensions are not expected to be natively understood, but may be used for pre-negotiated exchange of message attributes between systems.

**Information Model**

Some Extension attributes are inherited from :ref:`Element`.

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
      - The 'logical' identifier of the data element in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - extensions
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - name
      -
      - string
      - 1..1
      - A name for the Extension. Should be indicative of its meaning and/or the type of information it value represents.
   *  - value
      -
      - ['number', 'string', 'boolean', 'object', 'array', 'null']
      - 1..1
      - The value of the Extension - can be any primitive or structured object
   *  - description
      -
      - string
      - 0..1
      - A description of the meaning or utility of the Extension, to explain the type of information it is meant to hold.

**Used in:** :ref:`Adjacency`, :ref:`Agent`, :ref:`Allele`, :ref:`CategoricalVariant`, :ref:`CisPhasedBlock`, :ref:`Coding`, :ref:`CohortAlleleFrequencyStudyResult`, :ref:`ComputationalVariantFunctionalImpactAnalysisResult`, :ref:`ConceptMapping`, :ref:`ConceptSet`, :ref:`Contribution`, :ref:`CopyNumberChange`, :ref:`CopyNumberCount`, :ref:`DataSet`, :ref:`DerivativeMolecule`, :ref:`Document`, :ref:`Entity`, :ref:`EvidenceLine`, :ref:`ExperimentalVariantFunctionalImpactProposition`, :ref:`ExperimentalVariantFunctionalImpactStudyResult`, :ref:`Expression`, :ref:`FunctionalDomain`, :ref:`Ga4ghIdentifiableObject`, :ref:`GeneDiseaseValidityProposition`, :ref:`GeneticContextVariantProposition`, :ref:`InformationEntity`, :ref:`LengthExpression`, :ref:`LiteralSequenceExpression`, :ref:`Location`, :ref:`MappableConcept`, :ref:`Method`, :ref:`MolecularVariation`, :ref:`Proposition`, :ref:`ReferenceLengthExpression`, :ref:`RelativeAllele`, :ref:`RelativeSequenceLocation`, :ref:`SequenceExpression`, :ref:`SequenceLocation`, :ref:`SequenceOffsetLocation`, :ref:`SequenceReference`, :ref:`Statement`, :ref:`StudyGroup`, :ref:`StudyResult`, :ref:`SubjectVariantProposition`, :ref:`SystemicVariation`, :ref:`Terminus`, :ref:`TraversalBlock`, :ref:`TumorVariantFrequencyStudyResult`, :ref:`UnspecifiedElement`, :ref:`VariantClinicalSignificanceProposition`, :ref:`VariantDiagnosticProposition`, :ref:`VariantMolecularConsequenceProposition`, :ref:`VariantOncogenicityProposition`, :ref:`VariantPathogenicityProposition`, :ref:`VariantPrognosticProposition`, :ref:`VariantTherapeuticResponseProposition`, :ref:`Variation`

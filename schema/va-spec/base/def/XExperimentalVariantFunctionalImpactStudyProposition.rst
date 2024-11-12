.. warning:: This data class is at a **draft** maturity level and may change
    significantly in future releases. Maturity levels are described in
    the :ref:`maturity-model`.

**Computational Definition**

A proposition reporting a conclusion from a single assay or study about the functional impact of a variant on a sequence feature (typically a gene or gene product).

**Information Model**

Some XExperimentalVariantFunctionalImpactStudyProposition attributes are inherited from :ref:`gks-core:Proposition`.

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
   *  - propositionText
      - 
      - string
      - 0..1
      - A natural-language expression of the Proposition's meaning. e.g. "BRCA2 c.8023A>G is pathogenic for Breast Cancer".
   *  - type
      - 
      - string
      - 1..1
      - MUST be "ExperimentalVariantFunctionalImpactStudyProposition".
   *  - subjectVariant
      - 
      - :ref:`MolecularVariation` | :ref:`CategoricalVariant` | :ref:`iriReference`
      - 1..1
      - A protein or genomic contextual or canonical molecular variant.
   *  - predicate
      - 
      - string
      - 1..1
      - The relationship this Proposition describes between the subject Variant and object Sequence Feature whose function it may alter.
   *  - objectSequenceFeature
      - 
      - :ref:`iriReference` | :ref:`MappableConcept`
      - 1..1
      - The sequence feature (typically a gene or gene product) on whose function the impact  of the subject variant is assessed.
   *  - studyContextQualifier
      - 
      - :ref:`Document` | :ref:`iriReference`
      - 1..1
      - The assay in which the reported variant functional impact was determined -  providing a specific experimental context in which this effect is asserted to hold.
   *  - impactTypeQualifier
      - 
      - string
      - 0..1
      - A term describing a specific type of functional impact that the variant is determined to have on the indicated sequence feature (e.g. decreased activity, dominant negative, neomorphic, reduced Ca2+ binding activity).

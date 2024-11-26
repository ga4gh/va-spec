.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A Proposition reporting a conclusion from a single study about whether a variant is associated with a disease (a diagnostic inclusion criterion), or absence of a disease (diagnostic exclusion criterion) - based on interpretation of the study's results.

**Information Model**

Some VariantDiagnosticProposition attributes are inherited from :ref:`ClinicalVariantProposition`.

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
   *  - subjectVariant
      - 
      - :ref:`MolecularVariation` | :ref:`CategoricalVariant` | :ref:`iriReference`
      - 1..1
      - A variant that is the subject of the Proposition.
   *  - geneContextQualifier
      - 
      - :ref:`MappableConcept` | :ref:`iriReference`
      - 0..1
      - Reports the gene through which the pathogenic effect asserted for the variant is mediated (i.e. it is the variant's impact on this gene that is responsible for causing the condition).
   *  - alleleOriginQualifier
      - 
      - :ref:`MappableConcept` | :ref:`iriReference`
      - 0..1
      - Reports whether the statement should be interpreted in the context of an inherited (germline) variant, an acquired (somatic) mutation, or another more nuanced concept.
   *  - type
      - 
      - string
      - 1..1
      - MUST be "VariantDiagnosticProposition".
   *  - predicate
      - 
      - string
      - 1..1
      - The relationship declared to hold between the subject and the object of the Statement.
   *  - objectCondition
      - 
      - :ref:`Condition` | :ref:`iriReference`
      - 1..1
      - The disease that is evaluated for diagnosis.

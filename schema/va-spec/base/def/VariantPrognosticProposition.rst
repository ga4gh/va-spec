.. note:: This data class is at a **trial use** maturity level and may \
    change in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A Proposition about whether a variant is associated with an improved or worse outcome for a disease.

**Information Model**

Some VariantPrognosticProposition attributes are inherited from :ref:`ClinicalVariantProposition`.

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
   *  - subjectVariant
      -
      - :ref:`MolecularVariation` | :ref:`CategoricalVariant` | :ref:`iriReference`
      - 1..1
      - A variant that is the subject of the Proposition.
   *  - geneContextQualifier
      -
      - :ref:`MappableConcept` | :ref:`iriReference`
      - 0..1
      - Reports a gene impacted by the variant, which may contribute to the association described in the Proposition.
   *  - alleleOriginQualifier
      -
      - :ref:`MappableConcept` | :ref:`iriReference`
      - 0..1
      - Reports whether the Proposition should be interpreted in the context of a heritable "germline" variant, an acquired "somatic" variant in a tumor, or a post-zygotic "mosaic" variant. While these are the most commonly reported allele origins, other more nuanced concepts can be captured  (e.g. "maternal" vs "paternal" allele origin). In practice, populating this field may be complicated by the fact that some sources report allele origin based on the type of tissue that was sequenced to identify the variant, and others use it more generally to specify a category of variant for which the proposition holds. The stated intent of this attribute is the latter. However, if an implementer is not sure about which is reported in their data, it may be safer to create an Extension to hold this information, where they can explicitly acknowledge this ambiguity.
   *  - type
      -
      - string
      - 1..1
      - MUST be "VariantPrognosticProposition".
   *  - predicate
      -
      - string
      - 1..1
      - The relationship the Proposition describes between the subject variant and object Condition. MUST be one of "associatedWithBetterOutcomeFor" or "associatedWithWorseOutcomeFor".
   *  - objectCondition
      -
      - :ref:`Condition` | :ref:`ConditionSet` | :ref:`iriReference`
      - 1..1
      - The disease that is evaluated for outcome.

.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A Proposition describing a type of consequence of a variant on transcript and protein molecules - typically reporting the type of sequence feature affected (e.g. 'intron variant', 'splice-site variant'), or an impact on the processing of the molecule along the path from gene to transcript to polypeptide (e.g. 'missense variant', 'frameshift variant'). Note that annotations about variant impact on gene product function, which may occur downstream of a molecular consequence, are not in scope here. These are covered by a Variant Functional Impact Proposition class.

**Information Model**

Some VariantMolecularConsequenceProposition attributes are inherited from :ref:`ClinicalVariantProposition`.

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
   *  - geneContextQualifier
      -
      - :ref:`MappableConcept` | :ref:`iriReference`
      - 0..1
      - Reports a gene impacted by the variant, which may contribute to the association described in the Proposition.
   *  - alleleOriginQualifier
      -
      - :ref:`MappableConcept` | :ref:`iriReference`
      - 0..1
      - Reports whether the Proposition should be interpreted in the context of a heritable "germline" variant, an acquired "somatic" variant in a tumor,  post-zygotic "mosaic" variant. While these are the most commonly reported allele origins, other more nuanced concepts can be captured  (e.g. "maternal" vs "paternal" allele origin"). In practice, populating this field may be complicated by the fact that some sources report allele origin based on the type of tissue that was sequenced to identify the variant, and others use it more generally to specify a category of variant for which the proposition holds. The stated intent of this attribute is the latter. However, if an implementer is not sure about which is reported in their data, it may be safer to create an Extension to hold this information, where they can explicitly acknowledge this ambiguity.
   *  - type
      -
      - string
      - 1..1
      - MUST be "VariantMolecularConsequenceProposition".
   *  - subjectVariant
      -
      - :ref:`Allele` | :ref:`Adjacency` | :ref:`CategoricalVariant` | :ref:`iriReference`
      - 1..1
      - A variant that is the subject of the Proposition.
   *  - predicate
      -
      - string
      - 1..1
      - The relationship the Proposition describes between the subject variant and object consequence terms for which the molecular consequence applies. MUST be "hasMolecularConsequence".
   *  - objectConsequence
      -
      - :ref:`MolecularConsequence` | :ref:`iriReference`
      - 1..1
      - The molecular consequence of the subject variant.
   *  - molecularVariationContextQualifiers
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Allele` | :ref:`Adjacency` | :ref:`iriReference`
      - 0..m
      - Sequence changes on transcript, mRNA, or protein molecules. The relationship between the subject variant and object terms only holds in the context of variations on molecules represented in this array.

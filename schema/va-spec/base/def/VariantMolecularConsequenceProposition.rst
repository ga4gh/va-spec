.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A Proposition describing a type of consequence of a variant on transcript and protein molecules - typically reporting the type of sequence feature affected (e.g. 'intron variant', 'splice-site variant'), or an impact on the processing of the molecule along the path from gene to transcript to polypeptide (e.g. 'missense variant', 'frameshift variant'). Note that annotations about variant impact on gene product function, which may occur downstream of a molecular consequence, are not in scope here. These are covered by a Variant Functional Impact Proposition classes.

**Information Model**

Some VariantMolecularConsequenceProposition attributes are inherited from :ref:`SubjectVariantProposition`.

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
   *  - type
      -
      - string
      - 1..1
      - MUST be "VariantMolecularConsequenceProposition".
   *  - subjectVariant
      -
      - :ref:`Allele` | :ref:`Adjacency` | :ref:`iriReference`
      - 1..1
      - MUST be a genomic variant specified against genomic reference sequence(s). This practice most directly reflects data conventions from sources like VEP, and aligns with the intended use of Molecular Consequence data. There are separate qualifier attributes in the model to capture transcript and/or protein level representations of the subject, that indicate the variant context in which the reported consequence(s) are actually manifest.
   *  - predicate
      -
      - string
      - 1..1
      - The relationship the Proposition describes between the subject variant and object consequence terms for which the molecular consequence applies. MUST be "hasMolecularConsequence".
   *  - objectConsequence
      -
      - :ref:`MappableConcept` | :ref:`ConceptSet` | :ref:`iriReference`
      - 1..1
      - The molecular consequence(s) of the subject variant, in the context of the qualifying transcript and/or protein variation context(s). These are typically terms from the 'structural_variant' branch of the Sequence Ontology, e.g. 'SO:0001627' (intron_variant), or 'SO:0001589' (frameshift_variant). If more than one consequence term apply, use a ConceptSet to capture them.
   *  - transcriptVariationContextQualifier
      -
      - :ref:`Allele` | :ref:`Adjacency` | :ref:`iriReference`
      - 0..1
      - The subject genomic variant as projected on a particular transcript or mRNA molecule. The reported relationship between the subject variant and object consequence terms holds specifically in the context of this transcript variation. A transcript variation context MUST be reported, unless the subject is an intergenic variant.
   *  - proteinVariationContextQualifier
      -
      - :ref:`Allele` | :ref:`Adjacency` | :ref:`iriReference`
      - 0..1
      - The subject genomic variant as projected on a particular protein molecule. The reported relationship between the subject variant and object consequence terms holds specifically in the context of this protein variation. A protein variation context MUST be accompanied by its corresponding transcript variation context.
   *  - geneContextQualifier
      -
      - :ref:`MappableConcept` | :ref:`iriReference`
      - 0..1
      - Reports a gene impacted by the variant, which may contribute to the association described in the Proposition.

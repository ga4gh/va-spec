.. admonition:: Draft
    :class: warning

    May change significantly in future releases. See |maturity-model|.

**Computational Definition**

A Statement describing the role of a variant in causing an inherited condition.

**Information Model**

This class refines :ref:`Statement`.

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
      - MUST be "Statement".
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
   *  - specifiedBy *(refined)*
      -
      - :ref:`Method` | :ref:`iriReference`
      - 1..1
      - The method that specifies how the pathogenicity classification is ultimately assigned to the variant, based on assessment of evidence.
   *  - contributions
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Ordered">&#8595;</span>
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
   *  - proposition *(refined)*
      -
      - :ref:`VariantPathogenicityProposition`
      - 1..1
      - A proposition about the pathogenicity of a variant, the validity of which is assessed and reported by the Statement. A Statement can put forth the proposition as being true, false, or uncertain, and may provide an assessment of the level of confidence/evidence supporting this claim.
   *  - direction
      -
      - string
      - 1..1
      - A term indicating whether the Statement supports, disputes, or remains neutral w.r.t. the validity of the Proposition it evaluates.
   *  - strength *(refined)*
      -
      - :ref:`MappableConcept`
      - 0..1
      - The strength of support that an ACMG 2015 Variant Pathogenicity statement is determined to provide for or against the proposed pathogenicity of the assessed variant. Strength is evaluated relative to the direction indicated by the 'direction' attribute. The indicated enumeration constrains the nested MappableConcept.primaryCoding > Coding.code attribute when capturing evidence strength.
   *  - score
      -
                        .. raw:: html

                            <span style="background-color: #D3D3D3; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Draft Maturity Level">D</span>
      - number
      - 0..1
      - A quantitative score that indicates the strength of a Proposition's assessment in the direction indicated (i.e. how strongly supported or disputed the Proposition is believed to be). Depending on its implementation, a score may reflect how *confident* that agent is that the Proposition is true or false, or the *strength of evidence* they believe supports or disputes it. Instructions for how to interpret the meaning of a given score may be gleaned from the method or document referenced in 'specifiedBy' attribute.
   *  - classification *(refined)*
      -
      - :ref:`MappableConcept`
      - 1..1
      - The classification of the variant's pathogenicity, based on the ACMG 2015 guidelines. These classifications should coincide with the direction and strength values as follows: 'pathogenic' with supports-strong, 'likely pathogenic' with supports-moderate, 'benign' with disputes-strong, 'likely benign' with disputes-moderate 'uncertain significance' can be one of three possibilities... supports-weak, disputes-weak or neutral for uncertain significance (favoring pathogenic), uncertain significance (favoring benign) or uncertain significance (favoring neither pathogenic nor benign). The 'low penetrance' and 'risk allele' versions of pathogenicity classifications would be applied based on whether the variant proposition was defined to have a 'penetrance' of 'low' or 'risk' respectively.
   *  - hasEvidenceLines *(refined)*
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`VariantPathogenicityEvidenceLine` | :ref:`iriReference`
      - 0..m
      - An evidence-based argument that supports or disputes the validity of the proposition that a Statement assesses or puts forth as true. The strength and direction of this argument (whether it supports or disputes the proposition, and how strongly) is based on an interpretation of one or more pieces of information as evidence (i.e. 'Evidence Items).

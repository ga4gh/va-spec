.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

The molecular consequence of the variant on a transcript and/or protein molecule.

**Information Model**


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
   *  - terms
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`MappableConcept` | :ref:`iriReference`
      - 0..m
      - One or more terms representing the specific types of consequence the variant has on transcript and/or protein molecules or regions. These are typically terms from the 'structural_variant' branch of the Sequence Ontology, e.g. 'SO:0001627' (intron_variant), or 'SO:0001589' (frameshift_variant).

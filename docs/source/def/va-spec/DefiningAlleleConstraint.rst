.. admonition:: Trial Use
    :class: note

    May change in future releases. See |maturity-model|.

**Computational Definition**

The defining allele and its associated relationships that are congruent with member variants.

**Information Model**

Some DefiningAlleleConstraint attributes are inherited from :ref:`Constraint`.

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
   *  - type
      -
      - string
      - 1..1
      - MUST be "DefiningAlleleConstraint"
   *  - allele
      -
      - :ref:`Allele` | :ref:`iriReference`
      - 1..1
      -
   *  - relations
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`MappableConcept`
      - 0..m
      - Defined relationships from which members relate to the defining allele.

.. admonition:: Draft
    :class: warning

    May change significantly in future releases. See |maturity-model|.

**Computational Definition**

Components that define a molecular adjacency of congruent elements.

**Information Model**

Some AdjacencyConstraint attributes are inherited from :ref:`Constraint`.

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
      - MUST be "AdjacencyConstraint"
   *  - adjoinedElements
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Ordered">&#8595;</span>
      - :ref:`iriReference` | :ref:`MappableConcept` | :ref:`Location` | :ref:`Terminus` | :ref:`UnspecifiedElement`
      - 2..2
      - The elements of the adjacency.
   *  - functionalDomains
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`FunctionalDomain`
      - 0..m
      - Functional domains whose presence or absence is required to satisfy the adjacency.
   *  - linker
      -
      - :ref:`SequenceExpression`
      - 0..1
      - The sequence found between the adjoined elements.
   *  - orderKnown
      -
      - boolean
      - 1..1
      - When orderKnown is true, the order of adjoinedElements is assumed to denote the 5' partner first and the 3' partner second. If orderKnown is false, then the order of adjoinedElements assumed not in fact to be known, as in the case of a fusion where only one or both partners are known, but not their relative order. This field is redundant and may be set to true when using Sequence Locations and following the VRS 2 Adjacency model, as the order is implied by the usage of start and end on respective adjoinedElements.

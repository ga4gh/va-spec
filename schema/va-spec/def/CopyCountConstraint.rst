.. admonition:: Trial Use
    :class: note

    May change in future releases. See |maturity-model|.

**Computational Definition**

The exact or range of copies that members of this categorical variant must satisfy.

**Information Model**

Some CopyCountConstraint attributes are inherited from :ref:`Constraint`.

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
      - MUST be "CopyCountConstraint"
   *  - copies
      -
      - integer | :ref:`Range`
      - 1..1
      - The precise value or range of copies members of this categorical variant must satisfy.

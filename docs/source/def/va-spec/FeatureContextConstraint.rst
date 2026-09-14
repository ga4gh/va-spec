.. admonition:: Draft
    :class: warning

    May change significantly in future releases. See |maturity-model|.

**Computational Definition**

The feature that members of this categorical variant are associated with.

**Information Model**

Some FeatureContextConstraint attributes are inherited from :ref:`Constraint`.

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
      - MUST be "FeatureContextConstraint"
   *  - featureContext
      -
      - :ref:`MappableConcept`
      - 1..1
      - A feature identifier.

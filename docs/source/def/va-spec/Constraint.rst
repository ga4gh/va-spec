.. admonition:: Trial Use
    :class: note

    May change in future releases. See |maturity-model|.

**Abstract Class** — not instantiated directly; concrete subclasses inherit its attributes.

**Computational Definition**

Constraints are used to construct an intensional semantics of categorical variant types.

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
   *  - type
      -
      - string
      - 1..1
      - MUST be set to the name of the concrete Constraint subtype.

This class must match **one of** the following:

* :ref:`DefiningAlleleConstraint`
* :ref:`DefiningLocationConstraint`
* :ref:`AdjacencyConstraint`
* :ref:`FeatureContextConstraint`
* :ref:`CopyCountConstraint`
* :ref:`CopyChangeConstraint`
* :ref:`FunctionConstraint`


**Subclasses:** :ref:`AdjacencyConstraint`, :ref:`CopyChangeConstraint`, :ref:`CopyCountConstraint`, :ref:`DefiningAlleleConstraint`, :ref:`DefiningLocationConstraint`, :ref:`FeatureContextConstraint`, :ref:`FunctionConstraint`

**Used in:** :ref:`CategoricalVariant`

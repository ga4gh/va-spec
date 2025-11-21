.. note:: This data class is at a **trial use** maturity level and may \
    change in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A group of two or more therapies that are applied in combination to a single patient/subject, or applied individually to a different subset of participants in a research study.

**Information Model**

Some TherapyGroup attributes are inherited from :ref:`ConceptSet`.

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
      - _Not Specified_
      - 0..1
      - MUST be "ConceptSet".
   *  - therapies
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Therapy` | :ref:`TherapyGroup`
      - 2..m
      - A list of therapies that are applied to treat a condition.
   *  - membershipOperator
      -
      - string
      - 1..1
      - The logical relationship between therapies in the group, that indicates how they were applied in treating participants in a study.  The value 'AND' indicates that all therapies in the group were applied in combination to a given patient or subject. The value 'OR' indicates that each therapy was applied individually to a distinct subset of participants in the cohort that was interrogated in a given study.

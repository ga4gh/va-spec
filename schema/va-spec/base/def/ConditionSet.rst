.. note:: This data class is at a **trial use** maturity level and may \
    change in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A set of conditions (diseases, phenotypes, traits) that occur together or are related, depending on the membership operator, and may manifest together in the same patient or individually in a different subset of participants in a research study.

**Information Model**

Some ConditionSet attributes are inherited from :ref:`ConceptSet`.

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
   *  - conditions
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Condition` | :ref:`ConditionSet`
      - 2..m
      - A list of conditions (diseases, phenotypes, traits) that are co-occurring or related, depending on the membership operator.
   *  - membershipOperator
      -
      - string
      - 1..1
      - The logical relationship between conditions in the set, that indicates how they manifest in patients/research subjects. The value 'AND' indicates that all conditions in the set co-occur together in a given patient or subject. The value 'OR' indicates that only one condition in the set manifests in each participant interrogated in a given study.

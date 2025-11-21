.. note:: This data class is at a **trial use** maturity level and may \
    change in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

A set of concepts that may be considered as dependent (occurring together), or independent (existing separately) in the context of some knowledge reported about them, as indicated by a set membership operator. e.g. a set of independent molecular consequences that both result from the presence of a particular genetic variant (membership operator = OR).

**Information Model**

Some ConceptSet attributes are inherited from :ref:`gks-core:Element`.

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
   *  - concepts
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`gks.core:MappableConcept` | :ref:`ConceptSet`
      - 2..m
      - A list of concepts that are dependent (occurring together), or independent (existing separately), depending on the membership operator.
   *  - membershipOperator
      -
      - string
      - 1..1
      - The logical relationship between concepts in the set, in the context of some knowledge reported about them. The value 'AND' indicates that the concepts are dependent and occur together in this context - i.e. the reported assertion is not necessarily true for each concept on its own - only in combination with the other(s). The value 'OR' indicates that each concept applies independently in this context - i.e. the reported assertion is necessarily true for each concept on its own, independent of the presence of the other(s).

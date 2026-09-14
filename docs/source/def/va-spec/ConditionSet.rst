.. admonition:: Trial Use
    :class: note

    May change in future releases. See |maturity-model|.

**Computational Definition**

A specialization of ConceptSet representing a set of conditions (diseases, phenotypes, traits) that occur together or are related, depending on the membership operator. Concepts are restricted to Condition and ConditionSet members.

**Information Model**

This class refines :ref:`ConceptSet`.

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
      - MUST be "ConceptSet".
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
   *  - conceptSetType
      -
      - string
      - 0..1
      - A term indicating the type of concept being represented by the ConceptSet.
   *  - concepts *(refined)*
      -
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Condition` | :ref:`ConditionSet`
      - 2..m
      - A list of concepts that are dependent (occurring together), or independent (existing separately), depending on the membership operator.
   *  - membershipOperator
      -
      - string
      - 1..1
      - The logical relationship between concepts in the set, in the context of some knowledge reported about them. The value 'AND' indicates that the concepts are dependent and occur together in this context - i.e. the reported assertion is not necessarily true for each concept on its own - only in combination with the other(s). The value 'OR' indicates that each concept applies independently in this context - i.e. the reported assertion is necessarily true for each concept on its own, independent of the presence of the other(s).

**Used in:** :ref:`VariantClinicalSignificanceProposition`, :ref:`VariantDiagnosticProposition`, :ref:`VariantOncogenicityProposition`, :ref:`VariantPathogenicityProposition`, :ref:`VariantPrognosticProposition`, :ref:`VariantTherapeuticResponseProposition`

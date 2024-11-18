.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

An object holding a name-value pair used to describe a trait or role of an individual member of a StudyGroup.

**Information Model**

Some Characteristic attributes are inherited from :ref:`gks-core:Element`.

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
      - The 'logical' identifier of the data element in the system of record, e.g. a UUID.  This 'id' is unique within a given system, but may or may not be globally unique outside the system. It is used within a system to reference an object from another.
   *  - extensions
      - 
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Extension`
      - 0..m
      - A list of extensions to the Entity, that allow for capture of information not directly supported by elements defined in the model.
   *  - name
      - 
      - string
      - 1..1
      - The type of the trait  or role described by the trait (e.g. 'ethnicity', 'sex', 'age', 'disease status').
   *  - value
      - 
      - string
      - 1..1
      - The specific value(s) that the indicated traitor role holds in all population members (e.g. 'east asian', 'female', 'adolescent', 'cancer').
   *  - valueOperator
      - 
      - boolean
      - 0..1
      - An operation that defines how to logically interpret a set of more than one Characteristic values ('AND', 'OR', 'NOT')

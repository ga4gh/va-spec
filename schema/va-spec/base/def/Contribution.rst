.. warning:: This data class is at a **draft** maturity level and may \
    change significantly in future releases. Maturity \
    levels are described in the :ref:`maturity-model`.

**Computational Definition**

An action taken by an agent in contributing to the creation, modification, assessment, or deprecation of a particular entity (e.g. a Statement, EvidenceLine, DataSet, Publication, etc.)

**Information Model**

Some Contribution attributes are inherited from :ref:`Activity`.

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
   *  - label
      - 
      - string
      - 0..1
      - A primary name for the entity.
   *  - description
      - 
      - string
      - 0..1
      - A free-text description of the Entity.
   *  - alternativeLabels
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
   *  - subtype
      - 
      - :ref:`MappableConcept`
      - 0..1
      - A specific type of activity the Activity instance represents.
   *  - date
      - 
      - _Not Specified_
      - 0..1
      - The date that the Activity was completed.
   *  - specifiedBy
      - 
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Method`
      - 0..m
      - A method that was followed in performing an Activity, that describes how it was executed.
   *  - type
      - 
      - string
      - 1..1
      - MUST be "Contribution".
   *  - contributor
      - 
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Agent`
      - 1..1
      - The agent that made the contribution.
   *  - activityType
      - 
      - :ref:`MappableConcept`
      - 0..1
      - The specific type of activity performed or role played by an agent in making the contribution (e.g. for a publication, agents may contribute as a primary author, editor, figure designer, data generator, etc. . Values of this property may be framed as activities or as contribution roles (e.g. using terms from the Contribution Role Ontology (CRO)).

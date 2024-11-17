.. warning:: This data class is at a **draft** maturity level and may change
    significantly in future releases. Maturity levels are described in
    the :ref:`maturity-model`.

**Computational Definition**

A reusable structure that encapsulates provenance metadata about a serialized data record or object in a particular dataset (as opposed to provenance about the real world entity this record or object represents).

**Information Model**

Some RecordMetadata attributes are inherited from :ref:`gks-core:Element`.

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
   *  - recordIdentifier
      - 
      - string
      - 0..1
      - The identifier of the data record or object described in this RecordMetadata object.
   *  - recordVersion
      - 
      - string
      - 0..1
      - The version number of the record-level artifact the object describes.
   *  - derivedFrom
      - 
      - string
      - 0..1
      - Another data record from which the record described here was derived, through a data ingest and/or transformation process. Value should be a string representing the identifier of the source record.
   *  - dateRecordCreated
      - 
      - :ref:`datetime`
      - 0..1
      - The date the record was initially created.
   *  - contributions
      - 
                        .. raw:: html

                            <span style="background-color: #B2DFEE; color: black; padding: 2px 6px; border: 1px solid black; border-radius: 3px; font-weight: bold; display: inline-block; margin-bottom: 5px;" title="Unordered">&#8942;</span>
      - :ref:`Contribution`
      - 0..m
      - Describes specific contributions made by an human or software agent to the creation, modification, or administrative management of a data record or object.

**Computational Definition**

A set of instructions that specify how to achieve some objective (e.g. experimental protocols,  curation guidelines, rule sets, etc.)

**Information Model**

Some Method attributes are inherited from :ref:`Entity`.

.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto
   
   *  - Field
      - Type
      - Limits
      - Description
   *  - id
      - string
      - 0..1
      - The 'logical' identifier of the entity in the system of record, e.g. a UUID. This 'id' is  unique within a given system. The identified entity may have a different 'id' in a different  system, or may refer to an 'id' for the shared concept in another system (e.g. a CURIE).
   *  - type
      - string
      - 1..1
      - MUST be "Method".
   *  - label
      - string
      - 0..1
      - 
   *  - extensions
      - `Extension <core.json#/$defs/Extension>`_
      - 0..m
      - 
   *  - is_reported_in
      - `CURIE <core.json#/$defs/CURIE>`_ | :ref:`Document`
      - 0..1
      - 
   *  - subtype
      - `Coding <core.json#/$defs/Coding>`_
      - 0..1
      - A more specific type of entity the method represents (e.g. Variant Interpretation Guideline,  Experimental Protocol)

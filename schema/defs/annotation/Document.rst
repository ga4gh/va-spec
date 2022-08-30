**Computational Definition**

a representation of a physical or digital document

**Information Model**

Some Document attributes are inherited from :ref:`Entity`.

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
      - Must be "Document"
   *  - label
      - string
      - 0..1
      - 
   *  - extensions
      - `Extension <core.json#/$defs/Extension>`_
      - 0..m
      - 
   *  - xrefs
      - `CURIE <core.json#/$defs/CURIE>`_
      - 0..m
      - An array of compact Uniform Resource Identifiers (CURIE) used to identify the document in other systems, such as digital object identifiers or PubMed IDs.
   *  - title
      - string
      - 0..1
      - 

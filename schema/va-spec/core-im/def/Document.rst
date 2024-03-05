**Computational Definition**

a representation of a physical or digital document

    **Information Model**
    
Some Document attributes are inherited from :ref:`gks.core:MappableEntity`.

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
       *  - label
          - string
          - 0..1
          - A primary label for the entity.
       *  - description
          - string
          - 0..1
          - A free-text description of the entity.
       *  - extensions
          - `Extension <../../gks-common/core.json#/$defs/Extension>`_
          - 0..m
          - 
       *  - mappings
          - `Mapping <../../gks-common/core.json#/$defs/Mapping>`_
          - 0..m
          - 
       *  - type
          - string
          - 0..1
          - Must be "Document"
       *  - title
          - string
          - 0..1
          - The title of the Document
       *  - url
          - string
          - 0..1
          - A URL at which the document may be retrieved.
       *  - doi
          - string
          - 0..1
          - A `Digital Object Identifier <https://www.doi.org/the-identifier/what-is-a-doi/>_`  for the document.
       *  - pmid
          - integer
          - 0..1
          - A `PubMed unique identifier <https://en.wikipedia.org/wiki/PubMed#PubMed_identifier>`_.

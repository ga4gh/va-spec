**Computational Definition**

The abstract entity representing a possible fact that may be put forth as true, or subjected to  an evidence-based assessment, by a Statement. As abstract entities, their identity and existence  are independent of space and time, and whether they are ever asserted to be true by some agent.  Propositions may be used in two contexts; (1) by Statements that assert them to be true or false,  or describe the overall level of confidence/evidence for or against them; (2) by Evidence Lines that  report the direction and strength of an evidence-based argument for the Proposition.

    **Information Model**
    
Some Proposition attributes are inherited from :ref:`gks.core:Entity`.

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
       *  - statementText
          - string
          - 0..1
          - A natural-language expression of the Proposition's meaning. e.g. "BRCA2 c.8023A>G is pathogenic for  Breast Cancer".
       *  - subject
          - {'$ref': '#/$defs/Entity'}
          - 1..1
          - The Entity or concept about which the Proposition is made.
       *  - predicate
          - {'$ref': '../../gks-common/core.json#/$defs/Coding'}
          - 1..1
          - The relationship asserted to hold between the subject and the object of the Proposition.
       *  - object
          - {'$ref': '#/$defs/Entity'}
          - 1..1
          - An Entity that is related to the subject of a Proposition via its predicate.
       *  - qualifier
          - :ref:`Entity` | `Coding <../../gks-common/core.json#/$defs/Coding>`_ | `IRI <../../gks-common/core.json#/$defs/IRI>`_
          - 0..1
          - An entity or concept applied to extend or refine the meaning of a Proposition's core subject-predicate-object  'triple' - by providing additional detail, or constraining the claim to apply in a particular context.
       *  - negated
          - string
          - 0..1
          - A boolean flag set to 'true' to represent a negation of the proposition expressed by the subject, predicate,  object, and qualifiers (e.g. that "Variant X is NOT pathogenic for Disease Y")/

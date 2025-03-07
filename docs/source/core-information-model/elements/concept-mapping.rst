.. _concept-mapping:

Concept Mapping
**************

.. include::  ../../../../schema/gks-core/def/ConceptMapping.rst


**IMPLEMENTATION GUIDANCE**

1. Populating the ``relation`` attribute
 - A mapping relation must be provided in any ``ConceptMapping``. 
 - Permissible values come from the 'mapping relation' branch of the skos ontology, which includes 5 possible mapping relations: relatedMatch, closeMatch, exactMatch, broaderMatch, narrowerMatch.  Refer to documentation/definitions `here <https://www.ebi.ac.uk/ols4/ontologies/skos/properties/http%253A%252F%252Fwww.w3.org%252F2004%252F02%252Fskos%252Fcore%2523mappingRelation?lang=en>`_, and chose the term that best fits. 
 - Use the root 'mappingRelation' term if unsure which to choose, or you do not care to discriminate between more specific relations.

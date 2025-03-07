.. _mappable-concept:

Mappable Concept
****************

.. include::  ../../../../schema/gks-core/def/MappableConcept.rst



**IMPLEMENTATION GUIDANCE**

1. Selecting a ``primaryCoding``

 -  The ``primaryCoding`` is intended to hold a code that is considered the primary representation of the concept, as defined or used in the data provider's system.  
 - This may be an internal/local code or identifier that is used to reference the concept, or a public code (e.g from a community ontology) that the system adopts for internal use.  
 - For example, ``civic.did:30``, ``MONDO:005061``, and ``C3512`` are all possible primary codes for representing the concept of 'lung adenocarcinoma' within a primary Coding.

     - ``civic.did:30`` is a local code defined by the data provider (CIViC)
     - ``MONDO:005061`` is namespaced CURIE from a community ontology (MONDO)
     - ``C3512`` is a code without a namespace from the NCI Thesaurus.  
- In all cases the source of the code should be reported in the ``Coding.system`` attribute. 

2. Populating the ``name`` attribute
 - Either a ``name`` or a ``primaryCoding`` is requried in every ``MappableConcept`` object.  
 - Use ``MappableConcept.name`` in cases where there is no code used by the data provider's system  for the concept. 
 - When there is a code, the name associated with it should be captured within the Coding that holds the code, rather than in this ``name`` attribute.

3. An Annotated Data Example: Representation of the Condition concept 'Lung Adenocarcinoma' in a dataset provided by the CIViC Knowledgebase, which includes three mappings to exact matches in community terminologies. 

.. code-block:: yaml

   conditionQualifier:
       conceptType: Condition                               # optional. a term describing the high level category of concept the MappableConcept object represents
       id: null                                             # optional. id is optional.  can be used if data provider wants / feels it is necessary to give the MappableConcept object itself a unique internal/local identifier for tracking the object in the message / system.                           
       name: null                                           # required (if no `primaryCoding`). used only in cases where there is no code for the concept. When there is a code, the name should be captured in the Coding that holds it. 
       primaryCoding:                                       # required (if no `name`). Takes a Coding object that holds the code considered primary - i.e. the primary representation defined or used in the data provider's system.
         code: civic.did:30                                 # required. symbol for the code in syntax defined the providing system indicated in the 'system' attribute. e.g. civic.did:30, MONDO:005061, C3512 are all possible codes for representing the concept of 'lung adenocarcinoma'.
         name: Lung Adenocarcinoma                          # optional. preferred name for the concept in the source code system (MONDO in this case).
         system: https://civicdb.org                        # required. takes a free text name or iri representing the code system (where an iri exists - could be a url for a homepage about it, or location for accessing content of the system)
         systemVersion: 2                                   # optional. version of the code system in whatever format the system uses. 
         iris:                                              # optional. iris for the concept represented by the code - typically resolvable urls for web pages where information about the concept and its code can be found.  Can be iris from the source code system, or from other systems that provide an iri or url with info about the concept.  
           - https://civicdb.org/diseases/30
        mappings:                                           # optional (mappings are optional). other codes for the concept that the data provider wants to provide. Captured in ConceptMapping objects, which hold a Coding object and a relation term (explicit declarations of the mapping relation).  
       - coding:                                            # required (must be provided in any ConceptMapping). A Coding for the concept, here the MONDO code as obtained from the OBO Foundry / Ontobee service 
           code: MONDO:0005061                              
           name: lung adenocarcinoma   
           system: https://ontobee.org/ontology/MONDO   
           systemVersion: 2025-02-04
           iris: 
             - http://purl.obolibrary.org/obo/MONDO_0005061 
         relation: exactMatch                                # required  (must be provided in any ConceptMapping). Permissible values come from the 'mapping relation' branch of the skos ontology, which includes 5 possible mapping relations: relatedMatch, closeMatch, exactMatch, broaderMatch, narrowerMatch.  Refer to documentation/definitions here (https://www.ebi.ac.uk/ols4/ontologies/skos/properties/http%253A%252F%252Fwww.w3.org%252F2004%252F02%252Fskos%252Fcore%2523mappingRelation?lang=en), and chose the term that best fits. Use the root skos 'mappingRelation' term if unsure which to choose.

       - coding:                                             # Coding for the NCIT Code as obtained from the original source NCIT Browser at https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&code=C3512
           code: C3512                                       # The NCIT browser/source doesn't natively use a curie-like representation
           name: Lung Adenocarcinoma
           system: https://ncithesaurus.nci.nih.gov/         # NCI Thesaurus (NCIT)
           iris: 
             - https://ncithesaurus.nci.nih.gov/ncitbrowser/ConceptReport.jsp?dictionary=NCI_Thesaurus&code=C3512
         relation: exactMatch

       - coding:                                             # Coding for the MeSH code as obtained from MeSH Browser at https://id.nlm.nih.gov/mesh/C538231
           code: C538231                                     # The MeSH system doesn't natively use a curie-like representation
           name: Adenocarcinoma of Lung
           system: https://id.nlm.nih.gov/mesh/              # Medical Subject Headings (MeSH)
           iris: 
             - https://id.nlm.nih.gov/mesh/C538231
         relation: exactMatch

````

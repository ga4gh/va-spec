.. _domain-entities:

Domain Entities
!!!!!!!!!!!!!!!

"Domain Entities" are entities in the domain of discourse that variant annotation data is about - e.g. **Genetic Variation**, and the **Conditions**, **Therapies**, or **Genes** to which they are related. They are considered to represent general types or concepts, as opposed to particular instances (e.g. the disease ‘Lung Cancer’, not ‘patient123’s lung cancer’; or the drug ‘Erlotinib’, not a particular dose given to patient123).

The VA-Spec does not define detailed models for specific types of domain entities - as this is the remit of other standards development organizations. The VA-Spec does incorporate established standard models where they exist (e.g. the `GA4GH Variant Representation Specification (VRS) <https://vrs.ga4gh.org/en/latest/index.html>`_ to represent genetic variation). 

For other types of domain entities, it uses the ``MappableConcept`` element to capture a simple code or name for the entity from an existing terminology or code system, along with optional mappings and metadata about the code system. For example, below the ``conditionQualifier`` attribute holds a ``MappableConcept`` object for Lung Adenocarcinoma as defined by the code "civic.did:30", and with a mapping to the ontology term "MONDO:0005061".

.. parsed-literal::

      "conditionQualifier": 
       {                            
        "conceptType": "Condition",
        "primaryCoding": 
        {
          "code": "civic.did:30",  
          "name": "Lung Adenocarcinoma",
          "system": "https://civicdb.org",                                                      
          "iris": ["https://civicdb.org/diseases/30"]
        },
          "mappings":  [
           {                                                                
            "coding": 
             {                                                                   
              "code": "MONDO:0005061",                             
              "name": "lung adenocarcinoma",  
              "system": "https://ontobee.org/ontology/MONDO",
              "systemVersion": "2025-02-04",
              "iris": ["http://purl.obolibrary.org/obo/MONDO_0005061"]
             },
            "relation": "exactMatch"
           }
         ]
       }

                                                                                                                                                                                                                             
Note that VA-Spec does define minimal structures to represent **sets** of Conditions or Therapies - but these are simply lists of ``MappableConcepts``, as described below.                                                                                                                                                                                                                       
                                                                                                                                                                                                                            
.. _Variation:
        
Variation
@@@@@@@@@

To represent genetic variations that are subjects of VA Statements, the VA-Spec imports two complementary GKS standards:

#. The `GA4GH Variant Representation Specification (VRS) <https://vrs.ga4gh.org/en/latest/index.html>`_, which provides JSON Schema for representing many classes of discrete genetic variation, and tools for generating globally-unique computed variant identifiers. VRS variants represent discrete instances of sequence variation in a specified context (reference, location, state) - which may include single continuous alleles, haplotypes, genotypes, and copy number changes.

#. The `GA4GH Categorical Variation Representation Specification (Cat-VRS) <https://github.com/ga4gh/cat-vrs?tab=readme-ov-file>`_, which is built on top of VRS and provides a terminology and data model for describing 'categorical' variation concepts. Categorical variations are intensionally defined sets of variations, based on criteria that must be met for inclusion in a given category, e.g. "BRAF V600 mutations", or "EGFR exon 19 deletions". 

        
.. _Condition:
        
Condition
@@@@@@@@@

.. include::  ../def/va-spec/Condition.rst
        
At present, individual conditions are represented using a ``MappableConcept`` object that captures a code or name for the condition, along with optional mappings and metadata about the code system. Sets of conditions are represented using the ``ConditionSet`` class, as described below.
        
**Implementation Guidance:**
        
By convention, cases where no condition is given by the data provider SHOULD be specified using a MappableConcept with a ``conceptType = "Absent"``. Additionally, either the ``name`` or ``primaryCoding`` attribute of a MappableConcept must be populated. The name or code may simply reiterate the conceptType (e.g. "Condition Absent"), or report a more specific nature or reason for the absence of a condition (e.g. "Data Missing in Source", "Condition Unknown", "All Mendelian Diseases").

        
.. _ConditionSet:
        
Condition Set
@@@@@@@@@@@@@
       
.. include::  ../def/va-spec/TraitSet.rst

        
.. _Therapeutic:
        
Therapeutic
@@@@@@@@@@@

.. include::  ../def/va-spec/Therapeutic.rst                                                                                                                                                                                                          
At present, individual therapies are represented using a ``MappableConcept`` object that captures a code or name for the therapy, along with optional mappings and metadata about the code system.  Groups of therapies are represented using the ``TherapyGroup`` class, as described below.

                     
.. _TherapyGroup:
        
Therapy Group
@@@@@@@@@@@@@

.. include::  ../def/va-spec/TherapyGroup.rst
        

.. _Gene:
                     
Gene
@@@@

**Computational Definition:** 

A gene is a region (or regions) of genetic sequence that includes all of the elements necessary to encode a functional transcript. A gene may include regulatory regions, transcribed regions and/or other functional sequence regions. (From SO:0000704)
        
**Information Model:**

At present, individual genes are represented as using a MappableConcept that captures a code or name for the gene, along with optional mappings and metadata about the code system. 


-----------

.. note:: Future versions of VA-Spec may incorporate richer models for representing certain types of domain entities, if/when suitable standards are defined by authoritative organizations. 

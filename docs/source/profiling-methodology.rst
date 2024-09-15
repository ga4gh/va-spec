Profiling Methodology
!!!!!!!!!!!!!!!!!!!!!

``WORK IN PROGRESS: PLEASE COME BACK SOON`` 

Modes of Use
############

The VA-Spec will support different levels of adoption and use - from direct contribution to model development and testing, to out-of-the-box adoption of final VA standards.
 * **Mode 1: Direct Adoption**: users want to use an existing VA model as is.
    * Use Case 
       * adopeters have an existing resource that provides variant knowledge, represented using an established model
       * adopters want to transform their data into VA-compliant form as best that existing VA models allow . . . not interested in developing or extending a profile
       * adopters don’t want to use VA model internally, or need VA model to support every last piece of data in their system. 

    * Guidenace:
       * review documentation of existing VA Standard Profiles `HERE <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html>`_.
       * access formal json schema specifications of selected models `HERE <https://github.com/ga4gh/va-spec/tree/1.x/schema/profiles/json>`_.

* **Mode 2: Modified Adoption**: users want to take standard and adapt for use in internal systems


* **Mode 3: De novo Profiling**: uers want to define profiles from scratch - for new statement types perhaps . . . 


Profiling Methodology
#####################

Initial version informally specified as instructions, conventions, examples.

Future work will provide templates and tools that help implement and validate the mothodology and its outputs.



--------------

The SEPIO Profiling Methodology
*******************************
In practice, application of SEPIO to represent actual data requires a 'Profiling' process, in which the gneeric Core-IM is specialized represent specific Statement types. For example, Figure XXX shows how the Core-IM could be specialized into profiles for Variant Pathogenicity, Molecular Consequence, and Therapeutic Response Statements. Note that these profiles exhibit very different levels of complexity, to support the specific evidence and provenance requirements for each type of Statement.   

FIGURE:

Legend: 


Profiling tasks may include:
 * Selecting a subset of classes and attributes needed to represent the Statement/use case of interest (e.g. a data creator may decide not to bring the ``Statement.hasEvidenceLines`` or the ``Evidence Line`` class into their profile).
 * Defining domain-specific subtypes of general purpose Core IM classes (e.g. ``Statement`` -> ``VariantPathogenicityStatement``).
 * Specializing certain attributes to capture domain-specific information (e.g. ``Statement.qualifier`` -> ``VariantPathogenicityStatement.alleleoriginQualifier``).
 * Defining or importing classes representing domain entities that a specific type of Statement is about (e.g. classes to represent a ``Variation``, ``Gene``, ``Disease``).
 * Constraining values of generic Core IM attributes to take specific domain entities or data types as values (e.g. restricting the ``VariantPathogenicityStatement.subject`` field to only take ‘Variation’ instances).
 * Defining domain-specific value sets that get bound to attributes taking coded values (e.g. binding ``VariantPathogenicityStatement.alleleoriginQualifier`` to take only `allele_origin terms <https://www.ebi.ac.uk/ols4/ontologies/geno/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGENO_0000877>`_ from the GENO Ontology)


Profiling tasks may include:
 * selecting a subset of classes and attributes needed to represent the Statement/use case of interest
     * e.g. a data creator may decide not to bring the ``Statement.hasEvidenceLines`` or the ``Evidence Line` class into their profile
 * defining domain-specific subtypes of general purpose Core IM classes
     * e.g. ``Statement`` -> ``VariantPathogenicityStatement``
 * specializing certain attributes to capture domain-specific information
     * e.g. ``Statement.qualifier`` -> ``VariantPathogenicityStatement.alleleoriginQualifier``
 * defining or importing classes representing domain entities that a specific type of Statement is about 
     * e.g. classes to represent a ``Variation``, ``Gene``, ``Disease``
 * constraining values of generic Core IM attributes to take specific domain entities or data types as values
     * e.g. restricting the ``VariantPathogenicityStatement.subject`` field to only take ‘Variation’ instances
 * defining domain-specific value sets that get bound to attributes taking coded values
     * e.g. binding ``VariantPathogenicityStatement.alleleoriginQualifier`` to take only `allele_origin <https://www.ebi.ac.uk/ols4/ontologies/geno/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGENO_0000877>`_ terms from the GENO Ontology

The Profiles that result from this process represent custom, domain-specific information models that can be implemented as formal schema for a particular use case or application.  




.. list-table::
   :class: clean-wrap
   :header-rows: 1
   :align: left
   :widths: auto

   *  - Profiling Task
      - Example
   *  - Select a subset of classes and attributes needed to represent the Statement/use case of interest 
      - Implementers may choose not to use the``Evidence Line` class and related attributes in their profile.
   *  - Define domain-specific subtypes of general purpose Core IM classes 
      - Specialize ``Statement`` -> ``VariantPathogenicityStatement``
   *  - Specialize attributes to capture domain-specific information
      - Specialize ``Statement.qualifier`` -> ``VariantPathogenicityStatement.alleleoriginQualifier``
   *  - Define or import classes for domain entities that profiles Statements are about
      - For a Variant Pathogencity Statement profile, classes to represent the subject ``Variation`` and object ``Disease`` 
   *  - Constrain values of Core IM attributes to take specific domain entities or data types as values
      - Restricting the ``VariantPathogenicityStatement.subject`` field to only take ‘Variation’ instances
   *  - Define value sets that get bound to attributes taking coded values
      - Binding ``VariantPathogenicityStatement.alleleoriginQualifier`` to take only `allele_origin terms from the GENO Ontology <https://www.ebi.ac.uk/ols4/ontologies/geno/classes/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGENO_0000877>`_). 












Figure XXX illulstrates coneptually how such 'Profiles' can be  dervied for representing variant knowledge, including a Variant Pathogenicity Statements, Molecular Consequence Statements, and Therapeutic REsponse Statements




specializaton of its generic elements for a particular domain or application, through a process called 'Profiling'



Implementation of the SEPIO model requires specialization of its general purpose elements with domain-specific features adn constraints, to generate ‘VA Profiles’. Profiles are domain- or application- specific data models that constrain the core information model, and can extend it to support custom schema for a particular use case.  The VA-Spec provides a Profiling Methodology to guide adopters in this process (which is not unlike the FHIR Profiling paradigm widely used in the clinical data domain).  A developing draft of this methodology can be found here.  Work is ongoing to refine and formalize this with template and tooling support. 



is used to extend this generic core model with of domain-specific content, to derive custom schema for representing specific types of Statemetns and supporting evidence and provenance.
It defines 
Figure XXX illulstrates coneptually how such 'Profiles' can be  dervied for representing variant knowledge, including a Variant Pathogenicity Statements, Molecular Consequence Statements, and Therapeutic REsponse Statements
LEgend: 




For more information,  see . . . .

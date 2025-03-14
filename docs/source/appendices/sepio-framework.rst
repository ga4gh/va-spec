.. _sepio-framework:

SEPIO Modeling Framework
!!!!!!!!!!!!!!!!!!!!!!!!

The SEPIO Modeling Framework is a suite of models, methods, and tools to enable the creation of interoperable schema for representing scientific assertions, and the evidence and provenance supporting them. SEPIO was first developed as an ontology by the Monarch Initiative to support standardized RDF representations of evidence and provenance across integrated genotype-phenotype datasets (the Scientific Evidence and Provenance Information Ontology). The ontological model has since been abstracted into a generic Core Information Model (IM) that can be implemented in any language or format. The Core IM is domain-agnostic, and able to represent assertions and their evidence and provenance of any kind.  Application of SEPIO to a specific data set or use case requires defining a ‘Profile’ that extends/customizes the generic core model for a specific domain or application.

The components of the SEPIO Framework include: 

#. **A Domain Analysis Model (DAM)**: an informal description of the domain we are modeling (scientific assertions and their evidence/provenance)
#. **A Core Information Model (IM)**:  defines data structures that can represent information about this domain (for any type of assertion and evidence).
#. **A 'Profiling' Methodology**:  Implementations extend the core model with domain-specific content to define a “SEPIO Profile” - a custom schema for a particular application or use case.
#. **Ontology Support**: An ontological representation of the core model that can be used if desired to produce linked data with ontology-based semantics.

The framework approach addresses challenges posed by the diversity of types, levels of complexity, and use cases for evidence and provenance across knowledge domains and application - which means there is no ‘one-size-fits-all’ solution. The framework allows custom models built on a common semantic foundation can provide a base level of understanding and interoperability, without restricting expressivity. While this approach may not always support out-of-the-box interoperability across all communities of use, it can significantly lower barriers to aggregating, harmonizing, and operating across disparate data.

See the `SEPIO Framework website <https://sepio-framework.github.io/sepio-linkml/about/>`_ for more information about this foundational standard on which the VA Specification is built. 

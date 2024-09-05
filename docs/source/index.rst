GA4GH Variant Annotation Specification
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

* The **Variant Annotation Specification (VA-Spec)** is a standard developed by the Global Alliance for Genomic Health to facilitate and improve sharing of knowledge about any form of genetic or molecular variation. 
* It defines a **set of information models** to represent different kinds of statements made about genetic variants - each built as **profiles** that extend a foundational **core information model**. 
* It provides machine-readable **json-schema specifications** of these models, to support sharing and validation of data through APIs and other exchange mechanisms. 
* It also provides a **modeling framework** through which implementers can build profiles for **new statement types**, or **extend existing profiles** to support novel use cases. 
* This framework has allowed for **implementation-driven development** that reduces bottlenecks imposed by centralized approaches, leverages the collective expertise and perspective of diverse applications, and delivers schema that have bene proven out in working data systems.

**VA-Spec Components:**

#. **A Generic Core Information Model (IM)**. A foundational, domain-agnostic conceptual model that includes SEPIO elements pertinent to VA use cases. *Provides a base on which VA-specific Statement Profiles are built for the GA4GH Community*. `LINK <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/index.html>`_

#. **Standard VA Profiles**: A set of standard models that extend the Core IM to represent specific Statement types, formalized as json-schema specifications. *Provides GA4GH community with recommended standards for out-of-the-box interoperability, and example of how to apply the modeling framework to create new Profiles.* `LINK <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html>`_

#. **A Modeling Framework**:  Implementation support and tooling to facilitate extension and de novo development of Profiles, and mechanisms for feedback to evolve the core spec. *Allows community-driven development and testing of new Profiles for specific annotation types and use cases*. (`IN PROGRESS`) 

#. **Reference Implementation(s)**. A library of software and services that demonstrate the creation, validation, and exchange of compliant data using GA4GH Profiles. *Provides a working example of code that can be adopted and/or extended by adopters.* (`IN PROGRESS`) 

Site Map:
*********
.. toctree::
   :maxdepth: 8
   :includehidden:

   overview
   quick-start
   core-information-model/index
   standard-profiles/index
   implementation-guidance

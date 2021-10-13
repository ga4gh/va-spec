# VA-spec

### Overview 
Variant Annotations are structured data object that holds a central piece of knowledge (a 'Statement') about a genetic variation, along with metadata supporting its interpretation and use. For example, a given annotation may assert knowledge about a variant's molecular consequence, impact on gene function, population frequency, pathogenicity, or impact on therapeutic response to treatment - plus evidence and provenance information supporting this knowledge.   

The GA4GH VA-Specification (VA-Spec) will define **a set of distinct schema** to represent different kinds of 'Statements' made about genetic variantions - each built on a common core information model. It will provide machine-readable messaging specifications to support sharing and validation of data through APIs and other exchange mechanisms. It will also provide a **modeling framework** through which adopters can refine or extend existing VA models, or define entirely new models for new annotation types, by extending the core information model. This framework will allow for a community-driven development paradigm that reduces bottlenecks imposed by centralized development, and leverage the collective expertise and innovations from diverse implementation contexts and use cases.

The VA-Spec builds on the work of the [Scientific Evidence and Provenance Information Ontology (SEPIO) Model and Framework](https://github.com/monarch-initiative/SEPIO-ontology). The coverage and perspective of the **SEPIO Information Model** are well aligned with VA use cases and requirements, and the **SEPIO Modeling Framework** supports a 'Profiling' approach that is well suited to the needs of the VA Community. Furthermore, SEPIO is already being applied in several VA Driver Projects, and its contributors are also members of various GA4GH workstreams. These existing integrations will facilitate the coordinated evolution of the VA ad SEPIO standards.

The SEPIO-based VA-Spec is being authored by a partnership among national resource providers and major public initiatives, working under the governance of the GA4GH. It has been informed by and will be tested in diverse, established, and actively developed Driver Projects, including **ClinGen**, **VICC**, **Genomics England**, the **Monarch Initiative**, **BRCA Exchange**, and **AGHA**. In these projects, it will be used to support different types of tools and information systems, including variant curation tools and interpretation platforms  (e.g. ClinGen, CIViC, Genomics England), variant annotation services (e.g. CGenoimcs England/CellBase), knowledge aggregators/portals (BRCA Exchange, Monarch Initiative), matchmaking applications (e.g. Matchmaker Exchange), and clinical information systems and decision support tools.

### VA-Spec Components
1. **A Generic VA-SEPIO Core Information Model (IM)**. A foundational, domain-agnostic  conceptual model that includes SEPIO elements pertinent to VA use cases. *Provides a base on which VA-specific Statement Profiles are built for the GA4GH Community*. 
2. **Base VA Statement Profiles**: A set of VA-defined models that specialize the Core IM for a specific Statement type. *Provides GA4GH community with recommended standards for out-of-the-box interoperability, and example of how to apply the modeling framework to create new Profiles.*
3. **A Modeling Framework**:  Implementation support and tooling to facilitate extension and de novo development of Profiles, and mechanisms for feedback to evolve the core spec. *Allows community-driven development and testing of new Profiles for specific annotation types and use cases*. 
4. **Reference Implementation(s)**. A library of software and services that demonstrate the creation, validation, and exchange of compliant data using GA4GH Profiles. *Provides a working example of code that can be adopted and/or extended by adopters.*


### Resources and Documentation
The VA team is preparing a v0 release, with formal documentation available soon. At present, modeling artifacts and documentation remains in various documents, slide decks, and Github tickets. Those linked below will provide an overview of this work.  

- **Recent Slide Decks and Presentations:**
    - [March 2021 Presentation to the Variant Interpretation for Cancer Consrtium (VICC)](https://docs.google.com/presentation/d/1ARYkRZtOfXonScqU3REXd7rVnq3aXrBN294FemlZ0vs/edit#) (includes a [video recording](https://www.youtube.com/watch?v=XNy0j4QBt0A))
    - [September 2020 GA4GH Plenary Presentation](https://docs.google.com/presentation/d/1ZFUXQbiUfkgCLE6aDZVrwW9fghu_VfbUsFLmFqPQzNA/edit#)
    - [June 2020 Presentation on SEPIO to the VA group](https://docs.google.com/presentation/d/1_MgJhaOx6fsNdLvKC_5g5V75JrA9oxaacVRQ-XmZFe0/edit#) (incudes a [video recording](https://www.youtube.com/watch?v=7uqgLYhvq0A))

- **Modeling Use Cases and Requirements Documentation**
    - [Data Example Catalog](https://docs.google.com/document/d/1WbW2ts7qX3ONJNj22BlcW4KqfxcPdLsUcnlua4SSZCc/edit#)
    - [Requirements Synthesis](https://docs.google.com/document/d/1J4AqGDEqyK8KAzfiowgHYKJNvzHuwHSHgkN9dleLemY/edit#)
    - [Evidence and Provenance Competency Questions](https://docs.google.com/spreadsheets/d/1HSqXaGgT--wBH4jnCMQy5fasw-0hoGq2p-Pp5kxJ2Jg/edit#gid=902191065)

- **Developing Work Products**:
    - [Statement Data Models](https://docs.google.com/spreadsheets/d/1zQU-Yv7gB7IHKIOVsTh-74BwdtgB9KQpKcWkSHZOa-Q/edit#gid=1646330759) - currently represented in a spreadsheet format. Other sheets in this doc define elements of the larger, foundational information model, but are not yet presented in a user friendly format. More accessible documentation is being generated manually for the upcoming v0 release, and longer term we will programmatically generate a formal specification and documentation from the spreadsheet representation of the model.
    - [Profiling Workflow and Templates](https://docs.google.com/document/d/1bTW_vUtwvIoiK8oKhCab3w_92sLp40NEl7CmXXbewUU/edit#heading=h.xqm2w4idoc2j) to support modelers perform the profiling process to generate models for a specific Statement type
    - An [Implemented Example of the Profiling Workflow](https://docs.google.com/document/d/1V8UbwubFbUCUHIy4lYMyHkkqN5YhjYSMlDsC3AE8iLY/edit) that illustrtes its use to define a Molecular Consequence Statement model
    - An [Early Draft of the VA-Spec v0 Document](https://docs.google.com/document/d/1GEaulzLwfed_0X05beAIhHNjzgG5dFFBQ3x_yXky8QQ/edit) which will include a description of the VA-SEPIO Core IM, and two VA Statement Profiles (Molecular Consequence, Therapeutic Response).
    - Hand-rolled [Data Example of a Therapeutic Response Statement](https://github.com/ga4gh/va-spec/blob/master/docs/Modeling/TherapeuticResponse/CIViC_Examples_TR_Profile_20210713.yml)
    
- **Administrative / Project Management Resources**:
    - [Github Issue Tracker](https://github.com/ga4gh/va-spec/issues) 
    - [Meeting Minutes](https://docs.google.com/document/d/1jbk2RiRUrceYMzM8yJEnyfa9w4UnlaUaj4vjqv7Dnws/edit#)
    - [VA Google Group](https://groups.google.com/a/ga4gh.org/g/ga4gh-variant-annotation) - email list-serv for project communications
    - [GA4GH-VA Google Drive](https://docs.google.com/document/d/1pnwvYBl8GOMFUw4_-VseHPGWwaWw-kQkBvfZPQ331ME/edit#heading=h.9x8o4qogo9jq)  Other documents associated with this effort 
    - [GA4GH VA Slack channel](https://ga4gh.slack.com/archives/CBGR3P1GR)
    
    *Contact justina.chung@ga4gh.org for access to the documents/systems above*


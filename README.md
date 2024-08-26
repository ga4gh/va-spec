# VA-spec

## _Official  VA-Spec v1 release coming in September 2024 - stay tuned!_

------

### Overview 
Variant Annotations are structured data object that holds a central piece of knowledge (a 'Statement') about a genetic variation, along with metadata supporting its interpretation and use. For example, a given annotation may assert knowledge about a variant's molecular consequence, impact on gene function, population frequency, pathogenicity, or impact on therapeutic response to treatment - with evidence and provenance information supporting this knowledge.   

The GA4GH VA-Specification (VA-Spec) will define **a set of distinct schema** to represent different kinds of 'Statements' made about genetic variantions - each built on a common core information model. It will provide machine-readable messaging specifications to support sharing and validation of data through APIs and other exchange mechanisms. It will also provide a **modeling framework** through which adopters can define, refine or extend VA Statement models, by extending the core information model. This framework will allow for a community-driven development paradigm that reduces bottlenecks imposed by centralized development, and leverage the collective expertise and innovations from diverse implementation contexts and use cases.

The VA-Spec builds on the work of the [Scientific Evidence and Provenance Information Ontology (SEPIO) Model and Framework](https://github.com/monarch-initiative/SEPIO-ontology). The coverage and perspective of the **SEPIO Information Model** are well aligned with VA use cases and requirements, and the **SEPIO Modeling Framework** supports a 'Profiling' approach that is well suited to the needs of the VA Community. Furthermore, SEPIO is already being applied in several VA Driver Projects, and its contributors are also members of various GA4GH workstreams. These existing integrations will facilitate the coordinated evolution of the VA ad SEPIO standards.

The SEPIO-based VA-Spec is being authored by a partnership among national resource providers and major public initiatives, working under the governance of the GA4GH. It has been informed by and will be tested in diverse, established, and actively developed Driver Projects, including **ClinGen**, **VICC**, **Genomics England**, the **Monarch Initiative**, **BRCA Exchange**, and **AGHA**. In these projects, it will be used to support different types of tools and information systems, including variant curation tools and interpretation platforms  (e.g. ClinGen, CIViC, Genomics England), variant annotation services (e.g. CGenoimcs England/CellBase), knowledge aggregators/portals (BRCA Exchange, Monarch Initiative), matchmaking applications (e.g. Matchmaker Exchange), and clinical information systems and decision support tools.

### VA-Spec Components to be provided include:
1. **A Generic Core Information Model (IM)**. A foundational, domain-agnostic conceptual model that includes SEPIO elements pertinent to VA use cases. *Provides a base on which VA-specific Statement Profiles are built for the GA4GH Community*. 
2. **Standard VA Statement Profiles**: A set of standard models that extend the Core IM to represent specific Statment types. *Provides GA4GH community with recommended standards for out-of-the-box interoperability, and example of how to apply the modeling framework to create new Profiles.*
3. **A Modeling Framework**:  Implementation support and tooling to facilitate extension and de novo development of Profiles, and mechanisms for feedback to evolve the core spec. *Allows community-driven development and testing of new Profiles for specific annotation types and use cases*. 
4. **Reference Implementation(s)**. A library of software and services that demonstrate the creation, validation, and exchange of compliant data using GA4GH Profiles. *Provides a working example of code that can be adopted and/or extended by adopters.*

### Resources and Documentation
The VA team is preparing an initial release, with formal documentation available soon. Fornow, a brief overview of the work can be found in these [April 2024 GA4GH Connect Slides](https://docs.google.com/presentation/d/122u_A-NVI1ZABU4fmFnuJUYesNM7sPCcYphzr_Za3pc/edit).
    
**Administrative / Project Management Resources**:
  - [Github Issue Tracker](https://github.com/ga4gh/va-spec/issues) 
  - [VA Google Group](https://groups.google.com/a/ga4gh.org/g/ga4gh-variant-annotation) - email list-serv for project communications
  - [GA4GH-VA Google Drive](https://docs.google.com/document/d/1pnwvYBl8GOMFUw4_-VseHPGWwaWw-kQkBvfZPQ331ME/edit#heading=h.9x8o4qogo9jq)  Other documents associated with this effort 
  - [GA4GH VA Slack channel](https://ga4gh.slack.com/archives/CBGR3P1GR)
    
 *Contact beatrice.amos@ga4gh.org for access to the documents/systems above*


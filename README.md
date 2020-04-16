# VA-spec

### Overview 
Variant Annotations are structured data object that holds a central piece of knowledge about a genetic variation, along with metadata supporting its interpretation and use. A given variant annotation may describe  knowledge about its molecular consequence, functional impact on gene function, population frequency, pathogenicity for a given disease, or impact on therapeutic response to a particular treatment.  The GA4GH VA-Specification will define an extensible data model for representation and exchange these and other diverse kinds of variant annotations.  It will provide machine-readable messaging specifications to support sharing and validation of data through APIs and other exchange mechanisms. It will also provide a formal framework for defining custom extensions to the core model - allowing community driven development of VA-based data models for new data types and use cases. A more detailed description of these components can be found [here](https://docs.google.com/document/d/1q8P1bjVyyslLcV8Gw_hXDc9JzOSuNbJyts-QDx1F17s/edit#).

The VA-Spec is being authored by a partnership among national resource providers and major public initiatives, working under the governance of the GA4GH.  It has been informed by and will be tested in diverse, established, and actively developed Driver Projects, including ClinGen, VICC, Genomics England, the Monarch Initiative, BRCA Exchange, AGHA. In these contexts, it will be used to support different types of tools and information systems, including variant curation tools and interpretation platforms  (e.g. ClinGen, CIViC, GeL), variant annotation services (e.g. CellBase), knowledge aggregators/portals (BRCA Exchange, Monarch Initiative), matchmaking applications (e.g. Matchmaker Exchange), and clinical information systems and decision support tools.

### VA-Spec Components
Planned Components for the VA-Spec include:
1. **A Core Information Model**.  A format- and language-agnostic specification for representing annotation data objects. *Provides human-readable documentation, and a foundation on which extensions and computable schema can be built.* `[In progress]`
2. **Extension Mechanisms and Support**. Technical guidance and conventions supporting creation of Implementation Guides (IGs) that specialize the generic core model for specific annotation types and use cases. *Allow community-driven development and testing of models and consensus-based emergence of standards*. `[In progress]`
3. **GA4GH Implementation Guides**. A set of GA*4GH IGs that provide concrete data models and formal message specifications for defined variant annotation types. *Provides community with a recommended standard for interoperability, and an example of how to apply the framework to create models for new annotation types.* `[In progress]`
4. **Reference Implementation(s)**. A library of software and services that demonstrate the creation and exchange of compliant data using GA4GH IGs. *Provides a working example of code that can be adopted and/or extended by adopters.* `[Planned]`


### Documentation and Artifacts
At present, modeling artifacts and documentation about VA efforts remains in various Google documents, slide decks, and tickets - several of which are linked below.  The VA team is preparing a v0 release, and more formal documentation accompanying this release will be available here soon.

- **Modeling Use Cases and Requirements**
    - [Data Example Catalog](https://docs.google.com/document/d/1WbW2ts7qX3ONJNj22BlcW4KqfxcPdLsUcnlua4SSZCc/edit#)
    - [Requirements Synthesis](https://docs.google.com/document/d/1J4AqGDEqyK8KAzfiowgHYKJNvzHuwHSHgkN9dleLemY/edit#)
    - [Evidence and Provenance Competency Questions](https://docs.google.com/spreadsheets/d/1HSqXaGgT--wBH4jnCMQy5fasw-0hoGq2p-Pp5kxJ2Jg/edit#gid=902191065)
- **Developing Work Products**:
    - [Github Issue Tracker](https://github.com/ga4gh/va-spec/issues) 
    - [Developing Data Models](https://docs.google.com/spreadsheets/d/1zQU-Yv7gB7IHKIOVsTh-74BwdtgB9KQpKcWkSHZOa-Q/edit#gid=1646330759)
- **Rodadmap Documents:**
    - [Official 2020 Roadmap](https://docs.google.com/document/d/1pnwvYBl8GOMFUw4_-VseHPGWwaWw-kQkBvfZPQ331ME/edit#heading=h.9x8o4qogo9jq) 
    - [VA-Spec as a Modeling Framework](https://docs.google.com/document/d/1q8P1bjVyyslLcV8Gw_hXDc9JzOSuNbJyts-QDx1F17s/edit#heading=h.3e4s876j01gp)
- **Slide Decks and Presentations:**
    - [March 2020 Virtual Connect VA Slides](https://docs.google.com/presentation/d/1ELY7TzuHx4h7M2hu1UTtWszk1wnb4-9mxZK3oJOZNNQ/edit#slide=id.g826c0c087a_0_241)
    - [Novmber 2019 Slide Deck](https://docs.google.com/presentation/d/1aqZUXem7bS_hHxLGnRY-KzCyvMEKSt8HBp-pEop76FM/edit#slide=id.g825df8a544_0_1)
    - [2020 Retrospective](https://docs.google.com/document/d/17WguFA7eRenRppA_v5JUkAiGCbBzJW_b1wI4Wyi_NqI/edit#heading=h.pk99du6pl3wp)
  
Other Working Documents can be found in the [GA4GH-VA Google Drive](https://docs.google.com/document/d/1pnwvYBl8GOMFUw4_-VseHPGWwaWw-kQkBvfZPQ331ME/edit#heading=h.9x8o4qogo9jq).


# VA-spec

**Official Documentaation:** https://va-ga4gh.readthedocs.io/en/latest

 **VA-Spec v1 release coming in September 2024 - stay tuned!**

-----

### Overview 

**Variant Annotations** are structured data object that holds a central piece of knowledge (a '**statement**') about a molecular variation (aka 'variant'), along with metadata supporting its interpretation and use. For example, a given annotation may assert knowledge about a variant's pathogenicity, impact on gene function, population frequency, molecular consequence, or effect on therapeutic response to treatment - and provide evidence and provenance information supporting this statement.

The GA4GH VA-Specification (VA-Spec) defines a **set of information models** to represent different kinds of statements made about genetic variants- each built as **"profiles"** that extend a foundational **core information model**. It provides machine-readable **json-schema specifications** of these models, to support sharing and validation of data through APIs and other exchange mechanisms. It also provides a **modeling framework** through which implementers can build profiles for new statement types, or refine and extend existing statement profiles to support novel use cases. 
This framework has allowed for **implementation-driven development** that reduces bottlenecks imposed by centralized approaches, leverages the collective expertise and perspective of diverse applications, and delivers schema that have bene proven out in working data systems.

The VA-Spec core information model and profiling approach is based on the [Scientific Evidence and Provenance Information Ontology (SEPIO) Model and Framework](https://sepio-framework.github.io/sepio-linkml/). SEPIO is already being applied by several VA Driver Projects, and its contributors are also members of various GA4GH workstreams. These existing integrations will facilitate the coordinated evolution of the VA ad SEPIO standards.

The VA-Spec is being authored by a partnership among national resource providers and major public initiatives, working under the governance of the GA4GH. It has been informed and tested in diverse, established, and actively developed Driver Projects, including **ClinGen**, **VICC**, **Genomics England**, the **Monarch Initiative**, **BRCA Exchange**, and **MAVEdb**. In these projects, it is/will be applied to support different types of tools and information systems, including variant **curation tools** and **interpretation platforms** (e.g. ClinGen, CIViC), variant **annotation services** (e.g. Genomics England/CellBase), **knowledge aggregators** (BRCA Exchange, Monarch Initiative), and experimental variant **analysis pipelines** (MAVEdb).


### VA-Spec Components:
1. **A Generic Core Information Model (IM)**. A foundational, domain-agnostic conceptual model that includes SEPIO elements pertinent to VA use cases. *Provides a base on which VA-specific Statement Profiles are built for the GA4GH Community*. ([`LINK`](https://va-ga4gh.readthedocs.io/en/latest/core-information-model/index.html))
2. **Standard VA Profiles**: A set of standard models that extend the Core IM to represent specific Statement types, formalized as json-schema specifications. *Provides GA4GH community with recommended standards for out-of-the-box interoperability, and example of how to apply the modeling framework to create new Profiles.* ([`LINK`](https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html))
3. **A Profiling Methodology**:  Implementation support and tooling to facilitate extension and de novo development of Profiles, and mechanisms for feedback to evolve the core spec. *Allows community-driven development and testing of new Profiles for specific annotation types and use cases*. (`IN PROGRESS`) 
4. **Reference Implementation(s)**. A library of software and services that demonstrate the creation, validation, and exchange of compliant data using GA4GH Profiles. *Provides a working example of code that can be adopted and/or extended by adopters.* (`IN PROGRESS`) 

### Resources and Documentation
The VA team is preparing an initial release, with formal documentation available soon. For now, a brief overview of the work can be found in these [April 2024 GA4GH Connect Slides](https://docs.google.com/presentation/d/122u_A-NVI1ZABU4fmFnuJUYesNM7sPCcYphzr_Za3pc/edit).
    
**Administrative / Project Management Resources**:
  - [Github Issue Tracker](https://github.com/ga4gh/va-spec/issues) 
  - [VA Google Group](https://groups.google.com/a/ga4gh.org/g/ga4gh-variant-annotation) - email list-serv for project communications
  - [GA4GH-VA Google Drive](https://docs.google.com/document/d/1pnwvYBl8GOMFUw4_-VseHPGWwaWw-kQkBvfZPQ331ME/edit#heading=h.9x8o4qogo9jq)  Other documents associated with this effort 
  - [GA4GH VA Slack channel](https://ga4gh.slack.com/archives/CBGR3P1GR)
    
 *Contact beatrice.amos@ga4gh.org for access to the documents/systems above*


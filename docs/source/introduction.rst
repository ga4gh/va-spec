Introduction
!!!!!!!!!!!

Overview
########

Variant Annotations are structured data object that holds a central statement of knowledge about a molecular variation (aka 'variant'), along with evidence and provenance metadata supporting its interpretation and use. For example, a given annotation may report knowledge about a variant's pathogenicity, impact on gene function, population frequency, molecular consequence, or effect on therapeutic response to treatment - and provide evidence and provenance information supporting this knowledge. For more on variant annotation definitions and scope, see  
`"What is a Variant Annotation?" <https://va-ga4gh.readthedocs.io/en/stable/faq.html#what-is-a-variant-annotation>`_, `"What types of variants are covered?" <https://va-ga4gh.readthedocs.io/en/stable/faq.html#what-types-of-variants-are-covered-by-the-va-spec>`_, and `"What types of variant knowledge are covered?" <https://va-ga4gh.readthedocs.io/en/stable/faq.html#what-types-of-variant-knowledge-are-covered-by-the-va-spec>`_ FAQ pages.

Reliable exchange of these and other types of Variant Annotations by clinicians, researchers, and testing laboratories is required to maximize the personal, public, research, and clinical value of genomic information.  The GA4GH Variant Annotation Specification (VA-Spec)  was developed by a partnership among national information resource providers, major public initiatives, and diagnostic testing laboratories — as an open specification to standardize the exchange of such variation knowledge.

The VA-Spec is comprised of the following components:

#. `A Foundational Core Information Model <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/index.html>`_: A domain-agnostic model for describing knowledge statements of any kind, and the evidence and provenance supporting them. This model, which is based on the SEPIO Framework, establishes a shared understanding of fundamental terms, concepts, and modeling patterns, and provides a foundation on which standard models for specific types of statements about molecular variation are built.  

#. `Standard VA Profiles <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html>`_: A set of models built as 'Profiles' of the Core Information Model, which describe specific types of statements made about molecular variation (e.g. 'Variant Pathogenicity Statements'). These models are provided as machine-readable json schema, to support validation and sharing of data through APIs and other exchange mechanisms. They provide a standard for representing different types of variation knowledge for the GA4GH community.

#. `A Modeling Framework <https://va-ga4gh.readthedocs.io/en/latest/modeling-framework.html>`_:  A profiling methodology and tooling support to guide VA and external developers in executing the profiling process.  This framework allows community adopters can build profiles for new statement types, or extend existing profiles - supporting an implementation-led approach that drives VA standards development.

#. `A Python Reference Implementation <https://va-ga4gh.readthedocs.io/en/stable/reference-implementation.html>`_:  A library of software and services that demonstrate the creation, validation, and exchange of compliant data using GA4GH Profiles. These resources provide a working example of code that can be adopted and/or extended by adopters. ``COMING SOON``

This framework has allowed for implementation-driven development that reduces bottlenecks imposed by centralized approaches, leverages the collective expertise and perspective of diverse applications, and delivers schema that have bene proven out in working data systems.

-------------

The document below provides an high-level introduction to VA-Spec models, development processes, and modes of use - with links to separate pages for additional details.

For a hands on experience with VA-Spec data, see the simple Variant Pathogenicity Statement example here (TO DO).



Modeling Foundations
####################
 The VA-Spec was built on top of the `SEPIO Modeling Framework <https://sepio-framework.github.io/sepio-linkml/about/>`_ - adopting its established models, conventions, and profiling methodology to produce standard models for the GA4GH community. 
 * The SEPIO framework provides a domain-agnostic **Core Information Model (Core-IM)** and **Profiling Methodology** that was used to define schema for specific kinds of VA Statements, and the specific kinds of evidence and provenance information that support them. 
 * The Core Information Model . . . 
 * The Profiling Methodology . . . 
 * The the VA-Spec has applied the framework to to define a VA-specific core-im as the foundation of . . . ,  and create several profiles for specific statement types, including 'Variant Pathogenicity Statement' and 'Variant Therapeutic Response Statement' profiles, among others found `here <https://va-ga4gh.readthedocs.io/en/stable/standard-profiles/index.html>`_. 


For more about the SEPIO Modeling Framework, including an overview its COre Information Model and Profiling MEthodology, see here. 








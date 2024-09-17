Quick Start Guide
!!!!!!!!!!!!!!!!!

``PREREQUISITES``: `Introduction <https://va-ga4gh.readthedocs.io/en/latest/introduction.html>`_


VA-Spec Models and Dependencies
###############################

`VA Standard Profile schema <https://github.com/ga4gh/va-spec/tree/1.x/schema/profiles/json>`_ represent the final output of modeling efforts that unfold across a stack of dependent models and specifications, as depicted below and described in detail in the `Introduction <https://va-ga4gh.readthedocs.io/en/stable/introduction.html#va-standards-development-and-dependencies>`_. 

It is **critical that developers understand these models and their dependencies** before beginning to use or contribute to the VA-Spec. 

.. _va-model-dependencies:

.. figure:: images/va-model-dependencies.png

   Ecosystem of VA Models and Dependencies

   **Legend** A hierarchy of models support generation of the Standard Profile Schema that are the final product of the VA-Specification. Arrows on the left describe PROCESSES through which downstream models are generated from more foundational ones. Arrows on the right describe the propagation of requirements from implementation models to INFORM upstream Core-IM expansion and refinement. The format of each model (e.g. 'YAML', 'JSON') is indicated by icons on each.

An overview of the interactions between repositories housing these models, along with links to source models and documentation, is provided at the `end of this page <https://va-ga4gh.readthedocs.io/en/latest/quick-start.html#github-repositories-and-links>`_.  

Where do I Start?
#################

New adopters will come to the VA-Spec with some requirements or representation of variant knowledge - be it an explicit model, or models implicit in data collection forms or data examples. There are many ways these adopters may engage with the VA-Spec as a Modeling Framework. Some may simply want to implement an existing Standard Profile out-of-the-box for their data. Others may find an existing Standard Profile insufficient - and wish to refine or extend it to meet their needs. And others may discover that no Standard Profile exists for the type of knowledge they want to represent, and collaborate with the VA team to derive a new Profile from the GKS Core-IM.

The DECISION TREE below is designed to help adopters navigate these options, and find the right entry point for engagement with the VA Framework based on their data and requirements.
 * Follow the tree downward, choosing the appropriate path based on your data and project requirements. 
 * Blue nodes present a **DECISION** to be made. Green nodes describe a terminal **ACTION** to be taken. 
 * Guidance to help you make Decisions or perform Actions is provided below the tree, organized by node number.

The workflow and guidance provided is the same for **Statement** Profiles, which are used to represent discrete assertions of variant knowledge (e.g. a pathogenicity classification), or **Study Result** Profiles, which are used to capture collections of data about a variant from a particular study or analysis dataset (e.g. the gnomAD cohort allele frequency dataset). 

.. _quick-start-decision-tree:

.. figure:: images/quick-start-decision-tree.png

   Decision Tree to guide Engagement of Adopters with the VA-Spec

   **Legend** The path on the **left** guides users in adopting or extending an existing Standard Profile. The path on the **right** guides users in creating an entirely new Standard Profile.

**Node Guidance and Resources:**

#. ``DECISION``: **Does a Standard Statement or Study Result Profile exist for my use case?**
    * Explore existing Standard Profiles `here <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html>`_ to see if any cover the type of Statement or Study Result you want to represent.

#. ``DECISION``: **Does the existing Standard Profile cover all my data and requirements??**
    * Use the documentation for the Profile (e.g. `here <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/statement-profiles.html#variant-pathogenicity-statement>`_) to map your data or model onto the classes and attributes the Profile  provides, noting any data that is not accommodated. 

#. ``DECISION``: **Does the GKS Core-IM contain elements needed to extend the existing Profile for any 'orphan' data?**
    * Explore the `GKS Core-IM <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/index.html>`_ to identify elements that might support your 'orphan' data (i.e. data items that are not supported by the existing Profile).

#. ``DECISION``: **Does upstream SEPIO Core-IM contain elements needed to extend the Profile for any orphan data??**
    * Explore the `SEPIO Core-IM <https://sepio-framework.github.io/sepio-linkml/>`_ to identify elements that might support your orphan data.
	
#. ``DECISION``: **Do I have the motivation to initiate Core-IM changes to support expanding the Profile for my orphan data??**
    * Consider if you need the Standard Profile to fully support all your data, given your use case, and the option to use `Extension <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/data-types.html#extension>`_ element. 
    * If you do, extending the Standard Profile will require working with SEPIO and VA teams to extend these upstream models, and then pulling these new elements into the Profile.
    * While changes to these core models will require a bit more work, the close relationship between SEPIO and GKS developers will enable efficient coordination of effort and propagation of new modeling elements across these core models. Please reach out to us for help. 

#. ``ACTION``: **Work with GKS team to change Core models, then expand Standard Profile using this new content**
    * If you decide you want to work with the VA team to enhance the Standard Profile to better support your data, make a concrete proposal for the changes or additions you need.
    * You may file a `Github Issue <https://github.com/ga4gh/va-spec/issues>`_ describing the proposed enhancements, or create them in a branch of the Profile and submit a `Pull Request <https://github.com/ga4gh/va-spec/pulls>`_.  
    * The VA Team will coordinate discussions with other implementers and upstream standards to ensure the proposed changes are amenable to implementation needs and aligned with broader VA modeling principles, and any changes made are propagated to GKS and SEPIO models. 
	
#. ``ACTION``: **Adopt the Standard Profile as is**
    * If the existing profile sufficiently supports your data and requirements, you can find its json schema specification `here <https://github.com/ga4gh/va-spec/tree/1.x/schema/profiles/json>`_ for implementation in your system.

#. ``ACTION``: **Extend the existing Profile using these GKS Core-IM elements**
    * Add the new Core-IM elements to the existing Profile, following the Profiling Methodology `here <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_ to specialize them for your data as needed.

#. ``ACTION``: **Pull required elements from the SEPIO Core-IM into the GKS Core-IM, and use them to expand the existing Profile**
    * Make a ticket or PR yourself, or contact the VA team for help pulling these elements into the GKS Core-IM.
    * These new Core-IM elements can then be included and specialized as needed into the existing Profile, following the Profiling Methodology Guidance `here <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_.

#. ``ACTION``: **Implement existing Standard Profile as is, and use 'Extensions' for unsupported data**
    * If it acceptable that the Profile does not directly support the orphan data in your specific implementation, you can use the `Extension <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/data-types.html#extension>`_ modeling pattern capture this data, and still be in compliance with the Profile specification. 
    * Alternatively, your implementation model can define bespoke attributes for this data, but these will not be compliant with the standard Profile. 
    * Regardless of your approach, we suggest that you file a `Github Issue <https://github.com/ga4gh/va-spec/issues>`_ describing your unmet need, so that we might one day add support to the model, and notify you when this happens. 

#. ``DECISION``: **Does the GKS Core-IM contain elements needed to define a new Profile for my data?**
    * If none of the existing Standard Profiles matches your data, you will have to help us create one!
    * You can follow the Profiling Methodology Guidance `here <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_.
    * An initial step is to look at the generic `GKS Core-IM <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/index.html>`_ to identify elements needed to support your data, and note any gaps that may exist. 

#. ``DECISION``: **Does the upstream SEPIO Core-IM contain elements  needed to define a new Profile for my data??**
    * If the GKS Core-IM does not support all of your data, look to the upstream `SEPIO Core-IM <https://sepio-framework.github.io/sepio-linkml/>`_ from which it was derived. 
    * It will have a larger selection of elements that can be pulled into the GKS Core-IM as needed. 
    * Note elements that you want to pull into the GKS Core-IM, as well as any data that for which it does not offer support. 
	
#. ``DECISION``: **Do I have the motivation to initiate Core-IM changes to support my Profile needs??**
    * If you need the Profile to fully support the orphan data, but the GKS and SEPIO Core-IMs do not have the elements you need, building your Profile will require working with SEPIO and VA teams to extend these upstream models, and then pulling these new elements into the Profile. Please reach out to us for help. 
    * While changes to these core models will require a bit more work, the close relationship between SEPIO and GKS developers will enable efficient coordination of effort and propagation of new modeling elements across these standards.
	
#. ``ACTION``: **Build the best Profile you can from Core models, and use  'Extensions' for unsupported data**
    * If it acceptable that the Profile does not directly support the orphan data in your specific implementation, you can use the `Extension <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/data-types.html#extension>`_ modeling pattern capture this data informally, and still be in compliance with the Profile specification. 
    * Alternatively, your implementation model can define bespoke attributes for this data, but these will not be compliant with the standard Profile. 
    * Regardless of your approach, we suggest that you file a `Github Issue <https://github.com/ga4gh/va-spec/issues>`_ describing your unmet need, so that we might one day add support to the model, and notify you when this happens. 

#. ``ACTION``: **Build new Standard Profile on existing GKS Core-IM**
    * If the GKS Core-IM has what you need to represent your data, follow the `Profiling Methodology <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_ to derive a Profile for your new Statement or study Result type.  Reach out for help as you go, and submit a `Pull Request <https://github.com/ga4gh/va-spec/pulls>`_ when you have a draft ready to share.
    * If the GKS Core-IM is lacking, consult the upstream SEPIO Core-IM to see if it contains the elements you need. If it does, contact the VA team for help pulling these into the GKS Core-IM, so they can be used in your Profile.
    * If neither Core-IM has what you need, building your Standard Profile may require working with SEPIO and VA teams to add support to these upstream models, and then pulling these new elements into your Profile.  Reach out and we will be happy to help.

#. ``ACTION``: **Pull required elements from the SEPIO Core-IM into the GKS Core-IM, and use to build new Profile**
    * Contact the VA team for help pulling these into the GKS Core-IM.
    * These new Core-IM elements can then be pulled into your new Profile, following the Profiling Methodology Guidance `here <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_ to specialize them for your data as needed.

#. ``ACTION``: **Work with GKS team to expand Core models, then build a Standard Profile using these new elements**
    * If you decide you want to work with the VA team to create a Standard Profile that fully supports your data, start by adding the proposed new elements into your Standard Profile. 
    * When a draft of your new Profile is ready for review, make a `Pull Request <https://github.com/ga4gh/va-spec/pulls>`_ to initiate a broader review.  
    * The VA Team will coordinate discussions with other implementers to ensure the proposed changes are amenable to implementation needs and aligned with broader VA modeling principles. 
    * We will also coordinate discussions with SEPIO developers to add new elements to these models as appropriate, ensuring compliance with these upstream standards.  

.. important:: While this workflow suggests a top-down structure for extending or defining new Standard Profiles on the Core-IM, the process is very much **driven by implementation requirements** in a bottom-up manner. New Standards are initiated as **Draft Implementation Profiles**, which are informed by and aim to use Core-IM elements where possible, but ultimately make decisions based on the needs of their specific application.  Such implementation models are evolved into VA Standards through subsequent efforts led by the VA team to coordinate among all potential adopters, and developers of upstream standards such as SEPIO - to align across these models and use cases in producing the final Standard. For more on this, see `here <https://va-ga4gh.readthedocs.io/en/latest/introduction.html#establishing-and-evolving-va-standards>`_. 

Github Repositories and Links
##############################

The diagram below describes the interactions between different repositories where specifications supporting the VA-Spec are housed - including where data models are imported (via Github submodules) and extended by another. It is important to understand these relationships and dependencies before you begin contributing to the VA Profiles. 

.. _gks-github-ecosystem:

.. figure:: images/gks-github-ecosystem.png

   Ecosystem of GKS Specification Github Repositories (as of September 2024)

.. important:: One feature to note is that the **GKS Core-IM**, along with **GKS Data Types** and **Domain Entities** that may be used by multiple GKS models, are housed in a shared **gks-commons repository**, from which they are imported into downstream specifications.

The imports described above support the creation of VA-Spec Profiles built from content from more foundational models, as illustrated in the figure below.

.. _va-model-import-hierarchy:

.. figure:: images/va-model-import-hierarchy.png

   Hierarchy of GKS data model imports used to build VA Standard Profiles. 

  **Legend** The VA-Spec uses Github submodules to import more foundational models.  **Cat-VRS** and **VRS** are imported to provide models for representing different kinds of molecular variation. **GKS-Commons** provides shared classes and data types that are shared across many GKS models. Information about the content of each of these models can be found in relevant sections of the VA-Spec documentation. 



**Model and Repository Links:**

**SEPIO Core-IM**:
 * **repository**: https://github.com/sepio-framework/sepio-linkml
 * **model source**: https://github.com/sepio-framework/sepio-linkml/blob/main/src/sepio_linkml/schema/sepio_linkml.yaml
 * **documentation**: https://sepio-framework.github.io/sepio-linkml/

**GKS Core-IM**: 
 * **repository**: https://github.com/ga4gh/gks-common/
 * **model source**: https://github.com/ga4gh/gks-common/blob/1.x/schema/core-im/core-im-source.yaml
 * **documentation**: https://va-ga4gh.readthedocs.io/en/latest/core-information-model/index.html

**GKS Domain Entity Models**: 
 * **repository**: https://github.com/ga4gh/gks-common/
 * **model source**: https://github.com/ga4gh/gks-common/blob/1.x/schema/domain-entities/domain-entities-source.yaml
 * **documentation**: https://va-ga4gh.readthedocs.io/en/latest/core-information-model/entities/domain-entities/index.html

**VA Standard Profile IMs**:
 * **repository**: https://github.com/ga4gh/va-spec
 * **model source**: https://github.com/ga4gh/va-spec/tree/1.x/schema/profiles
 * **documentation**: https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html

**VA Standard Profile JSON Schema**: 
 * **repository**: https://github.com/ga4gh/va-spec
 * **model source**: https://github.com/ga4gh/va-spec/tree/1.x/schema/profiles/json (do not edit directly, these are automatically generated from standard profile source yaml files via metaschema processor tooling)
 * **documentation**: https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html

**Implementation Schema**:
 * **repository**: not under VA control - these are distributed across implementation repositories
 * **model source**:  will be specific to each implementing project
 * **documentation**: not under VA control - distributed across implementation websites and documents




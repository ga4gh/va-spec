Quick Start Guide
!!!!!!!!!!!!!!!!!

``PREREQUISITES``: `Introduction <https://va-ga4gh.readthedocs.io/en/latest/introduction.html>`_

`VA Standard Profile schema <https://github.com/ga4gh/va-spec/tree/1.x/schema/profiles/json>`_ represent the final output of modeling efforts that unfold across a stack of dependent models and specifications, as depicted below and described in detail in the `Introduction <https://va-ga4gh.readthedocs.io/en/stable/introduction.html#va-standards-development-and-dependencies>`_. 

It is **critical that developers understand these models and their dependencies** before beginning to use or contribute to the VA-Spec. 

.. _va-model-dependencies:

.. figure:: images/va-model-dependencies.png

   Ecosystem of VA Models and Dependencies

   **Legend** A hierarchy of models and standards support generation of the Standard Profile Schema that are the final product of the VA-Specification. Arrows on the left describe ``PROCESSES`` through which downstream models are generated from more foundational ones. Arrows on the right describe the propagation of requirements from implementation models to inform upstream Core-IM expansion and refinement. The format of each model (e.g. 'YAML', 'JSON') is indicated by icons on each.

An overview of the interactions between repositories housing these models, along with links to source models and documentation, is provided at the end of this page.  


Where do I Start?
#################
As a modeling framework, there are many ways that users may engage with the VA-Spec. Some users may simply want to adopt an existing Standard Profile out-of-the-box for their data. Others may find an existing profile insufficient and wish to refine or extend it to meet their needs. And others may discover that no Profile exists for the type of knowledge they want to represent, and collaborate with the VA team to derive a new Standard Profile from the Core-IM.

The **decision tree** below is designed to help newcomers navigate these options, and find the right entry point for engagement with the VA Framework based on their data and requirements. While it focuses on development and use of **Statement** Profiles, the same workflow and recommendations apply for **Study Result** Profiles.

 * Follow the tree downward, choosing the appropriate path based on your data and project requirements. 
 * Blue nodes present a  **Decision** to be made. Red nodes describe a terminal **Aciton** to be taken. 
 * Guidance to help you answer Decision nodes or act on Action nodes is provided below the tree, organized by node number.

.. note:: The tree is focused on development and use of **Statement** Profiles, used to represent discrete assertions of variant knowledge (e.g. a pathogenicity classification). But the same workflow and recommendations apply to **Study Result** Profiles, which are used to capture collections of data about a variant from a particular study or analysis dataset (e.g. the gnomAD cohort allele frequency dataset). 

.. image:: images/quick-start-decision-tree2.png
  :width: 1000

**Node Guidance and Resources:**

.. note:: If you get stuck or have questions at any point in the process, reach out to the VA Team for help - on `Slack <https://ga4gh.slack.com/archives/CBGR3P1GR>`_, though our `mailing list <https://groups.google.com/a/ga4gh.org/g/ga4gh-variant-annotation>`_, or in our `issue tracker <https://github.com/ga4gh/va-spec/issues>`_.

#. ``DECISION``: **Does a Statement Profile exist for my use case?**
    * Explore existing Statement Profiles `here <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html>`_ to see if any cover the type of Statement you want to represent.

#. ``DECISION``: **Does the existing Statement Profile cover all my data and requirements?**
    * Use the documentation for the Profile (e.g. `here <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/statement-profiles.html#variant-pathogenicity-statement>`_) to map your data or model onto the classes and attributes the Profile  provides, noting any data that is not accommodated. 

#. ``DECISION``: **Does the GKS Core-IM contain elements needed to extend the existing Profile for my 'orphan' data?**
    * Explore the `GKS Core-IM <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/index.html>`_ to identify elements that might support your 'orphan' data (i.e. data items that are not supported by the existing Profile).

#. ``DECISION``: **Does upstream SEPIO Core-IM contain elements needed to define a Statement Profile for my orphan data?**
    * Explore the `SEPIO Core-IM <https://sepio-framework.github.io/sepio-linkml/>`_ to identify elements that might support your orphan data.
	
#. ``DECISION``: **Do I have the time and will to formally extend/refine the profile?**
     * Consider if you need the Profile to fully support all your data,given your use case, and the option ot use `Extension <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/data-types.html#extension>`_ element. IF you do, extending the Statement Profile will require working with SEPIO and VA teams to extend these upstream models, and then pulling these new elements into the Profile.
     * While changes to these core models will require a bit more work, the close relationship between SEPIO and GKS developers will enable efficient coordination of effort and propagation of new modeling elements across these standards. Please reach out to us for help. 

#. ``ACTION``: **Formally extend/refine the Statement Profile to support my orphan data and requirements**
    * If you decide you want to work with the VA team to enhance the Standard Profile to better support your data, make a concrete proposal for the changes or additions you need.
    * To do this, you may file a `Github Issue <https://github.com/ga4gh/va-spec/issues>`_ describing your proposed enhancements, or create them in a branch of the Profile and submit as a `Pull Request <https://github.com/ga4gh/va-spec/pulls>`_.  
    * The VA Team will coordinate discussions with other implementers and standards to ensure the proposed changes are amenable to implementation needs and aligned with broader VA modeling principles, and any changes made are propagated upstream to GKS and SEPIO Core IMs. 
	
#. ``ACTION``: **Adopt the Statement Profile as is**
    * If the existing profile sufficiently supports your data and requirements, you can find its json schema specification `here <https://github.com/ga4gh/va-spec/tree/1.x/schema/profiles/json>`_ for implementation in your system.

#. ``ACTION``: **Extend the Statement Profile using these GKS Core-IM elements**
    * Add the new Core-IM elements to the existing Profile, following the Profiling Methodology `here <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_ to specialize them for your data as needed.

#. ``ACTION``: **Pull required elements from the SEPIO Core-IM into the GKS Core-IM, and build Statement Profile**
    * Contact the VA team for help pulling these into the GKS Core-IM.
    * These new Core-IM elements can then be pulled into the existing Profile, following the Profiling Methodology Guidance `here <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_ to specialize them for your data as needed.

#. ``ACTION``: **Adopt Statement Profile as is, and use 'Extensions' for unsupported data as desired**
    * If it acceptable that the Profile does not directly support the orphan data, you can use the `Extension <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/data-types.html#extension>`_ modeling pattern capture this data informally, and still be in compliance with the Profile specification. 
    * We suggest that you still file a `Github Issue <https://github.com/ga4gh/va-spec/issues>`_ describing your unmet need, so that we might one day add support to the model, and notify you if/when this happens. 

#. ``DECISION``: **Does the GKS Core-IM contain elements needed to define a new Profile for my data?**
    * If none of the existing Standard Profiles matches your data, you will have to help us create one!
    * You can follow the Profiling Methodology Guidance `here <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_.
    * An initial step is to look at the generic `GKS Core-IM <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/index.html>`_ to identify elements needed to support your data, and note any gaps that may exist. 

#. ``DECISION``: **Does upstream SEPIO Core-IM contain elements needed to define a Statement Profile for my data?**
    * If the GKS Core-IM does not support all of your data, look to the upstream `SEPIO Core-IM <https://sepio-framework.github.io/sepio-linkml/>`_ from which it was derived. 
    * It will have a larger selection of elements that can be pulled into the GKS Core-IM as needed. 
    * Note elements that you want to pull into the GKS Core-IM, as well as any data that for which it does not offer support. 
	
#. ``DECISION``: **Do I have the time and will to implement Core-IM changes to support my needs?**
    * If you need the Profile to fully support the orphan data, but the GKS and SEPIO Core-IMs do not have the elements you need, building your Profile will require working with SEPIO and VA teams to extend these upstream models, and then pulling these new elements into the Profile. Please reach out to us for help. 
    * While changes to these core models will require a bit more work, the close relationship between SEPIO and GKS developers will enable efficient coordination of effort and propagation of new modeling elements across these standards.
	
#. ``ACTION``: Build Profile from existing Core-IM elements, use  'Extensions' to capture unsupported data
    * If it acceptable that the Profile does not directly support the orphan data, you can use the `Extension <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/data-types.html#extension>`_ modeling pattern capture this data informally, and still be in compliance with the Profile specification. 
    * We suggest that you still file a `Github Issue <https://github.com/ga4gh/va-spec/issues>`_ describing your unmet need, so that we might one day add support to the model, and notify you if/when this happens. 

#. ``ACTION``: Build new Statement Profile on the existing GKS Core-IM
    * If the GKS Core-IM has what you need to represent your data, follow the `Profiling Methodology <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_ to derive a Profile for your new Statement type.  Reach out for help as you go, and submit a `Pull Request <https://github.com/ga4gh/va-spec/pulls>`_ when you have a draft ready to share.
    * If the GKS Core-IM is lacking, consult the upstream SEPIO Core-IM to see if it contains the elements you need. If it does, contact the VA team for help pulling these into the GKS Core-IM, so they can be used in your Profile.
    * If neither Core-IM has what you need, building your Statement Profile may require working with SEPIO and VA teams to add support to these upstream models, and then pulling these new elements into your Profile.  Reach out and we will be happy to help.

#. ``ACTION``: Pull required elements from the SEPIO Core-IM into the GKS Core-IM, and build Statement Profile 
    * Contact the VA team for help pulling these into the GKS Core-IM.
    * These new Core-IM elements can then be pulled into your new Profile, following the Profiling Methodology Guidance `here <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_ to specialize them for your data as needed.

#. ``ACTION``: Work with SEPIO / GKS teams to change Core-IM models, then build Statement Profile on them
    * If you decide you want to work with the VA team to create a Statement Profile that fully  supports your data, start by adding the proposed new elements into your Statement Profile. 
    * When a draft of your new Profile is ready for review, make a `Pull Request <https://github.com/ga4gh/va-spec/pulls>`_ to initiate a broader review.  
    * The VA Team will coordinate discussions with other implementers to ensure the proposed changes are amenable to implementation needs and aligned with broader VA modeling principles. 
    * We will also coordinate discussions with SEPIO developers to add new elements to these models as appropriate, ensuring compliance with these upstream standards.  


Github Repositories and Links
##############################

The diagram below describes the interactions between different repositories where specifications supporting the VA-Spec are housed - including where data models are imported (via Github submodules) and extended by another. It is important to understand these relationships and dependencies before you begin contributing to the VA Profiles. 

.. _gks-github-ecosystem:

.. figure:: images/gks-github-ecosystem.png

   Ecosystem of GKS Specification Github Repositories (as of September 2024)

.. important:: One feature to note is that the **GKS Core-IM**, along with **GKS Data Types** and **Domain Entities** that may be used by multiple GKS models, are hosued in a shared **gks-commons repository**, from which they are imported into downstream specifications.

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




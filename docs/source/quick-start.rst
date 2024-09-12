Quick Start Guide
!!!!!!!!!!!!!!!!!

``PREREQUISITES``: `Introduction <https://va-ga4gh.readthedocs.io/en/latest/introduction.html>`_

Modes of Use
############

The VA-Spec will support different levels of adoption and use - from direct contribution to model development and testing, to out-of-the-box adoption of final VA standards.

 **Mode 1: Direct Adoption**: users want to use an existing VA model as is.
  * Use Case 
      * adopeters have an existing resource that provides variant knowledge, represented using an established model
      * adopters want to transform their data into VA-compliant form as best that existing VA models allow . . . not interested in developing or extending a profile
      * adopters don’t want to use VA model internally, or need VA model to support every last piece of data in their system. 

  * Guidance:
      * review documentation of existing VA Standard Profiles `HERE <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html>`_.
      * access formal json schema specifications of selected models `HERE <https://github.com/ga4gh/va-spec/tree/1.x/schema/profiles/json>`_.

**Mode 2: Modified Adoption**: users want to take standard and adapt for use in internal systems


**Mode 3: De novo Profiling**: uers want to define profiles from scratch - for new statement types perhaps . . . 


Where Do I Start?
#################

As noted, there are many ways that users may engage with the VA-Spec, depending on their data and project requirements.  The **decision tree** below is designed to help newcomers find the right entry point for engagement with the VA Framework.  
 * Follow the tree downward by choosing the appropriate path based on your data and project requirements.
 * For each blue ``DECISION`` node you traverse, you may consult information and linked resources provided in text below the tree for guidance.
 * When a red ``ACTION`` node is reached, follow the guidance for that node below. 


.. image:: images/quick-start-decision-tree.png
  :width: 1000


**Node Guidance:**

If you get stuck or have questions at any point in the process,  reach out to the VA Team for help - on Slack here, in the issue tracker here, or on our monthly community calls here.

#. ``DECISION``: **Does a Statement Profile exist for my use case?**
    #. Explore documentation about existing Statement Profiles `here <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/index.html>`_ to see if any cover the type of Statement you need to represent.

#. ``DECISION``: **Does the existing Statement Profile cover all my data and requirements?**
    #. Use the documentation for the existing profile `here <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/statement-profiles.html#variant-pathogenicity-statement>`_ to map your data onto the classes and attributes it provides. Note any data that is not accommodated by the existing model. 

#. ``DECISION``: **Does the GKS Core-IM contain elements needed to extend the Profile for my data?**
    #. Look at the generic `GKS Core-IM <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/index.html>`_ to identify elements that might support your orphan data.

#. ``DECISION``: **Does upstream SEPIO Core-IM contain elements needed to define a Statement Profile for my data?**
    #. Look at the `SEPIO Core-IM <https://sepio-framework.github.io/sepio-linkml/>`_ to identify elements that might support your orphan data.
	
#. ``DECISION``: **Do I have the time and will to formally extend/refine the profile?**
    #. If you need the Profile to fully support the orphan data, but the GKS and SEPIO Core-IMs do not have the elements you need, extending the Statement Profile will require working with SEPIO and VA teams to extend these upstream models, and then pulling these new elements into the Profile. Please reach out to us for help. 
    #. While changes to these core models will require a bit more work, the close relationship between SEPIO and GKS developers will enable efficient coordination of effort and propagation of new modeling elements across these standards. 

#. ``ACTION``: **Formally extend/refine the Statement Profile to address my requirements**
    #. If you decide you want to work with the VA team to enhance the Profile to better support your data, start by adding proposed elements into the existing Statement Profile. 
    #. You may file a `Github Issue <https://github.com/ga4gh/va-spec/issues>`_ describing your needs, make a `Pull Request <https://github.com/ga4gh/va-spec/pulls>`_ on the Profile proposing model updates, or reach out for help via the communication channels listed above.  
    #. The VA Team will coordinate discussions with other implementers to ensure the proposed changes are amenable to implementation needs and aligned with broader VA modeling principles. 
    #. We will also coordinate discussions with SEPIO developers to propagate requested changes from the Profile upstream to GKS and SEPIO Core IMs. 
	
#. ``ACTION``: **Adopt the Statement Profile as is**
    #. If the existing profile covers the data you need it to, you can find its json schema specification `here <https://github.com/ga4gh/va-spec/tree/1.x/schema/profiles/json>`_ for implementation in your system.

#. ``ACTION``: **Extend the Statement Profile using these GKS Core-IM elements**
    #. Add the new Core-IM elements to the existing Profile, following the Profiling Methodology Guidance `here <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_ to specialize them for your data as needed.

#. ``ACTION``: **Pull required elements from the SEPIO Core-IM into the GKS Core-IM, and build Statement Profile**
    #. Contact the VA team for help pulling these into the GKS Core-IM.
    #. These new Core-IM elements can then be pulled into the existing Profile, following the Profiling Methodology Guidance `here <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_ to specialize them for your data as needed.

#. ``ACTION``: **Adopt Statement Profile as is, and use 'Extensions' for unsupported data as desired**
    #. If it acceptable that the Profile does not directly support the orphan data, you can use the `Extension <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/data-types.html#extension>`_ modeling pattern capture this data informally, and still be in compliance with the Profile specification. 
	b. We suggest that you still file a `Github Issue <https://github.com/ga4gh/va-spec/issues>`_ describing your unmet need, so that we might one day add support to the model, and notify you if/when this happens. 

#. ``DECISION``: **Does the GKS Core-IM contain elements needed to define a new Profile for my data?**
    #. If none of the existing Standard Profiles matches your data, you will have to help us create one!
    #. You can follow the Profiling Methodology Guidance `here <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_.
    #. An initial step is to look at the generic `GKS Core-IM <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/index.html>`_ to identify elements needed to support your data, and note any gaps that may exist. 

#. ``DECISION``: **Does upstream SEPIO Core-IM contain elements needed to define a Statement Profile for my data?**
    #. If the GKS Core-IM does not support all of your data, look to the upstream `SEPIO Core-IM <https://sepio-framework.github.io/sepio-linkml/>`_ from which it was derived. 
    #. It will have a larger selection of elements that can be pulled into the GKS Core-IM as needed. 
    #. Note elements that you want to pull into the GKS Core-IM, as well as any data that for which it does not offer support. 
	
#. ``DECISION``: **Do I have the time and will to implement Core-IM changes to support my needs?**
    #. If you need the Profile to fully support the orphan data, but the GKS and SEPIO Core-IMs do not have the elements you need, building your Profile will require working with SEPIO and VA teams to extend these upstream models, and then pulling these new elements into the Profile. Please reach out to us for help. 
    #. While changes to these core models will require a bit more work, the close relationship between SEPIO and GKS developers will enable efficient coordination of effort and propagation of new modeling elements across these standards.
	
#. ``ACTION``: Build Profile from existing Core-IM elements, use  'Extensions' to capture unsupported data
    #. If it acceptable that the Profile does not directly support the orphan data, you can use the `Extension <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/data-types.html#extension>`_ modeling pattern capture this data informally, and still be in compliance with the Profile specification. 
    #. We suggest that you still file a `Github Issue <https://github.com/ga4gh/va-spec/issues>`_ describing your unmet need, so that we might one day add support to the model, and notify you if/when this happens. 

#. ``ACTION``: Build new Statement Profile on the existing GKS Core-IM
    #. If the GKS Core-IM has what you need to represent your data, follow the `Profiling Methodology <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_ to derive a Profile for your new Statement type.  Reach out for help as you go, and submit a `Pull Request <https://github.com/ga4gh/va-spec/pulls>`_ when you have a draft ready to share.
    #. If the GKS Core-IM is lacking, consult the upstream SEPIO Core-IM to see if it contains the elements you need. If it does, contact the VA team for help pulling these into the GKS Core-IM, so they can be used in your Profile.
    #. If neither Core-IM has what you need, building your Statement Profile may require working with SEPIO and VA teams to add support to these upstream models, and then pulling these new elements into your Profile.  Reach out and we will be happy to help.

#. ``ACTION``: Pull required elements from the SEPIO Core-IM into the GKS Core-IM, and build Statement Profile 
    #. Contact the VA team for help pulling these into the GKS Core-IM.
    #. These new Core-IM elements can then be pulled into your new Profile, following the Profiling Methodology Guidance `here <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_ to specialize them for your data as needed.

#. ``ACTION``: Work with SEPIO / GKS teams to change Core-IM models, then build Statement Profile on them
    #. If you decide you want to work with the VA team to create a Statement Profile that fully  supports your data, start by adding the proposed new elements into your Statement Profile. 
    #. When a draft of your new Profile is ready for review, make a `Pull Request <https://github.com/ga4gh/va-spec/pulls>`_ to initiate a broader review.  
    #. The VA Team will coordinate discussions with other implementers to ensure the proposed changes are amenable to implementation needs and aligned with broader VA modeling principles. 
    #. We will also coordinate discussions with SEPIO developers to add new elements to these models as appropriate, ensuring compliance with these upstream standards.  


-----------------

Types of Profiles
#################
While the majority of applications of the VA-Spec deal in knowledge statements, and use **Statement** Profiles, the modeling framework supports  profiling of other Core-IM classes such as **Study Result**.  Study Results are used when the information captured represents data items a study or dataset pertaining to some variant of interest, as  opposed to a broader statement of knowledge (e.g, one that may be concluded from interpretation of such data).  

For example, the `CohortAlleleFrequencyStudyResult <https://va-ga4gh.readthedocs.io/en/latest/standard-profiles/study-result-profiles.html#cohort-allele-frequency-study-result>`_ profile specializes the StudyResult class to represent select data from statistical analyses of allele frequencies in different human populations along with methodological and quality metadata.  More information on the StudyResult class and how it can be profiled can be found `here <https://va-ga4gh.readthedocs.io/en/latest/core-information-model/entities/information-entities/study-result.html>`_  and `here <https://va-ga4gh.readthedocs.io/en/latest/profiling-methodology.html>`_.

Note that the decision tree above focuses on getting you to a **Statement** Profile for your data,  but the same workflow and recommendations apply for **Study Result** Profiles.

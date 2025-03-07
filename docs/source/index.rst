GA4GH Variant Annotation Specification
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

The **Variant Annotation Specification (VA-Spec)** is a standard developed by the **Global Alliance for Genomics and Health (GA4GH)** to facilitate sharing of biological and clinical knowledge about genetic variation. 

Readers may wish to review this :ref:`annotated data example <variant-pathogenicity-statement-example>`, to see an end product of the modeling framework before diving in to the documentation below. 

--------

**Documentation Overview:**

* :ref:`Introduction <introduction>`
   An entry point for understanding the VA-Spec and how its components are developed, with links to more detailed content.
* :ref:`VA Core Model <gks-core>`
   Detailed descriptions and implementation guidance for the classes and attributes in the foundational VA Core Model.
* :ref:`VA Standard Profiles <va-standard-profiles>`
   Profiles defined for specific types of Statements, Evidence Lines, Propositions, and Study Results, provided as computable json schema.
* :ref:`Community Profile Sets <community-profile-sets>`
   Sets of VA Standard Profiles that align with terminological conventions of a particular community guideline for generating variant knowledge.
* :ref:`Implementations <implementations>`
   Documentation about code libraries that facilitate implementation of the VA-Spec.
* :ref:`Modeling Foundations <modeling-foundations>`
   An overview of the modeling patterns and principles that underpin VA-Spec information models.
* :ref:`Examples <examples>`
   A set of examples illustrating representation of data using VA Standard Profiles. 
* :ref:`Appendices <appendices>`
   A collection of pages with additional information on various aspects of the VA-Spec.

If you have questions or feedback, please reach out to the VA Team on `Slack <https://ga4gh.slack.com/archives/CBGR3P1GR>`_, through our `mailing list <https://groups.google.com/a/ga4gh.org/g/ga4gh-variant-annotation>`_, or in our `issue tracker <https://github.com/ga4gh/va-spec/issues>`_.

--------

**Full Site Map:**

.. toctree::
   :maxdepth: 4

   introduction
   core-information-model/index
   va-standard-profiles/index
   community-profile-sets/index
   rimplementations
   modeling-foundations
   examples/index
   appendices/index




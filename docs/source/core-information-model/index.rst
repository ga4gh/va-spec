.. _va-core-model:

VA Core Model
!!!!!!!!!!!!!

The **VA Core Model** is a domain-agnostic model that supports explicit representation of scientific knowledge about genetic variation, and the evidence and provenance supporting it. The initial version was derived from the `SEPIO Core Information Model <https://sepio-framework.github.io/sepio-linkml/gks-core-diagram/>`_, through selection of elements needed to support current VA implementation use cases. The VA Core Model is the foundation on which more specialized models for representing specific types of Statements, Study Results, Evidence Lines, and Propositions are built - through a process called 'profiling'.

A hierarchical view of the VA Core Model is illustrated below, followed by links to detailed information about each class.

More about the modeling principles and patterns employed by the Core Model, and the types of data structures it supports, can be found on the :ref:`Modeling Foundations <modeling-foundations>` page.

.. gks-core-class-hierarchy:

.. figure:: ../images/core-im-class-hierarchy.png

   Core Class Hierarchy

   **Legend** Hierarchical structure of classes and attributes comprising the domain-agnostic VA Core Model. Note that a hierarchy of Domain Entity classes has been defined to represent things like Genes, Conditions, and Therapeutic Procedures. This if described separately `here <https://github.com/ga4gh/va-spec/edit/1.x/docs/source/core-information-model/entities/domain-entities/index.rst>`_.

.. toctree::
   :maxdepth: 4
   :caption: VA Core Model Classes

   entities/index
   elements/index
   data-types
   domain-entities

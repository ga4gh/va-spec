.. _va-core-model:

VA Core Model
!!!!!!!!!!!!!

The **VA Core Model** is a domain-agnostic model for representing scientific knowledge about genetic variation, and the evidence and provenance supporting it.

A hierarchical view of the VA Core Model is below. See the :ref:`Modeling Foundations <modeling-foundations>` section for an overview of modeling principles and patterns that govern its use.

.. core-class-hierarchy:

.. figure:: ../images/core-model-class-hierarchy.png

   Core Class Hierarchy

   **Legend**: Hierarchical structure of classes and attributes comprising the domain-agnostic VA Core Model. Classes in darker grey represent the key knowledge artifacts that root VA Profile data structures. Simple classes for representing :ref:`Domain Entities <domain-entities>` such Conditions and Therapies are defined in the VA Core Model, but are not shown here.

Links below (or menu to the left) provide detailed information about the attributes of each class, and guidance for their use.

.. toctree::
   :maxdepth: 4
   :caption: VA Core Model Classes

   entities/index
   elements/index
   data-types
   domain-entities

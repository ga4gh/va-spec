.. _core-class-hierarchy:

Core Class Hierarchy
!!!!!!!!!!!!!!!!!!!!

Below is a hierarchical view of classes in the VA Core Model, where attributes are inherited by child classes.

.. core-class-hierarchy:

.. figure:: ../images/core-model-class-hierarchy.png

   Core Class Hierarchy

   **Legend**: Hierarchical structure of classes and attributes comprising the domain-agnostic VA Core Model. Classes in darker grey represent the key knowledge artifacts that root VA Profile data structures. Simple classes for representing :ref:`Domain Entities <domain-entities>` such Conditions and Therapies are defined in the VA Core Model, but are not shown here.

**Primary Classes** in the model include :ref:`Statement <Statement>`, :ref:`Study Result <StudyResult>`, and :ref:`Evidence Line <EvidenceLine>` - which root larger data structures used to collect data in VA Models as described in the :ref:`next section <data-structures>`. Other primary classes are used to capture provenance information about these key knowledge artifacts. 

**Complex Data Type** classes hold collections of related fields that are used to capture values of certain attributes in the primary classes (e.g. see the many attributes that take a MappableConept as thier value). 

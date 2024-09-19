.. _core-information-model:

Core Information Model
!!!!!!!!!!!!!!!!!!!!!!

``PREREQUISITES:`` :ref:`Introduction <introduction>`

The **GKS Core Information Model (Core-IM)** is a domain-agnostic model that supports explicit representation of scientific knowledge, and the evidence and provenance supporting it. The initial version was derived from the `SEPIO Core Information Model <https://sepio-framework.github.io/sepio-linkml/core-im-diagram/>`_, through selection of elements needed to support initial VA implementation use cases. This Core-IM is the foundation on which Profiles for specific types of Statements and Study Results are built.  

A hierarchical view of this core model is illustrated below, followed by links to detailed information about each class. More about the modeling standards, patterns, and principles employed by the Core-IM can be found on the :ref:`Modeling Foundations page<modeling-foundations>`. 

.. core-im-class-hierarchy:

.. figure:: ../images/core-im-class-hierarchy.png

   Core-IM Class Hierarchy

   **Legend** Hierarchical structure of classes and attributes comprising the domain-agnostic Core-IM. Note that a hierarchy of Domain Entity classes has been defined to represent things like Genes, Conditions, and Therapeutic Procedures. This if described separately `here <https://github.com/ga4gh/va-spec/edit/1.x/docs/source/core-information-model/entities/domain-entities/index.rst>`_. 

.. toctree::
   :maxdepth: 4
   :caption: Core-IM Classes and Data Types

   entities/index
   data-types

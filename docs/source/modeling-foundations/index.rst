.. _modeling-foundations:

Modeling Foundations
!!!!!!!!!!!!!!!!!!!!

The **VA Core Model** is a domain-agnostic model for representing scientific knowledge about genetic variation, and the evidence and provenance supporting it. This model is the foundation on which more specialized models for representing specific types of Statements, Study Results, an Evidence Lines are built - through a process called 'Profiling'.

This section provides a foundational understanding of key principles and patterns applied in the VA-Spec, which should be reviewed before digging deeper into the documentation. It introduces:

1. The scope and utility of :ref:`Core Classes <core-classes>` in VA Models
2. The :ref:`Data Structures <data-structures>` that can be built using these classes to support different use cases
3. The special role that :ref:`Propositions <propositions>` play in VA Mdoels.
4. The :ref:`Profiling <profiles>` paradigm that underpins creation of formal schema for representing specific types of variant knowledge
5. The approach taken to representing :ref:`Domain Entities <domain-entity-representation>` relevant for variant annotations 

It also provides a detailed :ref:`Example Scenario <example-scenario>` that shows how Statement, Evidence Line, and Study Result profiles may be created, shared, and used together to represent a Variant Pathogenicity classification with rich evidence and provenance information.


**Index:**

.. toctree::
   :maxdepth: 4

   core-classes
   data-structures
   propositions
   profiles
   domain-entity-representation
   example-scenario

Core Information Model
!!!!!!!!!!!!!!!!!!!!!!

The **Core Information Model (Core-IM)** is a domain-agnostic model for representing statements of knowledge, and the foundation on which profiles for specific types of Statements and Study Results are built. 

A hierarchical view of this model is illustrated below, along with links to separate pages outlining details of each class. 

More information about the standards, patterns, and principles employed by the Core-IM can be found on the `Modeling Foundations <https://va-ga4gh.readthedocs.io/en/stable/modeling-foundations.html>`_ page. 

.. core-im-class-hierarchy:

.. figure:: ../images/core-im-class-hierarchy.png

**Legend** Figure 1: Hierarchical structure of classes and attributes comprising the domain-agnostic Core-IM. Note that a hierarchy of Domain Entity classes has been defined to represent things like Genes, Conditions, and Therapeutic Procedures. This if described separately `here <https://github.com/ga4gh/va-spec/edit/1.x/docs/source/core-information-model/entities/domain-entities/index.rst>`_. 

.. toctree::
    :maxdepth: 6

    entities/index
    data-types

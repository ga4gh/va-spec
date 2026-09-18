.. _core-class-hierarchy:

Core Class Hierarchy
!!!!!!!!!!!!!!!!!!!!

Below is a hierarchical view of classes in the VA Core Model, where attributes are inherited by child classes.

.. core-class-hierarchy:

.. raw:: html

   <iframe src="../_static/diagrams/core-class-hierarchy-model.html" style="width:100%; height:650px; border:0;" title="Core Class Hierarchy"></iframe>

**Legend**: Hierarchical structure of classes and attributes comprising the domain-agnostic VA Core Model. Simple classes for representing :ref:`Domain Entities <domain-entities>` such Conditions and Therapies are defined in the VA Core Model, but are not shown here.

**Primary Classes** in the model include :ref:`Statement <Statement>` and :ref:`Study Result <StudyResult>` - which root larger data structures used to collect data in VA Models as described in the :ref:`next section <data-structures>`. A discrete, evidence-based argument (an :ref:`Evidence Line <EvidenceLine>`) is not a separate class: it is a **Statement** referenced from another Statement's ``hasEvidenceLines`` attribute. Other primary classes are used to capture provenance information about these key knowledge artifacts. :ref:`Propositions <Proposition>` play a special role in VA Models, as descried :ref:`here <propositions>`. Many attributes across these primary classes (e.g. a Statement's ``strength``, ``outcome``, and ``quality``) take a :ref:`MappableConcept` as their value, which lets a data provider represent such values using a coded term from whatever system they use internally, a plain-text name where no code exists, or both - while also supporting explicit mappings to equivalent codes in other terminologies, so consumers of the data aren't limited to the source system's own vocabulary.

**Complex Data Type** classes hold collections of related fields that are used to capture values of certain attributes in the primary classes.

.. _core-classes:

Core Classes
!!!!!!!!!!!!

The diagram below shows a hierarchical view of classes in the VA Core Model below, where attributes are inherited by child classes.

.. core-class-hierarchy:

.. figure:: ../images/core-model-class-hierarchy.png

   Core Class Hierarchy

   **Legend** Hierarchical structure of classes and attributes comprising the domain-agnostic VA Core Model. Classes in darker grey represent the 'keystone classes' that root most VA data structures. Minimal classes for domain entities such Conditions and Therapies has been defined in the model :ref:`here <domain-entities>` but are not shown above.

Three classes in particular align with the levels of information that are provided by most community databases, and curated in most variant interpretation platform:

- :ref:`Statements <Statement>`: assertions or assessments of general knowledge about a variant - e.g. an assertion that the PTEN:c.35A>T variant is pathogenic for Hamartoma Tumor Syndrome, or an assessment that there is at present only moderate evidence supporting this possible fact.

- :ref:`Study Results <StudyResult>`:  defined collections of data items about a specific variant that result from a particular study or analysis - e.g. cohort allele frequency data and scores about PTEN:c.35A>T in different populations from the gnomAD dataset.
- :ref:`Evidence Lines <EvidenceLine>`: assessments of how a specific set of information is interpreted as evidence for some possible fact (which may ultimately be asserted as true or false in a Statement), e.g. assessment of the strength and direction of evidence population frequency data provides for the possible pathogenicity of PTEN:c.35A>T.

These **Keystone Classes** are the basis of :ref:`Profiles <va-profiles>` supported by the VA-Spec, and the data strucutres that can be built around each are described in the next section. 

The remaining **Primary Classes** rooted at **Entity** are attached to these core classes to represent provenance information describing how, when, by whom, and using what resources they were created. 

The **Complex Data Types** rooted at the **Element** class hold collections of related fields that are used to capture values of certain attributes in the primary classes (e.g. see the many attributes that take a MappableConept as thier value). 


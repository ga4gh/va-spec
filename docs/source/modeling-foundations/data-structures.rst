.. _data-structures:

Data Structures
!!!!!!!!!!!!!!!

Below we describe the data structures that can be built around three 'keystone classes' in the VA Core Model: Statements, Study Results, and Evdence Lines. These classes represent the kinds of artifacts reported in community databases and interpretation platforms. Accordingly, they are the basis of VA Profile schema provided by the VA-Spec, which are used by implementations to structure and exchange variant knowledge from their systems. 


Statement Structure
$$$$$$$$$$$$$$$$$$$

:ref:`Statements <Statement>` represent assertions or assessments of general knowledge about a variant - e.g. an assertion that the PTEN:c.35A>T variant is pathogenic for Hamartoma Tumor Syndrome, or an assessment that there is at present only moderate evidence supporting this possible fact.

In VA-Spec data, Statement objects root the larger data structure below, which allows tracking of provenance information at the level of a Statement and each supporting Evidence Line and Item. More on the internal semantics of this class can be found in the :ref:`Statement Class <Statement>` page.

.. core-im-statement-data-structure:

.. figure:: images/core-im-statement-proposition-data-structure.png

   Statement Data Structure

   **Legend** A class-level view of the Statement-based structures supported in VA-Spec data. Italicized text under class names illustrate the kind of information each class may report, in the case of a Variant Pathogenicity Statement supported by Population Allele Frequency evidence.

In this structure:
 * A **Statement** object roots a central axis where it is linked to one or more **Evidence Lines** representing discrete arguments for or against it.
 * Each **Evidence Line** may then be linked to one or more **Evidence Items** - specific **Information Entities** that were used to build an evidence-based argument.
 * Surrounding this central axis are classes that describe the provenance of these artifacts, including **Contributions** made to them by **Agents**, **Activities** performed in doing so, **Methods** that specify their creation, and **Documents** that describe them.

A data example illustrating the structure for a Variant Pathogenicity Statement can be found :ref:`here<acmg-variant-pathogenicity-statement-with-evidence>`.

.. important:: 
   The role of Propositions in  
**Propositions** provide a referencable and re-usable structure that encapsulates the abstract meaning of possible facts that may be asserted/assessed in a **Statement**, or toward which evidence is interpreted in an **Evidence Line**. For example, in the :ref:`Example Scenario <example-scenario>` the same Proposition object is used to capture the core meaning of what the root Statement asserts to be true, and what each of its supporting Evidence Lines evaluates a specific type of evidence against. Propositions are used only in the context of Statement and Evidence Line classes, and convey no knowledge on their own.  For more information, see the :ref:`Proposition <Proposition>` page, and related :ref:`Design Decision <use-of-propositions>`.


Evidence Line Structure
$$$$$$$$$$$$$$$$$$$$$$$

:ref:`Evidence Lines <EvidenceLine>` represent assessments of how a specific set of information is interpreted as evidence for some possible fact (i.e. their 'target proposition'), which may ultimately be asserted as true or false in a Statement.  For example, an assessment that some set of gnomAD allele frequency data about the PTEN:c.35A>T variant provides a *moderate* evidence *supporting* its pathogenicity for Hamartoma Tumor Syndrome.

As seen in the Statement Structure above, Evidence Lines may be linked to a Statement for which they represent a supporting or disputing argument. However some organizations 'pre-curate' such arguments in the absence of a definitive Statement they support, so that they can be retrieved and collectively assessed once sufficient evidence exists to make a definitive assertion about their target proposition. 

In VA-Spec data, an EvidenceLine object roots the data structure below, which like the Statement class supports precise tracking of provenance information. More on the internal semantics of this class can be found in the :ref:`SEvidence Line Class <EvidenceLine>` page.

.. core-im-evidence-line-structure:

.. figure:: images/evidence-line-structure.png

   Evidence Line Data Structure

   **Legend** A class-level view of the Evidence Line-based structures supported in VA-Spec data. Italicized text under class names illustrate the kind of information each class may report - here for an Evidence Line representing a *moderate* argument *supporting* the pathogenicity of a particular variant, based on allele frequency data from gnomAD.

In this structure, the Evidence Items contributing to the **Evidence Line** can be grouped and tied to an assessment of the direction and strength of support provided for or against a particular 'Target Proposition' (the possible fact towards which the evidence is assessed). And as with Statements, clear and precise provenance information about the Evidence Line and Evidence Items can be captured in supporting **Method**, **Document**, **Contribution**, **Agent**, and **Activity** objects.



Study Result Structure
@@@@@@@@@@@@@@@@@@@@@@

:ref:`Study Results <StudyResult>` represent defined collections of data items about a specific variant that result from a particular study or analysis - e.g. select cohort allele frequency data and scores about PTEN:c.35A>T in different populations from the gnomAD dataset. Curators often collect and assess such collections of data as evidence during the process of interpreting a particular variant - which may result in a higher order Statement about it. 

As seen in the Statement Structure above, Study Results may be linked to Evidence Lines or directly to Statements they support. However some organizations 'pre-curate' and store Study Results as stand-aling artifacts, which can be retrieved and assessed as evidence at a later time for possible facts for which they may provide support. 

In VA-Spec data, a StudyResult object roots the data structure below, which like the Statement and Evidence Line classes supports detailed tracking of provenance information. More on the internal semantics of this class can be found in the :ref:`Study Result Class <StudyResult>` page.

.. core-im-study-result-data-structure:

.. figure:: images/core-im-study-result-data-structure.png

   Study Result Data Structure

   **Legend** A class-level view of the Study Result-based structures supported in VA-Spec data. Italicized text under class names illustrate the kind of information each class may report in the case of a Cohort Allele Frequency Study Result reporting data from the gnomAD dataset about a particular variant.

In this structure, the data items collected in the **Study Result** can be linked to the larger **Data Set** or sets from which they came, and a description of the **Study Group** from which the data was collected. And as with Statements, clear and precise provenance information about the Study Result and DataSet can be captured in supporting **Method**, **Document**, **Contribution**, **Agent**, and **Activity** objects.






Propositions
@@@@@@@@@@@@

**Propositions** provide a referencable and re-usable structure that encapsulates the abstract meaning of possible facts that may be asserted/assessed in a **Statement**, or toward which evidence is interpreted in an **Evidence Line**. For example, in the :ref:`Example Scenario <example-scenario>` the same Proposition object is used to capture the core meaning of what the root Statement asserts to be true, and what each of its supporting Evidence Lines evaluates a specific type of evidence against. Propositions are used only in the context of Statement and Evidence Line classes, and convey no knowledge on their own.  For more information, see the :ref:`Proposition <Proposition>` page, and related :ref:`Design Decision <use-of-propositions>`.

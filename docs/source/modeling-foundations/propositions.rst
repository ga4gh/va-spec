.. _propositions:


Role of Propositions
!!!!!!!!!!!!!!!!!!!!

:ref:`Propositions <Proposition>` represent **possible facts** about the domain of discourse that may be true or false. They are abstract entities that capture a ‘sharable’ piece of meaning whose identity is independent of space and time, and which make no claim as to whether the sentiment it expresses is true or not.

As illustrated in the :ref:`Data Structures <data-structures>` section, the job of a **Proposition** object is to encapsulate a structured representation of a possible fact so it can be referenced and reused across **Statements** and **Evidence Lines**.

Propositions in Statements
##########################

In a **Statement**, a given **Proposition** may be *asserted* to be true or false, or *assessed* to report the strength of existing evidence supporting it (e.g. "there is presently *moderate* evidence *supporting* the proposition that *'HRAS:c.173C>T causes Costello Syndrome'"*). 

An example of a **Proposition** as an *assessed* possible fact is illustrated below.

.. figure:: ../images/statement-proposition-role.png

   Role of Propositions in Statements

   Legend: **Left panel.** Abridged version of the Variant Pathogenicity Statement model. **Center Panel.** An example of a Variant Pathogenicity Statement object (note use of shorthand syntax to capture values that should be wrapped in MappableConcepts). **Right Panel.** Plain language meaning of what structured data in the example reports to be true. Use of propositions in each panel is highlighted in red text.


Propositions in Evidence Lines
##############################

In an **Evidence Line**, a given **Proposition** captures the possible fact toward which **Evidence Items** are assessed and scored (e.g. that gnomAD population frequency evidence items are evaluated toward proposition that *"HRAS:c.173C>T causes Costello Syndrome"* when assessing the evidence as   providing *moderate* *support*). An example of a *Proposition** in this role is illustrated below.

.. figure:: ../images/evidence-line-proposition-role.png

   Role of Propositions in Evidence Lines

   Legend: **Left panel.** Abridged version of a Pathogenicity Evidence Line model. **Center Panel:** An example of a Pathogenicity Evidence Line object (note use of shorthand syntax to capture values that should be wrapped in MappableConcepts). **Right Panel:** Plain language meaning of what structured data in the example reports to be true. Use of propositions in each panel is highlighted in red text.

----------

In VA-Spec data, **Propositions** are used only in the context of a **Statement** or **Evidence Line**, as they convey no knowledge in the absence of the assessments these objects provide. 

While **Propositions** are *required* in Statements, they are *optional* in **Evidence Lines** - and can be omitted if the **Evidence Line** is attached to a **Statement** with the same **Proposition**. For example, in the :ref:`data example here <<acmg-variant-pathogenicity-statement-example-with-evidence>` the root **Statement** asserts the same **Proposition** (``Proposition001``) toward which its two **Evidence Lines** evaluate the support provided by population frequency and functional impact data. This **Proposition** object is explicitly referenced in the **Evidence Lines** in the example, but omission of this reference is permissible, and would imply that the target **Proposition** here is the same as that in the root **Statement**.

For more information, see the :ref:`Proposition <Proposition>` page, and related :ref:`Design Decision <use-of-propositions>`.

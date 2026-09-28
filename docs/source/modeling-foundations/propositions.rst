.. _propositions:


Role of Propositions
!!!!!!!!!!!!!!!!!!!!

:ref:`Propositions <Proposition>` represent **possible facts** about the domain of discourse that may be true or false. They are abstract entities that capture a ‘sharable’ piece of meaning whose identity is independent of space and time, and which make no claim as to whether the sentiment it expresses is true or not.

As illustrated in the :ref:`Data Structures <data-structures>` section, the job of a **Proposition** object is to encapsulate a structured representation of a possible fact so it can be referenced and reused across **Statements** and **Evidence Lines**.

Propositions in Statements
##########################

In a **Statement**, a given **Proposition** may be *asserted* to be true or false, or *assessed* to report the strength of existing evidence for or against it (e.g. "there is presently *likely* evidence *disputing* the proposition that *'SOS1:c.3322G>A is causal for RASopathy'"*).

An example of a **Proposition** as an *assessed* possible fact is illustrated below.

.. raw:: html

   <iframe src="../_static/diagrams/statement-proposition-role.html" style="width:100%; height:420px; border:0;" title="Role of Propositions in Statements"></iframe>

Legend: **Left panel (Model).** Abridged version of the Variant Pathogenicity Statement model. **Center Panel (Data Example).** An example of a Variant Pathogenicity Statement object (note use of shorthand syntax to capture values that should be wrapped in MappableConcepts). **Right Panel (Meaning).** Plain language meaning of what structured data in the example reports to be true. Proposition-related content in each panel is highlighted.


Propositions in Evidence Lines
##############################

In a **Statement** used as an **Evidence Line**, the ``proposition`` attribute captures the possible fact toward which **Evidence Items** are assessed and scored (e.g. that a gnomAD population frequency evidence item is evaluated toward the proposition that *"SOS1:c.3322G>A is causal for RASopathy"* when assessing the evidence as providing *strong* support *against* it). An example of a *Proposition** in this role is illustrated below.

.. raw:: html

   <iframe src="../_static/diagrams/evidence-line-proposition-role.html" style="width:100%; height:420px; border:0;" title="Role of Propositions in Evidence Lines"></iframe>

Legend: **Left panel (Model).** Abridged version of a Pathogenicity Evidence Line model. **Center Panel (Data Example).** An example of a Pathogenicity Evidence Line object (note use of shorthand syntax to capture values that should be wrapped in MappableConcepts). **Right Panel (Meaning).** Plain language meaning of what structured data in the example reports to be true. Proposition-related content in each panel is highlighted.

----------

In VA-Spec data, **Propositions** are used only in the context of a **Statement** or **Evidence Line**, as they convey no knowledge in the absence of the assessments these objects provide.

A **Statement** references its Proposition via its ``proposition`` attribute, while an **Evidence Line** references the possible fact its evidence is assessed against via its ``targetProposition`` attribute. In practice a **Proposition** should always be given for a Statement that stands on its own, but ``targetProposition`` may be omitted from an **Evidence Line** when it would simply repeat the **Proposition** of the Statement it supports. For example, in the :ref:`data example here <acmg-variant-pathogenicity-statement-example-with-evidence>` the root **Statement** asserts the same **Proposition** (``Proposition001``) toward which its two **Evidence Lines** evaluate the support provided by population frequency and functional impact data. This **Proposition** object is explicitly referenced in the **Evidence Lines** in the example, but omission of this reference is permissible, and would imply that the target **Proposition** here is the same as that in the root **Statement**.

For more information, see the :ref:`Proposition <Proposition>` page, and related :ref:`Design Decision <use-of-propositions>`.

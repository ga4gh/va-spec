.. _propositions:


Propositions
!!!!!!!!!!!!


You may have noted that Both the :ref:`Statement <Statement>` and :ref:`Evidence Line <EvidenceLine>` classes in the Core model reference a Proposition object.

<<FIGURE: close up of these two class boxes with the propositon attributes highlighted>>




**Propositions** represent possible facts about the domain of discourse that may be true or false. They are abstract entities that capture a ‘sharable’ piece of meaning whose identity and existence is independent of space and time, and makes no claim as to whether the sentiment it expresses is true or not.

In the VA Core Model, the job of a Proposition object is to convey the meaning of a possible fact, which can be referenced and reused by Statements and Evidence Lines. 

In a Statement, this is the possible fact that is asserted to be true or false, or that is assessed to report the overall level of confidence/evidence supporting it.  

In an Evidence Line, this is the possibe fact toward which evidence information is interpreted to detering the direciton and strenght of support this information provides.


. . . .







Specifically:
- Statements may report that a proposition was asserted by a particular agent to be true or false, or may report the overall level of confidence or evidence supporting or disputing a proposition for which a definitive assertion cannot yet be made. Such Statements are based on the agent’s interpretation of evidence as providing discrete argument(s) for or against the proposition.
- Evidence Lines are used to represent each such discrete evidence-based argument. They report that a particular collection of information (evidence items) was assessed and scored as evidence to support or dispute some target proposition. It is typically through the assessment of several distinct Evidence Lines that a particular Proposition is ultimately asserted to be true or false in a Statement.





that may be asserted/assessed in a **Statement**, or toward which evidence is interpreted in an **Evidence Line**. For example, in the :ref:`Example Scenario <example-scenario>` the same Proposition object is used to capture the core meaning of what the root Statement asserts to be true, and what each of its supporting Evidence Lines evaluates a specific type of evidence against. Propositions are used only in the context of Statement and Evidence Line classes, and convey no knowledge on their own.  For more information, see the :ref:`Proposition <Proposition>` page, and related :ref:`Design Decision <use-of-propositions>`.




Proposition objects serve a unique and important purpose in the VA Core Model, providing a referencable that can be reused in Statement and Evidence Line objects.

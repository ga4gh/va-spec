.. _va-profiles:

VA Profiles
!!!!!!!!!!!

VA Profiles are specializations of generic VA Core Model classes that have been constrained and/or extended to represent a particular type of knowledge (e.g. a varaint pathogenicity classification).

Profiles are provided as machine-readable JSON Schema, for use by implementers in structuring, validating, and exchanging variant data in their systems.  

At present, VA Profiles can be built on four core classes: 

 * :ref:`Statement<Statement>` Profiles support discrete assertions of **general knowledge** about a variant (e.g. a pathogenicity classification).

 * :ref:`Evidence Line<EvidenceLine>` Profiles describe **how information is interpreted as evidence** supporting or disputing a possible fact (Proposition) that may ultimately be asserted in a Statement about a variant (e.g. how data from an experimental functional impact analysis are interpreted to provide 'strong' evidence that 'supports' an assertion of the variant's pathogenicity).

 * :ref:`Proposition<Proposition>` Profiles are **used exclusively within Statement and Evidence Line objects** - where they encapsulate the **semantics of the possible fact** that may be asserted in a Statement, or against which evidence may be assessed in an Evidence Line (e.g. pathogenicity propositions capture a possible fact that some variant is causal for some disease).

 * :ref:`Study Result <StudyResult>` Profiles capture collections of **data items about a specific variant** from a particular study or analysis (e.g. functional impact data about the `PTEN:c.35A>T (p.Asn12Ile) variant in the `MAVE dataset<https://www.mavedb.org/score-sets/urn:mavedb:00000013-a-1>`_). Study Results are often used to describe data used as evidence to support higher order assertions such as pathogenicity classifications. 

The `data example here<variant-pathogenicity-statement-example>` illustrates how profiles of these different types maybe used together to describe a variant pathogenicity classification, and the evidence and provenance supporting it. 

In version 1.0 of the VA-Spec, we distinguish between two categories of profiles:

- **Base Profiles**:  Specialize generic VA core classes for a particular type of knowledge, through formal definition of concrete subclasses. This Base Profiling approach is used to create :ref:`Proposition Profiles<proposition-profiles>` and :ref:`Study Result Profiles<study-result-profiles>`, which can be used/referenced within Statement and Evidence Line profiles.
- **Community Profiles**: Layer additional constraints on top of VA core classes to enforce alignment with terminology conventions of a specific community guideline (e.g. ACMG 2015). These constraints are defined using a native JSON Schema composition approach, which does not result in creation of concrete subcalsses for each profile. In version 1.0 of the VA Spec, this constraint-based mechanism approach is used to define :ref:`Statement<Statement>` and :ref:`Evidence Line<EvidenceLine>` profiles - which incorporate Base Proposition Profiles to specify the type of possible fact they assert to be true, or evaluate evidence against, respectively.

.. note:: Representation of a particular type of Statement using VA-Spec does not require a Profile be specifically defined for it. The `Statement Community Profiles <community-profiles>` included in version 1.0 of the VA-Spec are there to support data providers pursuing strict alignment with a particular community guidelines. Implementers who do not seek such alignment can build their own schema for Statements to report any of the knowledge types specified in VA :ref:`Base Proposition profiles<proposition-profiles>`. Starting with the core Statement class, simply bind its ``proposition`` attribute to the relevant Proposition class, and use other Statement attributes and core classes to represent additional information about the Statement (e.g. strength, provenance, source documents, etc). The `data example here<https://github.com/ga4gh/va-spec/blob/1.x/tests/fixtures/VA-ClinVar-SCV-Example-001.yaml>`_ illustrates application of this approach to create non-ACMG-compliant representations of ClinVar pathogenicity data.  


.. toctree::
   :maxdepth: 4
   :titlesonly:

   base-profiles/index
   community-profiles/index

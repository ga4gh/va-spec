.. _va-profiles:

VA Profiles
!!!!!!!!!!!

VA Profiles extend generic VA Core Model classes with specializations to support a particular type of knowledge (e.g. a variant pathogenicity), and/or align with established community terminology and curation conventions (e.g. the ACMG-2015 Guidelines)

A :ref:`Profiling Methodology <profiling-methodology>` specifies how profiles are authored as YAML-based specifications, from which machine-readable JSON Schema are derived and used by implementers to structure, validate, and exchange variant data in their systems.

The VA-Spec currently supports profiles of four Core Model classes:

 - :ref:`Statement Profiles <Statement>` support assertions of general knowledge about a variant (e.g. classification of the *PTEN:c.35A>T(p.Asn12Ile)* variant as likely pathogenic in the `ClinVar knowledgebase <https://www.ncbi.nlm.nih.gov/clinvar/RCV001214844.7/>`_).

 - :ref:`Evidence Line Profiles <EvidenceLine>` describe how information is interpreted as evidence supporting or disputing a proposition that may ultimately be asserted as true in a Statement (e.g. how data from an experimental functional impact analysis are interpreted to provide strong evidence supporting  an assertion that *PTEN:c.35A>T(p.Asn12Ile)* is pathogenic).

 - :ref:`Study Result Profiles <StudyResult>` capture collections of data items about a specific variant from a particular study or analysis, which often represent evidence for higher order Statements about the variant (e.g. functional impact data about *PTEN:c.35A>T(p.Asn12Ile)* from the `MAVE dataset <https://www.mavedb.org/score-sets/urn:mavedb:00000013-a-1>`_).

 - :ref:`Proposition Profiles <Proposition>` are used exclusively within Statement and Evidence Line objects - where they encapsulate the semantics of the possible fact that may be asserted in a Statement, or against which evidence may be assessed in an Evidence Line (e.g. a proposition that *"PTEN:c.35A>T(p.Asn12Ile)* is causal for Hamartoma Tumor Syndrome").

The :ref:`data example here <acmg-variant-pathogenicity-statement-with-evidence>` illustrates how profiles of these different types can be used together to represent a variant pathogenicity classification.

-----

.. _base-vs-community-profiling:

**Base Profiles vs Community Profiles:**
 In version 1.0 of the VA-Spec, we distinguish between two categories of profiles:

- **Base Profiles**:

  - Specialize generic VA core classes for a particular type of knowledge, through formal definition of concrete subclasses.
  - This Base Profiling approach is used to create :ref:`Proposition Profiles<proposition-profiles>` and :ref:`Study Result Profiles<study-result-profiles>`, which can be used/referenced within Statement and Evidence Line profiles.

- **Community Profiles**:

  - Layer additional constraints on top of VA core classes to enforce alignment with terminology conventions of a specific community guideline (e.g. ACMG 2015).
  - These constraints are defined using  a schema composition approach that leverages the JSON Schema ``allOf`` keyword, which does not result in creation of concrete subclasses for each profile.
  - This constraint-based mechanism approach is used to define :ref:`Statement<Statement>` and :ref:`Evidence Line<EvidenceLine>` profiles - which incorporate Propositions to specify the possible fact they assert to be true or evaluate evidence against, respectively.

-----

**Implementation Notes:**

**1. Building Custom Statement and Evidence Line Models using Propositions:**

  - Representation of a particular type of **Statement** or **Evidence Line** using the VA-Spec does not always require a Profile to be specifically defined for it.
  - The :ref:`Statement and Evidence Line Community Profiles <community-profiles>` included in version 1.0 of the VA-Spec are there to support data providers pursuing strict alignment with a particular community guidelines.
  - Implementers who do not seek such alignment can build their own schema for Statements or Evidence Lines to report on any of the knowledge types specified in VA :ref:`Base Proposition profiles<proposition-profiles>`.
  - For example, starting with the core :ref:`Statement<Statement` class, simply bind its ``proposition`` attribute to the relevant Proposition base profile, and use other Statement attributes and core classes to represent additional information about the Statement  as desired (e.g. strength, classification, methods, etc).
  - The |simple_test_fixtures_example| illustrates application of this approach to create a custom, non-ACMG-compliant representation of a pathogenicity statement.


-----

**Index:**

.. toctree::
   :maxdepth: 4
   :titlesonly:

   base-profiles/index
   community-profiles/index

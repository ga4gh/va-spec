.. _va-profiles:

VA Profiles
!!!!!!!!!!!

VA Profiles extend generic VA Core Model classes with specializations to support a particular type of knowledge (e.g. a variant pathogenicity), or align with established community terminology and curation conventions (e.g. the ACMG-2015 Guidelines)

Profiles are authored as YAML-based specifications, from which machine-readable JSON Schema are derived and used by implementers to structure, validate, and exchange variant data in their systems.

The VA-Spec currently supports profiles of four Core Model classes:

 - :ref:`Statement<Statement>` Profiles support discrete assertions of general knowledge about a variant (e.g. a pathogenicity classification).

 - :ref:`Evidence Line<EvidenceLine>` Profiles describe how information is interpreted as evidence supporting or disputing a possible fact (Proposition) that may ultimately be asserted in a Statement about a variant (e.g. how data from an experimental functional impact analysis are interpreted to provide 'strong' evidence that 'supports' an assertion of the variant's pathogenicity).

 - :ref:`Study Result <StudyResult>` Profiles capture collections of data items about a specific variant from a particular study or analysis (e.g. functional impact data about the PTEN:c.35A>T(p.Asn12Ile) variant in the `MAVE dataset <https://www.mavedb.org/score-sets/urn:mavedb:00000013-a-1>`_). Study Results are often used to describe data used as evidence to support higher order assertions such as pathogenicity classifications.

 - :ref:`Proposition<Proposition>` Profiles are used exclusively within Statement and Evidence Line objects - where they encapsulate the semantics of the possible fact that may be asserted in a Statement, or against which evidence may be assessed in an Evidence Line (e.g. pathogenicity propositions capture a possible fact that some variant is causal for some disease).

The :ref:`data example here<variant-pathogenicity-statement-example>` illustrates how profiles of these different types can be used together to represent a variant pathogenicity classification.

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

**1. Building Statement and Evidence Line Models using Propositions:**

  - Representation of a particular type of **Statement** or **Evidence Line** using the VA-Spec does not require a Profile be specifically defined for it.
  - The :ref:`Statement and Evidence Line Community Profiles <community-profiles>` included in version 1.0 of the VA-Spec are there to support data providers pursuing strict alignment with a particular community guidelines.
  - Implementers who do not seek such alignment can build their own schema for Statements or Evidence Lines to report on any of the knowledge types specified in VA :ref:`Base Proposition profiles<proposition-profiles>`.
  - For example, starting with the core :ref:`Statement<Statement` class, simply bind its ``proposition`` attribute to the relevant Proposition base profile, and use other Statement attributes and core classes to represent additional information about the Statement (e.g. strength, provenance, source documents, etc).
  - The `data example here <https://github.com/ga4gh/va-spec/blob/|github_version|/tests/fixtures/VA-ClinVar-SCV-Example-001.yaml>`_ illustrates application of this approach to create non-ACMG-compliant representations of ClinVar pathogenicity statements.


-----

**Index:**

.. toctree::
   :maxdepth: 4
   :titlesonly:

   base-profiles/index
   community-profiles/index

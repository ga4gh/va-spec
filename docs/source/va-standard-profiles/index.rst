.. _va-profiles:

VA Profiles
!!!!!!!!!!!

VA Profiles extend generic VA Core Model classes with specializations to support a particular type of knowledge (e.g. a variant pathogenicity), and/or align with established community terminology and curation conventions (e.g. the ACMG-2015 Guidelines)

A :ref:`Profiling Approach <profile-authoring-mechanisms>` specifies how profiles are authored as YAML-based specifications, from which machine-readable JSON Schema are derived and used by implementers to structure, validate, and exchange variant data in their systems.

The VA-Spec currently supports profiles of four Core Model classes:

 - :ref:`Statement Profiles <Statement>` support assertions of general knowledge about a variant (e.g. classification of the *PTEN:c.35A>T(p.Asn12Ile)* variant as likely pathogenic in the `ClinVar knowledgebase <https://www.ncbi.nlm.nih.gov/clinvar/RCV001214844.7/>`_).

 - :ref:`Evidence Line Profiles <EvidenceLine>` describe how information is interpreted as evidence supporting or disputing a proposition that may ultimately be asserted as true in a Statement (e.g. how data from an experimental functional impact analysis are interpreted to provide strong evidence supporting  an assertion that *PTEN:c.35A>T(p.Asn12Ile)* is pathogenic).

 - :ref:`Study Result Profiles <StudyResult>` capture collections of data items about a specific variant from a particular study or analysis, which often represent evidence for higher order Statements about the variant (e.g. functional impact data about *PTEN:c.35A>T(p.Asn12Ile)* from the `MAVE dataset <https://www.mavedb.org/score-sets/urn:mavedb:00000013-a-1>`_).

 - :ref:`Proposition Profiles <Proposition>` are used exclusively within Statement and Evidence Line objects - where they encapsulate the semantics of the possible fact that may be asserted in a Statement, or against which evidence may be assessed in an Evidence Line (e.g. a proposition that *"PTEN:c.35A>T(p.Asn12Ile)* is causal for Hamartoma Tumor Syndrome").

The :ref:`data example here <acmg-variant-pathogenicity-statement-example-with-evidence>` illustrates how profiles of these different types can be used together to represent a variant pathogenicity classification.

-----

.. _base-vs-community-profiling:

In version 1.0 of the VA-Spec, we distinguish between two categories of profiles:

 **Base Profiles**:

  - Specialize generic VA core classes for a particular type of knowledge, through formal definition of concrete subclasses.
  - This Base Profiling approach is used to create :ref:`Proposition Profiles<proposition-profiles>` and :ref:`Study Result Profiles<study-result-profiles>`, which can be used/referenced within Statement and Evidence Line profiles.

 **Community Profiles**:

  - Layer additional constraints on top of VA core classes to enforce alignment with terminology conventions of a specific community guideline (e.g. ACMG 2015).
  - These constraints are defined using a schema composition approach, which does not result in creation of concrete subclasses for each profile.
  - This approach is used to define :ref:`Statement<Statement>` and :ref:`Evidence Line<EvidenceLine>` profiles - which incorporate Propositions to specify the possible fact they assert to be true or evaluate evidence against, respectively.
  - Notably, it is possible to define more than one Community Profile for a given knowledge type, each of which aligns with a different community guideline. For example, separate Pathogenicity community profiles may end up being defined to align with current ACMG 2015 Guidelines, and a forthcoming updated version of these guidelines.

For technical guidance around how these types of profiles are authored and implemented, see the :ref:`Developer Guide <developer-guide>` section. 



-----

**Index:**

.. toctree::
   :maxdepth: 4
   :titlesonly:

   base-profiles/index
   community-profiles/index
   custom-profiles

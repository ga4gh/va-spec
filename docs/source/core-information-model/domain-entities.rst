.. _domain-entities:

Domain Entities
!!!!!!!!!!!!!!!

Domain Entities are the real world concepts in the domain of discourse that variant annotation data is about - e.g. **Genetic Variation**, and the **Conditions**, **Therapies**, or **Genes** to which they are related. They are considered to represent general types or concepts (e.g. the disease 'Lung Cancer’), as opposed to particular instances of these concepts (‘patient X’s manifestation of lung cancer’).

The VA-Spec does not define detailed models for representing such domain entities - as this is the remit of other standards development organizations.

Where suitable standards exist they are incorporated into the VA-Spec - as we have done with the `VRS <https://vrs.ga4gh.org/en/latest/index.html>`_ and `CatVRS <https://cat-vrs.readthedocs.io/en/latest/index.html>`_ models for representing genetic variation.

Version 1 of the VA-Spec represents all other Domain Entity types using a simple :ref:`IRI Reference <iriReference>`, or a :ref:`Mappable Concept <mappable-concept>` which bundles an established code for the entity with metadata and mappings for the code and code system. The example below shows a Mappable Concept used to capture the domain entity 'Lung Adenocarcinoma', using the primary code ``civic.did:30``, along with a mapping to the ontology term ``MONDO:0005061``.

.. parsed-literal::

      "conditionQualifier":
      {
        "conceptType": "Condition",
        "primaryCoding":
        {
          "code": "civic.did:30",
          "name": "Lung Adenocarcinoma",
          "system": "https://civicdb.org",
          "iris": ["https://civicdb.org/diseases/30"]
        },
          "mappings":  [
           {
            "coding":
             {
              "code": "MONDO:0005061",
              "name": "lung adenocarcinoma",
              "system": "https://ontobee.org/ontology/MONDO",
              "systemVersion": "2025-02-04",
              "iris": ["http://purl.obolibrary.org/obo/MONDO_0005061"]
             },
            "relation": "exactMatch"
           }
         ]
      }

Finally, where there is a need to represent collections of more than one Domain Entity, classes are defined to capture these as sets of Mappable Concepts (e.g. ``ConditionSet``, ``Therapy Group``).

Below we detail how different types of Domain Entities relevant to variant knowledge are currently represented in the VA-Spec.

Future versions of the VA-Spec may incorporate richer models for other Domain Entity types as suitable community standards emerge.

.. _Variation:

Variation
@@@@@@@@@

**Computational Definition**

Variation subjects of VA knowledge may be discrete instances of sequence variation in a specified context (reference, location, state) - which may include single continuous alleles, haplotypes, genotypes, and copy number changes; or intensionally defined categories or sets of variations, based on criteria that must be met for inclusion in a given set (e.g. "BRAF V600 mutations", or "EGFR exon 19 deletions").

**Information Model**

To represent these diverse types of variation, the VA-Spec imports two complementary GKS standards:

  - The `GA4GH Variant Representation Specification (VRS) <https://vrs.ga4gh.org/en/latest/index.html>`_, which provides JSON Schema for representing many classes of discrete genetic variation, and tools for generating globally-unique computed variant identifiers.

  - The `GA4GH Categorical Variation Representation Specification (Cat-VRS) <https://github.com/ga4gh/cat-vrs?tab=readme-ov-file>`_, which is built on top of VRS and provides a terminology and data model for describing 'categorical' variation concepts.

**Examples**
  - A |discrete_allele| as a VRS object
  - A |canonical_allele| as a Cat-VRS object

.. _Condition:

Condition
@@@@@@@@@

.. include::  ../def/va-spec/Condition.rst

The **Condition** schema is defined simply as ``oneOf`` an :ref:`IRI Reference <iriReference>` or a :ref:`Mappable Concept <mappable-concept>`.

**Examples**
 - |nonsyndromic_genetic_hearing_loss| as a Mappable Concept

**Implementation Guidance**

- **Indicating when no condition is provided.**

  - By convention, cases where no condition is given by the data provider SHOULD be specified using a MappableConcept with a ``conceptType = "Absent"``. Additionally, either the ``name`` or ``primaryCoding`` attribute of a MappableConcept must be populated.
  - The name or code may simply reiterate the conceptType (e.g. "Condition Absent"), or report a more specific nature or reason for the absence of a condition (e.g. "Data Missing in Source", "Condition Unknown", "All Mendelian Diseases").

.. _ConditionSet:

Condition Set
@@@@@@@@@@@@@

.. include::  ../def/va-spec/ConditionSet.rst

**Examples**
  - A set of |two_co-occurring_phenotypes|

**Implementation Guidance:**

  - Populating the ``membershipOperator`` attribute:
     - The membershipOperator `AND` should be used when the Conditions listed are considered as co-occurring together in a single patient/subject.
     - The membershipOperator `OR` should be used only in the specific scenario where a study is done on a cohort of individuals that manifest only one of the conditions in the set.

       - Conclusions about this condition are determined based on an aggregate statistical analysis across all members of this mixed cohort - because the study does not provide the statistical power to make a conclusion about each condition individually.
       - In such cases, it would be misleading to create separate statements about each condition on its own.
       - Conditions in such groups are typically related in their etiology or manifestation, and patients are pooled to make a single cohort that is large enough support a statistically significant results about this grouping of related conditions.


.. _Therapeutic:

Therapeutic
@@@@@@@@@@@

.. include::  ../def/va-spec/Therapeutic.rst

The **Therapeutic** schema is defined simply as ``oneOf`` an :ref:`IRI Reference <iriReference>` or a :ref:`Mappable Concept <mappable-concept>`.

**Examples**
  - |afatinib| as a Mappable Concept

.. _TherapyGroup:

Therapy Group
@@@@@@@@@@@@@

At present, the VA-Spec includes  a ``TherapyGroup`` schema for representing groups of therapies.

.. include::  ../def/va-spec/TherapyGroup.rst

**Examples**
  - A combination treatment of |arsenic_trioxide_&_tretinoin|

**Implementation Guidance**

  - Populating the ``membershipOperator`` attribute:

    - The membershipOperator `AND` should be used when all therapies in the group were applied in combination to a given patient or subject.
    - The membershipOperator `OR` should be used only in the specific scenario where a study is done on a cohort of individuals that receive one of the therapies in the group - and the treatment response is determined based on an aggregate statistical analysis across all members of this mixed cohort. In such cases, the study does not provide the statistical power to make a conclusion about response to each therapy individually.

      - Therapies in such groups are typically related in their treatment mechanism (e.g. members of the same drug class), and recipients are pooled to make a single cohort that is large enough support a statistically significant results about that class of treatments.
      - Future iterations of the VA-Spec may support representation of these categorical groupings of therapies, but for now we capture the individual therapies used in the study in a TherapyGroup.


.. _Gene:

Gene
@@@@

**Computational Definition**

A gene is a region (or regions) of genetic sequence that includes all of the elements necessary to encode a functional transcript. A gene may include regulatory regions, transcribed regions and/or other functional sequence regions. (From SO:0000704)

**Information Model**

No dedicated class or schema is defined for Genes at present. Rather, individual genes are referenced in data using an :ref:`IRI Reference <iriReference> or a :ref:`Mappable Concept <mappable-concept>` that captures a code or name for the gene, along with optional mappings and metadata about the code system

**Examples**
  - |brca2_gene| as a Mappable Concept


-----------

.. note:: Future versions of VA-Spec may incorporate richer models for representing certain types of domain entities, if/when suitable standards are defined by authoritative organizations.

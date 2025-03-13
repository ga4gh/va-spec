.. _community-profiles:

Community Profiles
!!!!!!!!!!!!!!!!!!

Community Profiles layer additional constraints on top of VA core classes to enforce alignment with terminology conventions of a specific community guideline. 

For example, profiles aligned with the "ACMG 2015 Variant Interpretation Guidelines" constrain the values of specific attributes by defining enumerations based on: 

- ACMG criterion codes (``PS3``, ``BS3``)
- ACMG criterion assessment outcomes (``met``, ``not met``)
- ACMG evidence strengths (``strong``, ``supporting``, ``moderate``)
- ACMG classification outcomes (``pathogenic``, ``likely pathogenic``, ``benign``, ``likely benign``, ``VUS``)

Version 1 of the VA-Spec includes Statement and Evidence Line community profiles aligned with three established varaint interpretation guidelines:

 - the `ACMG 2015 Pathogenicity Interpretation Guidelines <https://pubmed.ncbi.nlm.nih.gov/27993330/>`_ 
 - the `ClinGen/CGC/VICC (CCV) 2022 Oncogenicity Interpretation Guidelines <https://pubmed.ncbi.nlm.nih.gov/35101336/>`_
 - the `AMP/ASCO/CAP (AAC) Guidleines for Clinical Interpretation of Genetic Variants <https://pubmed.ncbi.nlm.nih.gov/25741868/>`_

-----

**Technical Specification of Community Profiles**

- Community Profiles layer constraints on core classes using a schema composition approach that leverages the JSON Schema ``allOf`` keyword. 
- This approach defines a named subschema, but unlike the Base Profiling approach does not result in creation of concrete subcalsses for each profile.  
- An example of the yaml-based profile authoring syntax for the :ref:`ACMG 2015 Variant Pathogenicity Statement Profile <variant-pathogenicity-statement-acmg-2015>` is below. It specifies that data must conform to the definition of the core :ref:`Statement<Statement>` class, *and* validate against the additionak constrants defined on ``proposition`` and ``classification`` properties.

.. code-block:: yaml

  VariantPathogenicityStatement:  
    maturity: draft
    description: >-
      A Statement describing the role of a variant in causing an inherited condition.
    allOf:
    - $ref: "/ga4gh/schema/va-spec/1.x/base/json/Statement"
    - properties:
        proposition:
          $ref: "/ga4gh/schema/va-spec/1.x/base/json/VariantPathogenicityProposition"
          description: >-
            A proposition about the pathogenicity of a varaint, the validity of which is assessed and reported by the Statement.
            A Statement can put forth the proposition as being true, false, or uncertain, and may provide an assessment of the
            level of confidence/evidence supporting this claim.
        classification:
          type: string
          enum:
            - pathogenic
            - likely pathogenic
            - uncertain significance
            - likely benign
            - benign

-----

**Index:**

.. toctree::
   :maxdepth: 4
   :titlesonly:

   acmg-2015-profiles
   ccv-2022-profiles
   aac-2017-profiles



.. warning:: This data class is at a **draft** maturity level and may change
    significantly in future releases. Maturity levels are described in
    the :ref:`maturity-model`.

**Computational Definition**

A Statement describing the role of a variant in causing an inherited condition.

**Profile Conditions**

This class adds the following conditions to the :ref:`variant-pathogenicity-statement-profile`:

- `VariantPathogenicityStatement.classification` is additionally defined as 
  *The ACMG 2015 classification of the variant's pathogenicity*.
    - `.classification.label` is constrained to values `pathogenic`, `likely pathogenic`,
      `uncertain significance`, `likely benign`, and `benign`.

.. _json-schema-catalog:

JSON Schema Catalog
!!!!!!!!!!!!!!!!!!!

Formal JSON schema files for Base and Community Profiles are stored across different directories in the VA-Spec repository.

To facilitate developer access to these key resources, we provide this central catalog of links for all VA Profile json schema files.

**Study Result Base Profiles:**
 - |cohort_allele_frequency_study_result_json_schema|
 - |experimental_variant_functional_impact_study_result_json_schema|
 - |tumor_variant_frequency_result_json_schema|

**Proposition Base Profiles:**
 - |pathogenicity_proposition_json_schema|
 - |oncogenicity_proposition_json_schema|
 - |therapeutic_response_proposition_json_schema|
 - |diagnostic_proposition_json_schema|
 - |prognostic_proposition_json_schema|
 - |experimental_variant_functional_impact_proposition_json_schema|

**Statement Community Profiles:**
 - |pathogenicity_statement_json_schema| (ACMG-2015)
 - |oncogenicity_study_statement_json_schema| (CCV-2022)
 - |therapeutic_response_study_statement_json_schema| (AAC-2017)
 - |diagnostic_study_statement_json_schema| (AAC-2017)
 - |prognostic_study_statement_json_schema| (AAC-2017)

**Evidence Line Community Profiles:**
 - |pathogenicity_evidence_line_json_schema| (ACMG-2015)
 - |oncogenicity_evidence_line_json_schema| (CCV-2022)

-------

JSON schema for **concrete VA Core classes** that can also be used to create and validate data are housed in the directory here: |core_class_json_schema_files|.

This includes schema for **Statement** and **Evidence Line** classes that are the basis for constraint-based Community Profiles, as well as schema for **Method**, **Document**, **Data Set**, **Contribution**, and **Agent** classes that support provenance representations within all Profiles.

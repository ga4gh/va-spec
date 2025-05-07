.. _json-schema-catalog:

JSON Schema Catalog
!!!!!!!!!!!!!!!!!!!

Formal JSON schema files for Base and Community Profiles are stored across different directories in the VA-Spec repository.

To facilitate developer access to these key resources, we provide this central catalog of links for all VA Profile json schema files. 

**Proposition Profiles:**
 - |pathogenicity_proposition_json_schema|
 - |oncogenicity_proposition_json_schema|
 - |therapeutic_response_proposition_json_schema|
 - |diagnostic_proposition_json_schema|
 - |prognostic_proposition_json_schema|
 - |experimental_variant_functional_impact_proposition_json_schema|

**Statement Profiles:**
 - |pathogenicity_statement_json_schema|
 - |oncogenicity_study_statement_json_schema|
 - |therapeutic_reponse_study_statement_json_schema|
 - |diagnostic_study_statement_json_schema|
 - |prognostic_study_statement_json_schema|

**Evidence Line Profiles:**
 - |pathogenicity_evidence_line_json_schema|
 - |oncogenicity_evidence_line_json_schema|

**Study Result Profiles:**
 - |cohort_allele_frequency_study_result_json_schema|
 - |experimental_variant_functional_impact_study_result_json_schema|

-------

JSON schema for **concrete VA Core classes** that can aslo be used to create and validate data are housed in the directory here: |core_class_json_schema_files|. 

This includes schema for **Statement** and **Evidence Line** classes that are the basis for constraint-based community profiles, as well as schema for **Method**, **Document**, **Data Set**, **Contribution**, and **Agent** classes that support provenance representations within Profiles. 

from pathlib import Path

root_dir = Path(__file__).parent.parent
schema_dir = root_dir / "schema"
allele_frequency_example_dir = root_dir / "docs" / "Modeling" / "CohortFrequency"
cohort_allele_frequency_schema_yaml_path = schema_dir / "cohortAlleleFreq.yaml"
cohort_allele_frequency_schema_json_path = schema_dir / "cohortAlleleFreq.json"
cohort_allele_frequency_example_yaml_path = allele_frequency_example_dir / "simple_result_example.yaml"

from jsonschema import validate
import pathlib
import json
import argparse

APP_ROOT = pathlib.Path.cwd()

SCHEMA_DIR = APP_ROOT / "schema"
SCHEMA_URI_ROOT = "file://" + str(SCHEMA_DIR)


def get_latest_file(source_name, file_obj_type):
    source_examples_dir = APP_ROOT / "examples" / f"{source_name}_data"
    files = (source_examples_dir).glob(f"{source_name}_cdm_metaschema_{file_obj_type}_*.json")
    sorted_files = sorted(files)
    return sorted_files[-1]


def validate_variation_descriptors(source_name):
    variation_descriptors_file = get_latest_file(source_name, "variation_descriptors")
    with open(variation_descriptors_file) as jf:
        vd_records = json.load(jf)

    variation_descriptor_schema = {
        "type": "array",
        "items": {
            "$ref": SCHEMA_URI_ROOT + "/vod.json#/definitions/VariationDescriptor"
        },
        "additionalProperties": False,
        "minItems": 1
    }

    validate(vd_records, variation_descriptor_schema)


def validate_statements(source_name):
    statements_file = get_latest_file(source_name, "statements")
    with open(statements_file) as jf:
        statement_records = json.load(jf)

    statement_file_schema = {
        "$schema": "http://json-schema.org/draft/2020-12/schema",
        "type": "array",
        "items": {
            "oneOf": [
                {"$ref": SCHEMA_URI_ROOT + "/annotation.json#/$defs/VariationGermlinePathogenicityStatement"},
                {"$ref": SCHEMA_URI_ROOT + "/annotation.json#/$defs/VariationNeoplasmTherapeuticResponseStatement"},
            ]
        },
        "additionalProperties": False,
        "minItems": 1
    }

    validate(statement_records, statement_file_schema)


def validate_methods(source_name):
    methods_file = get_latest_file(source_name, "methods")
    with open(methods_file) as jf:
        method_records = json.load(jf)

    method_file_schema = {
        "type": "array",
        "items": {
            "$ref": SCHEMA_URI_ROOT + "/annotation.json#/$defs/Method"
        },
        "additionalProperties": False,
        "minItems": 1
    }

    validate(method_records, method_file_schema)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", choices=["civic", "moa"],
                        type=str.lower, required=True)
    args = parser.parse_args()
    source_name = args.source

    validate_variation_descriptors(source_name)
    validate_statements(source_name)
    validate_methods(source_name)

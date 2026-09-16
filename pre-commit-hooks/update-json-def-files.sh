#!/bin/bash

REPO_ROOT=$(git rev-parse --show-toplevel)
cd "$REPO_ROOT" || exit 1

make_output=$(make -C schema all)

if [[ "$make_output" == "make: Nothing to be done for \`all\'." ]]; then
  echo "No changes to source files in schema/."
else
  echo "Source files updated, regenerating and staging."

  # Copy the regenerated class defs into docs/source/def so the docs stay
  # self-contained (docs .rst include only in-source files).
  bash "$REPO_ROOT/tools/sync-docs-def.sh"

  git add $(git diff --name-only -- \
    'schema/va-spec/*-source.yaml' \
    'schema/va-spec/**/*-source.yaml' \
    'schema/va-spec/json/**' \
    'schema/va-spec/def/**' \
    'docs/source/def/**')
fi

exit 0

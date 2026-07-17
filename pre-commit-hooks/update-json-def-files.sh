#!/bin/bash

REPO_ROOT=$(git rev-parse --show-toplevel)
SCHEMA_DIR="$REPO_ROOT/schema"

cd "$SCHEMA_DIR" || exit 1

make_output=$(make all)

if [[ "$make_output" == "make: Nothing to be done for \`all\'." ]]; then
  echo "No changes to source files in $SCHEMA_DIR."
else
  echo "Source files updated, adding changes to commit."

  git add $(git diff --name-only -- \
    'va-spec/**/*-source.yaml' \
    'va-spec/**/json/*' \
    'va-spec/**/def/*')
fi

exit 0

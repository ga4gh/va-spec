#!/bin/bash
# Copy generated class definition .rst files from the schema tree into
# docs/source/def/ so the documentation is self-contained: every `.. include::`
# in docs/source/**/*.rst then resolves to a real file INSIDE docs/source, with
# no symlinks or relative paths that escape the docs source tree.
#
# Run after regenerating the schema (`make -C schema all`). The pre-commit hook
# runs this automatically. RTD runs it via a build.jobs.pre_build step.
set -e
ROOT=$(git rev-parse --show-toplevel)
SRC="$ROOT/schema/va-spec/def"
DST="$ROOT/docs/source/def"

rm -rf "$DST/va-spec" "$DST/va-spec.aac-2017" "$DST/va-spec.acmg-2015" "$DST/va-spec.ccv-2022"
mkdir -p "$DST/va-spec"
cp "$SRC"/*.rst "$DST/va-spec/"
for c in aac-2017 acmg-2015 ccv-2022; do
  mkdir -p "$DST/va-spec.$c"
  cp "$SRC/$c"/*.rst "$DST/va-spec.$c/"
done
echo "Synced schema def -> docs/source/def (va-spec, va-spec.{aac-2017,acmg-2015,ccv-2022})"

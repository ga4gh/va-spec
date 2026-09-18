# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

VA-Spec (Variant Annotation Specification) is a GA4GH schema project. Its
JSON Schema and docs are **generated**, not hand-written: every `*-source.yaml`
file under `schema/va-spec/` is compiled by the `ga4gh.gkm.metaschema`
processor (console entrypoints `source2classes`, `source2splitjs`, `y2t`) into
`json/` (JSON Schema) and `def/` (reStructuredText attribute tables). Treat
generated `json/`, `def/`, and `docs/source/def/` as build output — edit the
`*-source.yaml` files and regenerate; don't hand-edit generated files.

VA-Spec sits at the top of a submodule chain, each also built by the same
processor: `va-spec → cat-vrs → vrs → gkm-core`. `schema/{cat-vrs,vrs,gkm-core}`
are real directories containing only symlinks into the submodule chain (a
`*-source.yaml` and a `json/` dir — no `def/`); their `def/` is regenerated
locally into `schema/va-spec/def/` instead.

## Setup

```
git clone --recurse-submodules git@github.com:ga4gh/va-spec.git
cd va-spec
make devready              # creates venv/3.12, installs .requirements.txt
source venv/3.12/bin/activate
pre-commit install
```

If you cloned without `--recurse-submodules`: `git submodule update --init --recursive`.

## Common commands

Regenerate schema after editing any `schema/va-spec/*-source.yaml`:
```
make -C schema clean && make -C schema all
```
Then sync the regenerated `def/` into the docs tree (the pre-commit hook does
this automatically on commit, but do it manually when iterating):
```
bash tools/sync-docs-def.sh
```

Run tests:
```
pytest tests/                                    # all tests (PYTHONPATH not needed)
pytest tests/test_negative.py                    # one file
pytest tests/test_extensibility.py::test_open_base_still_enforces_required_triple  # one test
```

Build docs:
```
cd docs && make html                             # one-shot -> docs/build/html
# or, for live-rebuild while editing (requires `brew install entr`):
cd docs && make clean watch &
```

## Architecture: the `schema/va-spec/` source layout

All of VA-Spec's own sources live **flat in one directory**, `schema/va-spec/`:
`va-spec-source.yaml` (core classes), `domain-entities-source.yaml` (Condition,
ConditionSet, Therapy, TherapyGroup), and three community profiles —
`aac-2017-profile-source.yaml`, `acmg-2015-profile-source.yaml`,
`ccv-2022-profile-source.yaml`.

The `<XXX>-profile-source.yaml` naming is a convention the metaschema
processor recognizes natively (see gks-metaschema's `METASCHEMA_BEHAVIOR.md`
§9, "profile sub-namespaces"): a file named that way contributes `XXX` as a
sub-namespace of its folder — its classes land in `json/XXX/` and `def/XXX/`
(nested under the folder's shared `json`/`def`, not sibling folders), and
every class `$id` becomes `.../json/XXX/<Class>`. The `XXX` in the filename
must match the `XXX` in the file's own `$id` (its final path segment), or the
processor raises an error. Base (non-profile) sources are unaffected — their
output sits directly under `json/`/`def/`. One flat `Makefile`/`prune.mk` in
`schema/va-spec/` builds every source in the folder; there are no
per-profile subdirectories or Makefiles.

Cross-references work the same way: "Used in:"/"Subclasses:" lists in the
generated docs are computed across **every** source in a folder together
(base sources and every profile), so a base class's doc page correctly shows
which profile classes reference it.

## Architecture: abstract, sealed, and closed classes

Every class in a `*-source.yaml` is either:
- **Concrete** (default): closed. The processor injects `additionalProperties:
  false` (or `unevaluatedProperties: false` for `allOf`/`anyOf`/`oneOf`-composed
  classes) — extra properties are rejected.
- **Abstract** (`abstract: true`): open by default. A `$ref`/`$refCurie` to an
  abstract class validates *any* structurally-conforming subclass — including
  ones the schema doesn't declare, which is what lets implementers define
  their own subclasses. `Proposition` and `StudyResult` are open this way, on
  purpose, so third parties can define custom proposition/study-result types.
  `Statement` and `EvidenceLine` are **concrete** (not abstract) — they are
  not meant to be extended with arbitrary new top-level classes; community
  profiles specialize them via `allOf` composition (narrowing existing
  fields), not via `inherits:`.
- **Sealed** (`sealed: true` on an abstract class): the processor
  auto-derives a `oneOf` over the class's concrete descendants, closing
  reference sites to that known set. Only meaningful on an abstract class; not
  currently used anywhere in this schema (both `Proposition` and `StudyResult`
  are intentionally left un-sealed/open).

`heritableProperties`/`heritableRequired`/`extends` do not exist in this
processor version — properties/required live directly on the class
(inherited via `properties`/`required` on the parent), and a subclass
specializes an inherited property by redeclaring it **under the same name**
(the processor forbids renaming an inherited property, and enforces
covariance: a subclass may narrow `const`/`default`/type constraints but not
change them incompatibly).

## Architecture: the subject/predicate/object/focus convention

`Proposition` declares `subject`, `predicate`, `object` (all required, loosely
typed); `StudyResult` declares `focus` (required). Every concrete subclass
narrows these **in place under the same name** — e.g.
`VariantPathogenicityProposition.subject` narrows to
`vrs:MolecularVariation | cat-vrs:CategoricalVariant | iriReference`, but the
property is still called `subject`, not `subjectVariant`. This is a hard
constraint of the processor (renaming isn't supported), not a style choice —
don't reintroduce per-subclass renamed variants of these fields.

## References across schema modules

A `$ref` must be a local `#/$defs/<Class>` reference. To reference a class in
an imported module (or a sibling `*-source.yaml` in the same folder, like a
profile referencing a base class), use `$refCurie: <namespace>:<Class>`, where
`<namespace>` is declared in that file's `namespaces:` block. A bare class
name or a full URL as a `$ref` value raises an error.

## Docs are self-contained

`docs/source/**/*.rst` must never reference anything outside `docs/source`
(no `../../submodules/...` includes, no symlinks pointing outside the tree).
Generated class-attribute tables are synced into `docs/source/def/` by
`tools/sync-docs-def.sh` (real files, not symlinks); the Maturity Model page
and its images are likewise materialized locally rather than included from a
submodule. `docs/source/github_links.txt` defines `|..._source_yaml|`/
`|..._json_schema|` substitutions (rendered by `conf.py`'s `extlinks`
mechanism) that link to specific files/lines in this repo on GitHub — Sphinx
does not validate these against disk, so a schema-file move/rename requires
updating this file by hand (it will not surface as a build warning).

## Testing model

`tests/config.py` builds its class registry by **globbing the generated
`json/` output** (`schema/*/json/*` for imported modules, plus
`schema/va-spec/json/*` and `schema/va-spec/json/*/*` for base classes and
profile sub-namespaces) — it does not hardcode class lists. The namespace for
a class is derived from its path: `va-spec:ClassName` for base classes,
`va-spec.<profile>:ClassName` for profile classes, `<module>:ClassName` for
imported modules (e.g. `vrs:Allele`).

`tests/test_examples.py` enforces two things beyond "do the listed examples
validate": every class at `draft` maturity or above must have at least one
registered example (`test_class_coverage`), and every property on those
classes must be exercised by at least one example (`test_property_coverage`),
with narrow, deliberate exceptions in `tests/tu_coverage_exceptions.yaml`
(used for properties that are legitimately optional and rarely populated,
like `id`/`aliases`/`description`) and a `va_excluded_classes` set in
`test_examples.py` for abstract classes and pure `type: array` wrapper/union
classes that have no standalone instance to test.

Adding a new class or property means adding/extending a fixture in
`tests/fixtures/` and registering it in `tests/test_definitions.yaml` —
otherwise the coverage tests fail.

## Branch conventions

The default/integration branch is **`v1`**, not `main`. Ballot work happens
on dated branches like `1.1.0-ballot.2026-09`. Version-branch creation is
restricted to repo administrators; feature branches are named
`<issue-number>-<short-description>` off an open issue. PRs for new features
target `v1`; PRs for version patches target the appropriate minor-version
branch instead. PR titles must reflect the associated issue, in the form
`#<issue-number> <description>` (e.g. `#250 Move ancillaryResults and
qualityMeasures into the core StudyResult class`, see
[CONTRIBUTING.md](../CONTRIBUTING.md)).

## Release notes

A ballot branch's name already encodes its **target release version** as a
SemVer `<MAJOR>.<MINOR>.<PATCH>-ballot.<YYYY>-<MM>` prefix (see the
"Pre-releases" section of `docs/source/appendices/maturity_model.rst`) — e.g.
branch `1.1.0-ballot.2026-09` targets release `1.1.0`. `docs/source/releases/`
holds one file per **minor** version line, `<major>.<minor>.rst` (e.g.
`1.0.rst`, `1.1.rst`), not one file per patch and not one file per ballot;
each file stacks a subsection per patch release under that line, newest
first (see `1.0.rst`: `1.0.1` above `1.0.0`), categorized per the maturity
model's Major/Minor/Patch version-increment rules (same file, `## Testing
model` below for the analogous class-registry rule; the increment rules
themselves live in `maturity_model.rst`'s "Versioning examples" section).

**When documenting a change made on a ballot branch, always add/update the
entry in that target version's file** (derive `<major>.<minor>` from the
branch name's prefix) — never a separate `<version>-ballot.<date>.rst` file.
Such a ballot-dated file may already exist alongside the target file as a
more detailed, ballot-cycle-specific technical changelog (e.g.
`1.1.0-ballot.2026-09.rst` next to `1.1.rst`), but it is not a substitute:
nothing links to it as "the 1.1.0 release notes," so a change documented only
there is effectively undocumented for the actual release. Whether a given
change lands in a brand-new `<major>.<minor>.rst` (first release under a new
line) or a new subsection of an existing one (a further patch under an
already-released minor line) follows from whether that file already exists.

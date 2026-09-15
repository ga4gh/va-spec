# Task: modernize the VA-Spec repo to the GKM metaschema 0.4.1 pipeline

Bring `va-spec` onto the same modernized GKM metaschema pipeline and imported-schema
conventions that were just applied to `ga4gh/cat-vrs` (and before it, `ga4gh/vrs` and
`gkm-core`). A `*-source.yaml` is compiled by the `ga4gh.gkm.metaschema` tools
(`source2classes` / `source2splitjs` / `y2t`) into split `json/` and `def/*.rst`, and
imported base schemas come from a git submodule.

**Work step by step, verify at each step, and STOP before committing — show the diff first.**

## Submodule / import chain

VA-Spec sits at the TOP of the chain and pulls everything through one submodule:

```text
va-spec
└─ submodules/cat-vrs            (git submodule → ga4gh/cat-vrs)
   └─ submodules/vrs             (nested → ga4gh/vrs)
      └─ submodules/gkm-core     (nested → ga4gh/gkm-core)
```

Under `schema/`, the imported schemas are currently **whole-directory symlinks** into
that chain, and `va-spec`'s OWN schema is a real, **multi-module** tree:

- `schema/cat-vrs`  → `../submodules/cat-vrs/schema/cat-vrs`
- `schema/vrs`      → `../submodules/cat-vrs/submodules/vrs/schema/vrs`
- `schema/gkm-core` → `../submodules/cat-vrs/submodules/vrs/submodules/gkm-core/schema/gkm-core`
- `schema/va-spec/{base,aac-2017,acmg-2015}` — va-spec's own source modules (each with its
  own `*-source.yaml`, `Makefile`, `prune.mk`, `json/`, `def/`). **Confirm the actual module
  list and their `*-source.yaml` files first** (`find schema/va-spec -name '*-source.yaml'`).

So you do **not** hand-edit cat-vrs / vrs / gkm-core here — you consume them by bumping the
`cat-vrs` submodule. Your source work is limited to VA-Spec's own module YAMLs.

## Target versions (the 2026-09 ballot line)

After bumping the `cat-vrs` submodule to its `1.1.1-ballot.2026-09` line, the imported
`$id` tokens will be:

- cat-vrs  `1.1.1-ballot.2026-09.1`
- vrs      `2.1.1-ballot.2026-09.1`
- gkm-core `1.2.1-ballot.2026-09.1`

Confirm each by reading the imported source `$id` via the symlinks after Step 1
(`schema/cat-vrs/cat-vrs-source.yaml`, `schema/vrs/vrs-source.yaml`,
`schema/gkm-core/gkm-core-source.yaml`).

## What "the new processor" changes (0.4.x convention)

1. **Package renamed** `ga4gh.gks.metaschema` → `ga4gh.gkm.metaschema` (import path
   `ga4gh.gkm.metaschema.*`). Console entrypoints keep their names, so `make all` still works.
2. **Abstract classes** are declared `abstract: true` (they render *open* — no
   `additionalProperties`/`unevaluatedProperties`). Concrete classes are *closed*; the
   processor injects `type: object`, so drop explicit `type: object` on concrete classes.
3. **`heritableProperties` / `heritableRequired` are gone** → plain `properties` / `required`
   on the abstract base (they descend to subclasses).
4. **`extends:` is removed and raises an error** → delete every `extends: <field>` line; the
   narrowed subclass property (e.g. a `type` `const`/`default`) stays as a plain property.
5. `inherits:` and cross-module `$refCurie: …` stay as-is — only their **namespace target
   paths** change (see Step 4/identity).

## Steps

1. **Sync the submodule to the tip of its tracked branch.**
   - `.gitmodules` currently tracks `submodule.submodules/cat-vrs.branch = 1.1.0-ballot.2026-07`
     — update it to the current cat-vrs ballot line **`1.1.1-ballot.2026-09`** (or `v1` once
     cat-vrs PR #257 merges — see decision points), then `git submodule sync`.
   - `git submodule update --remote submodules/cat-vrs` uses the branch in LOCAL `.git/config`,
     which can be **stale** — if it checks out the wrong commit, reset it to match the `branch =`
     in `.gitmodules`, then re-sync.
   - Init the nested submodules **from inside cat-vrs** so the pointer isn't reverted:
     `git -C submodules/cat-vrs submodule update --init --recursive`.
   - Verify the three imported `$id` tokens (above) via the `schema/*` symlinks.

2. **`.requirements.txt`:** replace `ga4gh.gks.metaschema==0.3.2` with
   `ga4gh.gkm.metaschema == 0.4.1` (from PyPI). Reinstall the venv (`make devready` /
   `pip install -r .requirements.txt --pre`). Confirm the entrypoints import
   `ga4gh.gkm.metaschema` and the old `gks` package/residue is gone.

3. **`docs/source/rst_epilog`:** add
   ```
   .. |maturity-model| replace:: :ref:`Maturity Model <maturity-model>`
   ```
   (0.4.1 admonitions emit "See |maturity-model|."). Ensure the maturity-model doc page has a
   `.. _maturity-model:` label. If VA-Spec's page is a symlink into a submodule, prefer making
   it a **real file** (copy from the sibling `../vrs` checkout or the submodule) so this repo
   owns the label. Also add any other substitutions the 0.4.1 admonitions reference if the docs
   build reports them undefined (e.g. `|indent|`).

4. **Migrate VA-Spec's own source YAMLs** (every `schema/va-spec/*/*-source.yaml`) per the
   convention rules above (drop `extends:`, `heritable*` → `properties`/`required`, mark
   abstract classes `abstract: true`, drop explicit `type: object` on concrete classes), and
   **retarget the imported namespace mappings** in each file to the new tokens:
   - `.../schema/cat-vrs/<old>/json/`  → `.../schema/cat-vrs/1.1.1-ballot.2026-09.1/json/`
   - `.../schema/vrs/<old>/json/`       → `.../schema/vrs/2.1.1-ballot.2026-09.1/json/`
   - `.../schema/gkm-core/<old>/json/`  → `.../schema/gkm-core/1.2.1-ballot.2026-09.1/json/`
   Decide VA-Spec's own `$id`/version (ballot bump vs keep) — see decision points — and apply it
   consistently across all modules.

5. **Decouple the docs from the submodule's PRE-GENERATED `def/`** so VA-Spec owns its
   imported-class defs (0.4.1 `y2t` emits def for imported classes into the local `def/`):
   - Under `schema/`, make each imported dir (`cat-vrs`, `vrs`, `gkm-core`) a **REAL folder**
     containing symlinks ONLY to the imported `*-source.yaml` (for `imports:`) and `json/` (for
     `$ref` resolution) — do **NOT** link the submodule's `def/`.
   - In **every** VA-Spec module's `schema/va-spec/<module>/prune.mk`, keep all generated
     `def/*` and prune only stray `json/*` (the current rule likely deletes any `def/` file
     whose class isn't in `build/<name>.classes`, which wipes the imported-class defs `y2t`
     generates). Determine which module(s) generate the imported-class defs the docs need
     (whichever module imports them — often the `base` module).
   - Repoint every `.. include:: .../def/{cat-vrs,vrs,gkm-core}/*.rst` in `docs/source/**/*.rst`
     to the locally generated `def/va-spec…/*.rst`, and delete the corresponding
     `docs/source/def/{cat-vrs,vrs,gkm-core}` symlinks.

6. **CI / pre-commit parity** (this is the piece the def-decoupling REQUIRES — mirror vrs commit
   `8cd1e5a` "check out submodules in precommit job; skip import-only schema dirs in hook"):
   - In the CI workflow that runs the `update-json-def-files` pre-commit hook (e.g.
     `.github/workflows/cqa.yaml`), make the checkout use `submodules: recursive` — otherwise
     `make all` cannot resolve the imported source symlinks on a fresh checkout.
   - In `pre-commit-hooks/update-json-def-files.sh`, **skip import-only dirs** — the newly-real
     `schema/{cat-vrs,vrs,gkm-core}` folders have no `Makefile`, and `make` there errors. Add a
     guard: `if [ ! -f "$DIR/Makefile" ]; then continue; fi`.
   - Confirm the test workflow already checks out `submodules: recursive`.

7. **Regenerate & verify:** from `schema/`, `make clean && make all`. Then:
   - `make test` passes. **GOTCHA:** tests resolve imported `$refs` by reading
     `schema/<module>/json/<Class>` straight off disk (see `tests/config.py`), so the `json/`
     symlinks MUST stay — only `def/` is replaced by local generation. Confirm which imported
     json `$refs` VA-Spec actually uses (cat-vrs / vrs / gkm-core classes) and that they resolve.
   - Docs `make html` builds clean (no warnings). Fix broken includes / undefined labels
     (missing imported-class doc stubs are the usual cause — add `docs/source/concepts/imported`
     stubs and toctree entries as needed).
   - **`oneOf` vs `anyOf`:** if any VA-Spec union (`oneOf`) that references an abstract imported
     base (e.g. `vrs:Location`, `vrs:Variation`) fails with "matches more than one schema",
     first re-sync — upstream restored the subtype `oneOf` unions on abstract Variation/Location
     (`Location` now discriminates again), so `oneOf` should be unambiguous. Only fall back to
     `anyOf` if a real ambiguity persists, and document it.

8. **Docs currency & imported-class notes:**
   - On each imported **VRS** and **Cat-VRS** class page, add a note linking the full definition
     in the latest upstream spec (`https://vrs.ga4gh.org/en/latest/…` for VRS,
     `https://cat-vrs.readthedocs.io/en/latest/…` for Cat-VRS). Do **NOT** add notes to
     **gkm-core** class pages (no public spec). Classify by each stub's `.. include::` target.
   - Fix stale version mentions in prose, branch-pinned URLs (`tree/<old-branch>`), and
     `/en/stable` vs `/en/latest` inconsistencies.

9. **Release notes:** add a new `docs/source/releases/<version>.rst` for this ballot capturing
   the pipeline modernization + dependency/version bump (and any schema-behavior change), and
   list it in the releases toctree. Keep it honest: if there's no net VA-Spec schema change,
   say so.

10. **Tests review:** reconcile any example that is documented but missing from
    `tests/test_definitions.yaml` (add it, or drop the doc page). Note that the suite is
    positive-only (no negative/"should-reject" cases) — flag this gap; optionally scaffold a
    negative test.

## Definition of done
- `cat-vrs` submodule bumped to `1.1.1-ballot.2026-09` (nested vrs `2.1.1-ballot.2026-09`,
  gkm-core `1.2.1-ballot.2026-09`); `.gitmodules` updated; `git submodule status --recursive` clean.
- `.requirements.txt` pins `ga4gh.gkm.metaschema == 0.4.1`; venv reinstalled.
- All VA-Spec module sources migrated (no `extends:`/`heritable*`, abstract marked, no explicit
  `type: object` on concretes); namespace mappings retargeted to the new tokens; VA-Spec `$id`
  decided and applied consistently.
- Imported `cat-vrs`/`vrs`/`gkm-core` dirs are real folders (source+json symlinks only, no def);
  every module's `prune.mk` keeps `def/*`; docs include local `def/va-spec…`; dead
  `docs/source/def/{cat-vrs,vrs,gkm-core}` symlinks removed.
- CI checks out submodules recursively for the pre-commit job; the hook skips import-only dirs.
- `make all` clean; `make test` passes (imported `$refs` resolve via the kept json symlinks);
  docs `make html` clean (no warnings).
- New ballot release-notes page added; documented-but-untested examples reconciled.
- **Nothing committed** — report the full change set and decision points first.

## Decision points to raise before committing
- **Which cat-vrs branch does `.gitmodules` track** — the ballot line `1.1.1-ballot.2026-09`
  (matches the current tip) or `v1` (the longer-lived integration branch, once cat-vrs PR #257
  merges)? This affects `git submodule update --remote`.
- **Does VA-Spec itself get a version/ballot bump** (e.g. `<X.Y.Z>-ballot.2026-09.1`)? The `$id`
  in every module changes if so — confirm the exact token, since it alters schema identity that
  downstream consumers depend on.
- **Which VA-Spec module owns the imported-class defs** for the docs (base vs each profile), and
  whether every profile module (`aac-2017`, `acmg-2015`) needs the same `prune.mk` change.
- **Metaschema pin style** — PyPI `== 0.4.1` (recommended, reproducible) vs a git ref.

## Reference
The equivalent, already-merged work is `ga4gh/cat-vrs` PR #257
("1.1.1-ballot.2026-09: GKM metaschema 0.4.1 pipeline + 2026-09 dependency refresh") and the
`ga4gh/vrs` commits it builds on (notably `8cd1e5a` for the CI/hook parity and `ff73e8c` for the
restored abstract `oneOf` unions). Read the migrated cat-vrs/vrs/gkm-core `*-source.yaml` (via
the `schema/*` symlinks after Step 1) as the worked examples of the convention transformation.

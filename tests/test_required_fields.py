"""Required-field regression tests.

These lock in the *required* contract of every VA-Spec class so that a required
property can never be dropped (or silently added) without a test failing. This
guards against regressions like the 1.1.0 one where ``Statement.direction`` --
required since 1.0 -- was accidentally dropped from ``Statement.required``
during the metaschema-layout reorg, leaving it optional in the generated schema.

How it works
------------
``tests/required_fields.yaml`` is a checked-in golden snapshot mapping each
``<namespace>:<Class>`` to the sorted list of properties it *unconditionally*
requires (see ``effective_required``). ``test_required_fields_match_snapshot``
recomputes that mapping from the generated JSON Schema and asserts it matches
the snapshot exactly, so any add/remove of a required field -- or of a whole
class -- surfaces as a failing test with a readable diff.

When you *intentionally* change a required field, regenerate the snapshot::

    (cd tests && python test_required_fields.py)

and commit the updated ``required_fields.yaml`` alongside the schema change, so
the change is deliberate and reviewable rather than silent.

Scope: VA-Spec's own classes (``va-spec`` base + community profiles). Imported
modules (vrs, cat-vrs, gkm-core) are owned upstream and bump via submodules, so
their required contract is not snapshotted here.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import yaml
import pytest
from config import js_def, test_path

SNAPSHOT_PATH = test_path / 'required_fields.yaml'


def effective_required(schema):
    """The set of properties a schema requires unconditionally.

    Unions ``required`` at the schema root and down every ``allOf`` branch
    (how community profiles compose extra required fields onto a base class,
    e.g. a profile Statement adds ``classification``/``specifiedBy`` on top of
    the base ``Statement``). ``if``/``then`` (conditional) and
    ``anyOf``/``oneOf`` (alternative) branches are intentionally excluded --
    they do not make a property *unconditionally* required. ``$ref`` targets
    are not followed: base-class required fields are already flattened into the
    referring class by the metaschema processor, and a change to a base class's
    own required list is caught on that base class's own snapshot entry.
    """
    req = set()
    if not isinstance(schema, dict):
        return req
    req.update(schema.get('required', []) or [])
    for member in schema.get('allOf', []) or []:
        req |= effective_required(member)
    return req


def compute_snapshot():
    """Map every va-spec class with required fields to its sorted required list."""
    snapshot = {}
    for name, definition in js_def.items():
        if not name.startswith('va-spec'):
            continue
        req = effective_required(definition)
        if req:
            snapshot[name] = sorted(req)
    return snapshot


def load_snapshot():
    with open(SNAPSHOT_PATH) as f:
        return yaml.safe_load(f)


def test_snapshot_file_exists():
    assert SNAPSHOT_PATH.exists(), (
        f"Missing {SNAPSHOT_PATH.name}; regenerate it with "
        f"'(cd tests && python test_required_fields.py)'"
    )


def test_required_fields_match_snapshot():
    actual = compute_snapshot()
    expected = load_snapshot()

    missing_classes = sorted(set(expected) - set(actual))
    new_classes = sorted(set(actual) - set(expected))
    assert not missing_classes, (
        f"Classes with required fields in the snapshot are gone from the schema: "
        f"{missing_classes}. If intentional, regenerate required_fields.yaml."
    )
    assert not new_classes, (
        f"Classes now declare required fields but are absent from the snapshot: "
        f"{new_classes}. If intentional, regenerate required_fields.yaml."
    )

    mismatches = {
        cls: {'expected': expected[cls], 'actual': actual[cls]}
        for cls in expected
        if expected[cls] != actual[cls]
    }
    assert not mismatches, (
        "Required-field contract changed for: "
        + ", ".join(
            f"{cls} (expected {m['expected']}, got {m['actual']})"
            for cls, m in mismatches.items()
        )
        + ". If intentional, regenerate required_fields.yaml; otherwise a "
        "required field was added or dropped by mistake."
    )


def test_statement_requires_direction_and_proposition():
    # Focused regression for the 1.1.0 bug: Statement must require both
    # 'proposition' and 'direction' (plus the 'type' discriminator).
    req = effective_required(js_def['va-spec:Statement'])
    assert 'direction' in req, "Statement.direction must be required"
    assert 'proposition' in req, "Statement.proposition must be required"


if __name__ == '__main__':
    snapshot = compute_snapshot()
    header = (
        "# Golden snapshot of required fields for every VA-Spec class.\n"
        "# Generated from the built JSON Schema; do not hand-edit.\n"
        "# Regenerate after an intentional required-field change with:\n"
        "#   (cd tests && python test_required_fields.py)\n"
        "# Guarded by tests/test_required_fields.py.\n"
    )
    with open(SNAPSHOT_PATH, 'w') as f:
        f.write(header)
        yaml.safe_dump(snapshot, f, default_flow_style=False, sort_keys=True)
    print(f"Wrote {SNAPSHOT_PATH} ({len(snapshot)} classes)")

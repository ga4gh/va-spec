#!/usr/bin/env python3
"""Canonicalize community-profile class ``$id`` URLs.

The metaschema tool derives a class ``$id`` from the source ``$id`` path joined
with ``json-target``. Because each community profile lives in ``schema/va-spec/<c>/``
but writes its output to the shared ``schema/va-spec/json/<c>/`` (json-target
``../json/<c>``), the generated ``$id`` picks up a normalized ``..`` segment, e.g.::

    .../va-spec/<ver>/aac-2017/../json/aac-2017/AmpAscoCapEvidenceLine

This rewrites those to the clean logical identifier::

    .../va-spec/<ver>/aac-2017/AmpAscoCapEvidenceLine

Only the ``$id`` string is changed; the physical layout (``json/<c>/``) is untouched.
"""
import glob
import os

HERE = os.path.dirname(os.path.abspath(__file__))
JSON_ROOT = os.path.normpath(os.path.join(HERE, "..", "schema", "va-spec", "json"))
COMMUNITIES = ["aac-2017", "acmg-2015", "ccv-2022"]

changed = 0
for c in COMMUNITIES:
    for p in glob.glob(os.path.join(JSON_ROOT, c, "*")):
        if not os.path.isfile(p):
            continue
        s = open(p).read()
        s2 = s.replace(f"/{c}/../json/{c}/", f"/{c}/")
        if s2 != s:
            open(p, "w").write(s2)
            changed += 1
print(f"canonicalized {changed} community $id(s)")

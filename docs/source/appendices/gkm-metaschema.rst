.. _gkm-metaschema:

The GKM Metaschema Processor
!!!!!!!!!!!!!!!!!!!!!!!!!!!!

VA-Spec's own schema is not hand-written JSON Schema. Every ``*-source.yaml`` file under
``schema/va-spec/`` (and, in the imported ``cat-vrs``/``vrs``/``gkm-core`` submodules, their
own source files) is written in a higher-level YAML authoring format and compiled by the
**GKM Metaschema processor** (the ``ga4gh.gkm.metaschema`` Python package) into the JSON
Schema and documentation that ship with the specification. This processor is shared
infrastructure across the GA4GH Genomic Knowledge Models (GKM) family of specifications
(GKM-Core, VRS, Cat-VRS, VA-Spec), so a change to the processor's behavior can affect all
of them together, and a VA-Spec release's compatibility with a given processor version is
tracked explicitly (see *Version pinning*, below).

What It Does
############

The processor reads the authoring-format YAML sources and produces two kinds of output:

  - **JSON Schema** (``json/``): the actual machine-readable schema that implementations
    validate data against. Each class defined in a source file becomes one JSON Schema
    document, with a ``$id`` computed from the module, version, and (for community profile
    classes) sub-namespace.
  - **RST attribute tables** (``def/``): a generated reStructuredText table of each class's
    properties, types, and cardinalities, included into the corresponding hand-written docs
    page via a Sphinx ``.. include::`` directive (e.g. :ref:`Statement`'s page includes
    ``def/va-spec/Statement.rst``). These are why a docs page's attribute table always
    matches the real schema: it's the same generated artifact, not a manually-maintained
    copy.

Three console entrypoints drive this, invoked from ``schema/va-spec/Makefile`` (and the
equivalent Makefiles in the imported submodules) via ``make -C schema clean && make -C
schema all``:

  - ``source2classes`` -- compiles ``*-source.yaml`` into JSON Schema (``json/``)
  - ``source2splitjs`` -- compiles the same sources into the split per-class JavaScript/JSON
    form some GKM tooling consumes
  - ``y2t`` ("YAML to table") -- generates the ``def/`` RST attribute tables

Authoring Conventions the Processor Understands
################################################

The authoring YAML is not raw JSON Schema; it's a more compact format that the processor
expands, applying a consistent set of conventions across every GKM specification:

  - **``abstract: true``** marks a class as abstract and left *open* (no
    ``additionalProperties: false`` injected), so a ``$ref``/``$refCurie`` to it validates
    any structurally-conforming subclass -- including ones the schema itself doesn't
    declare. Every other class is concrete and *closed*: the processor injects
    ``additionalProperties: false`` (or ``unevaluatedProperties: false`` for classes
    composed via ``allOf``/``anyOf``/``oneOf``) automatically, and there's no need to write
    ``type: object`` explicitly -- the processor adds it.
  - **``sealed: true``**, meaningful only on an abstract class, auto-derives a closed
    ``oneOf`` over that class's concrete descendants, so reference sites are restricted to
    the schema's own known subtypes rather than staying open to implementer-defined ones.
  - **Properties and ``required`` are inherited directly** through a class's ``inherits:``
    chain -- there is no separate ``heritableProperties``/``heritableRequired`` mechanism,
    and no ``extends:`` keyword. A subclass specializes an inherited property by
    redeclaring it *under the same name*: the processor does not support renaming an
    inherited property, and enforces covariance (a subclass may narrow a ``const``,
    ``default``, or type constraint, but not change it incompatibly).
  - **``$refCurie: <namespace>:<Class>``** is how a source file references a class defined
    in a different module, or in a sibling source file within the same folder (e.g. a
    community profile referencing a base ``va-spec`` class). The ``<namespace>`` must be
    declared in that file's own ``namespaces:`` block. A ``$ref`` value, by contrast, must
    always be a local ``#/$defs/<Class>`` reference -- a bare class name or a full URL as a
    ``$ref`` raises a processor error.
  - **Profile sub-namespaces**: a source file named ``<XXX>-profile-source.yaml`` (VA-Spec's
    convention for its three community profiles) contributes ``XXX`` as a sub-namespace of
    the folder it lives in -- its classes land in ``json/XXX/`` and ``def/XXX/`` rather than
    at the folder's own root, and every class ``$id`` in that file becomes
    ``.../json/XXX/<Class>``. The ``XXX`` in the filename must match the ``XXX`` in the
    file's own ``$id``, or the processor raises an error.
  - **Cross-reference computation**: "Used in:"/"Subclasses:" lists on a generated def page
    are computed across every source file in a folder together, so a base class's page
    correctly lists which sibling profile classes reference it -- not just other classes
    defined in the same source file.

Role in Testing
################

The generated ``json/`` output, not the source YAML, is what VA-Spec's test suite
(``pytest tests/``) actually validates data against, and it's also what the test suite uses
to discover *which* classes exist in the first place: ``tests/config.py`` builds its class
registry by globbing the generated ``json/`` output (``schema/*/json/*`` for imported
modules, plus ``schema/va-spec/json/*`` and ``schema/va-spec/json/*/*`` for VA-Spec's own
base and profile classes) rather than hardcoding a class list, so newly-added classes are
picked up automatically once the schema is regenerated. Two coverage checks in
``tests/test_examples.py`` then run against that registry: every class at *draft* maturity
or above must have at least one registered example, and every property on those classes
must be exercised by at least one example -- both enforced by inspecting the generated
schema, not the authoring source.

Role in Documentation
######################

Beyond the ``def/`` attribute tables described above, the processor's generated-docs
features are themselves versioned, additive capabilities that VA-Spec's docs rely on:

  - a class composed via ``allOf`` gets a **Composes:** line on its def page naming the
    class it composes onto, mirroring the **Inherits:**/**Subclasses:** lines already shown
    for ``inherits:``-based classes;
  - a composed class with ``if``/``then`` constraints gets an **Additional Constraints**
    table summarizing them (e.g. the AAC-2017 tier-based rules on
    :ref:`VariantClinicalSignificanceStatement`);
  - an ``anyOf``/``oneOf`` composition whose only constraint is "at least one of" a set of
    properties renders as a plain-language sentence instead of a duplicated placeholder
    bullet list (see :ref:`MappableConcept`, which requires at least one of ``name`` or
    ``primaryCoding``).

``tools/sync-docs-def.sh`` copies the generated ``def/`` output into ``docs/source/def/`` as
real files (not symlinks), wired into the pre-commit hook so the docs tree stays
self-contained and in sync automatically on every commit that touches the schema.

Version Pinning
################

Because the processor's own behavior (how it expands the authoring format, what it
validates, what it generates) can change between releases, the version of
``ga4gh.gkm.metaschema`` a given VA-Spec release was built with is meaningful context for
understanding that release's schema -- see the :ref:`releases` notes for the specific
processor version changes pulled into each VA-Spec release line.

See Also
########

  - `ga4gh.gkm.metaschema on PyPI <https://pypi.org/project/ga4gh.gkm.metaschema/>`_
  - :ref:`releases` -- for the processor version history reflected in each VA-Spec release

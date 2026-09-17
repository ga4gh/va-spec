---
name: va-spec-class-diagram
description: Generate a compact, semi-technical HTML class-relationship diagram for VA-Spec docs (classes, properties, cardinalities, associations) in the project's established visual style. Use when adding or replacing a diagram in docs/source/**/*.rst that needs to show class structure and associations between va-spec/gkm-core classes -- not for general explainer/infographic graphics (use the explainer-graphic skill for those).
---

# VA-Spec Class Diagram

Produces small, embeddable class diagrams for the VA-Spec Sphinx docs: boxes for classes (name + a
few representative properties with type/cardinality), thin connector lines with role labels for
associations, and light annotations for the modeling nuances that aren't obvious from field names
alone. This is a **project-local fork** of the general `explainer-graphic` skill's spirit (find the
clearest way to show a concept) but aimed at a semi-technical reader who wants to understand class
structure quickly, not an infographic/analogy audience. Do not edit the global `explainer-graphic`
skill to chase this look — this skill is intentionally separate and lives only in this repo.

## When to use this

The reader is a spec implementer or data modeler skimming `docs/source/**/*.rst`, not a general
audience. The diagram sits inline next to technical prose that already explains the concept in
words — its job is to make the class shapes and associations click at a glance, in a small footprint
(these are NOT full-page posters). Reach for this skill whenever a docs page needs a new or replacement
class/association diagram; reach for `explainer-graphic` instead if the actual ask is a real-world-analogy
teaching graphic for a non-technical audience.

## Reference implementation

`example.html` in this skill's directory is the canonical, approved reference — a diagram of
`Statement`/`Proposition`/`Method`/`Contribution`/`Document`/`EvidenceLine`/`EvidenceItem`/`StudyResult`/`DataItem`
built with this skill. **Copy its `<style>` block verbatim** as the starting point for any new diagram;
only add new component variants if the reference truly doesn't cover the shape you need (and if you
do, fold the addition back into this file's component vocabulary below so it stays reusable).

## Design tokens

CSS custom properties, light mode first, `:root[data-theme="dark"]` and
`@media (prefers-color-scheme: dark)` overrides matching (see `example.html` for the exact block —
copy it, don't retype it):

- `--bg` / `--ink` / `--ink-soft` — page background, primary text, secondary/muted text
- `--line` / `--line-strong` — hairline borders (frames) vs. solid borders (class boxes, connectors)
- `--box` / `--box-role` — fill for a normal class box vs. a "same class, additional role" box
- `--accent` — used sparingly for type annotations and stereotype labels
- `--tu` / `--d` — maturity badge colors (Trial Use / Draft; add `--n` if a Normative class shows up)

Typography: `-apple-system, "Segoe UI", system-ui, sans-serif` for page chrome (title/caption/legend);
`ui-monospace, "SF Mono", "Cascadia Code", Consolas, monospace` for everything that is a literal
schema identifier (class names, property names, types) — this distinguishes "the model's actual
vocabulary" from prose at a glance. Keep the page itself small and unstyled otherwise: no hero, no
big color blocks, no decorative illustration. It's a diagram, not a poster.

## Component vocabulary

- **`.cls`** — a class box: header (`.head` with class `.name`, monospace) + `.body` listing 2-5
  representative properties as `.prop` lines (`<b>propName</b>: <span class="ty">Type or cardinality</span>`).
  An optional `.foot` holds one short italic annotation for a non-obvious modeling nuance — not a
  general description, only something a reader would otherwise get wrong.
- **`.cls.role`** — dashed border + `--box-role` fill. Means "this is the *same class* as a plain
  `.cls` box elsewhere in the diagram, just appearing again in a different structural role" (e.g. a
  `Statement` nested as an `«EvidenceLine»` or an `«EvidenceItem»`). Use a `.stereo` line
  (`&laquo;RoleName&raquo;`) above the class name to name the role. Never invent a new dashed-box
  meaning — it always means "additional role of a class shown solidly elsewhere," per the legend.
- **`.badge`** (`.tu` / `.d`) — small maturity marker, fixed to the box's top-right corner. Source the
  letter from that class's actual `maturity:` value in the relevant `*-source.yaml`: `TU` (trial use),
  `D` (draft), `N` (normative, if it ever comes up). Every class box gets one — don't skip it.
- **`.vconnector`** — a vertical arrow between two stacked boxes, with a `.role` label (the property
  name) and a `.card` cardinality label (`0..1`, `0..m`, `1..1`, etc.).
- **`.side-connector`** — a short horizontal arrow used when boxes sit side-by-side (e.g. peripheral
  classes like `Proposition`/`Method`/`Contribution`/`Document` flanking a central class). Add the
  `.reverse` modifier when the arrowhead needs to point left instead of right (see arrow-direction
  rule below). Give every `.side-connector` a fixed width (see `example.html`) so parallel connectors
  in a stacked column line up — don't let label text length change the box alignment.
- **`.frame`** — a large dashed grouping rectangle with a small `.frame-label` tab in the top-left
  corner, used to show that several sibling boxes are all subclasses/shapes of one abstract parent
  (e.g. wrapping `StudyResult`/`DataItem`/`Statement «EvidenceItem»` in an `InformationEntity` frame).
  Keep the label subtle — it should read as context, not compete with the boxes it contains.
- **`.legend`** — keep it minimal. Only call out things that aren't self-evident from the boxes
  themselves (e.g. what a dashed box means, what the badges mean). Don't legend obvious things like
  "solid box = a class."

## Content rules

- **Arrows point away from the class that owns the property**, toward the class(es) that property's
  type references — i.e. standard UML directed-association convention. If `Statement.specifiedBy`
  references `Method`, the arrow goes `Statement → Method`, not the reverse, regardless of which side
  of the layout the boxes end up on.
- **Field format**: `propertyName: Type` or `propertyName: cardinality` (pick whichever is more
  informative for that field — don't cram both into a 10px-wide box). Show 2-5 fields per box, the
  ones that matter for understanding the relationship the diagram is about — not an exhaustive
  attribute list (that's what the generated `def/` pages are for).
- **Required vs. optional matters and often differs by context.** A property can be required on one
  class but optional when the same class plays a different role (e.g. `Statement.proposition` is
  `1..1` at the top level, `0..1` when the Statement is nested as an EvidenceLine) — get this from the
  actual `required:` list in the source YAML for each context, don't assume uniform cardinality just
  because it's "the same property."
- **Verify every class name, field name, type, and cardinality against the current
  `schema/va-spec/*.yaml` / `schema/gkm-core/*.yaml` sources before publishing** — never carry over
  values from a previous diagram version without rechecking, since the schema moves.
- Keep prose annotations (`.foot`, `.caption`) short, and only use them for things a reader would
  otherwise get wrong or miss — not general restatement of what the box already shows.

## Output and delivery

- Self-contained single HTML file (inline `<style>`, no external requests — the Artifact CSP blocks
  external fonts/scripts anyway).
- Support both themes via the tokens above; the file may be viewed standalone or embedded.
- Final destination is `docs/source/_static/diagrams/<name>.html`, embedded into the relevant
  `.rst` page via an iframe:

  ```rst
  .. raw:: html

     <iframe src="../_static/diagrams/<name>.html" style="width:100%; height:<Npx>; border:0;" title="<description>"></iframe>
  ```

  (`html_static_path = ["_static"]` is already configured in `docs/source/conf.py`, so files placed
  there ship with the built site automatically — no extra Sphinx config needed.) Pick the iframe
  height to fit the diagram without a scrollbar at typical viewport widths; check the built page in
  `sphinx-build` output before calling it done, since iframe height doesn't auto-fit to content.
- Before treating a diagram as final, publish it as an Artifact for review — these diagrams get
  iterated on with real design feedback (layout direction, what to include/exclude, arrow direction,
  alignment), so don't skip the review step even when the content itself seems obviously correct.

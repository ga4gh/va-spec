---
name: va-spec-doc-diagrams
description: House style and rules for the interactive HTML diagrams embedded in the VA-Spec Sphinx docs (docs/source/_static/diagrams/*.html) — the class-hierarchy tree, the narrative "data structure" diagrams, and the developer-guide structural diagrams. Use when creating, editing, tightening, or re-rendering any of these embedded diagrams. For the older single-diagram property-box/worked-example style, see the sibling va-spec-class-diagram skill.
---

# VA-Spec Doc Diagrams

These are small, **self-contained, interactive HTML files** in
`docs/source/_static/diagrams/*.html`, embedded in `docs/source/**/*.rst` via a
`.. raw:: html` `<iframe>`. They render class shapes, attributes, and
associations for a semi-technical reader skimming the docs. They are **not**
generated from the schema by a processor — they are hand-authored HTML/CSS/SVG
that a human maintains and re-renders. Keep them faithful to the **current**
generated schema (see "Reconcile to the current model" below).

Every diagram shares one technical scaffold and picks one of three archetypes.

## The shared scaffold (copy it, don't reinvent)

Copy the `<style>` tokens + the `fit()`/`syncFrameHeight()` script from an
existing diagram of the same archetype rather than retyping them.

- **Theme tokens.** A `:root` block of CSS custom properties (`--bg`, `--ink`,
  `--ink-soft`, `--line-strong`, `--box`, `--accent`, …), redefined under both
  `:root[data-theme="dark"]` and `@media (prefers-color-scheme: dark)` so the
  diagram tracks the reader's light/dark theme. Style everything through the
  tokens; never hard-code a hex in a component rule.
- **Scale-to-fit.** `#stage` (overflow hidden) wraps `#scale-inner`
  (`width: max-content`). A `fit()` function measures natural width and applies
  `transform: scale(min(1, stageWidth / naturalWidth))` so the diagram always
  fits the RTD column (~800px) and never scrolls sideways. Wider natural width →
  more scale-down → smaller text, so **narrower is more legible** in RTD.
- **iframe height sync.** `syncFrameHeight()` sets `window.frameElement.style.height`
  to the rendered body height (falls back to a `postMessage({type:'va-spec-diagram-height'})`
  handled by `docs/source/_static/diagram-iframe-height.js`, listed in
  `conf.py`'s `html_js_files`). The inline `height:NNNpx` in the `.rst` iframe is
  only a pre-JS fallback — set it to the measured height (see workflow) to avoid
  layout shift.
- **Clickable boxes.** Class boxes are `<a class="..." target="_top" href="../../…#anchor">`
  linking to that class's own doc page (relative path from the diagram file;
  anchor is the lowercased class name). `:hover`/`:focus-visible` get an accent
  outline.
- **Title/caption/legend** sit outside the scaled stage, centered, `max-width`
  clamped to the diagram's own width by `fit()`.

## Archetype 1 — inheritance / hierarchy tree

Canonical file: `core-class-hierarchy-model.html`. Shows `inherits:` edges with
open (hollow) UML triangles pointing at the parent, boxes with a header
(stereotype + class name), a full attribute list, and a maturity badge (TU/D).

- **Attribute line format:** `name: type [min..max]` — `.nm` bold (the
  property), `.ty` in `--accent` (the datatype, ` | `-joined unions with `IRI`
  abbreviating `iriReference`), `.card` a bracketed cardinality
  (`[1..1]` required scalar, `[0..1]` optional scalar, `[N..m]` list using
  `minItems`). One line per attribute, `white-space: nowrap`.
- **Own attributes only.** Each box lists the attributes the class *introduces*
  (its own JSON `properties` minus its diagram-parent's), because inherited ones
  appear on the ancestor box and the inheritance edge carries them down. Source
  them from the generated JSON (`schema/va-spec/json/<Class>` and
  `schema/gkm-core/json/<Class>`), not by hand — regenerate the box bodies with
  a small script when the schema changes.
- **Boxes are content-sized** (`width: max-content`) so no attribute wraps and
  there's no wasted right-margin; tighten the inter-column gaps rather than the
  boxes.
- **Connectors are SVG, computed after layout** by a `drawTree()` that reads
  `getBoundingClientRect()` for every box and routes each edge (modes:
  `straight`, `left-fan`/`right-fan` for satellites stacked beside the parent,
  `bottom-fan` and `lower` for children/grandchildren below). Routing must not
  cross a box or another line — verify by eye at 2× and, when in doubt, by
  walking each drawn segment against every other box's rect.

## Archetype 2 — narrative "data structure" diagram

Canonical files: `statement-data-structure.html`, `evidence-line-data-structure.html`,
`study-result-data-structure.html`. A radial, **class-level** view: a central
vertical axis of blue "artifact" boxes flanked by gray "provenance" boxes, each
box showing the class name + an italic `(e.g. …)` narrative that the section's
prose leans on (no attribute list). Associations are orthogonal SVG arrows
pointing from a class to the object it references, labeled `role` over
`cardinality`.

- **Box roles.** `.node` = gray provenance class. `.node.axis` = central artifact
  (blue fill, `--axis`). `.node.main` = the diagram's **root** class (the one the
  section is about) — emphasized with a **heavier outline, larger name text, and
  a slightly larger box** (the inner `.prop-box`/Proposition box stays normal
  weight). A nested `.prop-box` renders an encapsulated Proposition with its own
  concrete example value.
- **Narrative text is the point.** Reuse one running example across all three
  diagrams and the surrounding prose (HRAS:c.173C>T / Costello Syndrome / gnomAD)
  so the worked story stays recognizable. Italic, `--ink-soft`.
- **Layout = fixed-size `.canvas` with absolutely-positioned boxes.** Rows read
  top→bottom along the axis; provenance boxes sit left/right. A small
  `layoutBoxes()` pass runs before `draw()`: boxes with `data-cy-ref="<node>"`
  are **vertically centered on that axis box** (so a row's boxes share a
  center-line and horizontal associations stay level and endpoints distribute
  evenly), and `data-below="<node>"` boxes are placed just under their reference.
  Do this in JS because box heights vary with wrapped narrative text.
- **Connectors** are a `C` array of `{from,to,role,card,pts(a,b),lab(a,b)}` where
  `pts` returns a polyline from measured rects and `lab` returns the label
  anchor. Route through **lanes** (a clear x between columns, a far-left/far-right
  lane for loop-arounds) so **no line crosses a box or another line**; stack
  multiple arrows into a shared target (e.g. three `reportedIn` into Document) at
  distinct top/middle/bottom entry points. `dash:true` + `note:'(profile)'` marks
  a profile-level (non-base) association (e.g. Study Result → StudyGroup `cohort`).
- **Keep it tight.** Boxes are narrow (mostly text, so they go narrow-and-tall);
  minimize whitespace between rows and columns; the narrower the canvas, the
  larger everything renders in RTD.

## Archetype 3 — developer-guide structural diagram

Canonical files: `core-model-classes-model.html`, `base-profiles-model.html`,
`community-profiles-model.html` (embedded in `developer-guide.rst`). Plain
class boxes (name + stereotype, no attributes) grouped to show a mechanism:
inheritance uses **hollow** triangles pointing to the parent; schema-composition
("constraint_over") uses a **filled** triangle. Dashed frames group community
sub-profiles. Simpler CSS bus/fan connectors (or a small SVG `drawTree`).

## Reconcile to the current model

These diagrams live in current docs, so match today's generated schema even when
recreating an older figure: e.g. `Activity`/`outputOf` no longer exist (provenance
is `Contribution`), `specifiedBy` is `0..1`, `Statement` uses `classification`
(not `outcome`), `EvidenceLine` is a distinct class with `evidenceOutcome`, and a
Study Result's group link is the profile-level `cohort` → `StudyGroup` (dashed),
not a base attribute. When in doubt, read `schema/va-spec/json/<Class>` /
`schema/gkm-core/json/<Class>`.

## Render / verify workflow

There is no browser automation in this repo; use the installed Chrome app
headless to render and measure (chromedriver/selenium are NOT available):

```
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
# 2x screenshot for visual review (wrap the file in an 820px-wide iframe like RTD)
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=2400 \
  --force-device-scale-factor=2 --screenshot=out.png --window-size=840,1000 "file://…/wrapper.html"
```

- **Wrapper** = a tiny HTML page with `<div style="width:820px;margin:auto"><iframe src="file://…/<diagram>.html" style="width:100%;border:0;height:NNNpx"></iframe></div>` so you review it at true RTD width.
- **Measure height** by rendering at device-scale 1 and scanning the PNG for the
  last non-white row (a few lines of PIL); set the `.rst` iframe `height:` to that
  (+ a small buffer). Re-measure whenever box content changes.
- **Always eyeball the connectors** for crossings and clipped labels; fix by
  nudging lane offsets / label anchors, not by widening the whole canvas.
- After editing, `cd docs && make html` must be warning-clean, then commit the
  `*.html` plus any changed `.rst` iframe heights.

## Guardrails

- Self-contained only: inline all CSS/JS, no external fonts/CDNs/network — the
  files render inside a docs iframe.
- Don't hand-edit generated `json/`, `def/`, or `docs/source/def/`; diagrams are
  `_static` assets and are safe to edit directly.
- Match the sibling diagrams' tokens/fonts exactly so the set reads as one system.

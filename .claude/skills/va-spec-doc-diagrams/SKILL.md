---
name: va-spec-doc-diagrams
description: House style and rules for the interactive HTML diagrams embedded in the VA-Spec Sphinx docs (docs/source/_static/diagrams/*.html) -- the class-hierarchy tree, the narrative "data structure" diagrams, and the developer-guide structural diagrams. Use when creating, editing, tightening, or re-rendering any of these embedded diagrams. For the older single-diagram property-box/worked-example style, see the sibling va-spec-class-diagram skill.
---

# VA-Spec Doc Diagrams

Small, **self-contained, interactive HTML files** in `docs/source/_static/diagrams/*.html`,
embedded in `docs/source/**/*.rst` via a `.. raw:: html` `<iframe>`. They render class shapes,
attributes, and associations for a semi-technical reader. They are hand-authored HTML/CSS/SVG
(not schema-generated), so keep them faithful to the **current** generated schema (see
"Reconcile"). Every diagram shares one scaffold and picks one of three archetypes. Copy the
`<style>` + scripts from an existing file of the same archetype rather than retyping them.

## Shared scaffold

- **Theme tokens.** `:root` custom properties (`--bg`, `--ink`, `--ink-soft`, `--line-strong`,
  `--box`, `--accent`, ...), redefined under `:root[data-theme="dark"]` **and**
  `@media (prefers-color-scheme: dark)`. Style through tokens; never hard-code a hex in a rule.
- **Scale-to-fit.** `#stage` (overflow hidden) wraps `#scale-inner` (`width: max-content`); a
  `fit()` applies `transform: scale(min(1, stageWidth/naturalWidth))` so the diagram fits RTD
  (~800px) and never scrolls sideways. Narrower natural width -> larger, more legible render.
- **iframe height sync.** `syncFrameHeight()` sets `window.frameElement.style.height` to the body
  height (falls back to `postMessage({type:'va-spec-diagram-height'})`, handled by
  `_static/diagram-iframe-height.js` in `conf.py`'s `html_js_files`). The inline `height:NNNpx`
  in the `.rst` iframe is only a pre-JS fallback -- set it to the measured height.
- **Standalone scroll.** Use `body { overflow-x: hidden; }` (NOT `overflow: hidden`) so the file
  scrolls vertically when opened directly in a browser; `overflow: hidden` blocks that. `#stage`
  keeps `overflow: hidden` (it clips the scaled content horizontally).
- **Clickable boxes.** Class boxes are `<a class="..." target="_top" href="../../...#anchor">` to
  that class's doc page (relative path; anchor = lowercased class name); `:hover`/`:focus-visible`
  get an accent outline.
- **Title/caption/legend** sit outside the scaled stage, centered, `max-width` clamped to the
  diagram's own width by `fit()`.

## Archetype 1 -- inheritance / hierarchy tree

Canonical: `core-class-hierarchy-model.html`. Boxes = header (stereotype + class name) + full
attribute list + maturity badge (TU/D); `inherits:` edges drawn as open (hollow) UML triangles
pointing at the parent.

- **Attribute line:** `name: type [min..max]` -- `.nm` bold (property), `.ty` in `--accent`
  (datatype, ` | `-joined unions, `IRI` abbreviating `iriReference`), `.card` a bracketed
  cardinality (`[1..1]` required scalar, `[0..1]` optional, `[N..m]` list from `minItems`). One
  line each, `white-space: nowrap` -- do **not** wrap.
- **Own attributes only.** Each box lists the attributes the class *introduces* (its JSON
  `properties` minus its diagram-parent's) sourced from `schema/va-spec/json/<Class>` /
  `schema/gkm-core/json/<Class>`; regenerate box bodies with a small script when the schema
  changes -- don't hand-maintain.
- **Uniform-width columns + single lane.** Each satellite column stretches its boxes to one width
  (`align-items: stretch` + `.cls { width: auto }`) so right edges align; then a **single** side
  lane, positioned just outside the **column's widest box** (not each box's own edge -- else a
  narrow box routes its lane behind a wider one), gives every connector one short, equal stub.
- **SVG routing, after layout.** `drawTree()` reads `getBoundingClientRect()` per box and routes
  each edge (`straight`, `left-fan`/`right-fan`, `bottom-fan`, `lower`). For a second row of
  children below the first row (e.g. StudyResult/DataItem under Statement/EvidenceLine), route the
  `lower` connectors up through the **measured gap between the two first-row boxes** (their
  `(right+left)/2`), not the parent's centre -- content-sized boxes differ in width, so the gap is
  off-centre and the parent-centre line would be overlaid by the wider box. No line may cross a box
  or another line; verify at 2x.

## Archetype 2 -- narrative "data structure" diagram

Canonical: `statement-data-structure.html`, `evidence-line-data-structure.html`,
`study-result-data-structure.html`. A radial, class-level view: a central vertical axis of blue
"artifact" boxes flanked by gray "provenance" boxes, each box = class name + italic `(e.g. ...)`
narrative (no attribute list). Orthogonal SVG arrows point from a class to the object it
references, labeled `role` over `cardinality`.

- **Box roles.** `.node` = gray provenance. `.node.axis` = central artifact (blue). `.node.main` =
  the diagram's **root** class (what the section is about) -- emphasized with a **heavier outline,
  larger name text, and slightly larger box**; the inner `.prop-box` (an encapsulated Proposition
  with a concrete value) stays normal weight. Reuse one running example (HRAS:c.173C>T / Costello /
  gnomAD) across all three diagrams and the prose.
- **Layout = fixed `.canvas` with absolutely-positioned boxes.** Keep the canvas tight (~820px
  wide -> near-1:1 in RTD); minimize the gaps between the three columns. A `layoutBoxes()` pass
  runs before `draw()`: `data-cy-ref="<node>"` vertically **centres** a provenance box on that axis
  box (so a row shares a centre-line and horizontal associations stay level with evenly-distributed
  endpoints); `data-below="<node>"` places a box just under its reference.
- **Connectors** = a `C` array of `{from,to,role,card,pts(a,b),lab(a,b)[,dash,note]}`; `pts`
  returns a polyline from measured rects, `lab` the label anchor. Route through **lanes** (a clear
  x between columns; far-left/far-right lanes for loop-arounds) so **no line crosses a box or
  another line**. `dash:true`+`note:'(profile)'` marks a profile-level (non-base) link (e.g. Study
  Result -> StudyGroup `cohort`).
- **Multiple arrows into one box -> separate edges.** When a box receives several same-role
  associations (e.g. three `reportedIn` into Document, three `contributions` into Contribution),
  do **not** stack them on one edge -- route them into **different edges** (top / right / bottom,
  or top / left / bottom) so both the arrowheads and their labels separate. Enter a box's TOP/
  BOTTOM edge by ending the polyline at `[boxCx +/- offset, box.t|box.b]`; the default
  `orient="auto-start-reverse"` marker points the head correctly.
- **Label placement.** A label may cover *its own* line but never another line or a box edge. Keep
  it clear of lanes (nudge along its segment into open space), and put loop labels in the clear gap
  **below** the boxes. When space is tight, prefer separating the lines vertically over cramming
  labels.

## Archetype 3 -- developer-guide structural diagram

Canonical: `core-model-classes-model.html`, `base-profiles-model.html`,
`community-profiles-model.html` (in `developer-guide.rst`). Plain class boxes (name + stereotype,
no attributes) grouped to show a mechanism: inheritance = **hollow** triangle to parent;
schema-composition ("constraint_over") = **filled** triangle; dashed frames group community
sub-profiles. Simple CSS bus/fan connectors or a small SVG `drawTree`.

## Reconcile to the current model

Match today's generated schema even when recreating an older figure: `Activity`/`outputOf` are
gone (provenance is `Contribution`); `specifiedBy` is `0..1`; `Statement` uses `classification`
(not `outcome`); `EvidenceLine` is a distinct class with `evidenceOutcome`; a Study Result's group
link is the profile-level `cohort` -> `StudyGroup` (dashed), not a base attribute. When unsure,
read `schema/va-spec/json/<Class>` / `schema/gkm-core/json/<Class>`.

## Render / verify workflow

No browser automation in this repo; use the installed Chrome app headless (chromedriver/selenium
are NOT available):

```
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --virtual-time-budget=2400 \
  --force-device-scale-factor=2 --screenshot=out.png --window-size=840,1000 "file://.../wrapper.html"
```

- **Wrapper** = a page with `<div style="width:820px;margin:auto"><iframe src="file://.../<diagram>.html"
  style="width:100%;border:0;height:NNNpx"></iframe></div>` to review at true RTD width.
- **Measure height** at device-scale 1: scan the PNG for the last non-white row (a few lines of
  PIL); set the `.rst` iframe `height:` to that + a small buffer. Re-measure when content changes.
- **Always eyeball connectors** for crossings and labels overlaying lines/box edges; fix by nudging
  lane offsets / label anchors or separating edges -- not by widening the whole canvas.
- After editing, `cd docs && make html` must be warning-clean; commit the `*.html` plus any changed
  `.rst` iframe heights.

## Guardrails

- Self-contained only: inline all CSS/JS, no external fonts/CDNs/network.
- Don't hand-edit generated `json/`, `def/`, or `docs/source/def/`; diagrams are `_static` assets,
  safe to edit directly.
- Match the sibling diagrams' tokens/fonts exactly so the set reads as one system.

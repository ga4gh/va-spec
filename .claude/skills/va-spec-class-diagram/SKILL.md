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
- **Box widths should have little to no dead space, but never guess a narrower width — measure it.**
  Since the figure drives the whole diagram's width (see the scale-to-fit rule below), a narrower box
  makes everything larger within the same column budget, so it's worth trimming — but `.prop` lines
  use `text-overflow: ellipsis`, which fails silently (truncated text, no build warning) if a box goes
  too narrow. Before picking a width, build a small throwaway test page with the box's real field
  strings at the real font/padding, sweep candidate widths, and check each element's
  `scrollWidth > clientWidth` (the exact ellipsis-triggering condition) rather than eyeballing it —
  then pick something a bit above the measured breaking point as a safety margin for font-rendering
  differences across browsers/OSes. Re-measure whenever field content changes; don't reuse an old
  width number for new text.

### Schema-validity policy

Every class and field shown in a diagram must exist in the current schema sources, with one
narrow, explicit exception:

- Before publishing, check each class box and each field line against the current
  `schema/va-spec/*.yaml` / `schema/gkm-core/*.yaml` (and cat-vrs/vrs sources, if referenced). This
  is the same check as the cardinality-verification rule above, but framed as existence, not just
  correctness — a class or property that doesn't exist at all is a different failure mode than one
  with a stale cardinality.
- If the diagram's author (the person directing this session, not a schema author found in git
  history) wants to include a class or field that does **not** currently exist in the schema — e.g.
  to represent a proposed or planned addition — confirm this is intentional with them before
  including it. Don't silently drop it, and don't silently include it as if it were real.
- If, after confirming, it's kept: annotate it visually as **"not currently available"** rather than
  presenting it as equivalent to real schema content. Use a `.foot` annotation on the box (or the
  specific `.prop` line) stating this plainly, and consider a distinct visual treatment (e.g. muted/
  lower-opacity text) so it doesn't read as authoritative at a glance. Do not reuse the `.badge`
  maturity markers (`TU`/`D`/`N`) for this — those describe maturity of something that exists, not
  existence itself.

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
  there ship with the built site automatically — no extra Sphinx config needed.) The `height:<Npx>`
  in that snippet is only a pre-JS placeholder to avoid a layout jump on first paint (pick roughly
  the diagram's natural unscaled height) — the diagram's own script resizes the real `<iframe>` to
  the exact rendered height once it runs (see below), so don't hand-tune this number precisely.
- **The diagram must scale to fit its column like a raster image, not reflow or scroll.** The
  sphinx_rtd_theme content column has a **fixed** `max-width` (currently 800px, confirmed via the
  theme's built CSS — it does not grow with a wider browser window), so any diagram wider than that
  will overflow a naively-embedded iframe. Two approaches were tried and rejected before landing on
  the one below — don't reintroduce either:
  - *Horizontal scroll* (`overflow-x: auto`) — rejected: the user explicitly called this
    unacceptable; the diagram must fit by default, not require scrolling to see all of it.
  - *Responsive reflow* (`@media` breakpoints that restack boxes vertically at narrow widths) —
    rejected: it rearranges the approved positions of classes in the diagram, which must stay fixed.
  - **Use instead: whole-diagram scale-to-fit.** Wrap everything after the opening `<div class="wrap">`
    in `<div id="stage"><div id="scale-inner"> ... </div></div>`. `#scale-inner` gets
    `width: max-content; margin: 0 auto; transform-origin: top left;` so it always lays out at its
    natural, un-squished size — nothing inside it ever shrinks or reflows. `#stage` gets
    `overflow: hidden`. A small inline script measures `#scale-inner`'s natural `scrollWidth` against
    `#stage`'s `clientWidth`, computes `scale = Math.min(1, available / natural)`, and applies
    `transform: scale(scale)` to `#scale-inner` plus `stage.style.height = naturalHeight * scale` so
    the container collapses to match. Re-run it on `window.resize` and via `ResizeObserver` on
    `#stage`. This shrinks the whole diagram uniformly (same behavior as an `<img>` with
    `max-width:100%`) while leaving every box's position, relative to every other box, byte-for-byte
    identical — see `example.html` for the exact script and the `transform-origin: top left` reasoning
    (this must be `top left`, not `top center`: when `#scale-inner` overflows its container, `margin:
    auto` resolves to 0 rather than centering it, so the box's real rendered position is flush left,
    and the scale has to shrink from that same anchor or it drifts off-position and clips).
  - Verify by taking headless-Chrome screenshots of the actual built `.rst` page (not just the
    standalone diagram file) at a few window widths (e.g. 500px, ~1024px, and something wide like
    1400px) — the RTD column's fixed max-width means a wide *browser* window alone won't catch
    overflow bugs; a real narrow *column* case must be checked.
  - **The figure (`.diagram`), not the surrounding prose, must drive the natural width.** A caption
    or title line that's wider than the figure (unwrapped, plain-text elements try to render on one
    line under `width: max-content`) will inflate `#scale-inner`'s measured natural width and force
    the figure to scale down more than it needs to — the exact bug that produces a needlessly tiny,
    hard-to-read diagram with lots of relatively huge caption text above it. Give `.diagram` its own
    `width: max-content` (so it always reports its true intrinsic width regardless of what else is in
    `#scale-inner`), and in the fit script, measure that width and set it as `max-width` on the
    title/caption/legend elements *before* measuring `#scale-inner`'s `scrollWidth` for the scale
    calculation — see `example.html`'s `textBlocks`/`diagramWidth` logic. This keeps the figure at
    the largest size the available space allows; text wraps to match it, never the reverse.
  - **No leftover blank space below the diagram, and the iframe height must never be a fixed/guessed
    number — treat it as continuously reactive, not something computed once.** A static iframe
    height (even one "corrected" a single time on load) goes stale the moment the available width
    changes again later for any reason — the RTD column resizing, a sidebar toggling, a font
    finishing load — and a stale height either leaves dead space or clips content. Because the whole
    file is a same-origin embed (served from the same site as the doc page that iframes it), reach
    the embedding `<iframe>` element via `window.frameElement` and keep its `style.height` mirrored
    to this document's own rendered height with a dedicated `ResizeObserver` on `document.body` (see
    `example.html`'s `syncFrameHeight`) — separate from the `ResizeObserver` on `#stage` that drives
    `fit()`'s width-based rescale. They're separate observers because scaling `#stage` is what
    *causes* `body` to change size, not the other way around; each end needs its own hook rather than
    threading one call through the other. This makes the sync reactive-by-construction to *any*
    layout change, not just the ones a hand-picked call site remembers to trigger.
    - **Measure the height via `document.body.getBoundingClientRect().height`, not
      `document.documentElement.scrollHeight` (or `document.body.scrollHeight`) — the latter is a
      trap.** For the document's designated scrolling element, `scrollHeight` is *floored to the
      current viewport height* — i.e. the iframe's own *existing* height — even when actual content
      is shorter, so it can only ever confirm whatever height the iframe already happens to have,
      never correct it (this is exactly what caused a real "large dead space below the figure"
      regression here). `getBoundingClientRect().height` on `body` is a plain geometry read, not a
      scrolling-element query, so it isn't subject to that floor — and since `*{box-sizing:
      border-box}` applies to `body` too, it already includes body's own top+bottom padding with no
      extra math needed.
    - Give the file its own `<!DOCTYPE html>` (it's parsed as an independent document via
      `iframe src=`, not inlined into the parent page) — without one it renders in quirks mode, which
      changes which element (`html` vs `body`) is the "scrolling element" the floor above applies to,
      making the bug even less predictable to reason about.
    - The `height:<Npx>` placeholder in the `.rst` embed snippet only matters for the brief instant
      before this script's first run — pick something reasonably close (measure the diagram's actual
      rendered height at a typical RTD column width) purely to avoid a visible flash, but don't treat
      getting that number exactly right as the fix; the fix is the continuous reactive sync above.
- Before treating a diagram as final, publish it as an Artifact for review — these diagrams get
  iterated on with real design feedback (layout direction, what to include/exclude, arrow direction,
  alignment), so don't skip the review step even when the content itself seems obviously correct.

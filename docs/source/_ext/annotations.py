"""Provide annotated-code-block directive for Sphinx.

Behaves exactly like a `.. code-block`, but replaces ALL comments with tooltips that
contain the comment text. This is useful for cases like example YAML files where we
might want to include lots of details about a given line.

Example

  .. annotated-code-block:: yaml

     SCV000778434.1:
       id: SCV000778434.1
       type: Statement  # This is a long comment describing this field. It will be replaced by a tooltip.

Notes
 * Indentation of the comment gets ignored, so don't bother lining them up.

Limitations (variably addressable if necessary)
 * Replaces ALL comments with tooltips
 * If a comment is on its own line, it'll still get replaced by a tooltip. Don't even try
   a multiline comment.
 * Assumes "#" for comment character (works for YAML, nothing else has been tested)
 * Tooltip always goes right, even if it's all the way to the right of the viewport.
 * Bleeds to the right of a viewport a bit if the line is too long (you can scroll, but
   it's annoying -- still better than before)

It works by post-processing the generated docs; it has no direct access to the parsed code
block or surrounding RST, only the HTML output. This creates some limitations, but
injecting the annotation in during code generation was causing some problems with syntax
highlighting.
"""

from __future__ import annotations

import re
from typing import Any, Dict, List

from docutils import nodes
from docutils.parsers.rst import Directive
from sphinx.highlighting import PygmentsBridge

# Pattern to identify comment-strings as highlighted by Pygments
COMMENT_SPAN_RE = re.compile(
    r"(?P<ws><span class=\"w\">[ \t]*</span>)?"
    r"(?P<comment><span class=\"c1\">#(?P<space>\s*)"
    r"(?P<text>.*?)</span>)",
    re.DOTALL,
)


def replace_comment_spans_with_tooltips(highlighted: str) -> str:
    """Replace highlighted code comment spans with a tooltip button.

    - Removes the comment marker '#'
    - Moves comment text into tooltip
    - Collapses any preceding whitespace span to a single space before the button

    :param highlighted:
    """

    def repl(m: re.Match[str]) -> str:
        # This is already HTML-escaped by Pygments, so we can embed directly
        text_html = (m.group("text") or "").lstrip()

        # handle empty comment
        if not text_html:
            return ""

        widget = (
            '<span class="ann-wrap">'
            '<button type="button" class="ann-btn" aria-label="annotation">+</button>'
            f'<span class="ann-tip" role="tooltip" hidden>{text_html}</span>'
            "</span>"
        )
        return widget

    return COMMENT_SPAN_RE.sub(repl, highlighted)


class annotated_code_block(nodes.General, nodes.Element):
    """A custom node that stores code + language."""


class AnnotatedCodeBlock(Directive):
    """Block of "annotated" code (code + added tooltip)

    Notes:
      - This post-processes the *highlighted HTML*, so Pygments is not disturbed.
      - It currently targets Pygments comment class "c1" which is typical for YAML.
    """

    required_arguments = 1  # language of the code block
    has_content = True
    option_spec: Dict[str, Any] = {}

    def run(self) -> List[nodes.Node]:
        lang = self.arguments[0].strip()
        code = "\n".join(self.content)

        node = annotated_code_block()
        node["language"] = lang
        node["code"] = code
        return [node]


def visit_annotated_code_block_html(self: Any, node: annotated_code_block) -> None:
    lang: str = node["language"]
    code: str = node["code"]

    highlighter = PygmentsBridge("html", self.config.pygments_style)
    highlighted = highlighter.highlight_block(code, lang, linenos=False)

    highlighted = replace_comment_spans_with_tooltips(highlighted)

    self.body.append(highlighted)
    raise nodes.SkipNode


def setup(app: Any) -> Dict[str, Any]:
    app.add_node(
        annotated_code_block,
        html=(visit_annotated_code_block_html, lambda self, node: None),
    )
    app.add_directive("annotated-code-block", AnnotatedCodeBlock)

    app.add_css_file("ann.css")
    app.add_js_file("ann.js")

    return {
        "version": "0.1.0",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }

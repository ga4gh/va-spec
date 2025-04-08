# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import re
import subprocess
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# def _get_git_tag():
#     res = subprocess.run("git describe --tags --exact-match".split(), capture_output=True)
#     if res.stderr.decode().startswith("fatal"):
#         # if no exact tag, then get branch
#         res = subprocess.run("git rev-parse --abbrev-ref HEAD".split(), capture_output=True)
#     tag = res.stdout.decode().strip()
#     return tag

# def _parse_release_as_version(rls):
#     m = re.match("^(\d+\.\d+)", rls)
#     if m:
#         return m.group(1)
#     return rls


# -- Project information -----------------------------------------------------

project = 'GA4GH Variant Annotation Specification'
copyright = '2024, GA4GH VA Contributors'
author = 'Committers'
master_doc = 'index'
# # N.B. RTD ignores these values. :-/
# release = _get_git_tag()
# version = _parse_release_as_version(release)
print("RTD env:")
print("READTHEDOCS              =", os.environ.get("READTHEDOCS"))
print("READTHEDOCS_VERSION      =", os.environ.get("READTHEDOCS_VERSION"))
print("READTHEDOCS_VERSION_NAME =", os.environ.get("READTHEDOCS_VERSION_NAME"))
print("READTHEDOCS_VERSION_TYPE =", os.environ.get("READTHEDOCS_VERSION_TYPE"))

# Get version info from ReadTheDocs
rtd_version = os.environ.get("READTHEDOCS_VERSION_NAME")  # actual branch/tag (e.g., "main", "1.x")

# Load static rst_epilog from file
rst_epilog_fn = os.path.join(os.path.dirname(__file__), 'rst_epilog')
with open(rst_epilog_fn, encoding="utf-8") as f:
    static_epilog = f.read().format(release=rtd_version)

# GitHub base URL
github_user = "ga4gh"
github_repo = "va-spec"
github_base = f"https://github.com/{github_user}/{github_repo}/blob/{rtd_version}"

# Path to the file with link mappings
link_file_path = os.path.join(os.path.dirname(__file__), "github_links.txt")

# Parse and build substitutions
dynamic_links = []

with open(link_file_path, encoding="utf-8") as f:
    for line in f:
        # Ignore blank lines or comments
        line = line.strip()
        if not line or line.startswith("#"):
            continue

        # Parse: substitution_name = path/to/file
        if "=" in line:
            label, filepath = [part.strip() for part in line.split("=", 1)]
            url = f"{github_base}/{filepath}"
            label_text = label.replace('_', ' ').title()
            link = f".. |{label}| replace:: `{label_text} <{url}>`__"
            dynamic_links.append(link)

# Combine everything into dynamic_epilog
dynamic_epilog = "\n".join(dynamic_links)

# Combine both static and dynamic epilogs
rst_epilog = static_epilog  + "\n" + dynamic_epilog

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.todo'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# TODO directive output
todo_include_todos = True
todo_emit_warnings = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_options = {
    'navigation_depth': 5,  # Increase to 4 levels of nested sections
    'collapse_navigation': False
}
html_logo = 'images/GA-logo.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_css_files = ['theme_overrides.css']

# Sidebars

html_sidebars = { '**': ['globaltoc.html', 'relations.html',
                         'sourcelink.html', 'searchbox.html'] }
html_context = {
    "conf_py_path": "/docs/source/",
    "display_github": True,
    "github_user": "ga4gh",
    "github_repo": "va-spec",
    "github_version": rtd_version,
}

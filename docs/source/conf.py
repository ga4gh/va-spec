# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- GIT branch and release info --------------------------------------------------------------
import os
import requests
import subprocess

def get_rtd_branch_from_github(repo="ga4gh/va-spec", default="main"):
    """
    If on ReadTheDocs and building a PR, fetch the true source branch name from GitHub.
    """
    if os.environ.get("READTHEDOCS") != "True":
        # Fallback: use git
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--abbrev-ref", "HEAD"],
                capture_output=True,
                check=True
            )
            branch = result.stdout.decode().strip()
            return branch if branch != "HEAD" else default
        except subprocess.CalledProcessError:
            return default

    version_type = os.environ.get("READTHEDOCS_VERSION_TYPE")
    pr_number = os.environ.get("READTHEDOCS_VERSION")

    if version_type != "external":
        return pr_number  # for 'branch' builds, this is the branch name

    token = os.environ.get("GITHUB_TOKEN")
    headers = {"Authorization": f"token {token}"} if token else {}

    try:
        response = requests.get(
            f"https://api.github.com/repos/{repo}/pulls/{pr_number}",
            headers=headers,
            timeout=5
        )
        if response.status_code == 200:
            return response.json()["head"]["ref"]  # actual source branch name
        else:
            print(f"GitHub API error: {response.status_code}")
    except Exception as e:
        print(f"GitHub API exception: {e}")

    return f"pull/{pr_number}"

# def get_git_branch_or_default(default="main"):
#     """
#     Get the current git branch even in a ReadTheDocs detached state.
#     """
#     # RTD PRs or branch builds
#     if os.environ.get("READTHEDOCS") == "True":
#         version = os.environ.get("READTHEDOCS_VERSION")
#         version_type = os.environ.get("READTHEDOCS_VERSION_TYPE")

#         if version_type in ("branch", "external"):  # external = PR
#             return version  # This is the branch name or PR ref

#     # Fallback: use git
#     try:
#         result = subprocess.run(
#             ["git", "rev-parse", "--abbrev-ref", "HEAD"],
#             capture_output=True,
#             check=True
#         )
#         branch = result.stdout.decode().strip()
#         return branch if branch != "HEAD" else default
#     except subprocess.CalledProcessError:
#         return default

def get_exact_git_tag():
    """
    Returns the exact tag for the current Git commit, if one exists.
    Returns None if the commit is not tagged exactly.
    """
    try:
        result = subprocess.run(
            ["git", "describe", "--tags", "--exact-match"],
            capture_output=True,
            check=True
        )
        tag = result.stdout.decode().strip()
        return tag if tag else None
    except subprocess.CalledProcessError:
        return None


# -- Project information -----------------------------------------------------

print("*!*!*!*!* Branch detected:", get_rtd_branch_from_github())
print("RTD env:", {
    "READTHEDOCS": os.environ.get("READTHEDOCS"),
    "READTHEDOCS_VERSION": os.environ.get("READTHEDOCS_VERSION"),
    "READTHEDOCS_VERSION_TYPE": os.environ.get("READTHEDOCS_VERSION_TYPE"),
})

project = 'GA4GH Variant Annotation Specification'
copyright = '2024, GA4GH VA Contributors'
author = 'Committers'
master_doc = 'index'
# get the release from the git tag if available, otherwise use the branch name
release = get_exact_git_tag()
if release == None:
    # If not on a tagged release, use the branch name
    release = get_rtd_branch_from_github(default="1.0")

# Load static rst_epilog from file
rst_epilog_fn = os.path.join(os.path.dirname(__file__), 'rst_epilog')
with open(rst_epilog_fn, encoding="utf-8") as f:
    static_epilog = f.read().format(release=release)

# GitHub base URL
github_user = "ga4gh"
github_repo = "va-spec"
github_base = f"https://github.com/{github_user}/{github_repo}/blob/{release}"

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
exclude_patterns = ["def/**"]

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
    "github_version": release,
}

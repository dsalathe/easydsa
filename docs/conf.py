"""Generate docs."""
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# Project information
project = "SimpleDSA"
copyright = "2024, David Salathé"
author = "David Salathé"
release = "0.2.0"

# General configuration
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.githubpages",
    "myst_parser",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# HTML output options
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

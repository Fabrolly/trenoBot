import datetime
import os
import sys

sys.path.extend(
    [
        os.path.join(os.path.dirname(__file__), "..", "backend"),
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "backend",
            "venv",
            "lib",
            "python3.8",
            "site-packages",
        ),
        os.path.join(os.path.dirname(__file__), "..", "frontend"),
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "frontend",
            "venv",
            "lib",
            "python3.8",
            "site-packages",
        ),
        os.path.join(os.path.dirname(__file__), "..", "telegram-bot"),
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "telegram-bot",
            "venv",
            "lib",
            "python3.8",
            "site-packages",
        ),
    ]
)

project = "TrenoBot"
author = "TrenoBot Team"
version = "1.0"

copyright = "{0}, TrenoBot".format(datetime.datetime.now().year)


extensions = [
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
    "sphinx.ext.autosummary",
    "sphinx.ext.doctest",
    "sphinx.ext.napoleon",
]


templates_path = ["_templates"]

exclude_patterns = ["_build", "_templates"]

html_theme = "sphinx_rtd_theme"

html_show_sphinx = False
html_show_sourcelink = True

autosummary_generate = True
autodoc_default_flags = ["members"]

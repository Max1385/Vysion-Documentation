import os
import sys
from datetime import date

sys.path.insert(0, os.path.abspath('../..'))

project = "Vysion"
copyright = f"{date.today().year}, Max1385"
author = "Max1385"

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
]

simplify_optional_unions = True
autodoc_member_order = "bysource"

intersphinx_mapping = {
    "py": ("https://docs.python.org/3", None),
    "aio": ("https://docs.aiohttp.org/en/stable/", None),
    "req": ("https://requests.readthedocs.io/en/latest/", None),
    "dc": ("https://docs.pycord.dev/en/master/", None),
    "dpy": ("https://discordpy.readthedocs.io/en/stable/", None),
    "sql": ("https://aiosqlite.omnilib.dev/en/stable/", None),
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "furo"
html_static_path = ["_static"]

html_logo = "_static/vysion.png"
html_favicon = "_static/vysion1.ico"

napoleon_numpy_docstring = True

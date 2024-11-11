# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'OCEAN Lab Manual'
copyright = '2024, Ramone Agard, Joey Scanga'
author = 'Ramone Agard, Joey Scanga'
release = '0.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "OCEAN_circle_colormatch.png"
html_context = {
    "display_github": True,
    "github_user": "washu-seal2",
    "github_repo": "OceanLabDocs",
    "github_version": "main",
    "conf_py_path": "/source/"
}

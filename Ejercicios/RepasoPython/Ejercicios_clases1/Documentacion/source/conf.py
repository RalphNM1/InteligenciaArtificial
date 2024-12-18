# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os 
import sys


project = 'Ejercicio Gestión de Hospital'
copyright = '2024, Ralphy Núñez Mercado'
author = 'Ralphy Núñez Mercado'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


sys.path.insert(0, os.path.abspath("../.."))
sys.setrecursionlimit(1500)

extensions = [ 
"sphinx.ext.autodoc", 
"sphinx.ext.todo", 
"sphinx.ext.viewcode",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output


# Activamos que incluya los TODO
todo_include_todos = True

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os 
import sys
from pathlib import Path


project = 'Ejercicio Gestión de Hospital'
copyright = '2024, Ralphy Núñez Mercado'
author = 'Ralphy Núñez Mercado'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


sys.path.insert(0, os.path.abspath("../../Modelo"))

try:
    import Ejercicios.RepasoPython.Ejercicios_clases1.Modelo.Ejercicios_clases1 as Ejercicios_clases1
    print("El módulo Ejercicios_clases1 fue importado correctamente.")
except ModuleNotFoundError as e:
    print(f"Error al importar el módulo: {e}")

#sys.path.append(str(Path('Modelo').resolve()))
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

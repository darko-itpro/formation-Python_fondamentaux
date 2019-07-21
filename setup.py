#!/usr/bin/env python

"""
Exemple de *build script* pour setuptools.

Ce script contient le *minimum* nécessaire pour créer une archive déployable. Ce
projet contient les packages inclus dans `training`, les autres sont considérés
comme des ressources de développement.

Pour créer une archive, exécuter à la racine::

    python setup.py sdist bdist_wheel

L'archive tar.gz créée pourra être installée par la commande::

    python -m pip install dist/training-python-dad3zero-1.0.0.tar.gz

.. seealse::

   `Python Packaging user guide <https://packaging.python.org/>`_
      Documentation sur la création d'archives. La documentation est orientée
      installation sur le Python Package index.
"""

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="training-python-darko-itpro",
    version="1.0.0",
    author="Darko Stankovski",
    author_email="darko.itpro@gmail.com",
    description="A basic package example",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darko-itpro/training-python",
    install_requires=['bottle>=0.12.16', 'Flask>=1.0.2'],
    packages=setuptools.find_packages(include=('training', 'training.*',)),
)
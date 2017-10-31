#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Ceci est un module qui ajoute le répertoire parent à sys.path afin que le projet
soit accessible par les notebooks.
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path().resolve().parent))

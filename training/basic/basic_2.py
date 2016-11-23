#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from builtins import input

"""
Sujet
-----

Saisir un nom et un âge en utilisant l'instruction input() puis affichez-les. 

Refaites l'exercice en transtypant la saisie
"""

nom = input("Votre nom ? ")
age = input("Votre age ? ")
print("Vous vous appelez {} et vous avez {} ans (raw input)".format(nom, age))

nom = str(input("Votre nom ? "))
age = int(input("Votre age ? "))
print("Vous vous appelez {} et vous avez {} ans (raw input bonne pratique)"\
    .format(nom, age))

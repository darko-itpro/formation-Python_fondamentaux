#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from builtins import input

"""
Sujet
-----

- Saisir deux nombres, comparez les pour afficher le plus petit

- Refaire l'exercice avec l'instruction ternaire

"""

val1 = int(input("Saisisez une valeur "))
val2 = int(input("Saisisez une autre valeur "))

if val1 > val2:
    minVal = val2
elif val2 > val1:
    minVal = val1
else:
    minVal = None

if minVal:
    print("{} est la plus petite valeur (structure if)".format(minVal))
else:
    print("Vous avez saisi la même valeur")

val1 = int(input("Saisisez une valeur "))
val2 = int(input("Saisisez une autre valeur "))

print("{} est la plus petite valeur (structure ternaire)"\
    .format(val1 if val1 < val2 else val2))

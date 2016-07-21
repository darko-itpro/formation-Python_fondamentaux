#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sujet
-----

Saisir un nom et un âge en utilisant l'instruction input() puis affichez-les. 

Refaire la saisie du nom avec l'instruction raw_input() et afficher le résultat 

Refaites l'exercice en transtypant la saisie
"""

nom = input("Votre nom ? ")
age = input("Votre age ? ")
print "Vous vous appelez {} et vous avez {} ans (input)".format(nom, age)

nom = raw_input("Votre nom ? ")
age = raw_input("Votre age ? ")
print "Vous vous appelez {} et vous avez {} ans (raw input)".format(nom, age)

nom = str(raw_input("Votre nom ? "))
age = int(raw_input("Votre age ? "))
print "Vous vous appelez {} et vous avez {} ans (raw input bonne pratique)"\
    .format(nom, age)

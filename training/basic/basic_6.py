#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""
    Sujet
    -----

    Initialisez deux entiers a = 0 et b = 10

    - Écrire une boucle affichant et incrémentant la valeur de a tant qu'elle
    reste inférieure à celle de b
    - Écrire une autre boucle décrémentant la valeur de b et affichant sa valeur
    si elle est impaire tant que b n'est pas nul.
"""

a = 0
b = 10

print ("Exo sur A")
while a < b:
    print (a)
    a += 1

print ("Exo sur B")
while b > 0:
    b -= 1
    if b % 2:
        print (b)

valeur_bornee = int(raw_input("Saisissez une valeur "))

if valeur_bornee in range(1, 11):
    print ("Vous avez saisi {}".format(valeur_bornee))
else:
    print ("Valeur en dehors des bornes")

ma_chaine = "hello world"

for char in ma_chaine:
    print (char)

ma_liste = ["Python", "Java", "Swift"]

for lang in ma_liste:
    print (lang)
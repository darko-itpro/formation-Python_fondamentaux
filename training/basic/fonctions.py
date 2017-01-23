#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Compteur de mots
    ^^^^^^^^^^^^^^^^

    Écrire une fonction compteur_mots acceptant une chaine de caractères en
    argument et qui renvoie un dictionnaire contenant la fréquence de tous les
    mots de la chaîne.

"""

from __future__ import print_function


def compteur_mots(chaine):
    frequence = {}
    for mot in chaine.split():
        if mot in frequence:
            frequence[mot] += 1

        else:
            frequence[mot] = 1

    tous_mots = frequence.keys()
    tous_mots.sort()
    for mot in tous_mots:
        print ("{} : {}".format(mot, frequence[mot]))


def compteur_mots_bis(chaine):
    frequence = {}
    for mot in chaine.split():
        frequence[mot] = frequence.get(mot, 0) + 1

    tous_mots = frequence.keys()
    tous_mots.sort()
    for mot in tous_mots:
        print("{} : {}".format(mot, frequence[mot]))


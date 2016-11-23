#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Sujets
    ------

    Ce module contient plusieurs sujets.

    Écrire une fonction table qui simule une table de multiplication.
    Cette fonction accepte 4 paramètre : base (la constante de multiplication),
    debut, fin, inc (pas d'avancement dans les nombres). La fonction doit
    afficher la table des bases de début à fin de inc en inc.

    Écrire une fonction compteur_mots acceptant une chaine de caractères en
    argument et qui renvoie un dictionnaire contenant la fréquence de tous les
    mots de la chaîne.

    Implémentez une pile LIFO avec une liste. Vous devez avoir 3 fonctions :
    * pile : Crée une pile à partir d'une suite de variables passées en paramètre
    * empile : ajoute un élément à la pile
    * dépile : retire le dernier élément ajouté
"""

from __future__ import print_function


def table(base, debut=0, fin=10, inc=1):

    print("Ma table")
    print("{:2} : {}"
          .format(base, [base * i for i in range(debut, fin + 1, inc)]))


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
        print ("{} : {}".format(mot, frequence[mot]))

pile_lifo = []


def pile(*args):
    global pile_lifo
    pile_lifo = list(args)


def empile(element):
    pile_lifo.append(element)


def depile():
    return pile_lifo.pop()


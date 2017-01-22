#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
    Implémentez une pile LIFO avec une liste. Vous devez avoir 3 fonctions :

    * pile : Crée une pile à partir d'une suite de variables passées en paramètre
    * empile : ajoute un élément à la pile
    * dépile : retire le dernier élément ajouté

"""

pile_lifo = []


def pile(*args):
    global pile_lifo
    pile_lifo = list(args)


def empile(element):
    pile_lifo.append(element)


def depile():
    return pile_lifo.pop()


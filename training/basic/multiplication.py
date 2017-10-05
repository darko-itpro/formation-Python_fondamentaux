#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
    Tables de multiplication
    ^^^^^^^^^^^^^^^^^^^^^^^^

    #. Ecrire une fonction qui affiche une table de multiplication de la valeur
       passée en paramètre sous la forme suivante (pour la table de 4)::

          4 |   8 |  12 |  16 |  20 |  24 |  28 |  32 |  36 |  40

    #. La fonction table multiplication doit avoir un paramètre optionnel
       **multiplicateur_max** qui est par défaut à 10.

    #. Ecrire une fonction qui à l'aide de la fonction précédente affiche la
       table de Pythagore avec le format suivant::

        ---------------------------------------------------------
          1 |   2 |   3 |   4 |   5 |   6 |   7 |   8 |   9 |  10
          2 |   4 |   6 |   8 |  10 |  12 |  14 |  16 |  18 |  20
          3 |   6 |   9 |  12 |  15 |  18 |  21 |  24 |  27 |  30
          4 |   8 |  12 |  16 |  20 |  24 |  28 |  32 |  36 |  40
          5 |  10 |  15 |  20 |  25 |  30 |  35 |  40 |  45 |  50
          6 |  12 |  18 |  24 |  30 |  36 |  42 |  48 |  54 |  60
          7 |  14 |  21 |  28 |  35 |  42 |  49 |  56 |  63 |  70
          8 |  16 |  24 |  32 |  40 |  48 |  56 |  64 |  72 |  80
          9 |  18 |  27 |  36 |  45 |  54 |  63 |  72 |  81 |  90
         10 |  20 |  30 |  40 |  50 |  60 |  70 |  80 |  90 | 100
        ---------------------------------------------------------

"""


def multiplication(value, max=10):
    for i in range(1, max):
        print("{:3}".format(value * i), end=" | ")
    print("{:3}".format(value * max))


def table_pythagore(max=10):
    print(("------" * max)[:-3])
    for i in range(1, max + 1):
        multiplication(i, max)
    print(("------" * max)[:-3])

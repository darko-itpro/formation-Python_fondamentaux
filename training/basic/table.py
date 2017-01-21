#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""
    Sujet
    -----

    Ecrire une fonction qui affiche la table de multiplication de la valeur passée en paramètre. Des paramètres *debut*,
    *fin* et *pas* peuvent être proposés optionnellement.

"""


def table(base, start=0, end=10, step=1):

    print("Ma table")
    print("{:2} : {}"
          .format(base, [base * i for i in range(start, end + 1, step)]))

if __name__ == "__main__":
    table(10)

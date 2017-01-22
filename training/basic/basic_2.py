#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Manipulation intéractive
    ^^^^^^^^^^^^^^^^^^^^^^^^

    #. Demander le nom et l’âge puis affichez-les ( exemple : Yoda a 800 ans )

    #. On souhaite écrire un programme de répartition d’addition. Pour cela, le programme doit demander le nombre de
       personnes et le total. Une fois le programme écrit, testez:

       * la répartition d’une addition de 47,90 € à 5.
       * la répartition d’une addition de 19 € à 3.
"""

from __future__ import print_function
from builtins import input

if __name__ == '__main__':
    name = str(input("Votre nom ? "))
    age = int(input("Votre age ? "))
    print("Vous vous appelez {} et vous avez {} ans"
          .format(name, age))

    n_people = int(input("Combien personnes ? "))
    value = float(input("Quelle somme ? "))
    print("Chacun paye {:.2f} €".format(value / n_people))

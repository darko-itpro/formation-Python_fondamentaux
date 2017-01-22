#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Manipulation simple
    ^^^^^^^^^^^^^^^^^^^

    #. Affectez les valeurs 6.892 et 19.7 aux variables temps et distance.

       * Calculez et affichez la valeur de la vitesse (m/s).
       * Améliorez l'affichage en imposant deux chiffres après le point décimal

    #. On partage à trois l'addition de 47,90 €, combien chacun doit payer ?

    #. On partage à deux l'addition de 19 €, combien chacun doit payer ?

"""

from __future__ import print_function

if __name__ == '__main__':
    temps = 6.892
    distance = 19.7

    print("Vitesse : {} m/s".format(distance / temps))
    print("Vitesse : {:.2f} m/s".format(distance / temps))

    print("Chacun paye : {}".format(47.90/3))
    print("Chacun paye : {}".format(19/2))

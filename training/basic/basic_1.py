#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""
Sujet
-----

- Affectez les valeurs 6.892 et 19.7 aux variables temps et distance. 

- Calculez et affichez la valeur de la vitesse (m/s) 

- Améliorez l'affichage en imposant deux chiffres après le point décimal

"""

temps = 6.892
distance = 19.7

print("Vitesse : {} m/s".format(distance/temps))
print("Vitesse : {:.2f} m/s".format(distance/temps))

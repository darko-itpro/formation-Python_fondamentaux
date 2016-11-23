#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from builtins import input

"""
    Sujet
    -----

    On désire sécuriser une enceinte pressurisée.

    On fixe une pression seuil P_LIMIT=3.5 et le volume est fixe a VOLUME=7.41.

    On demande de saisir la pression courante

    Le script doit simuler le comportement suivant :
    - Si la pression est le double de la pression seuil : arrêt immédiat.
    - Si la pression est supperieur a la pression : demander
    de diminuer la temperature
    - Si la pression est inferrieure a 1 : demander d'augmenter la temperature
    - Sinon, déclarer que tout va bien.

    Note : cette version boucle la question tant qu'il n'y a pas d'arrêt ou que
    tout va bien.
"""

P_LIMIT = 3.5
VOLUME = 7.41

while True:
    pression_actuel = float(input("Quel est la pression actuelle ?"))

    if pression_actuel > P_LIMIT * 2:
        print ("Arrêt de l'enceinte !!!")
        break
    elif pression_actuel > P_LIMIT:
        print ("Diminuez temperature")
    elif pression_actuel < 1:
        print ("Augmentez temperature")
    else:
        print ("Tout va bien…")
        break

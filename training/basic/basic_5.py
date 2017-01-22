#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Conditions multiples
    ^^^^^^^^^^^^^^^^^^^^

    On désire sécuriser une enceinte pressurisée. On fixe une pression seuil **P_LIMIT=3.5** et le volume est fixe a
    **VOLUME=7.41**.

    Le script doit simuler le comportement suivant :

    * Si la pression est supérieure au double du seuils : arrêt immédiat.
    * Si la pression est supérieure à la pression seuil : demander de diminuer la température
    * Si la pression est inférieur à 1 : demander d'augmenter la température
    * Sinon, déclarer que tout va bien.

    #. Écrivez le script
    #. Améliorez le script en indiquant de quelle valeur la température doit être modifiée. Rappel de thermodynamique :
       PV = nRT simplifié ici par **PV = T**.
    #. Incluez ce script dans une boucle qui répète la question tant que soit la situation soit rétablie soit l'enceinte
       arrêtée.

"""

from __future__ import print_function
from builtins import input

if __name__ == "__main__":
    P_LIMIT = 3.5
    VOLUME = 7.41

    while True:
        pression_actuel = float(input("Quel est la pression actuelle ? "))

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

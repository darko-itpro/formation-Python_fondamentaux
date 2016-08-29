#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

"""
    Sujet
    -----

    On désire sécuriser une enceinte pressurisée.

    On fixe une pression seuil p_seuil=3.5 et un volume seuil v_seuil=7.41.

    On demande de saisir la pression et le volume courant de l'enceinte.

    Le script doit simuler le comportement suivant :
    - Si le volume et la pression sont supérieurs aux seuils : arrêt immédiat.
    - Si seul la pression est supérieure à la pression seuil : demander
    d'augmenter le volume.
    - Si seul le volume est supérieure au volume seuil : demander de diminuer
    le volume.
    - Sinon, déclarer que tout va bien.

    Note : cette version boucle la question tant qu'il n'y a pas d'arrêt ou que
    tout va bien.
"""

PRESSION_SEUIL = 3.5
VOLUME_SEUIL = 7.41

while True:
    pression_actuel = float(raw_input("Quel est la pression actuelle ?"))
    volume_actuel = float(raw_input("Quel est le volume actuel ?"))

    if pression_actuel > PRESSION_SEUIL and volume_actuel > VOLUME_SEUIL:
        print ("Arrêt de l'enceinte !!!")
        break
    elif pression_actuel > PRESSION_SEUIL:
        print ("Augmentez le volume")
    elif volume_actuel > VOLUME_SEUIL:
        print ("Diminuez le volume")
    else:
        print ("Tout va bien…")
        break

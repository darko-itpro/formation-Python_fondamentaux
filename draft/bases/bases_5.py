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

    #. Écrivez le script et testez le avec différentes valeurs de pression.
    #. Améliorez le script en indiquant de quelle valeur la température doit être modifiée. Rappel de thermodynamique :
       PV = nRT simplifié ici par **PV = T**.
    #. Incluez ce script dans une boucle qui demande à l'utilisateur de saisir la pression tant que la situation n'est
       pas rétablie ou que l'enceinte n'est pas arrêtée.
    #. Modifiez l'exercice en demandant la temperature

"""

P_LIMIT = 3.5
VOLUME = 7.41

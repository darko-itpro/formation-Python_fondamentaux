#!/usr/bin/env python

"""
Module *solution* de l'exercices "quel est la valeur la plus élevée de
montants".


L'exéction de ce module est supposé à la racine du projet pour le chemin vers le
fichier de données.
"""
import os.path

FILE_NAME = "assets/comptage-voyageurs-trains-transilien.csv"

if not os.path.exists(FILE_NAME):
    print('Attention, exécutez ce module à la racine du projet !')
    import sys
    sys.exit(1)

with open(FILE_NAME) as SNCF_FILE:

    SNCF_FILE.readline()

    max_montants = 0
    station = None

    for line in SNCF_FILE:
        line_data = line.split(';')
        montants = int(line_data[-1])
        if montants > max_montants:
            max_montants = montants
            station = line_data[0]

    print('Max', max_montants, station)

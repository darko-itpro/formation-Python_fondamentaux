#!/usr/bin/env python 

import os.path

FILE_NAME = "assets/comptage-voyageurs-trains-transilien.csv"


def load_counting(file_path=FILE_NAME):

    if not os.path.exists(file_path):
        print('Attention, exécutez ce module à la racine du projet !')
        import sys
        sys.exit(1)

    with open(file_path) as SNCF_FILE:

        SNCF_FILE.readline()

        for line in SNCF_FILE:
            line_data = line.split(';')
            # Nom gare;Code gare;Type de jour;Date de comptage;Ligne;Tranche_horaire;Montants

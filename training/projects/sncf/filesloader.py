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


def load_stations_idf(file_path="../../../assets/SNCF/sncf-gares-et-arrets-transilien-ile-de-france.csv"):
    """
    Générateur pour l'extraction des informations de gares IDF.

    :param file_path: Chemin vers le fichier
    :return: Pour chaque gare, retourne un tuple (libellé, nom, numéro INSEE,
    adresse, ville, navigo). Navigo représente la zone Navigo.
    """

    with open(file_path) as stations_file:
        stations_file.readline()

        for line in stations_file:
            data = line.split(';')
            libelle = data[3]
            name = data[6]
            address = data[7]
            INSEE_number = data[8]
            city = data[9]
            navigo = data[-2]

            yield libelle, name, INSEE_number, address, city, navigo


if __name__ == "__main__":
    for data in load_stations_idf():
        if int(float(data[-1])) == 1:
            print(data)

"""
Démonstration de la différence de parsing basique entre l'usage du module csv ou le parsing "à la main".
"""

import csv

file_path = "../../assets/ministere_culture/frequentation-des-musees-de-france.csv"


def open_csv(path):
    """
    Affiche chaque ligne du fichier csv à l'aide du module csv

    :param path: chemin vers le fichier à parser
    """
    with open(path) as museum_file:
        csvreader = csv.reader(museum_file, delimiter=';')
        for row in csvreader:
            print(row)


def open_file(path):
    """
    Affiche chaque ligne du fichier csv avec un traitement "manuel"

    :param path: chemin vers le fichier à parser
    """

    with open(path) as museum_file:
        for line in museum_file:
            print(line.split(";"))


def open_dict_csv(path):
    """
    Affiche chaque ligne du fichier csv à l'aide du module csv sous forme d'un dictionnaire pour chaque ligne. Les clefs
    sont définies par l'en-tête.

    :param path: chemin vers le fichier à parser
    """
    with open(path) as museum_file:
        csvreader = csv.DictReader(museum_file, delimiter=';')
        for row in csvreader:
            print(row)

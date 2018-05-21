#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ce module contient les outils pour charger les données média à partir de
fichiers.
"""

import re
import os

SERIES_RE = re.compile("-s([0-9]{2})e([0-9]{2})-")

SERIES_FULL_NAME = "Silicon_Valley-s01e03-Articles_Of_Incorporation.avi"


def get_series_value_from_file(filename):
    """
    Retourne les données sur un épisode. Les valeurs sont :
    * Nom de la série
    * Numéro de la saison
    * Numéro de l'épisode
    * Titre de l'épisode
    * Extension du fichier

    :param filename: nom du fichier duquel extraire les données
    :return: une liste de chaines de caractères.
    :return type: list
    """
    series_file_name, series_ext = os.path.splitext(filename)

    series_match = SERIES_RE.search(series_file_name)

    if series_match:
        return series_file_name[:series_match.start()].replace('_', ' '),\
               series_match.group(1),\
               series_match.group(2),\
               series_file_name[series_match.end():].replace('_', ' '),\
               series_ext


def open_file(filepath):
    """
    Fonction spécifique aux exercices pour charger les noms de fichiers à partir
    d'un fichier.

    :param filepath: Chemin vers le fichier contenant les noms de fichiers épisodes
    :return: Une liste de tuples (titre série, numéro série, numéro épisode, titre épisode)
    """
    if os.path.exists(filepath):
        media_file = open(filepath, 'r')
        media_data = [get_series_value_from_file(media[:-1])
                      for media in media_file]
        media_file.close()

        return media_data
    else:
        return None


if __name__ == '__main__':

    import argparse

    PARSER = argparse.ArgumentParser(description='')
    PARSER.add_argument("-f", "--file", help="Path to the file to parse",
                        type=str, action="store")

    ARGS = PARSER.parse_args()

    if ARGS.file:
        for media in open_file(ARGS.file):
            print(media)
    else:
        print(get_series_value_from_file(SERIES_FULL_NAME))

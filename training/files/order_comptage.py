#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Module illustrant la manipulation d'un fichier à l'aide d'un objet connecteur
dédié.
"""


class ComptageReader:
    """
    Classe dédiée à la manipulation d'un fichier de comptage SNCF.
    """

    def __init__(self, path):
        try:
            self._sncf_file = open(path, "r")
        except IOError:
            raise ValueError('Reader can\'t be created')

    def max_count(self, specific_station=None):
        """
        Retourne le nombre maximum de montants de l'analyse.

        :param specific_station: le nom d'une gare ou None. Si None, le résultat
        sera le max de tout le fichier, sinon pour la gare donnée.
        :return: le maximum de montants et le nom de la gare
        """
        self._sncf_file.seek(0)

        max_passengers = 0
        station = specific_station if specific_station else ''

        self._sncf_file.readline()

        for line in self._sncf_file:
            line_infos = line.split(';')
            if not specific_station or specific_station == line_infos[0]:
                if int(line_infos[-1]) > max_passengers:
                    max_passengers = int(line_infos[-1])
                    station = line_infos[0]

        return max_passengers, station

    def get_stations(self):
        """
        Permet d'obtenir la liste des gares

        :return: Une liste ordonnée alphabétiquement des gares.
        """
        self._sncf_file.seek(0)

        stations = set()

        self._sncf_file.readline()

        for line in self._sncf_file:
            stations.add(line.split(';')[0])

        return sorted(stations)

    def count_stations(self):
        """
        Compte le nombre d'occurence de chaque gare.

        :return: Un dictionnaire avec pour clef un nom de gare et en valeur le
        nombre d'occurences de celle-ci dans le fichier.
        """
        self._sncf_file.seek(0)

        self._sncf_file.readline()

        stations = {}

        for line_info in self._sncf_file:
            station = line_info.split(';')[0]
            stations[station] = stations.get(station, 0) + 1

        return stations

    def __del__(self):
        """
        Avant la destruction de cet objet, s'assure de la fermeture du fichier.

        :return:
        """
        try:
            if not self._sncf_file.closed:
                self._sncf_file.close()
        except AttributeError:
            # Cette exception sera levée si l'attribut n'existe pas ce qui se
            # prodiura le plus souvent si un mauvais chemin est fourni. Dans
            # notre cas, on ne fait rien.
            pass


class DocumentWriter:
    """
    Objet permétant de contrôler l'écriture dans un fichier.
    """
    def __init__(self, path):
        try:
            self._file = open(path, 'x')
        except IOError:
            raise ValueError('Writer can\'t be created')

    def write(self, content):
        """
        Écrit le paramètre dans le fichier

        :param content: Une chaine de caractères à écrire.
        :return:
        """
        self._file.write(str(content))

    def __del__(self):
        """
        Avant la destruction de cet objet, s'assure de la fermeture du fichier.

        :return:
        """
        try:
            if not self._file.closed:
                self._file.close()
        except AttributeError:
            # Cette exception sera levée si l'attribut n'existe pas ce qui se
            # prodiura le plus souvent si un mauvais chemin est fourni. Dans
            # notre cas, on ne fait rien.
            pass


if __name__ == "__main__":

    # Les instructions suivantes illustrent l'usage de ces deux classes.

    import argparse

    parser = argparse.ArgumentParser(
        description="Pour illustrer l'usage des classes contenues dans ce module,"
                    " il est nécessaire de fournir le chemin vers le fichier de "
                    "comptage."
    )

    parser.add_argument('path', help="Path to the file", type=str)

    args = parser.parse_args()

    try:
        sncf_reader = ComptageReader(args.path)
    except ValueError:
        print("Arrêt car mauvais chemin passé en paramètre")
        exit(1)

    max_analysis = sncf_reader.max_count('Argenteuil')
    print("Max montants : {} à {}".format(max_analysis[0], max_analysis[1]))

    max_analysis = sncf_reader.max_count('')
    print("Max montants : {} à {}".format(max_analysis[0], max_analysis[1]))

    stations_dict = sncf_reader.count_stations()
    for station, count in sorted(stations_dict.items(), key=lambda x: x[0]):
        print("{:4} {}".format(count, station))


    print(sncf_reader.get_stations())

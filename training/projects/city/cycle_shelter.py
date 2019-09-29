#!/usr/bin/env python

from typing import Optional, Callable, List
import geopy.distance


class Geopoint:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    @property
    def coordinates(self):
        return self.latitude, self.longitude


class CycleStation:
    def __init__(self, identifier, name, capacity: int, location: Geopoint):
        self.identifier = identifier
        self.name = name
        self.capacity = int(capacity)
        self.location = location

        if self.capacity < 0:
            raise ValueError(f"Inconsistent capacity {self.capacity}")

    def __str__(self):
        return "{} {}".format(self.name, self.capacity)

    def __repr__(self):
        return self.__str__()

    def distance_to(self, other):
        return geopy.distance.distance(self.location.coordinates,
                                       other.location.coordinates).km


def velib_station_processor(data: List[str]) -> CycleStation:
    """
    Processeur d'une liste, les données attendues sont :
    - indice 0 : identifiant de la station
    - indice 1 : nom de la station
    - indice 2 : capacité de la station

    :param data: une liste de chaines de caractères correspondant aux données
    décrites ci-dessus.
    :return: Une station.
    """
    station = CycleStation(data[0], data[1], data[2],
                           Geopoint(data[3], data[4]))
    return station


def file_loader(path: str, processor: Optional[Callable] = None,
                separator: str = ";"):
    """
    Ouvre un fichier type csv et traite ses données en fonction d'un processeur

    :param path: chemin vers le fichier à traiter
    :param processor: fonction prenant une liste en paramètre afin d'extraire
    des informations. Retourne une donnée qui sera ajoutée à la liste
    retrournée.
    :param separator: caractère (ou chaine de caractères) séparateurs des
    données. Par défaut, c'est le point-virgule (;).
    :return:
    """
    with open(path) as data_file:
        data_file.readline()

        data = []

        for line in data_file:
            if processor:
                data.append(processor(line.split(separator)))
            else:
                data.append(line.split(separator))

        return data

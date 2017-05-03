#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Sujets
    ------

    Définir une classe Position avec un constructeur fournissant les coordonnées
    par défaut d'une position (exemple : x=0, y=0)

    Instanciez un objet et affichez les paramètres

    Enrichissez la classe en surchargeant la méthode d'affichage et d'addition
    de deux positions

    Instanciez deux positions et affichez leur somme
"""


class Position(object):
    """
    Position defines a position in space.
    """
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def coordinates(self):
        return self._x, self._y

    def __str__(self):
        return 'Point x:%d y:%d' % (self._x, self._y)

    def __add__(self, other):
        """
        L'addition d'une Position avec une autre instance du même type retourne
        un nouvel objet dont les coordonnées sont les additions des deux objets
        additionnés. Si cette addition est avec un entier ou float, celui-ci est
        additionné aux coordonnées.

        :param other:
        :return:
        """
        if hasattr(other, 'coordinates'):
            return Position(self._x + other.coordinates()[0],
                            self._y + other.coordinates()[1])
        else:
            return Position(self._x + other, self._y + other)


class Location(Position):
    """
    A Location is a uncertain position so it uses a radius for the error margin.
    """
    def __init__(self, x=0, y=0, radius=0):
        Position.__init__(self, x, y)
        self._radius = radius
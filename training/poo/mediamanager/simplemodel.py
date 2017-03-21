#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Ce module propose des définitions de classes similaires à mediamodel mais simplifiées
"""


class Episode:
    """
    Un épisode d'une série
    """
    def __init__(self, number, title):
        self._number = number
        self.title = title

    def number(self):
        return self._number

    def __lt__(self, other):
        """
        Methode surchargée pour permettre un tri naturel sur le numéro d'épisode.
        :param other: un autre Episode ou un objet possédant une méthode number()
        :return: True si cet objet est inférieur, sinon False.
        """
        return self._number < other.number()


class Season:
    """
    Une saison d'une série. Un objet de ce type est avant tout un container
    """
    def __init__(self, number):
        self._number = number
        self._episodes = []

    def number(self):
        return self._number

    def add(self, episode):
        self._episodes.append(episode)
        self._episodes.sort()

    def episodes(self):
        """
        Retourne une liste des épisodes sous forme d'une copie afin d'éviter les
        modifications involontaires.
        :return: Une copie de la liste des épisodes
        """
        return list(self._episodes)


class TvShow:
    def __init__(self, name):
        self.name = name
        self._seasons = []

    def add_episode(self, episode, season_number):
        for season in self._seasons:
            if season.number() == season_number:
                season.add(episode)
                break
        else:
            season = Season(season_number)
            season.add(episode)
            self._seasons.append(season)

    def seasons(self):
        return list(self._seasons)

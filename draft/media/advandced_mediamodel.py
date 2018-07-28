#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Ce module propose des définitions de classes similaires à mediamodel mais simplifiées
"""


class Episode:
    """
    Un épisode d'une série
    """
    def __init__(self, title, number, season=None):
        try:
            if not title or title.isspace():
                raise ValueError('Empty title')
        except AttributeError:
            raise ValueError('Title may not be a String')

        self._title = title
        self._number = int(number)
        self._season = int(season) if season else None

    def get_number(self):
        return self._number

    @property
    def title(self):
        return self._title

    @property
    def season(self):
        return self._season

    def __lt__(self, other):
        """
        Methode surchargée pour permettre un tri naturel sur le numéro d'épisode.
        :param other: un autre Episode ou un objet possédant une méthode number()
        :return: True si cet objet est inférieur, sinon False.
        """
        return self.number < other.number

    number = property(get_number)


class Season:
    """
    Une saison d'une série. Un objet de ce type est avant tout un container
    :param number: le numéro de la saison qui peut être 0 (en général pour
    ranger les épisoedes spéciaux) ou None.
    """
    def __init__(self, number):
        self._number = number
        self._episodes = []

    @property
    def number(self):
        return self._number

    def add(self, episode):
        for _episode in self._episodes:
            if _episode.number == episode.number:
                raise ValueError("Epsode exists")

        self._episodes.append(episode)
        self._episodes.sort()

    @property
    def episodes(self):
        """
        Retourne une liste des épisodes sous forme d'une copie afin d'éviter les
        modifications involontaires.
        :return: Une copie de la liste des épisodes
        """
        return list(self._episodes)


class TvShow:
    def __init__(self, name):
        self._name = name
        self._seasons = []

    def add_episode(self, title, number, season_number=None):
        for season in self._seasons:
            if season.number == season_number:
                season.add(Episode(title, number, season_number))
                break
        else:
            season = Season(season_number)
            season.add(Episode(title, number, season_number))
            self._seasons.append(season)

    def episodes(self):
        episodesl = list()
        for season in self._seasons:
            episodesl.extend(season.episodes)

        return episodesl

    def season(self, number):
        for season in self._seasons:
            if season.number == number:
                return season

    @property
    def name(self):
        return self._name

    @property
    def seasons(self):
        return list(self._seasons)

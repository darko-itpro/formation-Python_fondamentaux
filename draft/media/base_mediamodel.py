#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Mediamodel de base mettant en œuvre l'héritage pour les types Movie et Episode.
"""


class Media:
    """
    Classe générique pour un média.
    """
    def __init__(self, title, duration=None):
        try:
            if not title or title.isspace():
                raise ValueError('Empty title')
        except AttributeError:
            raise ValueError('Title must be a non-whitespace String')

        self._title = title
        self._duration = int(duration) if duration else None

    @property
    def title(self):
        return self._title

    @property
    def duration(self):
        return self._duration

    def hm_duration(self):
        """
        Human readable duration

        :return: la durée sous forme de tuple (heures, minutes)
        """
        if self._duration:
            return divmod(self._duration, 60)
        else:
            return None


class Episode(Media):
    def __init__(self, title, number, season=None, duration=None):
        Media.__init__(self, title, duration)
        self._number = int(number)
        self._season = int(season) if season else None

    def __eq__(self, other):
        return self.number == other.number and self.season == other.season

    @property
    def number(self):
        return self._number

    @property
    def season(self):
        return self._season


class TvShow(object):
    """
    Décrit une série télévisée

    :param name: Le nom de la série
    """
    def __init__(self, name):
        """
        Constructeur d'une série télévisée

        :param name: Le nom de la série
        """
        self._name = name
        self._episodes = []

    @property
    def name(self):
        return self._name

    def get_episodes(self, season_number=None):
        """
        Retourne une liste d'épisodes

        :param season_number: Numéro de la saison afin de retourner une liste
            d'épisodes filtrés sur cette saison.
        :type season_number: Int positif

        :return: Une liste d'épisodes
        """
        if season_number:
            return [episode
                    for episode in self._episodes
                    if episode.season == season_number]
        else:
            return list(self._episodes)

    def add_episode(self, title, number, season=None):
        """
        Ajoute un épisode à la saison à partir de ses informations de base.

        :param title: Titre de l'épisode
        :param number: Numéro de l'épisode dans la saison
        :type number: Int positif
        :param season: Saison de l'épisode
        :type season: Int positif
        """
        episode = Episode(title, number, season)

        if episode in self._episodes:
            raise ValueError('Episode exists')

        self._episodes.append(episode)


class Movie(Media):
    def __init__(self, title, duration=None, director=None):
        Media.__init__(self, title, duration)
        try:
            if director and director.isspace():
                raise ValueError('Director must be non-whitespaces')
        except AttributeError:
            raise ValueError('Director must be a string')

        self._director = director if director else None

    @property
    def director(self):
        return self._director

#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Mediamodel de base mettant en œuvre l'héritage pour les types Movie et Episode.

L'usage des property est décrit des deux manières, par décorateurs au sein de
Media et Movie, par la classe property dans la classe Episode.
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
        if self._duration:
            return divmod(self._duration, 60)
        else:
            return None


class Episode(Media):
    def __init__(self, title, number, season=None, duration=None):
        Media.__init__(self, title, duration)
        self._number = int(number)
        self._season = int(season) if season else None

    def _get_number(self):
        return self._number

    def _get_season(self):
        return self._season

    number = property(_get_number)
    season = property(_get_season)


class TvShow(object):
    def __init__(self, name):
        self._name = name
        self._episodes = []

    def _get_name(self):
        return self._name

    name = property(_get_name)

    def get_episodes(self, season_number=None):
        if season_number:
            return [episode
                    for episode in self._episodes
                    if episode.season == season_number]
        else:
            return list(self._episodes)

    def add_episode(self, title, number, season=None):
        for episode in self._episodes:
            if episode.number == number and episode.season == season:
                raise ValueError('Episode exists')

        self._episodes.append(Episode(title, number, season))


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

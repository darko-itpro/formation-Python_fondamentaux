#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module définissant les objets *métier* de la gestion d'une médiathèque.
"""


class TvShow:
    def __init__(self, name):
        self.name = name
        self._episodes = []

    @property
    def episodes(self):
        return self._episodes.copy()

    def add_episode(self, title, number, season_number):
        new_episode = Episode(title, number, season_number)
        if new_episode in self._episodes:
            raise ValueError("Episode [s{:02}e{:02}-{}]exists"
                             .format(season_number, number, title))

        self._episodes.append(new_episode)

    def get_episodes(self, season=None):
        if season is not None:
            season = int(season)
            return [episode
                    for episode in self.episodes
                    if episode.season_number == season]
        else:
            return self.episodes


class Episode:
    def __init__(self, title, number, season_number):
        self.title = title
        self.number = int(number)
        self.season_number = int(season_number)

    def __eq__(self, other):
        if not isinstance(other, Episode):
            return False
        else:
            return self.number == other.number \
                   and self.season_number == other.season_number

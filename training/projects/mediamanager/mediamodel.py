#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module définissant les objets *métier* de la gestion d'une médiathèque.
"""

import dataclasses as dc


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


@dc.dataclass(eq=False, frozen=True)
class Episode:
    title: str
    number: int
    season_number: int

    def __post_init__(self):
        """
        Méthode exécutée après l'initialisation chargée ici de vérifier la
        cohérence des données.
        """
        if self.number < 0:
            raise ValueError(f"Episode number should be positive "
                             f"({self.number})")

        if self.season_number < 0:
            raise ValueError(f"Episode season number should be positive "
                             f"({self.season_number})")

    def __eq__(self, other):
        """
        Le critère d'égalité entre deux épisodes se limite aux numéro d'épisode
        et numéro de saison.

        :param other: L'objet avec lequel self est comparé.
        :return: Vrai si le numéro d'épisode et numéro de saison sont égaux
        sinon faux. Les autres paramètres ne sont pas pris en compte.
        """
        if not isinstance(other, Episode):
            return False
        else:
            return (self.number, self.season_number) == (other.number,
                                                         other.season_number)

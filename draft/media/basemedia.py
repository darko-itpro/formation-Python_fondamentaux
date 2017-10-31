#!/usr/bin/env python 
# -*- coding: utf-8 -*-


class Episode(object):
    def __init__(self, title, number, season=None):
        try:
            if not title or title.isspace():
                raise ValueError('Empty title')
        except AttributeError:
            raise ValueError('Title may not be a String')

        self._title = title
        self._number = int(number)
        self._season = int(season) if season else None

    @property
    def title(self):
        return self._title

    @property
    def number(self):
        return self._number

    @property
    def season(self):
        return self._season


class TvShow(object):
    def __init__(self, name):
        self._name = name
        self._episodes = []

    @property
    def name(self):
        return self._name

    def episodes(self):
        return list(self._episodes)

    def add_episode(self, title, number, season=None):
        for episode in self._episodes:
            if episode.number == number and episode.season == season:
                raise ValueError('Episode exists')

        self._episodes.append(Episode(title, number, season))

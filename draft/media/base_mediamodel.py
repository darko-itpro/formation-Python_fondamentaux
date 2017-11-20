#!/usr/bin/env python 
# -*- coding: utf-8 -*-


class Episode(object):
    def __init__(self, title, number, season=None, duration=None):
        try:
            if not title or title.isspace():
                raise ValueError('Empty title')
        except AttributeError:
            raise ValueError('Title may not be a String')

        self._title = title
        self._number = int(number)
        self._season = int(season) if season else None
        self._duration = int(duration) if duration else None

    def _get_title(self):
        return self._title

    def _get_number(self):
        return self._number

    def _get_season(self):
        return self._season

    def _get_duration(self):
        return self._duration

    title = property(_get_title)
    number = property(_get_number)
    season = property(_get_season)
    duration = property(_get_duration)


class TvShow(object):
    def __init__(self, name):
        self._name = name
        self._episodes = []

    def _get_name(self):
        return self._name

    name = property(_get_name)

    def episodes(self):
        return list(self._episodes)

    def add_episode(self, title, number, season=None):
        for episode in self._episodes:
            if episode.number == number and episode.season == season:
                raise ValueError('Episode exists')

        self._episodes.append(Episode(title, number, season))

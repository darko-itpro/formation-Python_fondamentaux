#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from training.projects.mediamanager import mediamodel


class ManagedData:
    def __init__(self, seen):
        self.seen = bool(seen)


class ManagedMovie(mediamodel.Movie, ManagedData):
    def __init__(self, title, duration=None, year=None, director=None,
                 seen=False):
        mediamodel.Movie.__init__(self, title, duration, year, director)
        ManagedData.__init__(self, seen)


class ManagedEpisode(mediamodel.Episode, ManagedData):
    def __init__(self, title, number, duration=None, year=None, seen=False):
        mediamodel.Episode.__init__(self, title, number, duration, year)
        ManagedData.__init__(self, seen)
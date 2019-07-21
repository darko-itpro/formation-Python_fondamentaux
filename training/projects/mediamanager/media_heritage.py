#!/usr/bin/env python 

"""
Ce module est destiné à illustrer la mise en œuvre de l'héritage.

Ce module reprend la classe *Episode* du modèle média. Si nous définissions une classe
"""


class Media:
    def __init__(self, title, year:int=None, duration:int=None):
        self.title = title
        self.year = int(year) if year is not None else None
        self.duration = int(duration) if duration is not None else None

    def __eq__(self, other):
        if not isinstance(other, Episode):
            return False
        else:
            return (self.title, self.year, self.duration) == (other.title,
                                                              other.year,
                                                              other.duration)


class Movie(Media):
    def __init__(self, title, director, year:int=None, duration:int=None):
        super().__init__(title, year, duration)
        self.director = director


class Episode(Media):
    def __init__(self, title, number: int, season_number: int,
                 duration: int = None, year: int = None):

        super().__init__(title, year, duration)
        self.number = int(number)
        self.season_number = int(season_number)

        if self.number < 0:
            raise ValueError(f"Episode number should be positive "
                             f"({self.number})")

        if self.season_number < 0:
            raise ValueError(f"Episode season number should be positive "
                             f"({self.season_number})")

    def __eq__(self, other):
        if not isinstance(other, Episode):
            return False
        else:
            return (self.number, self.season_number) == (other.number,
                                                         other.season_number)
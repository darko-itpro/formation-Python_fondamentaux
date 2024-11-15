
class Episode:
    def __init__(self, title: str, number: int, season_number: int,
                 duration: int = None, year: int = None):
        self.title = title
        self.number = number
        self.season_number = season_number
        self.duration = duration
        self.year = year

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.number, self.season_number) == (other.number, other.season_number)


class TvShow:
    def __init__(self, name):
        self.name = name
        self._episodes = []

    @property
    def duration(self):
        return sum([episode.duration
                    for episode in self._episodes])

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

    @property
    def episodes(self):
        return self._episodes.copy()

    def add_episode(self, title, number, season_number, duration=None, year=None):
        episode = Episode(title, number, season_number, duration, year)
        if episode in self._episodes:
            raise ValueError('Duplicate episode')
        self._episodes.append(episode)

    def __str__(self):
        return f"Show {self.name} ({len(self._episodes)} episodes)"

    def __repr__(self):
        return f"TvShow({self.name})"

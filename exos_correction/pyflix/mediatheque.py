
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
    def __init__(self, name:str):
        self.name = name.title()
        self._episodes = []

    @property
    def duration(self):
        return sum([episode.duration for episode in self._episodes])

    @property
    def episodes(self):
        return self._episodes.copy()

    def add_episode(self, title:str, number:int, season_number:int, duration:int=None, year:int=None):
        new_episode = Episode(title, number, season_number, duration, year)
        if new_episode in self._episodes:
            raise ValueError(f"Duplicate episode {number}, {season_number}")

        self._episodes.append(new_episode)

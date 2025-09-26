
class Episode:
    def __init__(self, title: str, season_number: int, number: int,
                 duration: int = None, year: int = None):
        self.title = title
        self.number = number
        self.season_number = season_number
        self.duration = duration
        self.year = year

    def __eq__(self, other):
        return (self.number, self.season_number) == (other.number , other.season_number)


class TvShow:
    def __init__(self, name: str):
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
    def name(self, new_name: str):
        self._name = new_name.title()

    @property
    def episodes(self):
        return self._episodes.copy()

    @episodes.deleter
    def episodes(self):
        self._episodes.clear()

    def add_episode(self, title: str,
                    season_number: int,
                    number: int,
                    duration: int = None,
                    year: int = None):
        new_episode = Episode(title, season_number, number, duration, year)
        if new_episode in self._episodes:
            raise ValueError(f"Episode '{new_episode.title}' already exists")
        self._episodes.append(new_episode)


class DuplicateError(ValueError):
    pass


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

    def __str__(self):
        return f'Episode {self.title} s{self.season_number:02}e{self.number:02}'


class TvShow:
    def __init__(self, name:str):
        self.name = name
        self._episodes = []

    @classmethod
    def with_episodes(cls, name:str, episodes:list):
        show = cls(name)
        for episode in episodes:
            show.add_episode(*episode)

        return show

    @property
    def duration(self):
        return sum((episode.duration
                    for episode in self._episodes))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name:str):
        self._name = new_name.title()

    @property
    def episodes(self):
        return self._episodes.copy()

    def add_episode(self, title:str, number:int, season_number:int, duration:int=None, year:int=None):
        new_episode = Episode(title, number, season_number, duration, year)

        if new_episode in self._episodes:
            raise DuplicateError(f'Duplicate episode season {season_number} episode {number}')

        self._episodes.append(new_episode)

    def __str__(self):
        return f"Show '{self.name}', {len(self._episodes)} episode(s)"

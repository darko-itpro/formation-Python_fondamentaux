
class Episode:
    def __init__(self, title: str, season_number: int, number: int,
                 duration: int = None, year: int = None):
        self.title = title
        self.number = number
        self.season_number = season_number
        self.duration = duration
        self.year = year

    def __str__(self):
        return f'Episode "{self.title}", s{self.season_number:02}e{self.number:02}'

    def __repr__(self):
        return f'Episode({self.title}, {self.season_number}, {self.number}, {self.duration}, {self.year})'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return (self.number, self.season_number) == (other.number, other.season_number)


class TvShow:
    def __init__(self, title: str):
        self.name = title
        self._episodes = []

    @property
    def duration(self):
        return sum([episode.duration for episode in self._episodes])

    @property
    def episodes(self):
        return self._episodes.copy()

    def add_episode(self, title: str, season_number: int, number: int, duration: int = None, year: int = None):
        new_episode = Episode(title, season_number, number, duration, year)
        if new_episode in self._episodes:
            raise ValueError('Episode already exists')

        self._episodes.append(new_episode)


    def __str__(self):
        return f'TvShow "{self.name}"'


    def __repr__(self):
        class_name = type(self).__name__
        # or: class_name = self.__class__.__name__
        return f"{class_name}(name={self.name!r})"



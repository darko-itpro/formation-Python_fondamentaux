
class Episode:
    def __init__(self, title: str, number: int, season_number: int, duration: int = None, year: int = None):
        self.title = title
        self.number = number
        self.season_number = int(season_number)
        self.duration = int(duration) if duration is not None else None
        self.year = int(year) if year is not None else None

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return (self.number, self.season_number) == (other.number, other.season_number)

    def __lt__(self, other):
        if not isinstance(other, self.__class__):
            raise TypeError(f"'<' not supported between instances of '{self.__class__}' and '{other.__class__}'")

        return (self.season_number, self.number) < (other.season_number, other.number)

    def __str__(self):
        return f"Episode {self.title} s{self.season_number:02}e{self.number:02}"

    def __repr__(self):
        return f"Episode({self.title}, {self.number}, {self.season_number}, {self.duration}, {self.year})"


class TvShow:
    def __init__(self, name: str):
        self.name = name.title()
        self._episodes = []

    def add_episode(self, title: str, number: int, season_number: int, duration: int = None, year: int = None):
        new_episode = Episode(title, number, season_number, duration, year)
        if new_episode in self._episodes:
            raise ValueError(f"Duplicate episode s{season_number:02}e{number:02}")

        self._episodes.append(new_episode)

    @property
    def duration(self):
        return sum([episode.duration
                    for episode in self._episodes])

    @property
    def episodes(self):
        return self._episodes.copy()

    def __str__(self):
        return f"Tv Show {self.name} ({len(self._episodes)} episodes)"

    def __repr__(self):
        return f"TvShow({self.name})"

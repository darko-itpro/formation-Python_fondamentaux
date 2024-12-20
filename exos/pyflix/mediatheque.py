class Media:
    def __init__(self, title, year):
        self.title = title.title()
        self.year = year


class Episode(Media):
    def __init__(self, title: str, season_number: int, number: int,
                 duration: int = None, year: int = None):
        super().__init__(title, year)

        self.number = number
        self.season_number = season_number
        self.duration = duration


    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return (self.number, self.season_number) == (other.number, other.season_number)


class TvShow:
    def __init__(self, name):
        self.name = name
        self._episodes = []

    def __str__(self):
        return f"Show {self.name} ({len(self._episodes)} episodes)"

    @property
    def duration(self):
        return sum([episode.duration
                    for episode in self._episodes])

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name:str):
        self._name = new_name.title()

    @property
    def year(self):
        return self._episodes[0].year, self._episodes[-1].year

    @property
    def episodes(self):
        return self._episodes.copy()

    def add_episode(self, title: str, season_number: int, number: int,
                 duration: int = None, year: int = None):
        episode = Episode(title, season_number, number, duration, year)

        if episode in self._episodes:
            raise ValueError("Episode Exists")

        self._episodes.append(episode)

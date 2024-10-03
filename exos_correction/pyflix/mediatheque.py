
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
        self.name = name.title()
        self.episodes = []

    def add_episode(self, title:str, number:int, season_number:int, duration:int=None, year:int=None):
        new_episode = Episode(title, number, season_number, duration, year)

        if new_episode in self.episodes:
            raise ValueError('Duplicate episode')

        self.episodes.append(new_episode)

    def __str__(self):
        return f"Show '{self.name}', {len(self.episodes)} episode(s)"

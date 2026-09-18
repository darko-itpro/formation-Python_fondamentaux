
class Episode:
    def __init__(self, title: str, season_number: int, number: int,
                 duration: int = None, year: int = None):
        self.title = title
        self.number = number
        self.season_number = season_number
        self.duration = duration
        self.year = year

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False

        return self.season_number == other.season_number and self.number == other.number

class TvShow:
    def __init__(self, name:str):
        if name is None or not name.strip():
            raise ValueError("Name cannot be empty")

        self.name = name
        self.episodes = []


    def add_episode(self, title, season_number, number, duration, year):
        new_episode = Episode(title, season_number, number, duration, year)

        if new_episode in self.episodes:
            raise ValueError("Episode already exists")

        self.episodes.append(new_episode)



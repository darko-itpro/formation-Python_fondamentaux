
class Episode:
    def __init__(self, title: str, season_number: int, number: int,
                 duration: int = None, year: int = None):
        self.title = title
        self.number = number
        self.season_number = season_number
        self.duration = duration
        self.year = year

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return False

        return (self.number, self.season_number) == (other.number, other.season_number)


class TvShow:
    def __init__(self, name):
        self.name = name
        self.episodes = []

    def add_episode(self, title:str, season_number: int, number: int,
                    duration: int|None = None, year: int|None = None):
        episode = Episode(title, season_number, number, duration, year)
        if episode in self.episodes:
            raise ValueError(f"Episode {episode.title} already exists")
        self.episodes.append(episode)

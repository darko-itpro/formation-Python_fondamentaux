
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
        self.name = name
        self._episodes = []
        
    @property
    def duration(self):
        return sum([episode.duration for episode in self._episodes])
        
    @property
    def episodes(self):
        return self._episodes.copy()

    def add_episode(self, title:str, season_number:int, number, duration:int|None = None, year:int|None = None):
        episode = Episode(title, season_number, number, duration, year)
        if episode in self._episodes:
            raise ValueError(f"Episode s{episode.season_number}e{episode.number} exists")
        
        self._episodes.append(episode)


class Episode:
    def __init__(self, title: str, season_number: int, number: int,
                 duration: int = None, year: int = None):
        self.title = title
        self.number = number
        self.season_number = season_number
        self.duration = duration
        self.year = year


class TvShow:
    def __init__(self, name: str):
        self.name = name
        self.episodes = []

    def add_episode(self, title: str,
                    season_number: int,
                    number: int,
                    duration: int = None,
                    year: int = None):
        self.episodes.append(Episode(title, season_number, number, duration, year))

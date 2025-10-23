
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

        return (self.number, self.season_number) == (other.number, other.season_number)

    def __str__(self):
        return f"{self.title} : s{self.season_number:02}e{self.number:02}"


class EpisodesIterator:
    def __init__(self, episodes:list[Episode]):
        self._episodes = episodes.copy()

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self._episodes.pop(0)
        except IndexError:
            raise StopIteration()


class TvShow:
    def __init__(self, new_name:str):
        self.name = new_name
        self._episodes = []

    @classmethod
    def with_episodes(cls, name, episodes):
        show = cls(name)
        for episode_data in episodes:
            show.add_episode(*episode_data)

        return show


    def __iter__(self):
        return EpisodesIterator(self.episodes)
        #return (episode for episode in self._episodes)

    @property
    def duration(self):
        return sum((episode.duration for episode in self._episodes))

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name:str):
        self._name = new_name.title()

    @property
    def episodes(self):
        return self._episodes.copy()

    def __len__(self):
        return len(self._episodes)

    def __contains__(self, item):
        return item in self._episodes

    def add_episode(self, title:str, season_number:int, number:int,
                    duration:int = None, year:int = None):
        new_episode = Episode(title, season_number, number, duration, year)

        if new_episode in self._episodes:
            raise ValueError("Episode exists")

        self._episodes.append(new_episode)

    def __str__(self):
        return f"{self._name} ({len(self._episodes)} episodes)"

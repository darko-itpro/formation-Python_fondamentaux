from pprint import pprint
import pyflix.datasource as ds

from exos.base import media_utils as mu


def find_first_unseen_episode(season:list[dict]):
    for index, episode in enumerate(season):
        if not mu.is_viewed(episode):
            return index, episode

    return tuple()


def get_playlist(season:list[dict]):
    item = find_first_unseen_episode(season)

    return season[item[0]:] if item else []

if __name__ == "__main__":
    bbt_s12 = ds.get_season('The Big Bang Theory', "Sheldon Cooper")



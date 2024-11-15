from pprint import pprint

import pyflix.datasource as ds
import exos_correction.base.episode_utils as eu
from exos.base.exo_02_01 import episode


def get_playlist_from(season:list) -> list:
    for index, episode in enumerate(season):
        if not eu.is_viewed(episode):
            return season[index:]

    return []


bbt_s12 = ds.get_season('The Big Bang Theory', "Sheldon Cooper")

playlist = get_playlist_from(bbt_s12)

remaining_time = 120

while remaining_time >= playlist[0]['duration']:
    episode = playlist.pop(0)
    print(episode['title'])
    remaining_time -= episode['duration']
    episode['viewed'] = True


print(remaining_time)
pprint(bbt_s12)

print("{}h{:02}".format(*divmod(sum([duration for _, duration, _ in ds.get_movies()]), 60)))



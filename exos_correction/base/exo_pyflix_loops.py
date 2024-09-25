from pprint import pprint
import pyflix.datasource as ds
import exos_correction.pyflix.episode_utils as eu
from exos_correction.base.exo_list import bbt_s12


def get_playlist_from(season: list) -> list:
    for index, episode in enumerate(season):
        if not eu.is_viewed(episode):
            return season[index:]

    return []


if __name__ == "__main__":
    show = ds.get_season(user="Me")

    playlist = get_playlist_from(show)

    time_remaining = 120

    while playlist and time_remaining > playlist[0]["duration"]:
        episode = playlist.pop(0)
        print(episode['title'])
        time_remaining -= episode['duration']
        episode["viewed"] = True

    pprint(show)

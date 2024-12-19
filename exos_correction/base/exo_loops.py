from pprint import pprint

import pyflix.datasource as ds
import exos.base.media_utils as mu

def get_playlist_from(season: list) -> list:
    for index, episode in enumerate(season):
        if not mu.is_viewed(episode):
            return season[index:]

if __name__ == "__main__":
    season = ds.get_season('The Big Bang Theory', "Sheldon Cooper")
    playlist = get_playlist_from(season)

    pprint(playlist)
    plalyst_size = len(playlist)

    time_remaining = 120

    while time_remaining > playlist[0]["duration"]:
        episode = playlist.pop(0)
        print(episode["title"])
        episode["viewed"] = True
        time_remaining = time_remaining - episode["duration"]

    print(time_remaining)
    pprint(season[-plalyst_size:])

import pyflix.datasource as ds
from pprint import pprint

import exos_correction.media_utils as mu

bbt_s12 = ds.get_season("me")

pprint(bbt_s12)

def get_playlist_from(season: list):
    playlist = []
    for index, episode in enumerate(season):
        if not mu.is_viewed(episode):
            playlist = season[index:]
            break

    return playlist


playlist = get_playlist_from(bbt_s12)

remaining_time = 120

while playlist and playlist[0]["duration"] <= remaining_time:
    episode = playlist.pop(0)
    print(episode['title'])
    remaining_time -= episode['duration']
    episode["viewed"] = True

print(remaining_time)
pprint(bbt_s12)

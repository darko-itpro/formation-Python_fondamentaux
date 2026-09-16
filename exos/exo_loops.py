import pyflix.datasource as ds
from pprint import pprint

import pyflix.media_utils as mu

season = ds.get_season('The Big Bang Theory', "Sheldon Cooper")

time_left = 120

playlist = mu.get_playlist_from(season)

while time_left > playlist[0]["duration"]:
    episode = playlist.pop(0)
    print(episode["title"])
    time_left -= episode["duration"]
    episode["viewed"] = True

pprint(season)
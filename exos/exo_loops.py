from pprint import pprint

import pyflix.datasource as ds
import pyflix.media_utils as md

season = ds.get_season('The Big Bang Theory', "Sheldon Cooper")

playlist = md.get_playlist_from(season)

remaining_time = 120

while remaining_time > playlist[0]["duration"]:
    episode = playlist.pop(0)
    print(episode["title"])
    remaining_time -= episode["duration"]
    episode['viewed'] = True

print(remaining_time)

pprint(season)
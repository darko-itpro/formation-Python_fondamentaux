import pyflix.datasource as ds

from pprint import pprint

import pyflix.media_utils as mu

season = ds.get_season('The Big Bang Theory', "Sheldon Cooper")

remaining_time = 120

playlist = mu.get_playlist_from(season)

while playlist and remaining_time > playlist[0]['duration']:
    episode = playlist.pop(0)
    print(episode['title'])
    remaining_time -= episode['duration']
    episode['viewed'] = True
    
pprint(season)

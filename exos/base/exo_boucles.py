import exos.base.episode_utils as eu
import pyflix.datasource as ds
from pprint import pprint

bbt_s12 = ds.get_season('The Big Bang Theory', "Sheldon Cooper")

playlist = eu.get_playlist_from(bbt_s12)

time_left = 120

while playlist and time_left > playlist[0]["duration"]:
    episode = playlist.pop(0)
    print(episode['title'])
    time_left -= episode['duration']
    episode['viewed'] = True

print(time_left)
pprint(bbt_s12)

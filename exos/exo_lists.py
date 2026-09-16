import pyflix.datasource as ds
from pprint import pprint

import pyflix.media_utils as mu

bbt_s12 = ds.get_season()

EPISODE_DURATION = 23

print(mu.episodes_duration(bbt_s12, EPISODE_DURATION))

pprint(mu.get_time_limited_playlist(bbt_s12, EPISODE_DURATION, 120))

playlist = bbt_s12.copy()

print(playlist.pop(0))
print(mu.episodes_duration(playlist, EPISODE_DURATION), mu.episodes_duration(bbt_s12, EPISODE_DURATION))
print(id(playlist) == id(bbt_s12))
print(playlist is bbt_s12)


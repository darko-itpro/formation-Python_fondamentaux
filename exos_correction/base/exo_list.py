from pprint import pprint
import pyflix.datasource as ds

bbt_s12 = ds.get_season()

EPISODE_DURATION = 23

def season_duration(season, episode_duration):
    return len(season) * episode_duration

print(season_duration(bbt_s12, EPISODE_DURATION))

def get_playlist(liste_ep:list, d_max:int, ep_duration:int):
    return liste_ep[:d_max // ep_duration]

pprint(get_playlist(bbt_s12, 120, EPISODE_DURATION))

playlist = bbt_s12.copy()

print(playlist.pop(0))
print(season_duration(playlist, EPISODE_DURATION),
      season_duration(bbt_s12, EPISODE_DURATION))

print(id(bbt_s12) == id(playlist))
print(bbt_s12 is playlist)
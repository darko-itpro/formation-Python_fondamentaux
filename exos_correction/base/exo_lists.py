from pprint import pprint

import pyflix.datasource as ds

bbt_s12 = ds.get_season()

EPISODE_DURATION = 23
remaining_time = 120

def episodes_duration(episodes:list, episode_duration:int):
    return len(episodes) * episode_duration

def get_evening_playlist(episodes:list, d_max:int, episode_duration:int):
    max_episodes = d_max // episode_duration
    return episodes[:max_episodes]

print(episodes_duration(bbt_s12, EPISODE_DURATION))

pprint(get_evening_playlist(bbt_s12, remaining_time, EPISODE_DURATION))

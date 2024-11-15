from pprint import pprint

import pyflix.datasource as ds

def episodes_duration(episodes:list, episode_duration:int):
    if episode_duration <= 0:
        raise ValueError('Negative value')
    return len(episodes) * episode_duration

def get_evening_playlist(episodes:list, d_max:int, episode_duration:int):
    max_episodes = d_max // episode_duration
    return episodes[:max_episodes]

if __name__ == "__main__":
    bbt_s12 = ds.get_season()

    EPISODE_DURATION = 23
    remaining_time = 120


    print(episodes_duration(bbt_s12, EPISODE_DURATION))

    pprint(get_evening_playlist(bbt_s12, remaining_time, EPISODE_DURATION))

    playlist = bbt_s12

    print(playlist.pop(0))

    print(id(playlist) == id(bbt_s12))
    print(playlist is bbt_s12)

    #print(episodes_duration(playlist, EPISODE_DURATION), episodes_duration(bbt_s12, EPISODE_DURATION))

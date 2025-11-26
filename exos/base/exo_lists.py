from pprint import pprint
import pyflix.datasource as ds


def duration_for(episodes:list, episode_duration:int):
    return len(episodes) * episode_duration

def get_playlist(episodes:list,
                 episode_duration:int,
                 max_duration:int):
    max_episodes = max_duration // episode_duration
    return episodes[:max_episodes]

if __name__ == '__main__':
    bbt_s12 = ds.get_season()

    remaining_duration = 120

    print(duration_for(bbt_s12, 23))

    pprint(get_playlist(bbt_s12, 23, remaining_duration))

    playlist = bbt_s12.copy()

    print(playlist.pop(0))
    print(duration_for(playlist, 23), duration_for(bbt_s12, 23))
    print(id(playlist) == id(bbt_s12))
    print(playlist is bbt_s12)

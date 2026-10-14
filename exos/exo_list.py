from pprint import pprint
import pyflix.datasource as ds


def episodes_duration(episodes:list, episode_duration: int):
    if episode_duration < 0:
        raise ValueError("Episode duration cannot be negative")

    return len(episodes) * episode_duration

def evening_playlist(episodes:list, episode_duration: int, max_duration: int):
    return episodes[:max_duration // episode_duration]

if __name__ == "__main__":
    bbt_s12 = ds.get_season()
    EPISODE_DURATION = 23
    evening_duration = 120

    episodes_llist = bbt_s12
    print(episodes_duration(episodes_llist, EPISODE_DURATION))

    pprint(evening_playlist(episodes_llist, EPISODE_DURATION, evening_duration))

    playlist = bbt_s12.copy()
    print(playlist.pop(0))
    print(episodes_duration(playlist, EPISODE_DURATION), episodes_duration(bbt_s12, EPISODE_DURATION))

    print(id(bbt_s12) == id(playlist))
    print( bbt_s12 is playlist)
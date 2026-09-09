import pyflix.datasource as ds
from pprint import pprint

def episodes_duration(episodes: list, episode_duration: int):
    return len(episodes) * episode_duration

if __name__ == "__main__":
    bbt_s12 = ds.get_season()

    EPISODE_DURATION = 23
    EVENING_FREE_TIME = 120
    print(episodes_duration(bbt_s12, EPISODE_DURATION))

    print("-----")

    pprint(bbt_s12[:EVENING_FREE_TIME // EPISODE_DURATION])

    print("-----")

    playlist = bbt_s12.copy()

    print(playlist.pop(0))
    print(episodes_duration(playlist, EPISODE_DURATION),
          episodes_duration(bbt_s12, EPISODE_DURATION))

    print(id(bbt_s12) == id(playlist))
    print(bbt_s12 is playlist)

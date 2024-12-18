from pprint import pprint
import pyflix.datasource as ds

def get_playlist(episodes:list, duration:int, episode_duration:int):
    return episodes[:(duration // episode_duration)]

if __name__ == "__main__":
    bbt_s12 = ds.get_season()

    EPISODE_DURATION = 23
    EVENING_TIME = 120

    print(len(bbt_s12) * EPISODE_DURATION)

    pprint(get_playlist(bbt_s12, EVENING_TIME, EPISODE_DURATION))

    playlist = bbt_s12.copy()
    print(playlist.pop(0))

    print(len(playlist) * EPISODE_DURATION, len(bbt_s12) * EPISODE_DURATION)
    print(id(playlist) == id(bbt_s12))
    print(bbt_s12 is playlist)

from pprint import pprint
import pyflix.datasource as ds

def get_duration(episodes, duration):
    return len(episodes) * duration

def get_playlist(episodes:list, time_left:int, episode_duration:int):
    return episodes[:time_left // episode_duration]

if __name__ == "__main__":
    bbt_s12 = ds.get_season()
    pprint(bbt_s12)

    EPISODE_DURATION = 23

    print("durée :", get_duration(bbt_s12, EPISODE_DURATION))

    pprint(get_playlist(bbt_s12, 120, EPISODE_DURATION))

    playlist = bbt_s12.copy()

    print(playlist.pop(0))

    print(id(bbt_s12) == id(playlist))
    print(bbt_s12 is playlist)

    print(get_duration(playlist, EPISODE_DURATION), get_duration(bbt_s12, EPISODE_DURATION))
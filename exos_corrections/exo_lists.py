from pprint import pprint
import pyflix.datasource as ds


def season_duration(episodes:list, episode_duration:int):
    return len(episodes) * episode_duration

def get_playlist(season:list, episode_duration:int, duration:int):
    n = duration // episode_duration
    return season[:n]

if __name__ == "__main__":
    bbt_s12 = ds.get_season()
    EPISODE_DURATION = 23

    print(season_duration(bbt_s12, EPISODE_DURATION))

    remaining_duration = 120

    pprint(get_playlist(bbt_s12, EPISODE_DURATION, remaining_duration))

    print("\n-- La playlist du soir --")

    playlist = bbt_s12.copy()
    print(playlist.pop(0))


    print(season_duration(playlist, EPISODE_DURATION))
    print(season_duration(bbt_s12, EPISODE_DURATION))

    print(playlist is bbt_s12)

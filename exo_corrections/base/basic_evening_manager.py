from pprint import pprint
import pyflix.datasource as ds

def season_duration(season:list, episode_duration:int):
    return len(season) * episode_duration

def get_playlist(season:list, episode_duration:int,  max_duration:int):
    return season[:max_duration // episode_duration]

if __name__ == "__main__":
    bbt_s12 = ds.get_season()
    EPISODE_DURATION = 23

    print(season_duration(bbt_s12, EPISODE_DURATION))

    pprint(get_playlist(bbt_s12,EPISODE_DURATION, 120))

    playlist = bbt_s12.copy()

    print(playlist.pop(0))

    print(season_duration(playlist, EPISODE_DURATION), season_duration(bbt_s12, EPISODE_DURATION))

    print(id(bbt_s12) == id(playlist))
    print(bbt_s12 is playlist)
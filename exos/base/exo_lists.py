from pprint import pprint
import pyflix.datasource as ds

def get_duration(episodes, duration):
    return len(episodes) * duration

if __name__ == "__main__":
    bbt_s12 = ds.get_season()
    pprint(bbt_s12)

    EPISODE_DURATION = 23

    print("durée :", get_duration(bbt_s12, EPISODE_DURATION))
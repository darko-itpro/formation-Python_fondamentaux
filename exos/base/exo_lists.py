from pprint import pprint
import pyflix.datasource as ds


def duration(episodes:list, duration:int):
    return len(episodes) * duration

def get_next_episodes(episodes:list, episode_duration:int, max_duration):
    return episodes[:max_duration // episode_duration]

if __name__ == '__main__':
    bbt_s12 = ds.get_season()
    EPISODE_DURATION = 23
    remaining_duration = 120

    print(duration(bbt_s12, EPISODE_DURATION))

    pprint(get_next_episodes(bbt_s12, EPISODE_DURATION, remaining_duration))
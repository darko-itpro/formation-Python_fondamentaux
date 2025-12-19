from pprint import pprint
import pyflix.datasource as ds


def duration(episodes:list, duration:int):
    if duration < 0:
        raise ValueError(f'duration must be positive, got {duration}')
    return len(episodes) * duration

def get_next_episodes(episodes:list, episode_duration:int, max_duration):
    return episodes[:max_duration // episode_duration]

if __name__ == '__main__':
    duration([], -2)
    bbt_s12 = ds.get_season()
    EPISODE_DURATION = 23
    remaining_duration = 120

    print(duration(bbt_s12, EPISODE_DURATION))

    #pprint(get_next_episodes(bbt_s12, EPISODE_DURATION, remaining_duration))

    playlist = bbt_s12.copy()
    print(playlist.pop(0))
    print(duration(playlist, EPISODE_DURATION), duration(bbt_s12, EPISODE_DURATION))

    print(id(bbt_s12) == id(playlist))
    print(bbt_s12 is playlist)

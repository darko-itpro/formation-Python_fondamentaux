import pyflix.datasource as ds

bbt_s12 = ds.get_season()

def duration_of(episodes:list, episode_duration:int) -> int:
    return len(episodes) * episode_duration

def get_first_episodes(episodes:list, episode_duration:int, max_duration: int) -> list:
    return episodes[:max_duration // episode_duration]

print(duration_of(bbt_s12, 23))

print(get_first_episodes(bbt_s12, 23, 120))

playlist = bbt_s12.copy()

print(playlist.pop(0))

print(duration_of(playlist, 23), duration_of(bbt_s12, 23))

print(id(bbt_s12) == id(playlist))
print(playlist is bbt_s12)

def is_viewed(episode:dict):
    try:
        return bool(episode["viewed"])
    except KeyError:
        return False


def episodes_duration(episodes: list, episode_duration: int):
    return len(episodes) * episode_duration


def get_time_limited_playlist(episodes: list, episode_duration: int, max_duration: int) -> list:

    max_episodes = max_duration // episode_duration

    return episodes[:max_episodes]


def find_first_unseen_episode(season: list) -> int:
    for index, episode in enumerate(season):
        if not is_viewed(episode):
            return index
    return index + 1


def get_playlist_from(season: list) -> list:
    return season[find_first_unseen_episode(season):]
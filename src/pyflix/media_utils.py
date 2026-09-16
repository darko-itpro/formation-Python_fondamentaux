def is_viewed(episode:dict):
    return "viewed" in episode and bool(episode["viewed"])


def episodes_duration(episodes: list, episode_duration: int):
    return len(episodes) * episode_duration


def get_time_limited_playlist(episodes: list, episode_duration: int, max_duration: int) -> list:

    max_episodes = max_duration // episode_duration

    return episodes[:max_episodes]
def is_viewed(episode: dict):
    try:
        return bool(episode["viewed"])
    except KeyError:
        return False


def get_index_first_unseen_episode(episodes: list) -> int:
    for index, episode in enumerate(episodes):
        if not is_viewed(episode):
            break
    return index

def get_playlist_from(episodes: list):
    start_index = get_index_first_unseen_episode(episodes)
    return episodes[start_index:]

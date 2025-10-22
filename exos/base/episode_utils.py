def is_viewed(episode:dict):
    return bool(episode.get("viewed", 0))


def find_first_unseen_episode(episodes:list):
    for index, episode in enumerate(episodes):
        if not is_viewed(episode):
            return index, episode

    return None


def get_playlist_from(episodes:list):
    try:
        index, _ = find_first_unseen_episode(episodes)
    except TypeError:
        return []

    return episodes[index:]

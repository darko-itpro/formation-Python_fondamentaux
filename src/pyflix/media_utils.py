def is_viewed(episode:dict):
    return "viewed" in episode and bool(episode["viewed"])


def get_first_unseen_episode(episodes: list):
    for index, episode in enumerate(episodes):
        if not is_viewed(episode):
            return index


def get_playlist_from(season:list):
    return season[get_first_unseen_episode(season):]
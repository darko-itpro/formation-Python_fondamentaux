def is_viewed(episode:dict):
    return bool(episode.get("viewed", 0))
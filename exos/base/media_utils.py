def is_viewed(episode:dict) -> bool:
    return bool(episode.get('viewed', False))

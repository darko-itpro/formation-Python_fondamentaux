def is_viewed(episode:list) -> bool:
    if len(episode) < 4:
        return False
    return bool(episode[3])

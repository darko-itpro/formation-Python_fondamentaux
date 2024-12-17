def is_viewed(episode:list) -> bool:
    return len(episode) > 3 and bool(episode[3])

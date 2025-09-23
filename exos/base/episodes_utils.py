def is_viewed(episode:list) -> bool:
    return len(episode) > 3 and bool(episode[3])

def is_viewed2(episode:list) -> bool:
    return bool(episode[3]) if len(episode) > 3 else False

def is_viewed(episode:dict) -> bool:
    try:
        return bool(episode['viewed'])
    except KeyError:
        return False
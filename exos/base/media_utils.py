def is_viewed(episode:dict):
    try:
        return bool(episode["viewed"])
    except KeyError:
        return False

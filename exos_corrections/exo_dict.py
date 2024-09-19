
def is_viewed(episode:dict):
    return bool(episode["viewed"]) if "viewed" in episode else False

def is_viewed(episode:dict):
    try:
        return bool(episode["viewed"])
    except KeyError:
        return False

def is_viewed(episode:dict):
    return bool(episode.get("viewed", False))
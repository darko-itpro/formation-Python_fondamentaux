
def is_viewed(episode:dict):
    try:
        return bool(episode["viewed"])
    except KeyError:
        return False

def is_viewed2(episode:dict):
    return bool(episode.get("viewed", False))

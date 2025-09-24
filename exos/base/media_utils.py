
def is_viewed(episode:dict) -> bool:
    #return "viewed" in episode and bool(episode["viewed"])
    #return bool(episode.get('viewed', False))
    try:
        return bool(episode["viewed"])
    except KeyError:
        return False
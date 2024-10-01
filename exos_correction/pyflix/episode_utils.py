
def is_viewed(episode:dict):
    return bool(episode.get("viewed", False))

def to_minutes(hours:int|str):
    return int(hours) * 60

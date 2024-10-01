
def is_viewed(episode:dict):
    return bool(episode.get("viewed", False))

def to_minutes(hours:int|str, minutes:int|str=0):
    return int(hours) * 60 + int(minutes)

def is_viewed(episode:dict):
    return bool(episode.get('viewed', False))


def to_minutes(hours:int|str, minutes:int|str=0):
    hours = int(hours)
    minutes = int(minutes)
    if hours < 0 or minutes < 0:
        raise ValueError("Negative values not supported")

    return hours * 60 + minutes

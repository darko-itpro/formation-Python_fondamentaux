def is_viewed(episode:list):
    return bool(len(episode) > 3 and episode[3])


def to_minutes(hours:int|str, minutes:int|str = 0):
    hours = int(hours)
    minutes = int(minutes)

    if hours < 0 or minutes < 0:
        raise ValueError("Negative values not accepted")

    return hours * 60 + minutes

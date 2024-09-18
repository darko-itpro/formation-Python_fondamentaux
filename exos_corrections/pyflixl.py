
def is_viewed(episode:list):
    try:
        return bool(episode[3])
    except IndexError:
        return False


def to_minutes(hours:int|str, minutes:int|str = 0):
    hours = int(hours)
    minutes = int(minutes)

    if hours < 0 or minutes < 0:
        raise ValueError("Negative values not accepted")

    return hours * 60 + minutes

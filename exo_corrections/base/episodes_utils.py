def is_viewed(episode:dict):
    try:
        return bool(episode["viewed"])
    except KeyError:
        return False


def to_minutes(hours:int|str, minutes:int|str = 0) -> int:
    """
    Converts hours and minutes to minute.

    Lorem Ipsum

    :param hours: Number of hours, must be positive or null.
    :param minutes:
    :raises ValueError: raised if values are negative
    :return:
    """
    hours = int(hours)
    minutes = int(minutes)

    if hours < 0 or minutes < 0:
        raise ValueError(f"Hours and minutes must be positive or null, got {hours} and {minutes}")
    return hours * 60 + minutes

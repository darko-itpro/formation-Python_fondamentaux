

def is_viewed(episode:list):
    try:
        return bool(episode[3])
    except IndexError:
        return False


def is_viewed(episode:list) -> bool:
#    return False if len(episode) < 4 else bool(episode[3]) # avec ternaire
    return len(episode) > 3 and bool(episode[3])

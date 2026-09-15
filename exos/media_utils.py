def is_viewed(episode:list) -> bool:
    return len(episode) > 3 and bool(episode[3])

# Autre possibilité, moins bien
#    return bool(episode[3]) if len(episode) > 3 else False

print('lib fonction')
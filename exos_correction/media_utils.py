

def to_minutes(hours: int|str, minutes: int|str = 0):
    return int(hours) * 60 + int(minutes)

def is_viewed(episode: dict):
    return 'viewed' in episode and bool(episode['viewed'])
    # return bool(episode.get('viewed', 0))


def episode_to_dict(episode: list) -> dict:
    return {'title': episode[0],
            'number': episode[1],
            'duration': episode[2],
            'viewed': episode[3] if len(episode) > 3 else 0,
            }

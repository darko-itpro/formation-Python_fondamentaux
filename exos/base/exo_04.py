
episode_viewed = ["The new Project", 1, 98, True]
episode_not_viewed = ['Installing the softwares', 2, 42, False]


def is_viewed(episode:list):
    if episode[3]:
        return True
    else:
        return False

assert is_viewed(episode_viewed) is False
assert is_viewed(episode_not_viewed) is False

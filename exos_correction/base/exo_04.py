
episode_viewed = ["The new Project", 1, 98, 2]
episode_not_viewed = ['Installing the softwares', 2, 42, 0]

def is_viewed(episode:list) -> bool:
    return episode[3]

is_viewed(episode_not_viewed)
is_viewed(episode_viewed)
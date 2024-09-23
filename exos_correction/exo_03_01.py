episode_viewed = ["The new Project", 1, 98, True]
episode_not_viewed = ['Installing the softwares', 2, 42, False]
episode_not_viewed_count = ['Installing the softwares', 2, 42, 0]

episode = episode_viewed
episode = episode_not_viewed_count

def is_viewed(episode:list) -> bool:
    viewed = episode[3]
    return bool(viewed)

print(is_viewed(episode))

episode_viewed = ["The new Project", 1, 98, 5]
episode_not_viewed = ['Installing the softwares', 2, 42, 0]

def is_viewed(episode:list) -> bool:
    return bool(episode[3])

print(is_viewed(episode_viewed))
print(is_viewed(episode_not_viewed))

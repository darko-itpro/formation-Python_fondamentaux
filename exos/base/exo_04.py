episode_viewed = ["The new Project", 1, 98, True]
episode_not_viewed = ['Installing the softwares', 2, 42, False]

def is_viewed(episode:list):

    viewed = episode[3]
    if viewed:
        return True
    else:
        return False

print(is_viewed(episode_viewed))
print(is_viewed(episode_not_viewed))
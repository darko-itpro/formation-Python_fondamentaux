
episode_viewed = ["The new Project", 1, 98, True]
episode_not_viewed = ['Installing the softwares', 2, 42, False]

episode = episode_viewed
# episode = episode_not_viewed

def is_viewed(episode:list):
    return bool(episode[3])

print("épisode vu" if is_viewed(episode) else "Episode non vu")
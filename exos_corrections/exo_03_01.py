
episode_viewed = ["The new Project", 1, 98, 1]
episode_not_viewed = ['Installing the softwares', 2, 42, 0]

episode = episode_viewed
# episode = episode_not_viewed

viewed = episode[3]
if viewed:
    print("Épisode vu")
else:
    print("Épisode NON vu")



print("Episode vu" if viewed > 0 else "Episode not viewed")

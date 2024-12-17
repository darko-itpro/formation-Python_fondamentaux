
episode_viewed = ["The new Project", 1, 98, 2]
episode_not_viewed = ['Installing the softwares', 2, 42, 0]

episode = episode_viewed
# episode = episode_not_viewed

viewed = episode[3]

if viewed:
    print("épisode vu")
else:
    print("épisode PAS vu")

print("épisode vu" if viewed else"épisode PAS vu")

episode_viewed = ["The new Project", 1, 98, 2]
episode_not_viewed = ['Installing the softwares', 2, 42, 0]

episode = episode_viewed
#episode = episode_not_viewed

is_viewed = episode[3]

if is_viewed:
    print("Episode vu")
else:
    print("episode non vu")

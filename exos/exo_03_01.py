
episode_viewed = ["The new Project", 1, 98, True]
episode_not_viewed = ['Installing the softwares', 2, 42, False]

episode = episode_viewed
#episode = episode_not_viewed

is_viewed = episode[3]

if is_viewed:
    print("Episode vu")
else:
    print("episode non vu")

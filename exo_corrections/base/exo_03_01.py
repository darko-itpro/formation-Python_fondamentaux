
episode_viewed = ["The new Project", 1, 98, True]
episode_not_viewed = ['Installing the softwares', 2, 42, False]

episode = episode_viewed
# episode = episode_not_viewed

# if episode[3]:
#     print("Vu")
# else:
#     print("Pas Vu")

viewed = episode[3]

# print( "vu" if viewed else "pas vu" )


def is_viewed(episode:list):
    return episode[3]

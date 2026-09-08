
episode_viewed = ["The new Project", 1, 98, True]
episode_not_viewed = ['Installing the softwares', 2, 42, False]

episode = episode_viewed


def display_if_viewed(episode:list):
    if is_viewed(episode):
        print("Episode", episode[0], "vu")
    else:
        print("Episode", episode[0], "pas vu")
    

def is_viewed(episode: list) -> bool:
    return episode[3]


display_if_viewed(episode_viewed)

display_if_viewed(episode_not_viewed)

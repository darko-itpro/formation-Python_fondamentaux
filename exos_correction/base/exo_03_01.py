
def is_viewed(episode:list) -> bool:
    return episode[3]

if __name__ == "__main__":
    episode_viewed = ["The new Project", 1, 98, True]
    episode_not_viewed = ['Installing the softwares', 2, 42, False]

    episode = episode_viewed
    # episode = episode_not_viewed

    viewed = episode[3]

    if viewed:
        print("épisode vu")
    else:
        print("épisode PAS vu")


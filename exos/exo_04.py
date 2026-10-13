
def is_viewed_bad(episode:list) -> None:
    viewed = episode[3]

    if viewed:
        print("You have watched this episode")
    else:
        print("You have not watched this episode")


def is_viewed(episode:list) -> bool:
    return episode[3]


if __name__ == "__main__":
    episode_viewed = ["The new Project", 1, 98, True]
    episode_not_viewed = ['Installing the softwares', 2, 42, False]

    is_viewed_bad(episode_viewed)
    is_viewed_bad(episode_not_viewed)

    if is_viewed(episode_viewed):
        print("You have watched this episode")
    else:
        print("You have not watched this episode")

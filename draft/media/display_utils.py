

def display_episodes(show):
    """
    Display episodes for a given show

    :param show: une série sous forme d'objet
    """
    print(f"{show.name}")
    if show.episodes:
        for episode in show:
            if hasattr(episode, "title"):
                print(f" - {episode.title} e{episode.number}s{episode.season.number}")
            else:
                print(f" - {episode}")
    else:
        print(" - Pas d'épisodes pour cette série - ")


def display_episodes(show):
    """
    Display episodes for a given show

    :param show: une série sous forme d'objet
    """
    print(f"{show.name}")
    if show.episodes:
        for episode in show.episodes:
            if hasattr(episode, "title"):
                print(f" - {episode.title} e{episode.number}s{episode.season_number}")
            else:
                print(f" - {episode}")
    else:
        print(" - Pas d'épisodes pour cette série - ")


def display_episodes_for_season(show, season:int = None):
    """
    Display episodes for a given show and a given season number

    :param show: une série sous forme d'objet
    :param season: le numéro de saison ou None.
    """
    print(f"{show.name}")
    if show.get_episodes(season):
        for episode in show.get_episodes(season):
            if hasattr(episode, "title"):
                print(f" - {episode.title} e{episode.number}s{episode.season_number}")
            else:
                print(f" - {episode}")
    else:
        print(" - Pas d'épisodes pour cette série - ")

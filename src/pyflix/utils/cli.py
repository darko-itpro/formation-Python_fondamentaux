"""
Ceci est un module de fonctions utiles pour l'affichage d'informations dans le
terminal.
"""


def display_shows(shows: dict) -> None:
    """
    Affiche dans le terminal les informations d'un dictionnaire de séries.

    La série doit avoir un attribut `name` et un attribut `episodes` contenant
    des objets ayant eux-mêmes un attribut `title`.

    :param shows: Dictionnaire dont les valeurs sont des objets série.
    """
    for show in shows.values():
        print("\n-----")
        display_show(show)


def display_show(show) -> None:
    """
    Affiche dans le terminal les informations d'une série. La série doit avoir
    un attribut `name` et un attribut `episodes` contenant des objets ayant
    eux-mêmes un attribut `title`.

    :param show: Objet représentant une série et possédant un attribut `name`et un
    attribut `episodes`.
    """
    print(show.name)

    try:
        print(f"Durée totale : {show.duration // 60}h{show.duration % 60:02}")
    except (AttributeError, TypeError):
        pass

    current_season = None
    for episode in show.episodes:
        if episode.season_number != current_season:
            current_season = episode.season_number
            print(f"Season {current_season}")
        print(f" - [{episode.number:02}] {episode.title}")
"""
Ceci est un module de fonctions utiles pour l'affichage d'informations dans le
terminal.
"""

def display_shows(shows:dict):
    """
    Affiche dans le terminal les informations d'un dictionnaire de séries.

    La série doit avoir un attribut `name` et un attribut `episodes` contenant
    des objets ayant eux-même un attribut `title`.

    :param shows: Dictionnaire dont les valeurs sont des objets série.
    """
    for show in shows.values():
        print("\n-----")
        display_show(show)

def display_show(show):
    """
    Affiche dans le terminal les informations d'une série. La série doit avoir
    un attribut `name` et un attribut `episodes` contenant des objets ayant
    eux-même un attribut `title`.

    :param show: Dictionnaire dont les valeurs sont des objets série.
    """
    print(show.name)
    for episode in show.episodes:
        print(f" - {episode.title}")

"""
Ce module est une copie de `pylib.utils.cli` mais utilisant la bibliothèque Rich pour
un affichage en terminal plus esthétique.
"""

from rich.tree import Tree
from rich.console import Console

console = Console()


def display_shows(shows: dict) -> None:
    """
    Affiche dans le terminal les informations d'un dictionnaire de séries.

    La série doit avoir un attribut `name` et un attribut `episodes` contenant
    des objets ayant eux-même un attribut `title`.

    :param shows: Dictionnaire dont les valeurs sont des objets série.
    """
    for show in shows.values():
        console.rule(show.name)
        display_show(show)


def display_show(show) -> None:
    """
    Affiche dans le terminal les informations d'une série. La série doit avoir
    un attribut `name` et un attribut `episodes` contenant des objets ayant
    eux-même un attribut `title`.

    :param show: Objet représentant une série et possédant un attribut `name`et un
    attribut `episodes`.
    """
    t_show = Tree(show.name)
    t_season = None
    current_season_number = None
    for episode in show.episodes:
        if current_season_number != episode.season_number:
            current_season_number = episode.season_number
            t_season = Tree(f"Season {current_season_number}", style="blue")
            t_show.add(t_season)
        t_season.add(f'[{episode.number:02}] {episode.title}', style="white")

    console.print(t_show)

    try:
        print(f"Durée totale : {show.duration // 60}h{show.duration % 60:02}")
    except (AttributeError, TypeError):
        pass
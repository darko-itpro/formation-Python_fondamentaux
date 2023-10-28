"""
Ce module est une copie de `pylib.utils.cli` mais utilisant la bibliothèque Rich pour
un affichage en terminal plus esthétique.
"""

from rich.tree import Tree
from rich.console import Console

console = Console()

def display_shows(shows:dict):
    """
    Affiche dans le terminal les informations d'un dictionnaire de séries.

    La série doit avoir un attribut `name` et un attribut `episodes` contenant
    des objets ayant eux-même un attribut `title`.

    :param shows: Dictionnaire dont les valeurs sont des objets série.
    """
    for show in shows.values():
        console.rule(show.name)
        display_show(show)

def display_show(show):
    """
    Affiche dans le terminal les informations d'une série. La série doit avoir
    un attribut `name` et un attribut `episodes` contenant des objets ayant
    eux-même un attribut `title`.

    :param show: Dictionnaire dont les valeurs sont des objets série.
    """
    t = Tree(show.name)
    for episode in show.episodes:
        t.add(episode.title, style="blue")

    console.print(t)

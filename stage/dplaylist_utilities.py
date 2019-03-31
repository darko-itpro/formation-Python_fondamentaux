#!/usr/bin/env python 

"""
Exemple de script pour gérer une playlist
"""


def create_playlist():
    """
    Crée une structure pour gérer une playlist.

    :return: Une playlist
    """
    return {}


def add_media_to_playlist(playlist, title, duration: int):
    """
    Ajoute un media sous la forme titre/durée à une playlist.

    Cette fonction met en œuvre l'approche fonctionnelle, le paramètre playlist
    n'est pas modifié et une nouvelle playlist est retournée.

    :param playlist: Une Playlist
    :param title: Le titre du média
    :type title: str
    :param duration: La durée en secondes du média
    :return: Une playlist équivalente au paramètre d'entrée avec un élément en
    plus
    """
    new_playlist = playlist.copy()
    new_playlist[title] = [title, int(duration)]

    return new_playlist


def display_playlist_content(playlist):
    """
    Affiche le contenu de la playlist

    :param playlist: La playlist dont on veut afficher le contenu
    """
    print('Ma Playlist :')
    for title, duration in playlist.values():
        minutes, seconds = divmod(duration, 60)
        print(' - {} {}m{:02}'.format(title, minutes, seconds))
        print()


def display_playlist_duration(playlist):
    """
    Affiche la durée totale de la playlist
    :param playlist: La playlist dont on veut la durée
    """
    pass  # TODO: Le stagiaire en prestation est parti avant de finir…

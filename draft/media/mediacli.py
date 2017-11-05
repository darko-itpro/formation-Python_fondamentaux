#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Module destiné à fournir une interface de type terminal.
"""

from draft.media import base_mediamodel as mediamodel


def episoedes_list():
    """
    Cette fonction attends une liste d'épisodes ordonnés.
    """
    print("Épisodes pour {}".format(_tvshow.name))
    episodes = _tvshow.episodes()
    if episodes:
        pass # TODO : ajouter le code pour lister les épisodes
    else:
        print("Pas d'épisodes pour la série.")


def add_episode():
    """
    Fonction qui permet d'ajouter un épisode à la série.
    :return:
    """
    ep_title = input("Titre de l'épisode")
    ep_season = input("Saison de l'épisode")
    ep_number = input("Numéro de l'épisode dans la saison")

    _tvshow.add_episode(ep_title, ep_number, ep_season)


actions = {}
actions['a'] = None
actions['s'] = None
actions['e'] = episoedes_list

if __name__ == "__main__":
    print("Gestion de série")
    tvshow_name = input("Entrez le titre de la série ")
    _tvshow = mediamodel.TvShow(tvshow_name)

    while True:
        print("""
        [a] ajouter un épisode
        [s] lister les saisons
        [e] lister les épisodes
        [q] sortie
        """)

        choice = input("Choix ? ")
        if choice in actions:
            actions[choice]()
        elif choice == "q":
            break
        else:
            print("Choix non valide")
    print("Bye")
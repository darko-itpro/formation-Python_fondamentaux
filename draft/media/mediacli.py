#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Module destiné à fournir une interface de type terminal.
"""

from draft.media import mediamodel as mediamodel


def saisons_list():
    """
    Fonction qui liste les saisons pour la série gérée.
    :return: None
    """
    print("Saisons pour {}".format(_tvshow.name))
    if len(_tvshow.seasons) > 0:
        for saison in _tvshow.seasons:
            print("Saison {} - {} épisodes".format(saison.number, len(saison.episodes)))
    else:
        print("Pas de saison pour la série {}".format(_tvshow.name))


def add_episode():
    """
    Fonction qui permet d'ajouter un épisode à la série.
    :return:
    """
    ep_title = input("Titre de l'épisode")
    ep_season = input("Saison de l'épisode")
    ep_number = input("Numéro de l'épisode dans la saison")

    _tvshow.add_episode(mediamodel.Episode(ep_title, ep_number), ep_season)

actions = {}
actions['a'] = None
actions['s'] = saisons_list
actions['e'] = None

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
#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Module destiné à fournir une interface de type terminal.
"""

from training.projects.mediamanager import mediamodel as mediamodel


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


def episodes_list():
    """
    Fonction qui liste les épisodes pour la série gérée
    :return: None
    """
    print("Épisodes pour {}".format(_tvshow.name))
    if len(_tvshow.seasons) > 0:
        for saison in _tvshow.seasons:
            print("Saison {}".format(saison.number))
            for episode in saison.episodes:
                print("({:>2}) {}".format(episode.number, episode.title))
    else:
        print("Pas d'épisodes pour la série {}".format(_tvshow.name))


def add_episode():
    """
    Fonction qui permet d'ajouter un épisode à la série.
    :return:
    """
    ep_title = input("Titre de l'épisode ")
    try:
        ep_season = int(input("Saison de l'épisode "))
        ep_number = int(input("Numéro de l'épisode dans la saison "))
    except ValueError:
        print("Les numéros doivent être des nombres.")
        return

    try:
        _tvshow.add_episode(mediamodel.Episode(ep_title, ep_number), ep_season)
    except ValueError:
        print("L'épisode {} de la saison {} existe déjà".format(ep_number, ep_season))

actions = {}
actions['a'] = add_episode
actions['s'] = saisons_list
actions['e'] = episodes_list

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

#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Module destiné à fournir une interface de type terminal. Doit être un module
principal.
"""

from draft.media import mediamodel as media


def episodes_list():
    """
    Fonction destinée à afficher une liste d'épisodes ordonnés.

    Cette fonction fait appel à la méthode get_episodes de l'objet saison.
    """
    print("Épisodes pour {}".format(_tvshow.name))
    episodes = _tvshow.get_episodes()
    if episodes:
        pass # TODO : ajouter le code pour lister les épisodes
    else:
        print("Pas d'épisodes pour la série.")


def add_episode():
    """
    Fonction qui permet d'ajouter un épisode à la série.

    Après avoir posé les questions pour récupérer les paramètres titre, saison
    et numéro d'épisode, elle fait appel à la méthode add_episode de l'objet
    saison.
    """
    ep_title = input("Titre de l'épisode")
    ep_season = input("Saison de l'épisode")
    ep_number = input("Numéro de l'épisode dans la saison")

    _tvshow.add_episode(ep_title, ep_number, ep_season)


if __name__ == "__main__":

    actions = {}
    actions['a'] = None
    actions['s'] = None
    actions['e'] = episodes_list

    print("Gestion de série")
    tvshow_name = input("Entrez le titre de la série ")

    _tvshow = media.TvShow(tvshow_name)

    while True:
        print("""
        [a] ajouter un épisode
        [s] lister les saisons
        [e] lister les épisodes
        [q] sortie
        """)

        choice = input("Choix ? ")
        if choice == "q":
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Choix non valide")
    print("Bye")
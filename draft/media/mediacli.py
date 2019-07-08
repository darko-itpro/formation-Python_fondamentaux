#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Module destiné à fournir une interface de type terminal. Doit être un module
principal.
"""

from draft.media import mediamodel as media


def display_existing_shows(path):
    #TODO: utilisez votre fonction de chargement de données
    for title in list(set([show[0]
                           for show in from_file.load_episode_from_file(path)])):
        print(" - {}".format(title))


def load_from_file(path, show):
    # TODO: utilisez votre fonction de chargement de données
    for data in from_file.load_episode_from_file(path):
        if data[0] == show.name:
            show.add_episode(data[3], data[2], data[1])


def episodes_list():
    """
    Fonction destinée à afficher une liste d'épisodes ordonnés.

    Cette fonction fait appel à la méthode get_episodes de l'objet saison.
    """
    print("Épisodes pour {}".format(my_show.name))
    episodes = my_show.get_episodes()
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

    my_show.add_episode(ep_title, ep_number, ep_season)


if __name__ == "__main__":

    actions = {}
    actions['a'] = None
    actions['s'] = None
    actions['e'] = episodes_list

    print("Gestion de série")
    PATH = None  # TODO: add path

    if PATH is not None:
        display_existing_shows(PATH)

    tvshow_name = input("Entrez le titre de la série ")

    my_show = media.TvShow(tvshow_name)

    if PATH is not None:
        load_from_file(PATH, my_show)

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

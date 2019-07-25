#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Module destiné à fournir une interface de type terminal.
"""

from draft.media import media_db as media


def episodes_list():
    """
    Fonction qui liste les épisodes pour la série gérée
    :return: Une liste d'épisodes
    """
    print("Liste d'épisodes")

    # TODO: Ajouter le code pour lister les épisodes.


def add_episode():
    """
    Fonction qui permet d'ajouter un épisode à la série.
    :return: None
    """
    ep_title = input("Titre de l'épisode ")
    try:
        ep_season = int(input("Saison de l'épisode "))
        ep_number = int(input("Numéro de l'épisode dans la saison "))
    except ValueError:
        print("Les numéros doivent être des nombres.")
        return

    # TODO: Ajouter le code pour ajouter un épisode en base


if __name__ == "__main__":

    actions = {}
    actions['a'] = add_episode
    actions['s'] = None
    actions['e'] = episodes_list

    print("Gestion de série")
    tvshow_name = input("Entrez le titre de la série ")

    show_db = media.TvShowDao()

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

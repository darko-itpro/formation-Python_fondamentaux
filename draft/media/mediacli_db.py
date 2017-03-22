#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from draft.media import media_db as media_db


def episodes_list():
    """
    Fonction qui liste les épisodes pour la série gérée
    :return: None
    """
    print("Liste d'épisodes")

    # TODO: Ajouter le code pour lister les épisodes.


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

    # TODO: Ajouter le code pour ajouter un épisode en base

actions = {}
actions['a'] = add_episode
actions['e'] = episodes_list

if __name__ == "__main__":
    print("Gestion de série")

    _db = media_db.MediaDao()

    while True:
        print("""
        [a] ajouter un épisode
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

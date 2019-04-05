#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module d'interface terminal avec l'utilisateur
"""

EPISODE_DETAIL_TEMPLATE = "s{:0>2}e{:0>2} {}"


def episodes_list():
    """
    Fonction qui liste les épisodes pour la série gérée
    :return: None
    """
    print("Liste d'épisodes")
    ep_liste = TV_SHOW.get_episodes()
    if ep_liste:
        for entry in ep_liste:
            print(EPISODE_DETAIL_TEMPLATE
                  .format(entry.season, entry.number, entry.title))
    else:
        print("Pas d'épisodes")


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
        TV_SHOW.add_episode(ep_title, str(ep_season), str(ep_number))
    except ValueError:
        print("L'épisode {} de la saison {} existe déjà"
              .format(ep_number, ep_season))


def display_shows(db_path):
    """
    Affiche les séries contenues dans un gestionnaire de séries.
    """
    if db_path is None:
        print('Gestion en mémoire.')
        return

    shows_db = media.MediaDao(db_path)

    shows = shows_db.get_shows()
    if shows:
        print('Séries disponibles :')
        for title in shows:
            print(title)
    else:
        print('Pas de série dans la base')


ACTIONS = {}
ACTIONS['a'] = add_episode
ACTIONS['e'] = episodes_list

if __name__ == "__main__":

    import argparse

    PARSER = argparse.ArgumentParser(
        description="Gestion de médiathèque. Par défaut, la gestion des données"
                    " est assurée par une base de données."
    )

    PARSER.add_argument('-s', '--statefull', action='store_true',
                        help="Force l'utilisation du modèle objet. "
                             "Ignoré si une base est spécifiée")
    PARSER.add_argument('-p', '--db_path',
                        help='Chemin vers le fichier de la base')

    ARGS = PARSER.parse_args()

    if ARGS.db_path:
        DB_PATH = ARGS.db_path
        from training.projects.mediamanager import media_db as media
    elif ARGS.statefull:
        DB_PATH = None
        from training.projects.mediamanager import mediamodel as media
    else:
        DB_PATH = "default.db"
        from training.projects.mediamanager import media_db as media

    display_shows(DB_PATH)

    print()

    SHOW_NAME = input("Quelle est votre série ? ")

    TV_SHOW = media.TvShow(SHOW_NAME, DB_PATH)

    print("Gestion de série")

    while True:
        print("""
        [a] ajouter un épisode
        [e] lister les épisodes
        [q] sortie
        """)

        CHOICE = input("Choix ? ")
        if CHOICE == "q":
            break
        elif CHOICE in ACTIONS:
            ACTIONS[CHOICE]()
        else:
            print("Choix non valide")
    print("Bye")

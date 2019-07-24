#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module d'interface terminal avec l'utilisateur
"""

EPISODE_DETAIL_TEMPLATE = "s{:0>2}e{:0>2} {}"


def episodes_list(tv_show):
    """
    Fonction qui liste les épisodes pour la série en paramètre
    :return: None
    """
    print("Liste d'épisodes")
    ep_liste = tv_show.get_episodes()
    if ep_liste:
        for entry in ep_liste:
            print(EPISODE_DETAIL_TEMPLATE
                  .format(entry.season_number, entry.number, entry.title))
    else:
        print("Pas d'épisodes")


def add_episode(tv_show):
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
        tv_show.add_episode(ep_title, str(ep_season), str(ep_number))
    except ValueError:
        print("L'épisode {} de la saison {} existe déjà"
              .format(ep_number, ep_season))


def display_shows(db_path):
    """
    Affiche les séries contenues dans un gestionnaire de séries.
    """
    from training.projects.mediamanager import media_db as media
    shows_db = media.MediaDao(db_path)

    shows = shows_db.get_shows()
    if shows:
        print('Séries disponibles :')
        for title in shows:
            print(title)
    else:
        print('Pas de série dans la base')


def display_main_menu(db_path):
    actions = {'a': add_episode,
               'e': episodes_list}

    if db_path is None:
        print("Gestion en mémoire")
        from training.projects.mediamanager import mediamodel as media
        show_name = input("Quelle est votre série ? ")
        tv_show = media.TvShow(show_name)
    else:
        from training.projects.mediamanager import media_db as media
        display_shows(db_path)
        print()
        show_name = input("Quelle est votre série ? ")
        tv_show = media.TvShow(show_name, db_path)

    print("Gestion de série")

    while True:
        print("""
        [a] ajouter un épisode
        [e] lister les épisodes
        [q] sortie
        """)

        choice = input("Choix ? ")
        if choice == "q":
            break
        elif choice in actions:
            actions[choice](tv_show)
        else:
            print("Choix non valide")
    print("Bye")


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
    elif ARGS.statefull:
        DB_PATH = None
    else:
        DB_PATH = "default.db"

    display_main_menu(DB_PATH)

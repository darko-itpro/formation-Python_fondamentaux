#!/usr/bin/env python

"""
Ce module illustre un launcher pour l'application media. Celui-ci gère les
paramètres passés à la ligne de commande et permet l'exécution des différentes
interfaces en fonction d'un paramètre command.

Work in progress

"""


def launch_app(_):
    # Manière simple de lancer l'interface tkinter
    import training.projects.mediamanager.media_tk


def launch_webapp(args):
    import training.projects.mediamanager.mediaweb as webapp
    webapp.app.run()


def load_data(args):
    import training.projects.mediamanager.media_file_loader as loader

    for media in loader.load_episode_from_file(args.file):
        print(media)


def load_cli(args):
    from training.projects.mediamanager import mediacli
    mediacli.display_main_menu(args.db_path)


if __name__ == '__main__':

    actions = {"cli": load_cli,
               "web": launch_webapp,
               "app": launch_app,
               "load": load_data}

    import argparse

    PARSER = argparse.ArgumentParser(
        description="Gestion de médiathèque. Par défaut, la gestion des données"
                    " est assurée par une base de données."
    )

    PARSER.add_argument("command", choices=list(actions),
                        help="Lance le programme en cli, web, app (Tkinter) ou "
                             "charge simplement des données en base.")

    PARSER.add_argument('-s', '--statefull', action='store_true',
                        help="Force l'utilisation du modèle objet. "
                             "La base de données est ignoré.")
    PARSER.add_argument('-p', '--db_path', default="default.db",
                        help='Chemin vers le fichier de la base')
    PARSER.add_argument('-f', '--file', help="Chemin vers le fichier contenant "
                                             "des données.")

    ARGS = PARSER.parse_args()

    print(ARGS.command)
    print(ARGS.db_path)

    actions[ARGS.command](ARGS)

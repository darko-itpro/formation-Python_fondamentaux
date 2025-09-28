from pathlib import Path
import logging

import pyflix.loaders.file_helpers as fu  # Module de la fonction chargeant les informations de séries.
import demos.pyflix.media_db as media  # Module contenant les objets liés à la gestion des médias

import demos.settings as conf

try:
    from pyflix.utils import rich_cli as cli
except ModuleNotFoundError:
    from pyflix.utils import cli


def load_data_from_path(path: str | Path, shows: dict[str, media.TvShow] = None) -> dict[str, media.TvShow]:
    """
    Charge les données d'une série à partir d'une source et retourne un dictionnaire de séries.

    Le paramètre optionnel `shows` permet de compléter une collection existante. La valeur par
    défaut est `None` car le dictionnaire est un type mutable.

    :param path: Chemin vers la source de données. Doit être un fichier csv ou un répertoire.
    :param shows: Dictionnaire de TvShows dont la clef est le titre. Optionnel. Si absent
    un nouveau dictionnaire est créé.
    :return: Un dictionnaire de TvShows dont la clef est le titre. Si un dictionnaire a été passé en
    argument, l'original n'est pas modifié.
    """

    path = Path(path) #  Pour s'assurer d'avoir un objet Path

    if path.is_dir():
        my_episodes = fu.load_from_filenames(path)
        logging.info(f"Using dir handler for path {path}")
    elif path.is_file():
        my_episodes = fu.load_from_csv(path)
        logging.info(f"Using csv handler for path {path}")
    else:
        raise ValueError(f"Provided path does not exist {path}")

    shows = shows.copy() if shows is not None else {}

    for show_name, *episode_data in my_episodes:
        if show_name not in shows:
            shows[show_name] = media.TvShow(show_name)

        show = shows[show_name]

        try:
            show.add_episode(*episode_data)
        except ValueError:
            logging.warning(f"Episode {episode_data[0]} for {show_name} exists")

    return shows

def load_default_data(shows:dict = None) -> dict[str, media.TvShow]:
    paths = []  # Liste des chemins vers les ressources à utiliser.
    shows = shows.copy() if shows is not None else {}  # Servira à stocker des données titre:show.

    # Configuration des chemins vers les ressources.
    paths.append(conf.ROOT_PATH.joinpath("assets", "showslist.csv"))
    paths.append(conf.ROOT_PATH.joinpath("assets", "files"))

    for source_path in paths:
        shows = load_data_from_path(source_path, shows)

    return shows

def add_data_to_shows(source_path:Path, shows:dict[str, media.TvShow] = None) -> dict[str, media.TvShow]:
    shows = shows.copy() if shows is not None else {}  # Servira à stocker des données titre:show.

    try:
        shows = load_data_from_path(source_path, shows)
    except ValueError:
        logging.error(f"Impossible de charger les données de {source_path}")

    return shows

def display_all_shows(shows:dict[str, media.TvShow]):
    cli.display_shows(shows)


def run():

    shows = {}  # Servira à stocker des données titre:show.

    shows = load_default_data(shows)

    cli.display_shows(shows)


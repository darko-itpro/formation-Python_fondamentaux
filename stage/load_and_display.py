import stage.file_utils as fu  # Module de la fonction chargeant les informations de séries.
import stage.mediatheque as media  # Module contenant les objets liés à la gestion des médias
from pylib.utils import cli
from pathlib import Path
import os.path


def load_data_from_path(path:str, shows:dict[str, media.TvShow] = None) -> dict[str, media.TvShow]:
    """
    Charge les données d'une série à partir d'une source et retourne un dictionnaire de séries.

    Le paramètre optionnel `shows` permet de compléter une collection existante. La valeur par
    défaut est `None` car le dictionnaire est un type mutable.

    :param path: Chemin vers la source de données. Doit être un fichier csv ou un répertoire.
    :param shows: Dictionnaire de TvShows dont la clef est le titre. Optionnel. Si non founri
    un nouveau dictionnaire est créé.
    :return: Un dictionnaire de TvShows dont la clef est le titre. Si un dictionnaire a été passé en
    argument, l'original n'est pas modifié.
    """
    if os.path.isdir(path):
        my_episodes = fu.load_from_filenames(path)
    elif os.path.isfile(path):
        my_episodes = fu.load_from_csv(path)
    else:
        raise ValueError(f"Provided path does not exist {path}")

    shows = shows.copy() if shows else {}

    for show_name, season, number, title, *other in my_episodes:  # *other premt de récupérer d'autres données
        if show_name not in shows:
            shows[show_name] = media.TvShow(show_name)

        show = shows[show_name]

        try:
            show.add_episode(title, number, season)
        except ValueError:
            print(f"Episode {title} for {show_name} exists")

    return shows


if __name__ == "__main__":
    # La ligne suivante utilse la variable `__file__`pour déterminer le chemin
    # du module afin de construire le chemin vers le fichier csv.
    csv_path = os.path.join(__file__, "..", "assets", "showslist.csv")
    dir_path = os.path.join(__file__, "..", "assets", "files")

    # Ci-dessous, les alternatives avec Path. Attention, dans ce cas, la racine sera
    # le répertoire d'exécution de Python et non le fichier.
    #  file_path = Path('.').resolve().parent / "assets" / "showslist.csv"
    #  dir_path = Path('.').resolve().parent / "assets" / "files"

    shows = load_data_from_path(file_path)
    cli.display_shows(shows)
import stage.file_utils as fu  # Module de la fonction chargeant les informations de séries.
import stage.mediatheque as media  # Module contenant les objets liés à la gestion des médias
from pylib.utils import cli
from pathlib import Path
import os.path


def load_data_from_file(path:str) -> dict[str, media.TvShow]:
    my_episodes = fu.load_from_csv(path)

    shows = {}

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
    file_path = os.path.join(__file__, "..", "assets", "showslist.csv")
    #  file_path = Path('.').resolve().parent / "assets" / "showslist.csv"  # Alternative avec Path

    shows = load_data_from_file(file_path)
    cli.display_shows(shows)
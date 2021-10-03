import stage.file_utils as fu  # Module de la fonction chargeant les informations de séries.
import pylib.media_db as media
from pylib.utils import cli
import os.path


def load_data_from_file(path:str) -> dict[str, media.TvShow]:
    my_episodes = fu.load_from_csv(path)

    shows = {}

    for show_name, season, number, title, duration, year in my_episodes:
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
    file_path = os.path.join(__file__, "../assets/showslist.csv")

    shows = load_data_from_file(file_path)
    cli.display_shows(shows)
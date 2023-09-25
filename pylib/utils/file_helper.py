from pathlib import Path
import re


def load_from_filenames(dir_path):
    """
    Générateur qui fournit les informations média série à partir du nom des fichiers du répertoire.
    
    :param dir_path: Chemin vers un répertoire de fichiers média correctement formatés
    """
    pattern = "-s(?P<season>[0-9]{2})e(?P<episode>[0-9]{2})-"
    p = Path(dir_path)
    for media_file in p.iterdir():
        episode_name = media_file.stem
        result = re.search(pattern, episode_name)

        if result:
            yield episode_name[:result.start()].replace("_", " "), \
                  result.group("season"), result.group("episode"), \
                  episode_name[result.end():].replace("_", " ")


def load_from_csv(file_path):
    """
    Générateur qui fournit les informations média série à partir d'un fichier csv
    
    :param file_path: Chemin vers un fichier csv correctement formaté
    :return: 
    """
    with open(file_path, encoding="utf-8") as csv_file:
        header = tuple(csv_file.readline().split(";"))
        if header != ("tvshow", "season", "ep_number", "ep_title", "duration", "year"):
            raise ValueError("Unexpected CSV structure")

        for episode in csv_file:
            yield tuple(episode.split(";"))

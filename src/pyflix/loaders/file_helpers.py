from pathlib import Path
import re


def load_from_filenames(dir_path:Path|str):
    """
    Générateur qui fournit les informations média série à partir du nom des fichiers du répertoire.

    Cette fonction se base sur les regex pour extraire les informations à partir d'un nom de
    fichier. Voir la documentation pour les détails sur la regax.

    :param dir_path: Chemin vers un répertoire de fichiers média correctement formatés
    """
    pattern = "-s(?P<season>[0-9]{2})e(?P<episode>[0-9]{2})-"
    p = Path(dir_path)
    for media_file in p.iterdir():
        episode_name = media_file.stem
        result = re.search(pattern, episode_name)

        if result:
            yield (episode_name[:result.start()].replace("_", " "),
                   episode_name[result.end():].replace("_", " "),
                   result.group("season"),
                   result.group("episode"),
                   )


def load_from_csv(file_path:Path|str):
    """
    Générateur qui fournit les informations média série à partir d'un fichier csv

    :param file_path: Chemin vers un fichier csv correctement formaté
    """
    with open(file_path, encoding="utf-8") as csv_file:
        header = tuple(csv_file.readline().strip().split(";"))
        if header != ("tvshow", "season", "ep_number", "ep_title", "duration", "year"):
            raise ValueError("Unexpected CSV structure")

        for episode in csv_file:
            show, season, number, title, duration, year = episode.strip().split(";")
            yield show, title, season, number, duration, year


def load_from_sources(sources:list[Path|str]):
    """
    Générateur qui fournit les informations média série à partir d'une liste de sources.

    :param sources: Liste chemins soit vers des fichiers csv soit vers des répertoires.
    """
    for source in sources:
        source = Path(source)

        if source.is_file():
            yield from load_from_csv(source)
        elif source.is_dir():
            yield from load_from_filenames(source)
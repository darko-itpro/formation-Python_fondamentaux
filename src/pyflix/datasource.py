"""
Ce module est une source de données pour les différents exercices.
"""

from pathlib import Path
import random
from pyflix.loaders import file_helpers
from collections.abc import Iterator

random.seed()


def get_shows_names() -> list[str]:
    """
    Permet de récupérer la liste des séries connues qui pourront être utilisé avec la
    fonction `get_season()`.

    :return: Liste des titres de séries.
    """
    file_path = Path(__file__).resolve().parent / "assets" / "tv_shows.csv"

    with open(file_path, encoding="utf-8") as bbt_file:
        bbt_file.readline()

        shows = [_process_line(line)[0]
                 for line in bbt_file]

    shows = sorted(list(set(shows)))

    return shows


def _process_line(episode_line: str) -> tuple[str, str, int, int, int, int]:
    """
    Extrait et transtype les données à partir d'une ligne type csv.

    :param episode_line: Une ligne type csv
    :return: Un N-uplet (nom saison, saison, numéro d'épisode, titre d'épisode, durée, année)
    """
    show, season, episode, title, duration, year = episode_line.rstrip().split(';')
    return show, title, int(season), int(episode), int(duration), int(year)


def _is_show(episode_line: str, show_name:str|None=None) -> bool:
    show_name = show_name or 'The Big Bang Theory'
    return episode_line.split(';')[0] == show_name


def _to_dict(show, title:str, season, episode, duration:int, year) -> dict:
    episode = {"title": title, "duration": duration}

    return episode


def get_movies() -> list[tuple[str, int, bool]]:
    """
    Fonction perméttant d'obtenir une liste de médias.

    :return: Une liste de médias au format `tuple(titre, durée, vu)`
    """
    return [("The Philosopher's Stone", 152, True),
            ("The Chamber of Secrets", 161, True),
            ("The Prisoner of Azkaban", 142, False),
            ("the Goblet of Fire", 157, True),
            ("the Order of the Phoenix", 138, False),
            ("the Half-Blood Prince", 153, True),
            ("the Deathly Hallows – Part 1", 126, False),
            ("the Deathly Hallows – Part 2", 130, False)]

def load_show(name:str|None=None) -> Iterator[tuple[str, ...]]:
    """
    Load show(s) episodes from the datasource.

    You can iterate through the shows which will be tuples (show name, episode title, season
    number, episode number, duration, year).

    The episodes order is not guaranteed.

    :param name: Name of a show. If provided, the episodes will be filtered on this show's name.
    :return: a generator object.
    """
    file_path = Path(__file__).resolve().parent / "assets" / "tv_shows.csv"
    if name is None:
        yield from file_helpers.load_from_csv(file_path)
    else:
        for episode in file_helpers.load_from_csv(file_path):
            if episode[0] == name:
                yield episode


# Specialized functions

def get_start_time() -> str:
    """
    Fonction simulant la collecte de la donnée de temps à partir d'une source de données.
    L'heure retournée est comprise entre '19h00' et '21h38'.

    :return: Une heure au format `"mmhss"` (`'%Mh%S'` pour les connaisseurs).
    """
    start_hour = random.randint(19, 21)
    start_minutes = random.randint(0, 59 if start_hour < 21 else 38)

    value = f"{start_hour:02}h{start_minutes:02}"

    return value

def get_season(show_name: str = None, user: str = None) -> list[dict]:
    """
    Fonction permettant d'accéder à la saison d'une série. Sans paramètre (ou avec `None`),
    retourne la liste des titres de la saison. Avec, retourne une liste d'épisodes sous forme
    de dictionnaires.

    Le nombre d'épisodes vus/non vus est aléatoire. Lors de la génération de la liste, chaque
    épisode a 80 % de chances d'être vu. Dès qu'un épisode n'a pas été vu, les suivants sont tous
    non-vus. Un épisode non vu a 60 % de chances de ne pas avoir la clef `viewed`.

    :param show_name: le nom d'une série, si omis, il s'agira de Big Bang Theory
    :param user: un identifiant d'utilisateur.
    :return: Si un identifant est donné, une liste d'épisodes où un épisode est représenté par un
    dictionnaire contenant les clefs `title`, `duration` et `viewed`. Si l'épisode n'a pas été vu,
    cette dernière peut être absente.
    """
    file_path = Path(__file__).resolve().parent / "assets" / "tv_shows.csv"

    with open(file_path, encoding="utf-8") as bbt_file:
        bbt_file.readline()

        if user is None:
            episodes = [_process_line(line)[1]
                        for line in bbt_file
                        if _is_show(line, show_name)]
        else:
            episodes = [_to_dict(*_process_line(line))
                        for line in bbt_file
                        if _is_show(line, show_name)]
            _randomize_viewed(episodes)

    return episodes


def _randomize_viewed(season: list) -> None:
    """
    Ajoute de manière aléatoire une clef `viewed` à une liste d'épisodes.

    Un épisode a 80% de chance d'être vu. Dès qu'un épisode n'est pas vu, les suivants sont
    également non-vus. Un épisode non-vu a 60% de chances de ne pas avoir la clef `viewed`.

    :param season: Une liste de dictionnaires
    """
    is_viewed = True

    for episode in season:
        if random.random() > 0.8:
            is_viewed = False

        if is_viewed:
            episode['viewed'] = True
        else:
            if random.random() > 0.4:
                episode['viewed'] = False
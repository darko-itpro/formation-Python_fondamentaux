"""
Ce module est une source de données pour les différents exercices.

Ces données sont hétéroclytes, évidemment, dans un "vrai" projet, elles seraient organisées par
arborescence fonctionnelle.
"""

from pathlib import Path
import random
random.seed()


def time_loader():
    """
    Fonction simulant la collecte d'une donnée à partir d'une source de données.
    """
    return "30"


def get_start_time():
    """
    Fonction simulant la collecte de la donnée à partir d'une source de données.
    """
    return "20h42"


def get_season(user=None) -> list:
    """
    Fonction permettant d'accéder à la saison d'une série. Sans paramètre (ou avec `None`, retourne
    la liste des titres de la saison. Avec, retourne une liste d'épisodes sous forme de
    dictionnaires.

    Le nombre d'épisodes vus/non vus est aléatoire. Lors de la génération de la liste, chaque
    épisode a 80 % de chances d'être vu. Dès qu'un épisode n'a pas été vu, les suivants sont tous
    non-vus. Un épisode non vu a 60 % de chances de ne pas avoir la clef `viewed`.

    :param user: un identifiant d'utilisateur.
    :return: Si un identifant est donné, une liste d'épisodes où un épisode est représenté par un
    dictionnaire contenant les clefs `title`, `duration` et `viewed`. Si l'épisode n'a pas été vu,
    cette dernière peut être absente.
    """
    file_path = Path(__file__).resolve().parent.parent / "assets" / "bbts12.csv"

    with open(file_path, encoding="utf-8") as bbt_file:
        bbt_file.readline()

        if user is None:
            return [_process_line(line)[3] for line in bbt_file]
        else:
            episodes = [_to_dict(*_process_line(line)) for line in bbt_file]
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
            if random.random() > 0.6:
                episode['viewed'] = False

def _process_line(episode_line: str):
    """
    Extrait et transtype les données à partir d'une ligne type csv.

    :param episode_line: Une ligne type csv
    :return: Un N-uplet (nom saison, saison, numéro d'épisode, titre d'épisode, durée, année)
    """
    show, season, episode, title, duration, year = episode_line.rstrip().split(';')
    return show, int(season), int(episode), title, int(duration), int(year)


def _to_dict(show, season, episode, title, duration, year):
    episode = {"title": title, "duration": duration}
    return episode


def get_movies():
    """
    Fonction permétant d'obtenir une liste de médias.
    """
    return [["The Philosopher's Stone", 152, True],
            ["The Chamber of Secrets", 161, True],
            ["The Prisoner of Azkaban", 142, False],
            ["the Goblet of Fire", 157, True],
            ["the Order of the Phoenix", 138, False],
            ["the Half-Blood Prince", 153, True],
            ["the Deathly Hallows – Part 1", 126, False],
            ["the Deathly Hallows – Part 2", 130, False]]

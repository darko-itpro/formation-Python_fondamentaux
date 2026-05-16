"""
Doc du module
"""

def is_viewed(episode:list) -> bool:
    """
    Retourne si l'épisode est vu ou pas.

    :param episode: Épisode avec les vus soit comptage soit booléen en 4ème positions
    :return: True si vu sinon False
    """
    try:
        return bool(episode[3])
    except IndexError:
        return False

def is_viewed_old(episode:list) -> bool:
    return len(episode) > 3 and bool(episode[3])


if __name__ == "__main__":
    print("coucou")
    print(__name__)

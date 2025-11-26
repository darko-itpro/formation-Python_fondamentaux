
def is_viewed(episode:dict):
    """
    explication de la fonction

    explication détaillée

    :param episode: explication du paramètre
    :return: explication du retour
    """
    try:
        return bool(episode["viewed"])
    except KeyError:
        return False

def add_to_playlist(episode: dict, playlist:list=None):
    if "title" not in episode:
        raise ValueError("This is not an episode")

    if playlist is None:
        playlist = []
    playlist = playlist.copy()

    playlist.append(episode)
    return playlist

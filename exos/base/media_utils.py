
def is_viewed(episode:dict):
    """
    explication de la fonction

    explication détaillée

    :param episode: explication du paramètre
    :return: explication du retour
    """
    return "viewed" in episode and bool(episode["viewed"])

def add_to_playlist(episode: dict, playlist:list=None):
    if playlist is None:
        playlist = []
    playlist = playlist.copy()

    playlist.append(episode)
    return playlist

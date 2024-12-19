

def is_viewed(episode:dict) -> bool:
    #return "viewed" in episode and bool(episode["viewed"])
    try:
        return bool(episode["viewed"])
    except KeyError:
        return False

def add_to_playlist(episode:dict, playlist:list[dict]=None):
    if "title" not in episode:
        raise ValueError("Data is not an episode (must contain key title)")

    if playlist is None:
        playlist = []
    else:
        playlist = playlist.copy()

    playlist.append(episode)
    return playlist


if __name__ == "__main__":
    pl1 = add_to_playlist({'title':'toto'})

    my_plylist = [{"title": "The Conjugal Configuration", "duration": 20, "viewed": True},
                  {"title": "The Conjugal Configuration", "duration": 20, "viewed": 3}]

    my_plylist = add_to_playlist({"title": "The other Conjugal Configuration", "duration": 20, "viewed": True},
                                 my_plylist)

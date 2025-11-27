from pprint import pprint
import pyflix.datasource as ds
import exos.base.media_utils as md

def get_first_unseen_episode(show:list[dict]):
    for index, episode in enumerate(show):
        if not md.is_viewed(episode):
            return index, episode

    return None

def get_playlist_from(show:list[dict]):
    try:
        index, _ = get_first_unseen_episode(show)
        return show[index:]
    except TypeError:
        return []


if __name__ == "__main__":
    show = ds.get_season('The Big Bang Theory', "Sheldon Cooper")

    remaining_time = 120

    playlist = get_playlist_from(show)
    len_ep_to_see = len(playlist)

    while playlist and remaining_time > playlist[0]["duration"]:
        episode = playlist.pop(0)
        print(episode['title'])
        remaining_time -= episode["duration"]
        episode["viewed"] = True

    pprint(show[-len_ep_to_see:])

import pyflix.datasource as ds
from pprint import pprint
import exos.base.media_utils as mu


def get_first_unseen_episode(episodes: list):
    for index, episode in enumerate(episodes):
        if not mu.is_viewed(episode):
            return index, episode
    return None

def get_playlist_from(episodes: list) -> list:
    index, _ = get_first_unseen_episode(episodes)
    return episodes[index:]

if __name__ == '__main__':
    my_show = ds.get_season('The Big Bang Theory', "Sheldon Cooper")

    playlist = get_playlist_from(my_show)

    time_remaining = 120

    while playlist and time_remaining > playlist[0]['duration']:
        episode = playlist.pop(0)
        print(episode["title"])
        episode["viewed"] = True
        time_remaining = time_remaining - playlist[0]['duration']

    print(time_remaining)

    pprint(my_show)
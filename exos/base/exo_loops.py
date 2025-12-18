from pprint import pprint
import pyflix.datasource as ds

from exos.base.media_utils import is_viewed


def get_first_unseen_episode(episodes:list) -> int:
    for index, episode in enumerate(episodes):
        if not is_viewed(episode):
            return index

def get_playlist_from(episodes:list):
    return episodes[get_first_unseen_episode(episodes):]

def watch_episodes(episodes:list, max_duration:int):
    while episodes[0]['duration'] <= max_duration:
        episode = episodes.pop(0)
        print(episode['title'])
        max_duration -= episode['duration']
        episode["viewed"] = True

    return max_duration


if __name__ == "__main__":
    bbt_s12 = ds.get_season('The Big Bang Theory', "Sheldon Cooper")
    reamining_time = 120

    playlist = get_playlist_from(bbt_s12)
    watch_episodes(playlist, reamining_time)

    pprint(bbt_s12)

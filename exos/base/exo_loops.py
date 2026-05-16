import pyflix.datasource as ds
from pprint import pprint
import exos.base.media_utils as mu

def find_first_unseen_episode(episodes: list):
    for index, episode in enumerate(episodes):
        if not mu.is_viewed(episode):
            return index, episode
    return index, episode

def get_playlist_from(season: list) -> list:
    index, _ = find_first_unseen_episode(season)
    return season[index:]

if __name__ == "__main__":
    bbt_s12 = ds.get_season('The Big Bang Theory', "Sheldon Cooper")

    time_remaining = 120

    playlist = get_playlist_from(bbt_s12)
    print(len(playlist))

    while playlist and time_remaining > playlist[0]['duration']:
        episode = playlist.pop(0)
        print(episode['title'])
        time_remaining -= episode['duration']
        episode['viewed'] = True

    pprint(bbt_s12)



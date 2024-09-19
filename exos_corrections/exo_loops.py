from pprint import pprint
import pyflix.datasource as ds
import exos_corrections.pyflix_dict as ep_tools
from exos.exo_03_02 import episode


def get_playlist_from(episodes: list) -> list:
    for index, episode in enumerate(episodes):
        if not ep_tools.is_viewed(episode):
            return episodes[index:]

    return []


if __name__ == "__main__":
    my_season = ds.get_season("John Doe")
    remaining_time = 120

    my_playlist = get_playlist_from(my_season)

    while remaining_time > my_playlist[0]["duration"]:
        episode = my_playlist.pop(0)
        print(episode["title"])
        remaining_time = remaining_time - episode["duration"]

        episode['viewed'] = True

    print(remaining_time)

    pprint(my_season)


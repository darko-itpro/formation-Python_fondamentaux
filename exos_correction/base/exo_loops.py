from pprint import pprint
import pyflix.datasource as ds
import exos_correction.pyflix.episode_utils as ep

def get_playlist_from(episodes:list[dict]):
    for index, episode in enumerate(episodes):
        if not ep.is_viewed(episode):
            return episodes[index:]

    return []


if __name__ == "__main__":
    season = ds.get_season(user="Me", show_name="The Rings of Power")
    time_remaining = 120

    playlist = get_playlist_from(season)

    while playlist and time_remaining > playlist[0]["duration"]:
        episode = playlist.pop(0)
        print(episode["title"])
        time_remaining -= episode['duration']
        episode["viewed"] = True
    print(time_remaining)
    pprint(season)

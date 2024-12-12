from pprint import pprint
import logging

from demos import settings
import exo_corrections.base.episodes_utils as eu
import pyflix.datasource as ds

def get_playlist_from(season: list[dict]) -> list:
    for index, episode in enumerate(season):
        if not eu.is_viewed(episode):
            return season[index:]

    return []

if __name__ == "__main__":
    season = ds.get_season("The Big Bang Theory", "Sheldon")
    logging.info(f"Série de {len(season)} épisodes chargée")

    playlist = get_playlist_from(season)
    logging.info(f"Playlist de {len(playlist)} épisodes")
    logging.info(f"Premier épisode à voir : '{playlist[0]['title']}'")

    start_index = len(season) - len(playlist)

    remaining_time = 120

    while playlist and remaining_time >= playlist[0]['duration']:
        episode = playlist.pop(0)
        print(episode['title'])
        remaining_time -= episode["duration"]
        episode['viewed'] = True

        logging.info(f"Durée restante : {remaining_time}")

    pprint(season[start_index:])




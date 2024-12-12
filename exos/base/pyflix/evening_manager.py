import exo_corrections.base.episodes_utils as eu

def get_playlist_from(season: list[dict]) -> list:
    for index, episode in enumerate(season):
        if not eu.is_viewed(episode):
            return season[index:]

    return []

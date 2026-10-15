def is_viewed(episode:dict) -> bool:
    return "viewed" in episode and bool(episode["viewed"])


def get_first_unseen_episode(episodes: list) -> int:
    index = 0
    for index, episode in enumerate(episodes):
        if not is_viewed(episode):
            return index
        
    return index



def get_playlist_from(season:list) -> list:
    return season[get_first_unseen_episode(season):]

def get_playlist_brut_style(season:list):
    for index, episode in enumerate(season):
        if not is_viewed(episode):
            extract = season[index:]
    else:
        extract = []
        
    return extract

import pyflix.datasource as ds


def medias_duration(episodes:list, episode_duration):
    return len(episodes) * episode_duration


def max_episodes_playlist(episodes:list, max_duration: int, episode_duration:int):
    max_episodes = max_duration // episode_duration
    return episodes[:max_episodes]


if __name__ == "__main__":
    bbt_s12 = ds.get_season()
    EPISODE_DURATION = 23

    print("La saison a une durée de {} minutes".format(medias_duration(bbt_s12, EPISODE_DURATION)))

    print("-- Ma soirée --")

    playlist = max_episodes_playlist(bbt_s12, 120, EPISODE_DURATION)
    print(playlist)

    print("-- Playlist Utilisteur --")

    playlist = bbt_s12.copy()


    print(playlist.pop(0))

    print(medias_duration(playlist, EPISODE_DURATION), medias_duration(bbt_s12, EPISODE_DURATION))
    print(id(bbt_s12) == id(playlist))
    print(bbt_s12 is playlist)

from pprint import pprint
import pyflix.datasource as ds

def collection_duration(episodes:list, episode_duration:int):
    return len(episodes) * episode_duration

def evening_playlist(episodes:list, evening_duration:int, episode_duration:int):
    return episodes[:evening_duration // episode_duration]

if __name__ == "__main__":
    bbt_s12 = ds.get_season()
    EPISODE_DURATION = 23

    print('Durée totale :', collection_duration(bbt_s12, EPISODE_DURATION))

    remaining_time = 120
    print('Playlist du soir :')
    pprint(evening_playlist(bbt_s12, remaining_time, EPISODE_DURATION))

    playlist:list = bbt_s12.copy()

    print(playlist.pop(0))

    print(collection_duration(playlist, EPISODE_DURATION), collection_duration(bbt_s12, EPISODE_DURATION))
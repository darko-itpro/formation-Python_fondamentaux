from pprint import pprint
import pyflix.datasource as ds
from exos.base.media_utils import is_viewed



if __name__ == "__main__":
    bbt_s12 = ds.get_season('The Big Bang Theory', "Sheldon Cooper")

    pprint(bbt_s12)


def get_first_unseen_episode(episodes:list) -> int:
    for index, episode in enumerate(episodes):
        if not is_viewed(episode):
            return index
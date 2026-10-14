import pyflix.datasource as ds

from pprint import pprint

import pyflix.media_utils as mu

season = ds.get_season('The Big Bang Theory', "Sheldon Cooper")

pprint(mu.get_playlist_from(season))
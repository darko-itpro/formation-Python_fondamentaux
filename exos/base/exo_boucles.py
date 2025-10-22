import exos.base.episode_utils as eu
import pyflix.datasource as ds

bbt_s12 = ds.get_season('The Big Bang Theory', "Sheldon Cooper")

playllist = eu.get_playlist_from(bbt_s12)



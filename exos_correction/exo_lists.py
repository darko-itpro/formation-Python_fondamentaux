import pyflix.datasource as ds
from pprint import pprint

bbt_s12 = ds.get_season()

print(len(bbt_s12))

playlist = bbt_s12.copy()

playlist.pop(0)
print(len(playlist), len(bbt_s12))

print(id(playlist) == id(bbt_s12))
print(playlist is bbt_s12)


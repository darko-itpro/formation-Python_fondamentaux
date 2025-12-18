from pprint import pprint
import pyflix.datasource as ds

pprint(ds.get_movies())

pprint( [movie[0] for movie in ds.get_movies()] )

pprint( [title for title, _, viewed in ds.get_movies() if not viewed] )

print(divmod(sum([duration for _, duration, _ in ds.get_movies()]), 60))
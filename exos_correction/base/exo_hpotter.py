from pprint import pprint
import pyflix.datasource as ds

pprint( [movie[0] for movie in ds.get_movies()] )

pprint( [title
         for title, _, viewed in ds.get_movies()
         if not viewed] )

print( sum([duration for _, duration, _ in ds.get_movies()]) )

print( divmod(sum([duration for _, duration, _ in ds.get_movies()]), 60) )

print( "Un marathon a une durée de {}h{:02}".format(*divmod(1159, 60)) )

print( "Un marathon a une durée de {}h{:02}"
       .format(*divmod(sum([duration
                            for _, duration, _ in ds.get_movies()]), 60))
       )
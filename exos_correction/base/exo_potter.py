import pyflix.datasource as ds

print( [movie[0]
        for movie in ds.get_movies()] )

print( [title
        for title, _, viewed in ds.get_movies()
        if not viewed])

print(divmod(sum([duration
                  for _, duration, _ in ds.get_movies()]), 60))


duration = (19, 19)
print("Le marathon a une durée de {}h{:02}".format(*duration))

print("Le marathon a une durée de {}h{:02}".format(*divmod(sum([duration
                  for _, duration, _ in ds.get_movies()]), 60)))
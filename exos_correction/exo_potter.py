import pyflix.datasource as ds

print(ds.get_movies())

print( [episode[0] for episode in ds.get_movies()] )
print( [title
        for title, _, viewed in ds.get_movies()
        if not viewed] )

print("Un marathon Harry Potter dure {:02}h{:02}".format(*divmod(
    sum([duration
         for _, duration, viewed in ds.get_movies()]
        ),
    60))
)

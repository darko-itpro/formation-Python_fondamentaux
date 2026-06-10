import pyflix.datasource as ds

print(" Noms titres ")
print(  [movie[0].title()
         for movie in ds.get_movies()]  )

print(" Restant à voir ")
print(  [title
         for title, _, viewed in ds.get_movies()
         if not viewed]  )

print(" Durée marathon ")

print( sum([duration for _, duration, _ in ds.get_movies()]) )

print( "Le marathon a une durée de {:02}h{:02}".format(
    *divmod(sum([duration for _, duration, _
                 in ds.get_movies()]),
            60))
)
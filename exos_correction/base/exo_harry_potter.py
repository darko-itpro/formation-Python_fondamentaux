import pyflix.datasource as ds

hpotter = ds.get_movies()

print(
    [movie[0] for movie in hpotter]
)

print(
    [title for title, _, viewed in hpotter if not viewed]
)

print(
    "Un marathon a une durée de {}h{:02}".format(*divmod(sum((duration for _, duration, _ in hpotter)), 60))
)

from pprint import pprint

import pyflix.datasource as ds

movies = ds.get_movies()

# Première question

print("Liste des titres")
pprint([title for title, _, _ in movies])

print("-----")

# Seconde question

print("Liste des titres qu'il me reste à voir")
pprint([title for title, _, seen in movies if not seen])

print("-----")

# Troisième question

print("Durée marathon Harry Potter")
print(sum([duration for _, duration, _ in movies]))
print("Durée marathon Harry Putter qu'il me reste à voir")
print(sum([duration
           for _, duration, seen in movies
           if not seen]))

print("-----")

# Bonus : soigner la présentation (ce n'était pas demandé)
marathon_duration = sum([duration for _, duration, _ in movies])

# Obtenir les informations de durée en heures et minutes (ouio, c'est 19h19)
print(divmod(marathon_duration, 60))

# Afficher ces informations corectement formaté :
print("Le marathon Harry Potter a une durée de {}h{:02}".format(*divmod(marathon_duration, 60)))


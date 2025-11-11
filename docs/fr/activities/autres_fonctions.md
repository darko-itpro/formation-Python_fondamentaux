# Quelques fonctions de plus…

Nous allons ajouter deux fonctions.

## Une fonction pour suivre le visionnage
Écrivez une fonction `view_episode(episode: dict)` qui incrémente (de 1) le nombre de vus de 
l'épisode passé en argument. Vous pouvez reprendre le jeu de données vu précédemment pour les tests.

## Une fonction pour gérer une playlist
Nous voulons gérer la notion de *playlist* soit une liste d'épisodes choisis par l'utilisateur.

Dans les exercices suivants, un épisode sera un dictionnaire contenant au moins une clefs `"title"`.

Une *playlist* sera simplement une liste. Pour la gérer, nous allons créer une fonction qui 
ajoutera un épisode à cette *playlist*. Cette fonction doit prendre deux paramètres.

Créez la fonction `add_to_playlist(episode: dict, playlist: list)`. Faites plusieurs appels pour 
ajouter plusieurs épisodes. Une playlist peut contenir plusieurs occurrences d'un même épisode.


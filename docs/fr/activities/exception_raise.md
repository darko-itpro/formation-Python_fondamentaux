# La levée d'exception

## Aide mémoire
Lever une exception se fait par appel à l'instruction `raise` :
```python
raise ValueError('un message d'erreur')
```

Vous trouverez la liste des exceptions sur [la page de la documentation des exceptions](https://docs.python.org/3/library/exceptions.html).

## Fichiers de travail
Pour les exercices de cet énoncé, vous allez travailler avec le fichier contenant la fonction
`add_to_playlist()`.

## Exercice
Nous allons ajouter une petite validation à cette fonction. Elle ne doit ajouter que des 
dictionnaires représentant des épisodes soit des dictionnaires possédant la clef `"title"`. 

Commencez par modifier votre fonction pour qu’elle adopte ce comportement.

Le code appelant doit savoir que l'ajout n'a pas été fait. Faites donc lever une exception dans ce 
cas.
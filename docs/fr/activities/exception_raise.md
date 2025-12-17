# La levée d'exception

## Aide mémoire
Lever une exception se fait par appel à l'instruction `raise` :
```python
raise ValueError("un message d'erreur")
```

Vous trouverez la liste des exceptions sur [la page de la documentation des exceptions](https://docs.python.org/3/library/exceptions.html).

## Fichiers de travail
Pour les exercices de cet énoncé, vous allez travailler avec le fichier contenant la fonction
`add_to_playlist()`.

## Exercice
Dans [l'exercice sur les listes](listes_2.md), vous avez créé une fonction calculant la durée d'une
liste d'épisode. Cette fonction prends en paramètres la liste et la durée des épisodes.

Cette durée doit être positive. Modifiez la fonction pour que si une durée négative ou nulle est 
passée, la fonction lève une exception de type `ValueError`. 
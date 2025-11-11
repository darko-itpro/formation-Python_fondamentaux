# Introduction aux fonctions

## Aide mémoire
La structure d’une fonction est

```python
def nom_fonction(param1, param2,):
    value = some_code()
    return value
```

Une fonction prends de 0 à n paramètres. Le retour est optionnel, si omis, la fonction retourne par
défaut `None`.

## Fichiers de travail
Pour les exercices de cet énoncé, vous allez reprendre le contenu des deux fichiers suivants :

 * `exos/exo_03_01.py` sur lequel vous avez travaillé.
 * `exos/exo_03_02.py` sur lequel vous avez travaillé.
 * `exos/exo_04.py` que vous allez créer

Après avoir créé le fichier `exos/exo_04.py`, recopiez-y les données des fichiers précédents. Vous
devrez renommer un des couples pour différencier celles avec un booléen de celles avec un entier.

## Création d’une fonction
Nous avons souhaité dans l’exercice précédent tester le code avec plusieurs données. Afin de
faciliter cette étape, nous allons déporter le code dans une fonction.

### Première version
Écrivez une fonction `is_viewed(episode)` qui affiche si l’épisode a été vu ou non. Pour un épisode
de titre Episode 1, l'affichage attendu est :

```sh
Episode 1
Cet épisode a été vu
```

ou

```sh
Episode 1
Cet épisode n'a pas été vu
```

### Bonne pratique avec les fonctions
Une bonne fonction ne fait qu’une seule chose (et la fait bien). Notre fonction en fait 2 : elle
détermine un état et affiche celui-ci. Ceci est une mauvaise pratique car :

 * si nous exécutons la fonction dans un environnement sans terminal, nous ne pouvons pas voir la
   valeur (sur un serveur, cette sortie est détruite).
 * si nous souhaitons obtenir cette valeur pour en faire quelque chose… et bien nous ne pouvons pas.

Il est donc préférable qu’une fonction qui calcule une valeur se contente de retourner cette valeur.
Un autre composant s’occupera d’en faire autre chose.

### Seconde version
Modifiez cette fonction pour qu’elle retourne `True` ou `False` en fonction du statut de l’épisode.
Le comportement global doit rester le même.
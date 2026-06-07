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

 * `exos/base/exo_03_01.py` sur lequel vous avez travaillé.
 * `exos/base/exo_04.py` que vous allez créer

Après avoir créé le fichier `exos/base/exo_04.py`, recopiez-y le contenu du fichier `exos/base/exo_03_01.py`.

## Création d’une fonction
Nous allons déplacer le code dans une fonction.

### Première version
Écrivez une fonction `is_viewed(episode:list) -> None` qui affiche si l’épisode a été vu ou non. 
Pour un épisode de titre Episode 1, l'affichage attendu est :

```sh
Episode 1
Cet épisode a été vu
```

ou

```sh
Episode 1
Cet épisode n'a pas été vu
```

---

### Bonne pratique avec les fonctions
Une bonne fonction ne fait qu’une seule chose (et la fait bien). Notre fonction en fait 2 : elle
détermine un état et affiche celui-ci. Ceci est une mauvaise pratique car :

 * si nous exécutons la fonction dans un environnement sans terminal, nous ne pouvons pas voir la
   valeur (sur un serveur, cette sortie est détruite).
 * si nous souhaitons obtenir cette valeur pour en faire quelque chose… et bien nous ne pouvons pas.

Il est donc préférable qu’une fonction qui calcule une valeur se contente de retourner cette valeur.
Un autre composant s’occupera d’en faire autre chose.

---

### Seconde version

Modifiez cette fonction pour que sa signature devienne `is_viewed(episode:list) -> bool` et retourne 
donc `True` ou `False` en fonction du statut de l’épisode. 

Le comportement global doit rester le même.

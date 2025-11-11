# Les listes

## Avant de commencer
Pour cet exercice et certains exercices suivants, vous aurez besoin d'une ressource supplémentaire
qui vous est fournie sous forme d'une bibliothèque à installer. Celle-ci n'est pas sur les repos
standard, elle est disponible sous forme d'un projet,
[Pyschool Lib](https://github.com/darko-itpro/pyschool-lib) Les instructions d'installation sont
disponibles dans le README.

## Présentation
Nous allons lancer un service de streaming vidéo, PyFlix, un peu comme Netflix mais en Python. Nous
allons donc gérer un catalogue.

Le module `pyflix.datasource`  contient une fonction nommée `get_season()` qui retourne la liste des
titre des épisodes de la saison 12 de Big Bang Theory. Nous allons extraire des informations de
cette liste.

Pour l'utilisation de cette fonction, vous pouvez consulter
[la page dédiée du wiki](https://github.com/darko-itpro/pyschool-lib/wiki/Le-module-pyflix.datasource)

### Créez une référence de la donnée
Affectez le retour de cette fonction à une variable `bbt_s12`. Il s’agit de la donnée de référence
de la saison chargée en mémoire dans votre module.

Nous utiliserons cette variable pour les questions suivantes (vous ne devez plus rappeler la
fonction pour ne pas surcharger le serveur). Les questions suivantes restent indépendantes entre elles.

### Astuce : afficher des collections
Pour afficher la collection, vous verrez que la fonction `print()` n’est pas adaptée. Elle affiche
le contenu de la liste sur une seule ligne, ce qui n’est pas *pratique* pour voir son contenu.
Pour voir le contenu de la liste, je vous propose d’utiliser la fonction
`pprint()` du module `pprint` :

```python
from pprint import pprint

pprint(bbt_s12)
```

Cette fonction a un nom qui ne rentrera pas en collision avec la fonction `print()`, vous pouvez
donc l’importer directement.

### Calculez la durée de la saison

Nous considérons que chaque épisode dure 23 minutes, combien de temps dure la saison ?

Pour cela, écrivez une fonction qui prends en argument (au moins) une liste d’épisodes et retourne
la durée de cette liste d’épisodes.

### Gérez votre playlist du soir
Nous voulons obtenir une liste des premiers épisodes dont la durée totale est inférieure ou égale à
une durée.

Pour cela, vous devez créer une fonction avec comme paramètre (au moins) une liste d’épisodes
(liste_ep) et cette durée maximum (d_max). Cette fonction doit retourner la liste des N premiers
épisodes de liste_ep où N est le nombre maximum d’épisodes à regarder. N étant un maximum.

Note : "liste_ep" et "d_max" sont utilisées ici pour référencer les données, vous pouvez utiliser
des noms plus adaptés comme paramètres.

Utilisez cette fonction avec `bbt_s12` comme argument et une durée de 2 heures.

### La playlist utilisateur
Les utilisateurs souhaitent suivre leur avancée dans une série, nous allons gérer ça sous forme
d’une *playlist* qui sera une copie de la saison. Le prochain épisode à regarder est le premier de
la playlist. Dès qu’il est vu, il est supprimé de la playlist.

Créez  une copie de la liste de la saison 12 (`bbt_s12`) dans une variable `playlist` (peu importe
si le nom était déjà utilisé pour la liste précédente).

Pour simuler la vision d’un épisode (le premier de la playlist), affichez simplement son titre. En
même temps, supprimez-le de la playlist. Vous pouvez bien entendu utiliser une fonction pour cela,
fonction qui prends en argument une liste d’épisodes.

La playlist ne contient que les épisodes restant à voir (actuellement un de moins que la série
complète). Utilisez la fonction qui calcule la durée pour afficher la  durée des épisodes restant
et de la saison complète pour comparer les deux valeurs.

Que remarquez-vous ?

# Les boucles

## Prérequis
Vous aurez besoin du package [pyflix](../pyflix.md)

## Objectifs
Dans cet exercice, nous allons simuler le comportement du media-center PyFlix.

La fonction  `get_season()` du module `pyflix.datasource` peut prendre deux paramètres, le premier
est le nom d'une série, le second est le nom (ou identifiant) d’un utilisateur. La signature de la
fonction est `get_season(show_name: str = None, user: str = None)`.

Nous récupérons alors la liste des épisodes. Chaque épisode est un dictionnaire.

Vous pouvez obtenir les épisodes de The Big Bang Theory de la manière suivante :
```python
pyflix.datasource.get_season('The Big Bang Theory', "Sheldon Cooper")
```

Nous voulons dans un premier temps écrire une fonction qui prends une saison complète en paramètre
et retourne la liste des épisodes restant à voir, c’est à dire l’extrait de la liste à partir du
premier épisode non vu.

Vous pouvez récupérer la liste des épisodes de Big Bang Theory pour vous faire des jeux de données.
Le retour de cette fonction servira de donnée "de prod’".

## Obtenir la liste des épisodes à voir
Écrivez une fonction `get_playlist_from(season: list) -> list` qui retourne la liste des épisodes
restant à voir. Cette liste commence à partir du premier épisode non vu jusqu’à la fin. Cette
fonction retourne donc une liste d’épisodes qui peut être vide si nous n'avons plus d'épisodes à
voir.

Vous êtes encouragé à utiliser les tests pour, d'une part, valider votre code et d'autre part, pour
vous aider à concevoir le modèle par une approche TDD. Si par cette démarche vous faites apparaitre
d'autres fonctions *intermédiaires*, c'est normal. Gardez-les et utilisez-les.

### Vous coincez ?
Si vous avez des difficultés à répondre à la question, vous pouvez consulter les indices suivants :
Les étapes de votre fonction devraient être :
<details>
<summary>Indice 1</summary>
Itérer sur les épisodes. Vous pouvez afficher chaque épisode pour valider que vous le faites.
</details>
<details>
<summary>Indice 2</summary>
Identifier les épisodes que vous n’avez pas vu. Vous pouvez n’afficher que ceux là lors de votre
itération pour valider votre code.
</details>
<details>
<summary>Indice 3</summary>
Identifier le premier épisode qu’il vous reste à voir. N’affichez alors que celui-là ou mieux,
écrivez le test qui démontre que que vous l'avez trouvé. La fonction retourne alors cet épisode.
</details>
<details>
<summary>Indice 4</summary>
Déterminer l’indice de cet épisode
</details>
<details>
<summary>Indice 5</summary>
Utiliser cet indice pour créer grâce au slicing une nouvelle liste des épisodes qu’il reste à voir.
</details>

## Ma soirée…
J’ai à nouveau 2 heures ce soir et je souhaite regarder des épisodes qu'il me reste à voir. Je veux
regarder le maximum d'épisodes en entier, c'est à dire que je dois finir l'épisode dans le temps
disponible.

Vous allez récupérer tous les épisodes d'une saison grâce à la fonction
`get_season(show_name: str = None, user: str = None)`. Fournissez bien un paramètre `name` pour
obtenir une liste d’épisodes avec l'information vus/non vus. Conservez cette collection dans une 
variable.

Obtenez la liste des épisodes qu’il me reste à voir grâce à la fonction de la première partie. 
Utilisez une variable que vous appellerez `playlist` pour la référencer.

Nous allons ensuite simuler le fonctionnement d’un media-center. Affichez le titre de l’épisode 
suivant en le supprimant de la playlist. Répétez ceci pour autant d’épisodes que je peux regarder 
en 2 heures.

Consignes : commencez par résoudre le problème au plus simple. Si vous écrivez une fonction, soyez 
cohérent dans le choix des paramètres.
Vous pouvez afficher les listes en fin de programme pour valider le traitement.

## Évolution un peu avancée…
Lorsque vous supprimez un épisode de la playlist, basculez le flag vu/pas vu à `True` dans la liste 
de référence.

*Indice* : rappelez-vous qu’en Python, tout est référence…
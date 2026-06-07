# Les dictionnaires

Jusqu'ici, nous avons travaillé avec des données où un épisode est représenté sous forme d'une 
liste. Mais nous avons vu que certaines données peuvent manquer. Imaginons que nous puissions avoir
l'information de l'année de production en 5ème position, lorsque l'information vu/pas vu est 
absente, cela peut être ingérable :

```python
episode_not_viewed = ["The new Project", 1, 98, 0]
episode_not_viewed = ['Installing the softwares', 2, 42]
episode_not_viewed_with_year = ["The new Project", 1, 98, 0, 2026]
episode_not_viewed_with_year = ['Installing the softwares', 2, 42, 2026]
```

Une représentation de données sous forme de liste est obtenue dans certains cas comme lors de la
lecture de fichiers CSV ou l’interrogation de bases de données. Mais nous avons alors encore 
l'information des _colonnes_. Pour gérer les données, cette structure est "peu pratique".

Nous allons travailler sur des données structurées en dictionnaires. La donnée a été chargée sous 
forme de liste par un parser qui connait la source et la transformera en dictionnaire.

La structure de la donnée sera la suivante :

```python
{"title": "The Conjugal Configuration",
 "duration": 20,
 "viewed": 0,
 "year": 2026
}
```

Ainsi, une donnée peut être abente, nous le saurons par absence de sa clef.

## Fichiers de travail
Dans un cas réel, nous devrions faire une évolution et donc remplacer le contenu de
`exos/bases/media_utils_v1.py` par un traitement à l'aide de dictionnaires. Dans le cadre d'une 
formation, afin de conserver les exercices que vous avez réalisés, nous allons travailler dans un 
nouveau fichier, renommez ce fichier `exos/bases/media_utils.py` sans *version*, car c'est le fichier 
définitif. Nous allons également travailler avec une nouvelle arborescence de tests.

## Exercices
### Prise en main des dictionnaires
Commencer par vous faire la main sur cette donnée. Recopiez cette donnée dans un shell intéractif ou
un script de brouillon pour faire quelques actions :

 * Affichez le titre.
 * Modifiez son statut (il doit devenir "vu") et affichez la donnée. Bien que le statut "vu/non vu"
est un booléen, anticipez qu'il puisse être autre chose.

### Une fonction pour le statut
Un épisode non-vu possède la clef `viewed` associée à la valeur `False` ou ne possède pas cette clef.
Essayez de déterminer comment gérer la situation.

Dans le module `exos/bases/media_utils.py`, écrivez une fonction  `is_viewed(episode: dict)` qui 
prend un dictionnaire en paramètre et qui retourne `True` si l’épisode a été vu sinon `False`. 
N’hésitez pas à utiliser une approche *test-first* pour écrire cette fonction grâce aux données à 
disposition.

Voici une série d'exemples de données qui vous donnent les cas de test.

Épisodes vus :

```python
{"title": "The Conjugal Configuration", "duration": 20, "viewed": True}
{"title": "The Conjugal Configuration", "duration": 20, "viewed": 3}
{"title": "The Conjugal Configuration", "duration": 20, "viewed": 3, "year": 2019}
```

Épisodes non vus :

```python
{"title": "The Conjugal Configuration", "duration": 20, "viewed": False}
{"title": "The Conjugal Configuration", "duration": 20, "viewed": 0}
{"title": "The Conjugal Configuration", "duration": 20}
{"title": "The Conjugal Configuration", "duration": 20, "year":2018}
```

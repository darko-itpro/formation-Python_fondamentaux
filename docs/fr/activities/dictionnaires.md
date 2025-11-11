# Les dictionnaires

Après la mise en production, nous avons découvert qu'il pouvait y avoir deux structures de données
pour un épisode **non vu** :

```python
episode_not_viewed = ["The new Project", 1, 98, 0]
episode_not_viewed = ['Installing the softwares', 2, 42]
```

La première contient un entier représentant le nombre de vus en quatrième position et le second n’a
que 3 valeurs. Le problème vient de sources de données différentes.

Si vous utilisez cette seconde donnée avec votre fonction, elle lèvera une exception.

Une représentation de données sous forme de liste est obtenue dans certains cas comme lors de la
lecture de fichiers CSV ou l’interrogation de bases de données. Mais cette structure est
"peu pratique". Aussi, nous allons travailler sur des données structurées en dictionnaires.
La donnée a été chargée sous forme de liste par un parser qui connait la source et la transformera
en dictionnaire.

La structure de la donnée sera la suivante :

```python
{"title": "The Conjugal Configuration",
 "duration": 20,
 "viewed": 0}
```

## Fichiers de travail
Dans un cas réel, nous serions en train de faire une évolution pour remplacer le contenu de
`exos\media_utils.py` par un traitement à l'aide de dictionnaires. Dans le cadre d'une formation,
afin de conserver les exercices que vous avez réalisé, renommez ce fichier en
`exos\media_utils_legacy.py` ainsi que les tests associés. N'oubliez pas de mettre à jour les
import si votre IDE ne vous assiste pas.

## Exercices
### Prise en main des dictionnaires
Commencer par nous faire la main sur cette donnée. Recopiez cette donnée dans un shell intéractif ou
un script de brouillon pour faire quelques actions :

Affichez le titre.
Modifiez son statut (il doit devenir "vu") et affichez la donnée. Bien que le statut "vu/non vu"
est un booléen, anticipez qu'il puisse être autre chose.

### Une fonction pour le statut
Un épisode non-vu possède la clef `viewed` associé à la valeur `False` ou ne possède pas cette clef.
Essayez de déterminer comment gérer la situation.

Dans le module `exos\media_utils.py`, écrivez une fonction  `is_viewed(episode: dict)` qui prends un
dictionnaire en paramètre et qui retourne `True` si l’épisode a été vu sinon `False`. N’hésitez pas
à utiliser une approche *test-first* pour écrire cette fonction grâce aux données à disposition.

Voici 2 exemples de données qui vous donnent les cas de test.

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

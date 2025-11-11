# Les listes

## Fichiers de travail
Pour les exercices de cet énoncé, vous allez travailler avec les fichiers suivants :

 * `exos/base/exo_02.py` qui vous est fourni.

## Contexte
Pour un projet de service de streaming vidéo, PyFlix (un peu comme Netflix mais en Python), nous
devons étudier la gestion de données pour représenter un épisode d'une série.

Nous allons représenter un épisode de Stranger Code (une série exclusive) de la manière suivante :

```python
["The new Project", 1, 98, 0]
```

Un épisode est représenté par une liste où :

 * Le premier élément est le titre
 * Le second est le numéro de l’épisode
 * Le troisième est la durée
 * Le quatrième est un compteur représentant le nombre de fois que l'épisode a été vu.

Cette valeur est déclarée et affectée à une variable dans le fichier `exo_02.py`.

---

## Exercice
 * Affichez le titre de l’épisode.
 * Affichez sa durée.

Voyez si vous pouvez avoir un code « compréhensible ».

Enfin :

 * affichez le nombre de fois où l’épisode a été vu
 * incrémentez cette valeur de 1
 * affichez le nombre de fois où l’épisode a été vu
 * Incrémentez de nouveau plusieurs fois avec la même instruction.

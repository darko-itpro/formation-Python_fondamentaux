# Les conditionnelles, seconde partie

Les deux exercices sont indépendants.

## Fichiers de travail
Pour les exercices de cet énoncé, vous allez travailler avec les fichiers suivants :

 * `exos/media_utils.py` que vous avez créé précédemment (il est possible que durant la formation
   un autre nom soit choisi).

## Exercice
Après la mise en production, nous avons découvert qu'il pouvait y avoir deux structures de données
pour un épisode non vu :

```python
episode_not_viewed = ["The new Project", 1, 98, 0]
episode_not_viewed = ['Installing the softwares', 2, 42]
```

La première contient un entier représentant le nombre de vus en quatrième position et le second
n’a que 3 valeurs.

Si vous utilisez cette seconde donnée avec votre fonction `is_viewed(episode:list)`, elle lèvera
une exception.

Faite évoluer la fonction pour qu’un épisode n’ayant pas l’information « vu » (qui n’a donc que 3
données) soit considéré comme « non-vu ».

Vous êtes encouragés à utiliser les tests. Vous n’aurez donc qu'un test à ajouter avec cette
nouvelle donnée.
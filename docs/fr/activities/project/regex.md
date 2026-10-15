# Les expressions rationnelles

Nous allons travailler avec le contenu du répertoire `/assets/files/`. Dans les exercices 
[sur les fichiers](files.md), vous avez créé une fonction pour obtenir le contenu de ce répertoire.

Le nom de chaque fichier a une structure bien définie :

```text
NOM_SERIE-sXXeYY-TITRE_EPISODE
```

où :

* `NOM_SERIE` est le nom de la série
* `XX` est le numéro de saison
* `YY` est le numéro de l'épisode
* `TITRE_EPISODE` est le titre de l'épisode

Créez une fonction qui, à partir de chaque nom de fichier, retourne une liste 
`[NOM_SERIE, TITRE_EPISODE, NUMERO_SAISON, NUMERO_EPISODE]` avec chaque donnée dans son bon type.
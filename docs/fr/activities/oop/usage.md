# Charger des données

Afin de vous permettre d'expérimenter le modèle objet, la lib de support vous fournit de quoi
alimenter ce modèle en données.

## Utiliser le modèle
Pour alimenter ce modèle avec des données, vous disposez d'une fonction (un générateur)
`pyflix.datasource.load_show(name=None)` dans la bibliothèque `pyschoollib`. Vous pouvez l'utiliser
de la manière suivante :

```python
import pyflix.datasource as ds

for episode_data in ds.load_show():
    pass
```

La donnée `episode_data` est un N-uplet contenant :

 - le nom de la série
 - le titre de l'épisode
 - le numéro de la saison de l'épisode
 - le numéro de l'épisode
 - la durée de l'épisode
 - l'année de diffusion de l'épisode

Sans fournir d'argument pour `name`, la fonction _retourne_ toutes les données pour toutes les
séries connues.

Vous pouvez fournir un argument à `name` qui doit être un nom de série et donc filtrer sur cette
série. Vous pouvez obtenir la liste des séries connues par `pyflix.datasource.get_shows_names()`.

Un exemple réel d'usage peut être :

```python
import pyflix.datasource as ds

show = TvShow("Arcane")

for episode_data in ds.load_show():
    show.add_episode(*episode_data[1:])
```

## Un pipeline
Dans le code à votre disposition, vous avez un scripte qui exploite les différents composants
abordés afin de charger les données d'un CSV pour alimenter les objets de connexion aux bases de
données SQLite. Vous pouvez l'exécuter avec :

```python
python -m demos.pyflix
```

Vous pouvez modifier le module `demos.pyflix.load_and_display` pour utiliser votre implémentation
de la *médiathèque*… si vous avez bien respecté les specs.

## Un modèle plus complet
Le modèle suivant ajoute la classe `Playlist`.

```mermaid
classDiagram
    direction LR
    class TvShow{
        +name : str
        +episodes : Episode[*] 
        +add_episode(title, season_number, number, duration, year)
    }
    class Episode{
        +title : str
        +number : int
        +season_number : int
        +duration=None : int
        +year=None : int
    }
    class Playlist{
        +name : str
        +episodes : Episode[*] 
        +add_episode(Episode episode)
        +watch_next_episode()
    }
    TvShow "1" --> "*" Episode : "Contient"
    Playlist "1" --> "*" Episode
```
Le constructeur de `Playlist` est similaire à celui de `TvShow`. La méthode `add_episode()` accepte un objet de type `Episode` car il doit provenir d'un `TvShow`.

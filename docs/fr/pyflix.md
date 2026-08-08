# Le package Pyflix

Pour certains exercices, il vous est demandé d'utiliser le module `pyflix.datasource`. Ce module est
dans un package dédié qui doit être _installé_.

## Précision sur la structure du projet
Le package `pyflix` est dans le répertoire `src`. Cette structure _src-based_ est typique d'un 
projet destiné au packaging. Le fichier de configuration `pyproject.toml` est configuré pour créer 
un package avec le contenu du répertoire `src`. Si on se limite à la configuration, le projet 
actuel tient dans le contenu du `src`.

Et en soi, c'est un _hack_ pour la formation car nous allons utiliser l'approche packaging en mode 
_éditable_. Ceci permet d'éditer le code et voir immédiatement le résultat.

## Installation du package

Assurez-vous d'être dans l'environnement virtuel et exécutez :

```bash
pip install -e .
```

## Utilisation de la bibliothèque

Dans un script Python ou dans le shell intéractif (ou iPython), vous pouvez importer le module 
`pyflix.datasource` :

```python
import pyflix.datasource as ds
```

Vous disposez alors d'un certain nombre de fonctions qu'il vous sera demandé d'utiliser dans 
certains exercices.

## Ressources pour l'utilisation

 * Une [documentation du module](https://darko-itpro.github.io/pyschool-lib/fr/api/pyflixdatasource/).
 * Des [exemples d'usage](https://darko-itpro.github.io/pyschool-lib/fr/tutos/data_load/) pour le
   chargement des données lors de la partie Programmation Orientée Objet.
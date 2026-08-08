# Résolution du problème de chemin : le package éditable

Dans l'exercice précédent, il vous a été demandé de déplacer la fonction dans le fichier 
`exos/media_utils_v1.py`. Essayez maintenant de l'utiliser à partir des fichiers de travail 
dans `exos/`. Si vous exécutez vos scripts à partir de PyCharm, ça va passer. Avec VS Code, non.
Si vous essayez à partir d'un termina avec `python exos/monscript.py`, ça ne passe pas non plus.

Ceci provient du problème des chemins construits par Python. Si l'exécution de la ligne de commande 
se corrige en utilisant `python -m exos.monscript`, ce n'est pas le cas pour l'exécution dans 
certains IDEs comme VS Code. Pour VS Code, il existe des solutions en configurant la création 
automatique avant chaque exécution d'une variable d'environnement `PYTHONPATH` qui référence la 
racine du projet. Mais il y a plus simple et _sécurisé_ en passant par le packaging.

## Un projet Python orienté packaging.
Un projet Python _orienté packaging_ a une structure _src-based layout_ au lieu de l'historique 
_flat layout_. Le répertoire `src` du porjet contient l'arborescence destinée à être packagée. Dans 
notre cas, c'est le projet serait le projet **pyflix** avec le module racine `pyflix`.

Pour que Python sache packager un projet, il lui faut un certain nombre d'informations qui sont 
déclarées dans le fichier `pyproject.toml`. Ce fichier est correctement configuré.

Le projet actuel peut créer un package qui contiendra l'arborescence du répertoire `src`. Mais ceci 
ne résoud pas le problème du développement.

## Installer le package en mode _éditable_.
Python apporte une solution : travailler dans la structure du package, comme en package, mais 
éditable. Pour cela, Python a une option qui permet de ne pas installer le projet mais de créer une
référence vers le projet au sein des packages.

Ainsi, dans un terminal, exécutez la commande :

```bash
pip install -e .
```

Ceci va donc _installer_ le projet `src` en mode éditable. Lorsque vous aurez un 
`import pyflix.module` dans vos scripts, Python ira chercher le code dans `src`. Ainsi, toute 
modification de `src/pyflix` est immédiatement disponible.

# A Python Training - Les bases

This is the practical cases for Python training I provide. Intended for french trainee, the rest of the explanations
are in french.

Ce référentiel complète la formation que je propose et est donc destiné à mes stagiaires. 

[![License](https://img.shields.io/github/license/darko-itpro/training-python.svg?style=plastic)](https://github.com/darko-itpro/training-python/blob/master/LICENSE)

Ces sources sont organisées pour proposer des exemples de code sur les thèmes couverts par les formations de base
Python. Elles respectent avec quelques adaptations l'organisation d'un package.

## Mise en place de l'environnement

### Prérequis
[Python](https://www.python.org) doit être installé sur votre poste. Si Python n'est pas présent,
vous pouvez l'installer à partir du site de la fondation sur le lien précédent.

La formation est prévue pour une version de Python 3.6+.

Python ainsi que les dépendances doivent être dans le PATH. Vous pouvez vérifier le bon
fonctionnement dans un terminal/invite de commande par les instructions

```
python --version
python -m pip --version
```

### Environnements de développement
Python ne nécessite aucun IDE en particulier.

Les environnements conseillés sont [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/)
et [Visual Studio Code](https://code.visualstudio.com/).

PyCharm est un environnement dédié à Python, il intègre donc un certain nombre d'outils. VS Code
nécessite l'installation d'un plug-in pour la prise en charge de Python.

## Récupérez le projet
Le projet peut être dans l'arborescence que vous souhaitez sur votre disque.

## Environnement virtuel
Un environnement virtuel permet d'isoler l'environnement du projet de votre environnement système. Il permet ainsi
d'éviter les conflits de dépendance et facilite l'exécution des programmes Python indépendament des versions de
l'interpréteur.

Créer un environnement virtuel n'est pas indispensable.

Il y a deux moyens de créer un environnement virtuel : par l'invite de commande ou par les outils intégrés des IDE
(PyCharm dans notre cas).

Par invite de commande, il suffit de se placer dans le répertoire du projet et d'exécuter l'instruction suivante :
```
python -m venv venv
```

Vous devez utiliser la version de l'interpréteur pour laquelle vous voulez créer un environnement virtuel. Ainsi, si
*python* pointe sur du 2.7 et que pour exécuter l'interpréteur python 3.6, il faut exécuter *python3.6*, l'instruction
est :
```
python3.6 -m venv venv
```

Le second *venv* est le nom du répertoire qui sera créé. Celui-ci contiendra toute la configuration de l'environnement
virtuel. Le nom *venv* est attribué par convention, celui-ci est par défaut dans les fichiers comme les git ignore.

Activer un environnement virtuel dépend de votre système, le plus simple est de consulter
[la documentation](https://docs.python.org/fr/3/library/venv.html).

### Installation de dépendances
[pip](https://pypi.python.org/pypi/pip) est le gestionnaire de dépendances qui va vous permettre
d'installer les dépendances nécessaires à ce projet.

**Attention** : `pip` utilise des ports dédiés pour communiquer avec les dépôts. Si vous êtes
derrière un Firewall, il sera nécessaire de lui communiquer le proxy.

Vous pouvez installer une dépendance spécifique par l'instruction

```shell
pip install ipython
```

Cette commande permet d'installer la dépendance `ipython`.

Les dépendances nécessaires au projet sont déclarées dans le fichier `requirements.txt`. Vous pouvez
donc tout installer avec la commande :

```shell
pip install -r requirements.txt
```
ou
```
python -m pip install -r requirements.txt
```

Votre environnement contient alors toutes les dépendances nécessaires.
 
## Documents d'illustration

Certains fichiers ont l'extension `.ipynob`. Il s'agit de documents de type *Jupyter Notebooks*
générés à l'aide de [Jupyter](http://jupyter.org/). Pour pouvoir les utiliser, vous devez avoir
installé la dépendance (vois section précédente).
 
Pour accéder à ces documents, il faut lancer le serveur Jupyter par la commande :

```
jupyter notebook
```
ou
```
python -m jupyter notebook
```

## Dépendances du projet
Le fichier requirements liste les dépendances nécessaires au projet dans son
ensemble. Il s'agit de :
 * [jupyter](https://jupyter.org/) : Jupyter sera utilisé pour ses notebooks,
 pratique en tant que cahier d'exercices
 * Pytest : utilisé pour la partie tests unitaires
 * Pytz : utilisé pour la gestion des TimeZone des dates.
 
## Ressources

Durant la formation, des ressources complémentaires peuvent être disponibles
[sur le partage suivant](https://goo.gl/lRyzMZ).

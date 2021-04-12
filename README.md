# A Python Training - Les bases

This is the practical cases for Python training I provide. Intended for french trainee, the rest of the explanations
are in french.

Ce référentiel complète la formation que je propose et est donc destiné à mes stagiaires. 

[![License](https://img.shields.io/github/license/darko-itpro/training-python.svg?style=plastic)](https://github.com/darko-itpro/training-python/blob/master/LICENSE)

Ces sources sont organisées pour proposer des exemples de code sur les thèmes couverts par les formations de base
Python. Elles respectent avec quelques adaptations l'organisation d'un package.

## Mise en place de l'environnement

### Prérequis
[Python](https://www.python.org) doit être installé sur votre poste.

La formation est prévue pour une version de Python 3.6+. Certains codes peuvent illuster des fonctionalités plus
récentes. Une version de Python plus récente permettra de tester ces codes mais n'est pas indispensable.

Python ainsi que les dépendances doivent être dans le PATH. Vous pouvez vérifier le bon fonctionnement dans un
terminal/invite de commande par les instructions

```
python --version
python -m pip --version
```

### Prérequis : les environnements de développement
Python ne nécessite aucun IDE en particulier et cette formation n'impose aucun outil.

La formation sera illustrée sur [PyCharm](https://www.jetbrains.com/fr-fr/pycharm/)
et [Visual Studio Code](https://code.visualstudio.com/). Ce dernier n'est pas dédié à Python et nécessite l'installation
du plug-in.

PyCharm possède plus de fonctionalités intégrées qui facilitent la vie du développeur mais le plug-in pour Visual Studio
Code évolue rapidement.

### Récupérez le projet
Le projet peut être dans l'arborescence que vous souhaitez sur votre disque.

### Configurez un environnement virtuel
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

Activer un environnement virtuel dépend de votre système, le plus simple est de consulter [la documentation](https://docs.python.org/fr/3/library/venv.html).

### Installez les dépendances
Dans un premier temps, vous n'aurez pas besoin de dépendances.

[pip](https://pypi.python.org/pypi/pip) est le gestionnaire de dépendances qui va nous permettre d'installer tout ce
qui est nécessaire à ce projet. Placez vous alors à la racine du projet et saisissez

```
pip install -r requirements.txt
```
ou
```
python -m pip install -r requirements.txt
```

Votre environnement contient alors toutes les dépendances nécessaires.
 
## Cahiers d'exercices

Le répertoire *workbooks* contient des *cahiers d'exercices*. Ceux-ci sont
des documents type *Jupyter Notebooks* générés à l'aide de
[Jupyter](http://jupyter.org/). Pour pouvoir les utiliser, vous devez avoir
installé la dépendance (vois section précédente).
 
Pour accéder aux cahiers d'exercice, dans un terminal à partir du répertoire
racine du projet,  exécutez la commande

```
jupyter notebook
```
ou
```
python -m jupyter notebook
```

Vous pouvez maintenant travailler avec les *workbooks*. Ceux-ci sont proposés
comme outil pour vous aider à vous familiariser avec le langage.

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

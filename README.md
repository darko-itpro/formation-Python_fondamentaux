# A Python Training - Les fondamentaux

This is the practical cases for Python training I provide. Intended for french trainee, the rest of the explanations
are in french.

Ce référentiel complète la formation que je propose et est donc destiné à mes stagiaires. 

[![License](https://img.shields.io/github/license/darko-itpro/training-python.svg?style=plastic)](https://github.com/darko-itpro/training-python/blob/master/LICENSE)

Ces sources sont organisées pour proposer des exemples de code sur les thèmes couverts par les formations de base
Python. Elles respectent avec quelques adaptations l'organisation d'un package.

## Récupérez le projet
Le projet peut être dans l'arborescence que vous souhaitez sur votre disque.

## Structure du projet
Ce projet est un projet de formation. Sa structure ne suit donc pas la
structure conventionnelle d'un projet Python. L'organisation des répertoires
est la suivante :
 * **assets** : contient des fichiers qui seront nécessaires pour le parcours 
 et la manipulation de fichiers.
 * **demos** : est un package contenant des fichiers de démonstration et
 d'illustration. Ce package contient également des exemples Tkinter.
 * **stage** : est votre répertoire de travail. Il est destiné à contenir le
 code que vous allez produire durant la formation et vous permettre de le
 retrouver dans cet emplacement unique.
 * **pylib** : est un répertoire contenant du code qui sera utilisé par vos
 programmes.

## Mise en place de l'environnement

### Prérequis
[Python](https://www.python.org) doit être installé sur votre poste.

La formation est prévue pour une version de Python 3.8+.

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

PyCharm est un environnement dédié à Python, il intègre donc un certain nombre
d'outils. PyCharm existe en version licenciée ou Community, cette dernière,
gratuite et complète, convient amplement à la formation.

VS Code nécessite l'installation d'un plug-in pour la prise en charge de
Python.

## Environnement virtuel
Un environnement virtuel permet d'isoler l'environnement du projet de votre
environnement système. Il permet ainsi d'éviter les conflits de dépendance et
facilite l'exécution des programmes Python indépendamment des versions de
l'interpréteur.

Créer un environnement virtuel n'est pas indispensable dans le cadre de cette formation en
particulier si vous utilisez une machine dédiée à la formation.

Si vous utilisez PyCharm, il vous proposera de créer automatiquement un environnement virtuel.

Si vous avez besoin d'information sur leur création et utilisation, vous pouvez consulter
[la documentation](https://docs.python.org/fr/3/library/venv.html).

### Installation de dépendances
[pip](https://pypi.python.org/pypi/pip) est le gestionnaire de dépendances qui
va vous permettre d'installer les dépendances nécessaires à ce projet.

**Attention** : `pip` utilise des ports dédiés pour communiquer avec les
dépôts. Si vous êtes derrière un Firewall, il sera nécessaire de lui
communiquer le proxy.

Vous pouvez installer une dépendance spécifique avec l'instruction
```shell
pip install ipython
```

Cette commande permet d'installer la dépendance `ipython`.

Les dépendances nécessaires au projet sont déclarées dans le fichier
`requirements.txt`. Vous pouvez donc installer l'ensemble des dépendances avec
la commande :

```shell
pip install -r requirements.txt
```
ou
```
python -m pip install -r requirements.txt
```

Votre environnement est alors prêt à l'emploi.
 
## Documents d'illustration

Certains fichiers ont l'extension `.ipynb`. Il s'agit de documents de type
*Jupyter Notebooks* générés à l'aide de [Jupyter](http://jupyter.org/). Pour
pouvoir les utiliser, vous devez avoir installé la dépendance (voir section
précédente ET suivante).
 
Pour accéder à ces documents, il faut lancer le serveur Jupyter par
l'instruction :
```
jupyter notebook
```
ou

```
python -m jupyter notebook
```

Notez que le projet Jupyter évolue, cette évolution est JupyterLab. Cette dépendance est
différente et doit être installée. Pour le lancer, vous devez exécuter :
```
jupyter lab
```

ou

```
python -m jupyter lab
```

## Dépendances du projet
Un projet Python est accompagné d'un fichier `requirements.txt` déclarant les dépendances de
développement nécessaires au projet. Le fichier `requirements.txt` de ce projet ne contient que
les dépendances minimum pour ce support de formation. Ceci afin de ne pas télécharger _trop_
d'archives en fonction de ce qu'autorise la plate-forme informatique du lieu de la formation.

Les dépendances dans ce fichier sont les suivantes :
 * [ipython](https://jupyter.org/) : il s'agit d'un shell intéractif avancé préféré au shell
   intéractif standard.
 * [Pytest](https://docs.pytest.org/) : utilisé pour la partie tests unitaires
 * [Pytz](https://pypi.org/project/pytz/) : utilisé pour la gestion des TimeZone des dates
 * [flake8](https://flake8.pycqa.org/) : outil de validation statique de code
 * [pylint](https://pypi.org/project/pylint/) : outil d'analyse statique de code

Un fichier `requirements-xtra.py` contient les dépendances optionnelles. Notez que celles-ci
peuvent être volumineuses (donc prendront du temps et de l'espace disque) et certaines sont
redondantes (jupyter et jupyter-lab par exemple afin de comparer les deux).
 * [jupyter](https://jupyter.org/) : Jupyter sera utilisé pour ses notebooks, documents
   d'illustration. Cette dépendance installera également le shell intéractif 
   avancé `ipython`.
 * [jupyter-lab](https://jupyter.org/) : est une évolution du projet Jupyter. Normalement on
   utilise l'un ou l'autre. Les deux sont présents dans le contexte de formation.
 * [rich](https://rich.readthedocs.io/) : bibliothèque destinée à un affichage de texte _riche_,
   c'est à dire avec couleur et styles, ainsi que du contenu _avancé_ comme des tableaux.
 
## Ressources

Durant la formation, des ressources complémentaires peuvent être disponibles
[sur le partage suivant](https://bit.ly/3uh2MEQ)

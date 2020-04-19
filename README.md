# A Python Training - Les bases

This is the practical cases for Python training I provide. Intended for french
trainee, the rest of the explanations are in french.

Ce référentiel complète la formation que je propose et est donc destiné à
mes stagiaires. 

[![License](https://img.shields.io/github/license/darko-itpro/training-python.svg?style=plastic)](https://github.com/darko-itpro/training-python/blob/master/LICENSE)

Ces sources sont organisées pour proposer des exemples de code sur les thèmes
couverts par les formations de base Python. Elles respectent avec quelques
adaptations l'organisation d'un package.

## Mise en place de l'environnement

### Prérequis
[Python](https://www.python.org) doit être installé. La formation est prévue
pour être compatible Python 3.4+ mais certains codes illustrent des
fonctionalitées récentes. Il sera alors nécessaire de disposer d'une version
compatible.

Python ainsi que les dépendances doivent être dans le PATH. Vous pouvez vérifier
le bon fonctionnement dans un terminal/invite de commande par les instructions

```
python --version
python -m pip --version
```

### Récupérez le projet
Récupérez ce projet en local. En fonction de vos outils et de vos connaissances de Git,
clonez le répertoire ou récupérez les sources dnas un zip. Vous pouvez placer le projet
où vous le souhaitez dans votre arborescence.

### Installez les dépendances
[pip](https://pypi.python.org/pypi/pip) est le gestionnaire de dépendances qui
va nous permettre d'installer tout ce qui est nécessaire à ce projet. Vous
pouvez évidemment travailler dans un [virtualenv](https://virtualenv.pypa.io/en/stable/)
dédié à la formation. Si vous utilisez un IDE tel que PyCharm, vous pouvez
l'utiliser pour créer ce virtualenv. Placez vous alors à la racine du projet et
saisissez

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
[Jupyter](http://jupyter.org/). Ce dernier est inclus dans les dépendances.
 
Dans un terminal à partir du répertoire racine du projet,  exécutez la
commande

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
 
## Ressources

Durant la formation, des ressources complémentaires peuvent être disponibles
[sur le partage suivant](https://goo.gl/lRyzMZ).

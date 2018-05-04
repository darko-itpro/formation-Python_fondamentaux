# Python Training

This is the practical cases for Python training I provide. Intended for french
trainee, the rest of the explanations are in french.

Ce référentiel complète la formation que je propose et est donc destiné à
mes stagiaires. 

Ces sources sont organisées pour suivre le déroulement de la formation tout en
respectant l'organisation d'un package.

**Important** : depuis janvier 2017, mes formations sont orientées Python3, ces
exercices et illustrations sont donc portés vers Python3 et une compatibilité
Python2 n'est plus garantie.

## Exercices pratiques formation Python

Ces sources contiennet un *corrigé* des exercices pratiques proposés en cours.
Rappelez-vous que bien que la devise de Python soit *Il y a une manière évidente
de faire*, il s'agit donc d'une proposition de *solution* dont l'objectif principal est d'illustrer
ce qui a été présenté en formation. Les répertoires d'intérêt sont :
* `/training/projects` propose plusieurs projets regroupés en packages.
    * `/bank` propose des modules sur le thème de la gestion de comptes bancaires.
    * `/mediamanager` contient des modules répondant aux différents exercices de création et
      gestion de médiathèque.
    * `/sncf` contient le module `best_day` qui est une solution de l'extraction de donnée à partir
      d'un fichier.
* `/training/cases` est un package contennat des modules illustrant des outils présentés durant la
  formation

Historiquement certains modules peuvent contenir le sujet.

La documentation accompagnant les sources dans le répertoire `/docs` contient les sujets d'exercice.
 Le plus simple pour y accéder pendant la formation est de générer la documentation.
 
Le répertoire `/draft` est un répertoire contenant des squelettes de modules à compléter.

## Mise en place de l'environnement

Il faut donc commencer par récupérer les sources en local.

Assurez-vous que [pip](https://pypi.python.org/pypi/pip) est installé. Créez
si vous le souhaitez un [virtualenv](https://virtualenv.pypa.io/en/stable/)
dédié à la formation. Si vous utilisez un IDE tel que PyCharm, vous pouvez l'utiliser pour créer
ce virtualenv. Placez vous alors à la racine du projet et saisissez

```
pip install -r requirements.txt
```

Votre environnement contient alors toutes les dépendances nécessaires. Il ne
reste plus qu'à générer la documentation. Placez-vous dans le répertoire *docs*
 et exécutez
 
```
make html
```

La documentation est alors dispoible dans le sous répertoire *_build/html*.

## Cahiers d'exercices

Le répertoire *workbooks* contient des *cahiers d'exercices*. Ceux-ci sont
des documents type *Jupyter Notebooks* générés à l'aide de
[Jupyter](http://jupyter.org/). Ce dernier est inclus dans les dépendances.
 
Placez-vous dans le répertoire *workbooks* et exécutez la commande

```
jupyter notebook 00_presentation.ipynb
```

Vous pouvez maintenant travailler avec les *workbooks*. Ceux-ci sont proposés
comme outil pour vous aider à vous familiariser avec le langage.

## Ressources

Le répertoire *assets* contient des fichiers issus de
l'[Opendata de la SNCF](https://data.sncf.com/). Les droits appartiennent
évidemment à la SNCF et ces fichiers sont présents ici pour disposer de documents
 texte volumineux à parcourir et explorer.
 
Durant la formation, des ressources complémentaires peuvent être disponibles
[sur le partage suivant](https://goo.gl/lRyzMZ).

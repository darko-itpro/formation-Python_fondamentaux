**************
Boite à outils
**************

Ce chapitre présente les outils nécessaires pour un développement Python, la
manière de se les procurer et de les configurer.

L’interpréteur
==============

L’interpréteur est le seul outil indispensable. Lorsqu'il est proposé par défaut
sur un système, c'est malheureusement la version obsolète 2.7. Il faudra donc
l'installer.

Pour Windows et Mac OS, télécharger la dernière version de Python via
l'URL https://www.python.org

Pour Linux, une version à installer est disponible sur python.org. Préférez
cependant la gestion par les paquets.

Gestionnaire de packages : Pip
==============================

Pip est le gestionnaire de packages Python recommandé par PyPA [#fpypa]_. Il permet
d’installer les packages avec leurs dépendances, mettre à jour, désinstaller et
même recréer un environnement de développement.

Pour toute information : https://pypi.python.org/pypi/pip

L’installation de pip dépend du système.

- Sous Windows ou Os X, pip peut être installé lors de l’installation de Python. Vérifiez que la case a été cochée…

- Sous Linux, préférez le gestionnaire de packages

L’usage de pip dans le contexte de la formation est détaillé dans la section
suivante.

iPython, l’interpréteur interactif évolué
=========================================

iPython est un interpréteur interactif évolué. Il permet l’introspection (et
donc la complétion), l’accès au shell système et propose ses propres commandes
magiques.

Pour l’installation : pip install ipython

Plus d’informations : http://ipython.org

Documentation : http://ipython.readthedocs.io/en/stable/

Virutalenv
==========

Virtualenv est la réponse au besoin de gérer plusieurs environnements sur un même système. Virtualenv permet de compartimenter et donc d'isoler les environnements de travail les un des autres.
Virtualenv s'installe via pip

Documentation : https://virtualenv.pypa.io/en/stable/

Environnement de développement
==============================

L’usage d’un environnement de développement n’est pas nécessaire pour Python. Il
est possible d’utiliser un simple éditeur de texte en s’assurant qu’il est
configuré en UTF-8. Un IDE (Environnement de Développement Intégré) apportera
tout de même certaines facilitées.

Il existe un certain nombre d’environnements intégrés plus ou moins complets. La
liste suivante n’est pas exhaustive.

IDLE
----

IDLE est un environnement développement inclus dans le paquet Python. Il est
donc toujours disponible. IDLE est écrit en Python à l’aide de Tkinter.

Eclipse + PyDev
---------------

PyDev est le plug-in pour Eclipse qui permet de développement en Python. Il est
assez complet.

PyCharm
-------

PyCharm est un IDE proposé par la société JetBrains à qui on doit IntelliJ Idea.
PyCharm est un logiciel qui existe sous deux licences, une commerciale et une
community. Cette seconde est gratuite et largement suffisante.

https://www.jetbrains.com/pycharm/download/

Autres outils
=============

Anaconda
--------

Destiné à l’écosystème scientifique, Anaconda propose un environnement complet
comprenant l’interpréteur Python et des bibliothèques pré-compilées pour les
environnements Windows et Mac Os. Il facilite ainsi la gestion de certaines
bibliothèques comme MathPlotLib ou l’environnement Spyder. En effet, ces
bibliothèques comportent du code en C qui doit être compilé lors de leur
installation. Cette procédure peut être laborieuse sur les systèmes Windows
et Os X mais pose moins de problèmes sur un Linux.

https://www.continuum.io/

Jupyter
-------

Le projet Jupyter notebook est un projet open-source d’application web qui
permet de partager des pages contenant du code exécutable. Ce projet sera
utilisé dans le cadre de la formation.

http://jupyter.org/

*****************************
Installer un poste de travail
*****************************

Python pour Windows ou Mac Os
=============================

Sur Windows, Python n’est pas installé par défaut. Sur Mac Os, Python est
installé en version 2.7. il est donc nécessaire dans les deux cas d’installer
Python dans sa version 3.x

Récupérez la dernière version de Python sur https://www.python.org/

La manière la plus sûr d’installer Python est de passer par l’installation
avancée :

- Lancez l’installation et choisissez Installation avancée
- Assurez-vous que l’installation de pip soit activée
- Assurez-vous que l’installation crée les paths ou variables d’environnement.
- Lancez l’installation.

.. figure:: ../assets/python_install_main.png

    Fenêtre d’installation, sous Windows, cochez la case Add Python to PATH.

Le plus important sous Windows est de cocher la case de **l’ajout au
PATH** qui est décochée par défaut.

Python pour Linux (CentOs)
==========================

En fonction des distributions, Python peut être installé en version 3. Dans le
cas où seul la version 2 est présente, suivez les instructions suivantes.

Installez Python à partir du centre des paquets. Les instructions suivantes sont
destinées à un système Red Hat ou dérivé adaptés à la plupart des Linux de
formation qui sont des CentOS :

.. code-block:: sh

    su -
    yum install python34
    yum install python34-pip
    yum install python34-tkinter
    python3 -m pip install --user ipykernel
    python3 -m ipykernel install --user

La première instruction vous donne les privilèges super-utilisateur et nécessite
le mot de passe root. Cette instruction est nécessaire pour installer les
paquets. Ces instructions installent les outils Python dans la version 3.4 qui
est celle disponible sous CentOs à l’écriture de ce document.

CentOs étant une distribution destinée aux serveurs, les interfaces graphiques
ne sont pas incluses dans les paquets. C’est pour cela qu’il est nécessaire
d’installer tkinter séparément sachant que tkinter est autrement disponible avec
l’installation standard de Python.

Vérifiez l’installation de Python
=================================

Pour vérifier que l’installation s’est bien passé, nous allons utiliser un
terminal (ou cmd pour Windows). Dans le terminal, si il n’y avait aucune version
se Python précédemment installée, exécutez les instructions suivantes :

.. code-block:: sh

    python --version
    pip --version

Si une version précédente était installée, exécutez

.. code-block:: sh

    python3 --version
    pip3 --version

Notez que pip est écrit en Python. L’exécutable est donc un raccourci pour l’une
ou l’autre des instructions suivantes :

.. code-block:: sh

    python -m pip --version
    python3 -m pip --version

Installation de PyCharm
=======================

Les illustrations de cette formation reposeront sur l’IDE PyCharm. PyCharm
propose une forte intégration de nombreux outils. Récupérez la version de
PyCharm Community correspondant à votre système
sur https://www.jetbrains.com/pycharm/download/ .

Lancez l’installation, vous pouvez utiliser les sélections par défaut.

Récupérez les sources du projet.
================================

Cette formation est accompagnée de sources disponibles sur le service
d’hébergement GitHub. Ces sources sont disponibles à l’adresse suivante :

https://github.com/darko-itpro/training-python.

Pour récupérer une version sur votre poste, choisissez le bouton Clone or
download.

Vous avez deux options pour récupérer ces sources : télécharger une archive ou
cloner le référentiel. Pour télécharger une archive, choisissez Download as ZIP.

Cloner le référentiel nécessite Git sur votre poste. Vous pouvez tester la
présence de git via l’instruction suivante saisie dans un terminal :

.. code-block:: sh

    git --version

Si git est absent, vous pouvez le récupérer et l’installer à partir
de https://git-scm.com/ .

L'avantage de cloner le référentiel est que si durant la formation, des
évolutions sont apportées aux sources, vous pourrez les mettre à jour. Vous
pourrez aussi créer une branche et gérer les évolutions de votre code durant la
formation.

Cette formation n’est pas une formation à git, aussi, le choix vous est laissé.
Si vous souhaitez utiliser Git sans connaitre les instructions, l’usage le plus
simple est de passer par son intégration dans PyCharm.

À partir de la fenêtre de démarrage de PyCharm, choisissez l'option . Dans le
formulaire suivant

Installation des dépendances
============================

Le projet de référence utilise quelques dépendances, c'est à dire des
bibliothèques qui ne sont pas proposées dans l'installation standard. Nous
allons évidemment utiliser pip pour les récupérer. L'utilitaire pip est capable
s'installer toutes les dépendances d'un projet grâce à un fichier, le pip
requirement file. Ce type de fichier s'appelle par convention requirements.txt
et est situé à la racine du projet. Vous pouvez consulter ce fichier qui est un
fichier texte.

Pour installer les dépendances du projet à partir de ce fichier, dans un
terminal (ou cmd), déplacez-vous jusqu'au répertoire contenant le fichier
requirements. Exécutez ensuite l’une des instructions suivante :

.. code-block:: sh

    pip3 install -r requirements.txt # si  une précédente version était installée.
    pip install -r requirements.txt  # si c’est la seule version installée
    sudo pip3 install -r requirements.txt # si vous êtes sur un système Linux et que vous n’êtes plus root et que une version de pip était installée pour Python 2.

L’utilitaire pip va télécharger toutes les dépendances listées dans ce fichier
ainsi que leurs dépendances.

.. rubric:: Footnotes

.. [#fpypa] Python Packaging Authority : https://www.pypa.io/
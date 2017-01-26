Stdlib
======

La page suivante contient un ensemble d'exercices pour la présentation de la stdlib.

Fichiers
--------

Le répertoire assets fourni des fichiers à parcourir.

En utilisant le fichier comptage-voyageurs-trains-transilien.csv

#. Afficher toutes les lignes du fichier dans le terminal.
#. Quelle est la ligne ayant le maximum de comptage (quel jour)
#. Quelle est la ligne ayant le maximum de comptage un jeudi

Regex
-----

Les fichiers suivants correspondent au pattern reconnu par le médiacenter Plex ::

    Silicon_Valley-s01e01-Minimum_Viable_Product.avi
    Silicon_Valley-s01e02-The_Cap_Table.avi
    Silicon_Valley-s01e03-Articles_Of_Incorporation.avi
    Mr_Robot-s02e07-H4ndshake.mp4
    Mr_Robot-s02e09-Init5.mp4
    Breaking_Bad-s04e05-Shotgun.avi
    Breaking_Bad-s04e08-Hermanos.avi
    Supergirl-s01e01-Pilot.mkv

#. Ecrivez un script qui permet d'extraire les noms de séries, numéro de saison,
   numéro d'épisode dans la saison, titre de l'épisode et type de fichier
   (extension).

Dans le fichier comptage voyageurs utilisé précédemment

#. Quelle ligne a eu le plus grand comptage lorsque celui-ci a été réalisé dans
   l'après-midi (entre 13h et 19h) ?


Regex et BDD
============

Créez une base de données permétant de stocker le catalogue de la médiathèque. Il
doit y avoir une table pour les séries, une table pour les saisons et une pour les
épisodes. Pour rappel, pour créer une table, utiisez l'instruction::

    CREATE TABLE matable IF NOT EXISTS


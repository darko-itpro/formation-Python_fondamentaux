Gestion de médiathèque
======================

Les exércices suivants ont pour thème la gestion de médiathèque et plus particulièrement, la gestion d'une bibliothèque
de séries télévisées.

Une série est modélisée par le concept de *série* (`tvshow`)  ayant comme caractéristiques le nom de la série. Chaque
série contient des *saisons* (`seasons`) dont la caractéristiques est le numéro de saison (int). Enfin, chaque saison
contient une collection d'épisodes (`episode`) caractérisés par leur numéro dans la saison et leur titre.

Modélisation objet
------------------

Dans un module dédié, écrivez la classe **Episode** permétant de gérer un épisode.

Ajoutez la classe **Season** permétant de gérer une saison. Le numéro de la saison est défini par un attribut
**number**. La classe doit avoir une méthode permétant d'ajouter un épisode et une méthode **episodes()** retournant la
liste des épisodes de la saison.

Ajoutez la classe **TvShow** qui possède un attribut **name**. La classe doit avoir une méthode
**add_episode(episode, season_number)** qui permet d'ajouter un épisode pour une saison et une méthode **seasons()** qui
retourne la liste des saisons.

Exceptions : contrôle d'intégrité
---------------------------------

Améliorez votre modèle qui doit lancer une exception si vous essayez d'ajouter une saison ou un épisode existant.
L'accès à un élément innexistant doit également retourner une exception.

Pour tester le mécanisme des esceptions, vous disposez du module **training.poo.mediamanager.mediacli**. Recopiez ce
module dans votre projet et adaptez-le.

Regex : chargement des données
------------------------------

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

Stockage des données
--------------------

Ecrivez le code qui permet de charger ces données à partir d'un fichier (en réalité, ce serait à partir de la liste
d'un répertoire) puis de sauvegarder les données dans une base de données.

Affichage des données
---------------------

Créez l'IHM permétant l'affichage des données.
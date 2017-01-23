Agence voyage train
===================

On va gérer des voyages en train.

Définissions d'abord la notion de **trajet** : deux lieux, un prix et une durée

Soit les trajets suivants :

* Paris à Lyon, 2 heures, 200 €
* Paris à Reims, 50 minutes, 80 €
* Paris à Grenoble, 3 heures, 280 €
* Lyon à Grenoble, 1h30, 60 €
* Reims à Strasbourg, 1h20, 110 €

Chaque trajet peut-être parcouru dans un sens ou dans l'autre.

Soit la notion de **Voyage**. Un voyage est caractérisé par une gare de départ et une liste de
trajets.

#. Créez une classe **Trip** permétant de gérer la notion de voyage
#. Créez une classe **segment** permétant de gérer la notion de trajet.
#. Ajoutez une méthode à la classe de *voyage* permétant d'obtenir le prix du voyage

Améliorer le comportement
-------------------------

Ajouter le comportement suivant :

#. Si on additionne deux trajets, il en résulte un voyage avec les trajets additionnés.
#. Si on additionne un trajet à un voyage, il s'ajoute à la liste des trajets.
#. Si on additionne deux voyages, il en résulte un voyage avec l'ensemble des trajets.
#. Si on multiplie un voyage par un entier, il s'agit d'un nombre de voyageurs et on obtient
   le coût total du voyage.

Consolider le modèle
--------------------

Un voyage a une gare de départ spécifiée. Un trajet ne peut être ajouté à un voyage si il n'a
pas une gare cohérente, c'est à dire qu'une des gare soit la gare du départ du trajet. Pour les
trajets suivants, la gare d'arrivée du trajets précédent est la gare de départ.

#. Modifiez le modèle pour gérer des trajets cohérents.

Ajouter une relation
--------------------

Un voyage est associé à un voyageur. Un voyageur est géré comme un client comme
défini dans la partie :ref:`bank-object-reference-label`.

#. Si vous avez défini la classe **Client**, réutilisez-la en tant qu'attribut d'un voyage.

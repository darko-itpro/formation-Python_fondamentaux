Gestion bancaire
================

Les exercices suivants sont sur le thème de la gestion bancaire.

Fonctions
---------

On souhaite gérer la notion de compte bancaire dans un module. Créez un module contenant 3 fonctions:

* create : parmet de créer un compte bancaire avec un solde initial (100 par défaut) et un identifiant
* withdraw : permet de faire un retrait de la somme passée en paramètre
* deposit : permet de faire un dépôt de la somme passée en paramètre

.. _bank-object-reference-label:

Définition d'objet de gestion bancaire
--------------------------------------

On souhaite gérer un compte bancaire sous forme d'objets. Créez une classe permétant cette gestion de compte bancaire.

#. Écrivez une classe **Account** qui a comme attributs un id et un solde (balance).
#. Écrivez les méthodes **deposit** et **withdraw** qui acceptent un paramètre **value**.
#. Testez la classe via le shell interactif.

La notion de compte devra être rattachée à un client. Un client est caractérisé par un nom, prénom et un identifiant.

#. Écrire une classe **Person** qui a comme attribut un identifiant, un nom et un prénom.

Relations entre classes
-----------------------

Un client peut posséder plusieurs comptes.

#. Ajouter attribut et méthode(s) pour permettre la gestion des clients et des comptes.

Spécialisation des comptes
--------------------------

Un compte courant est un compte bancaire qui peut être à découvert (avec une limite fixée à 5000).

Un compte à débit différé est un compte dont le solde n'est débité qu'en fois par mois. Il faut donc garder en mémoire
les opérations jusqu'à les exécuter.

Un compte d'épargne est un compte qui est rémunéré d'un certain taux une fois par mois.

#. Créez ces deux types de comptes en exploitant l'héritage
#. Ces deux comptes doivent déclarer et implanter une méthode **triggerMontlyAction**
   qui, pour le compte à débit différé, fait la somme de toutes les opétations en
   attente, débite le solde et supprime les actions et pour le compte épargne,
   crédite le compte en fonction du taux.
#. Ajoutons la contrainte qu'un client ne peut avoir que 5 comptes.
#. Écrire une fonction qui pour une liste de comptes exécute les opérations mensuelles.


Gestion des erreurs
-------------------

Ajouter une gestion des erreurs :

#. Ajouter un compte alors que le client en a déjà 5 doit déclencher une erreur
#. Faire un retrait entrainant un solde débiteur alors que le compte ne doit pas l'être doit
   déclencher une erreur
#. Créditer ou débiter une somme négative doit déclencher une erreur.

Observez le comportement du code à l'aide du script training.poo.bank.bank_term_ihm après
l'avoir adapté à votre gestion bancaire.

Qualité
-------

#. Ajoutez de la documentation à vos classes
#. Écrivez quelques classes de test.
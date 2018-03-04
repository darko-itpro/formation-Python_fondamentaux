**************************
Les structures de contrôle
**************************

Les structures de contrôle servent à structurer l’exécution du code. Elles
permettent de définir des **blocs** qui vont être exécutés de manière
**conditionnelle** ou **en boucle**.

Le bloc est un ensemble d’instructions qui est précédé d’une **déclaration**.
Une déclaration est toujours terminée par deux points ( : ). Il n’y a pas de
délimiteur comme les accolades en Python.  Ce qui définira un bloc, c’est que
les instructions seront **indentées** par rapport à la déclaration.

Les blocs
=========

Les blocs sont donc un ensemble d'instructions exécutées en fonction de la
déclaration qui le précède. Ces instructions sont indentées par rapport à la
déclaration, c'est à dire qu'ils sont en retrait. Ce retrait est défini par la
pep 8 comme étant de **4 espaces**.

Veillez donc à vous assurer que votre éditeur de code convertisse les
tabulations en 4 espaces.

L'instruction ``pass``
======================

L'instruction ``pass`` est une instruction que ne fait… rien. Après une
déclaration de bloc (que ce soit une structure de contrôle, une déclaration de
fonction ou de classe), l'interpréteur attends une ligne indentée. Si vous
n'avez aucune instruction à déclarer dans le bloc (voir les cas lors de la
formation), l'instruction ``pass`` permet de ne pas avoir d'erreur
d'interprétation.
::

    >>> if True:
    ...     pass
    ...

Exécution conditionnelle avec if
================================

L'instruction ``if`` permet d'exécuter un bloc d’instructions de manière
conditionnelle.
::

    >>> if knight == "Arthur":
    ...      print("Is the King")
    ...

Une ou plusieurs conditions alternatives peuvent être déclarées avec
l’instruction ``elif``. L’instruction ``else`` permet de gérer tous les autres
cas.
::

    >>> if knight == "Arthur":
    ...     print("Is the King")
    ... elif knight == "Robin":
    ...     print("He's not that brave")
    ... else:
    ...     print("Who's that lad ?")

Les différentes conditions sont exclusives. À la première condition évaluée à
vrai (``True``), l'interprèteur exécuté le bloc puis sort de la structure
conditionnelle.

La condition, aussi appelée structure de contrôle, doit retourner une expression
booléenne. Cette expression peut aussi bien être le retour d'une fonction que le
résultat d’un opérateur de comparaison ou d’un opérateur logique.

Les opérateurs de comparaison
-----------------------------

Les opérateurs de comparaisons entre deux déclarations sont :

+----+-------------------------+
| <  | Strictement inférieur à |
+----+-------------------------+
| >  | Strictement supérieur à |
+----+-------------------------+
| <= | Inférieur ou égal à     |
+----+-------------------------+
| >= | Supérieur ou égal à     |
+----+-------------------------+
| == | Égal à                  |
+----+-------------------------+
| != | Différent de            |
+----+-------------------------+

Les opérateurs logiques
-----------------------

Les opérateurs logiques, nom utilisé pour les valeurs de vérité de l’algèbre de
Bool, sont la conjonction (et), la disjonction (ou) et la négation (non). En
Python, les mots-clef respectifs sont  ``and``, ``or`` et ``not``.

Soient X et Y deux expressions qui retournent une valeur booléenne.

- Conjonction : X ET Y est vrai si et seulement si X est vrai et Y est vrai

   En python, elle s’écrit ``X and Y``.
- Disjonction : X OU Y est vrai si et seulement si X est vrai ou Y est vrai 

  En python, elle s’écrit ``X or Y``.
- Négation : la négation de X est vrai si et seulement si X est faux 

  En python, elle s’écrit ``not X``.

En python, les fonctions de conjonction et de disjonction sont des opérations
paresseuses. Si l’évaluation du premier terme ne laisse aucun doute sur le
résultat de l’opération (si X est faux pour une conjonction ou X est vrai pour
une disjonction), le second terne n’est pas évalué. Gardez ceci à l’esprit si
les expressions sont des appels de fonctions.

Parcourir des collections avec for
----------------------------------

Itérer avec while
-----------------

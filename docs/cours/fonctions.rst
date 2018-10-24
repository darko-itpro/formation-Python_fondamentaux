*************
Les fonctions
*************

Les fonctions permettent de grouper des instructions afin de les exécuter par un
nom logique. Elles peuvent recevoir des paramètres et peuvent produit une valeur
de retour.

Une fonction est déclarée par le mot clef ``def`` suivi du nom de la fonction et
de parenthèses. Le corps de la fonction est un ensemble d'instructions indentées
par rapport à cette déclaration. Pour appeler cette fonction, il suffit de
déclarer son nom suivi de parenthèses.
::

    >>> def count_to_three():
    ...     print('one')
    ...     print('two')
    ...     print('three')
    ...
    >>> count_to_three()
    one
    two
    three

Si la fonction attend des paramètres, ceux-ci doivent être déclarés dans les
parenthèses. Tout comme les variables classiques, aucun type n'est déclaré pour
ces paramètres. Le nom des paramètres définissent des variables qui devront être
utilisées dans la fonction. Lors de l'appel de la fonction, il devra y avoir
autant de valeurs dans les parenthèses que de paramètres attendus.
::

    >>> def your_favorite_language(answer):
    ...     if answer != "Python":
    ...         print("Oh, cool, but try Python")
    ...     else:
    ...         print("Good Choice !")
    ...
    >>> your_favorite_language("Python")
    Good Choice !

Une fonction peut retourner une donnée. L'instruction pour retourner une donnée
est return suivi de la donnée. Lorsque l’interpréteur rencontre l'instruction
return, il sort de la fonction en retournant la donnée. Les instructions
suivantes ne seront donc pas exécutées. L'instruction return est optionnelle. Si
elle est omise, la fonction retournera une donnée par défaut : None.
::

    >>> def double(x):
    ...     if x:
    ...         return x * 2
    ...     print('Other than None')
    ...
    >>> double(None)
    Other than None

En Python, on ne déclare pas le retour (une fonction a toujours un retour). Il
est possible de retourner plusieurs valeurs en les déclarant à la suite après
l'instruction return. La fonction retournera alors un tuple contenant tous ces
éléments.
::

    >>> def multi_result():
    ...     return 'Question', 42
    ...
    >>> res = multi_result()
    >>> print(res[0], res[1])
    Question 42
    >>> res1, res2 = multi_result()
    >>> print(res1, res2)
    Question 42

Des arguments d'une fonction peuvent être optionnels. Pour qu'un argument soit
optionnel, il faut lui attribuer une valeur par défaut dans la déclaration de la
fonction. Si un argument est déclaré optionnel, tous les arguments suivants de
la déclaration de la fonction doivent également être optionnels.

Lors de l'appel à une fonction, une valeur peut être attribuée à un paramètre de
manière positionnelle ou par affectation spécifique au paramètre.
::

    >>> def create_account(nid, value='100', allowed=1000):
    ...     print(nid, value, allowed)
    ...
    >>> create_account('THX1138')
    THX1138 100 1000
    >>> create_account('THX1138', 500)
    THX1138 500 1000
    >>> create_account('THX1138', allowed=500)
    THX1138 100 500

Fonctions variadics
===================

Une fonction peut accepter un nombre non-prédéfini de paramètres. Afin d'offrir
cette possibilité, il faut y dédier une variable caractérisée par l'opérateur
``*`` communément appelé splat. L'opérateur splat peut être utilisé
conjointement à d'autres paramètres si il est placé en dernier paramètre
positionnel. Toutes les valeurs qui n'ont pas été affectés à un paramètre seront
passées à celui-ci qui contiendra un tuple.

Il est possible de passer des variable sous la forme clef/valeur de manière
similaire à l'affectation de valeur a un paramètre. Dans ce cas, il faut définir
un autre paramètre conteneur préfixé par un double-splat ``**``.

Communément, on utilise les noms ``*args`` et ``**kargs`` ou ``**kwargs`` (pour
KeyWord). Ce nom n’est pas imposé mais suffisamment communs pour être identifiés
de suite.
::

    >>> def multi_args(*args, **kargs):
    ...     for n in args:
    ...         print(n)
    ...     for k in kargs.keys():
    ...         print(k, ":",  kargs[k])
    ...
    >>> multi_args('toto', 'titi', 42, answer='42')
    toto
    titi
    42
    answer : 42

Portée des variables
====================

Pour comprendre la notion de portée des variable, il faut savoir que Python
définit des espaces de nommage en fonction du contexte. On va appeler contexte
global le niveau d’un module et contexte local celui des fonctions. Les
instructions déclarées dans les fonctions s’exécutent donc dans le contexte de
la fonction.

Une variable déclarée dans une fonction est donc déclarée dans l’espace local de
la fonction et n'est visible que dans la fonction. Lorsque l'exécution de la
fonction est terminée, cette variable est détruite.

Une variable déclarée en dehors de la fonction est visible dans la fonction à la
condition qu'elle ai été déclarée avant. Cette variable ne sera visible au sein
de la fonction qu'en lecture seule. Ainsi, si la fonction déclare une variable
du même nom, cette variable sera une nouvelle variable déclarée dans l’espace
local qui masquera celle du bloc supérieur.

Cette restriction de visibilité existe pour éviter une altération silencieuse
des données du bloc appelant. La bonne pratique pour modifier des données suite
à un appel de fonction est de récupérer les données par retour de fonction et
les affecter explicitement.

Python offre la possibilité d'accéder en écriture a une variable globale lorsque
cela est indispensable. Pour cela, il faut déclarée dans la fonction la variable
par la directive ``global``.
::

    >>> answer = 42
    >>> def func():
    ...     global answer
    ...     answer == 1
    ...
    >>> func()
    >>> print(answer)
    42

La directive ``global`` réfère au scope du module. Il existe une autre
directive, ``nonlocal``, qui réfère un scope supérieur à l'exclusion du global.

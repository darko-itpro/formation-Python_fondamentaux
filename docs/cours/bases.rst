*****************
Python, les bases
*****************

Dans cette partie, nous allons voir comment manipuler des données.

Données et variables
====================

En Python, les variables référencent des données. Une variables ne contient pas
la valeur mais une référence vers une valeur. En Python, nous ne déclarons pas
le type des données référencées par les variables. Le type est déterminé
dynamiquement par l’interpréteur.

Python est un langage de haut niveau qui va gérer la mémoire par un mécanisme de
comptage de références. Le développeur n’a pas à se soucier de la gestion de la
mémoire. Les données seront détruites lorsqu’elles ne seront plus accessibles,
c’est à dire lorsqu’elles ne seront plus référencées.
::

    >>> # Affectation d'une donnée à une variable
    >>> ma_variable = 10
    >>> print(type(ma_variable))
    <class 'int'>
    >>> del ma_variable
    >>> # la variable ma_variable n'existe plus et la donnée a été supprimée

Règles de nommage
-----------------

Les variables en Python peuvent contenir un caractère alphanumérique sans
diacritique [#fdiac]_ (tel que les accents, cédille…) ou un caractère souligné
_. Le premier caractère ne peut pas être un caractère numérique (de 0 à 9).
Python est sensible à la casse (capitale ou minuscule).

L’expression rationnelle représentant un nom de variable Python peut s’écrire
**[a-zA-Z_][a-zA-Z0-9_]\***.

En plus de la règle de nommage, vous ne pouvez pas utiliser les mots réservés
dont voici la liste.

+--------+----------+---------+----------+--------+
| False  | class    | finally | is       | return |
+--------+----------+---------+----------+--------+
| None   | continue | for     | lambda   | try    |
+--------+----------+---------+----------+--------+
| True	 | def      | from    | nonlocal | while  |
+--------+----------+---------+----------+--------+
| and    | del      | global  | not      | with   |
+--------+----------+---------+----------+--------+
| as     | elif     | if      | or       | yield  |
+--------+----------+---------+----------+--------+
| assert | else     | import  | pass     |        |
+--------+----------+---------+----------+--------+
| break  | except   | in      | raise    |        |
+--------+----------+---------+----------+--------+

Conventions de codage : la PEP 8
--------------------------------

Tout développement nécessite de s’accorder sur des conventions de codage afin de
rendre l’ensemble du code lisible et maintenance. Dans l’univers Python, ces
règles et conventions sont généralisés dans la **PEP 8** [#fpep8]_. Une **PEP**,
pour **Python Enhancement Proposal**, est un document destiné à proposer une
évolution du langage puis, si accepté, à documenter cette évolution.
L’explication plus détaillée est publiée dans la PEP 1 [#fpep1]_ et la liste de
toutes les PEPs dans la PEP 0 [#fpeps]_.

La PEP 8 est le document formalisant les règles de codage adoptées par la
communauté. La PEP 8 propose des règles sur le choix des noms à adopter ainsi
que leur typographie. Par exemple :

- Évitez les caractères l, O ou I comme nom de variable à une lettre (en général des indices) car en fonction des polices, ils ne sont pas lisibles.
- Lettres minuscules pour les noms de modules, variables et fonctions. Pour représenter plusieurs mots, les séparer par le caractère souligné (exemple : ``ma_variable``).
- Lettres capitales et souligné pour les constantes (exemple : ``MA_CONSTANTE``)
- Camelcase (ou CapWords) pour les noms de classes (exemple: ``MaClasse``)

Affecter des données à des variables
------------------------------------

L’opérateur égal ``=`` permet d’affecter une donnée à une variable. Il y a
plusieurs manières d'utiliser cet opérateur comme illustré dans le code
ci-après :

- l’affectation simple (ligne 1)
- l’affectation multiple (la même donnée est référencée par plusieurs variables (ligne 2)
- l’affectation en parallèle (ligne 3 et 4)
- l’assignation de valeurs consécutives (ligne 5)

    >>> var = 42
    >>> var1 = var2 = 42
    >>> question, answer = 42, "Meaning of life"
    >>> question, answer = answer, question
    >>> var1, var2, var3 = ["meaning", 42, None]

Pour une question de lisibilité et de maintenance, **privilégiez l’affectation
simple**. Utilisez l’affectation en parallèle pour inverser le contenu de
variables comme l’illustre la ligne 4.

L’utilité de l’assignation par valeurs consécutives prend tout son sens avec le
retour de valeurs multiples d’une fonction.

Manipuler et comprendre des données
-----------------------------------

Python propose plusieurs outils permettant de comprendre les variables et
données manipulés. Soit une variable ma_variable :

- ``print(ma_variable)`` affiche la valeur référencée par la variable
- ``print(type(ma_variable))`` affiche le type de la valeur référencée par la variable
- ``dir(ma_variable)`` retourne la liste des attributs d'une variable, et plus généralement, d'un type
- ``help(ma_variable)`` affiche l’aide sur une variable ou plutôt du type de la variable.

Les types de base (built-in)
============================

Les types numériques
--------------------

En Python, nous avons 3 types numériques : ``int`` qui représente les entiers,
``float`` pour les réels et complex pour les nombres complexe.

Il existe également le type booléens (``bool``) qui est un un sous-type des
entiers.

Python est un langage non déclaratif, c’est à dire que vous ne déclarez pas le
type de la donnée. Cependant, si vous devez manipuler un donnée d’un autre type
que celle déduite par l’interpréteur, il faut la convertir grâce aux fonctions
correspondantes : ``int(var)``, ``float(var)`` ou ``complex(var1, var2)``.

Ci-dessous, vous avez un exemple de déclaration de types numérique
::

    >>> var_int = int(42.2)
    >>> var_int = 42

    >>> var_float = float(3)
    >>> var_float = 3.
    >>> var_float = 3.14

    >>> var_cpx = complex(42, 2)
    >>> var_cpx = 42 + 2j
    >>> var_cpx.real
    42.0
    >>> var_cpx.imag
    2.0

En Python, il n'y a pas de taille maximum des entiers. Si sa valeur est comprise
entre **-2^(n-1)** et **2^(n-1)-1**, il est géré en registre, sinon en mémoire.

Opérations sur les types numériques
===================================

Python propose les opérateurs mathématique classiques.

+--------+------------------+
| x + y  | Addition         |
+--------+------------------+
| x - y  | Soustraction     |
+--------+------------------+
| x * y  | Multiplication   |
+--------+------------------+
| x / y  | Division         |
+--------+------------------+
| x // y | Division entière |
+--------+------------------+
| x % y  | Reste            |
+--------+------------------+
| -x     | Opposé           |
+--------+------------------+
| +x     |                  |
+--------+------------------+
| x ** y | Puissance        |
+--------+------------------+

La priorité des opérateurs est la priorité mathématique. À priorité égale, les
opérations sont résolues de gauche à droite. Les parenthèses ont la plus grande
priorité et permettent de grouper les opérations.

Les opérateurs binaires
=======================

Python permet des opérations binaires.

+--------+-------------------+
| x \| y | Ou binaire        |
+--------+-------------------+
| x ^ y  | Ou exclusif       |
+--------+-------------------+
| x & y  | Et binaire        |
+--------+-------------------+
| x << y | Décalage à gauche |
+--------+-------------------+
| x >> y | Décalage à droite |
+--------+-------------------+
| ~ x    | Inversion         |
+--------+-------------------+

    >>> x = 5
    >>> y = 6
    >>> res = x | y
    >>> print(res)
    7

5 en binaire est ``0b101``

6 en binaire est ``0b110``

Donc ``0b101`` OU BINAIRE ``0b110`` donne ``0b111`` soit 7.

*************
Les séquences
*************

La notion de séquences regroupe les types qui représentent des collections.
Python propose plusieurs types de base : les chaines de caractères (``string``),
les listes, les tuples, les ensembles (``set``) et les dictionnaires.

String, list et tuples fonctionnent de manière très similaire. Le tableau
suivant regroupe certains opérateurs et les deux méthodes qui sont communs ces
trois séquences. Dans ce tableau, s est une séquence, x un élément de la
séquence, n et i des entiers.

+------------+--------------------------------------+
| x in s     | True si s contient x, sinon False    |
+------------+--------------------------------------+
| x not in s | False si s contient x, sinon True    |
+------------+--------------------------------------+
| s1 + s2    | Concaténation                        |
+------------+--------------------------------------+
| s * n      | Répétition                           |
+------------+--------------------------------------+
| s[i]       | Élément à l’indice ou clef i         |
+------------+--------------------------------------+
| len(s)     | Taille de la chaine                  |
+------------+--------------------------------------+
| min(s)     | Plus petit élément de la séquence    |
+------------+--------------------------------------+
| max(s)     | Plus grand élément de la séquence    |
+------------+--------------------------------------+
| s.index(x) | Indice de la première occurence de x |
+------------+--------------------------------------+
| s.count(x) | Nombre total d’occurrences de x      |
+------------+--------------------------------------+

Les chaines de caractères
=========================

Les chaines de caractères sont délimitées par des simples, doubles ou
triple-double-quotes. Ces derniers sont des string-literais dont le contenu est
échappé. Les chaines de caractères sont **immuables** et sont encodées
en **Unicode**.

Dans l’exemple suivant, les lignes 11 et 12 sont équivalentes. La ligne 13 vous
montre comment définir un menu d’une interface en ligne de commande.
::

    >>> question = 'Meaning of life'
    >>> question = "Meaning of life"
    >>> choice = """Choose:
    ...  1) first choice
    ...  2) second choice"""
    ...

    >>> print(choice)
    Choose:
     1) first choice
     2) second choice

Les listes
==========

Les listes sont des **séquences ordonnées d’objets**. Les listes **peuvent être
modifiées**. Elles sont représentées entre crochets.
::

    >>> knights = ["Arthur", "Lancelot", "Robin", "Bedevere", "Galaad"]
    >>> h2g2 = ["Meaning of life", 42]

Les tuples
==========

Les tuples sont des **séquences ordonnées d’objets**. Les tuples **ne peuvent
pas être modifiés**. Ils sont représentées entre parenthèses.

Si ils sont en général présentés entre parenthèses, c’est surtout la présence
de la virgule qui fait le tuple. Ceci est d’autant plus important pour le tuple
*singleton* pour lequel il ne faut pas oublier une virgule.
::

    >>> knights = ("Arthur", "Lancelot", "Robin", "Bedevere", "Galaad")
    >>> h2g2 = "Meaning of life", 42
    >>> type(h2g2)
    tuple

    >>> tuple_singleton = 42,
    >>> type(tuple_singleton)
    tuple

Les types ``str``, ``list`` et ``tuple` possèdent un ensemble de méthodes qui
permet de les manipuler. Vous pouvez consulter l’ensemble des méthodes par
l’instruction ``help(str)``, ``help(list)`` et ``help(tuple)``. Vous avez
ci-dessous un exemple d’utilisation des méthodes du type ``str``.
::

    >>> question = 'Meaning of life'

    >>> print(question.upper())
    MEANING OF LIFE

    >>> print(question.split())
    ['Meaning', 'of', 'life']

    >>> ".".join(question)
    'M.e.a.n.i.n.g. .o.f. .l.i.f.e'

    >>> question.isalnum()
    False

Ainsi que des méthodes pour le type ``list``.
::

    >>> knights = ["Arthur", "Lancelot"]

    >>> knights.append('Robin')

    >>> knights.extend(['Bedevere', 'Galaad'])

    >>> knights.pop()
    'Galaad'

    >>> knights.insert(2, 'Galaad')
    >>> print(knights)
    ['Arthur', 'Lancelot', 'Galaad', 'Robin', 'Bedevere']

    >>> knights.remove('Robin')
    >>> print(knights)
    ['Arthur', 'Lancelot', 'Galaad', 'Bedevere']

    >>> knights.reverse()

    >>> knights.sort()
    >>> print(knights)
    ['Arthur', 'Bedevere', 'Galaad', 'Lancelot']

Accès aux éléments
==================

L’accès aux éléments d’une chaine, liste ou tuple se fait par l’indice de cet
élément entre crochet. Python permet l’usage d’indices négatifs afin d'accéder
aux éléments à partir de la fin.
::

    >>> knights = ["Arthur", "Lancelot", "Robin", "Bedevere", "Galaad"]
    >>> antagonist = 'Killer Rabbit of Caerbannog'

    >>> print(knights[2])
    Robin

    >>> print(antagonist[2])
    l

    >>> print(knights[-1])
    Galaad

    >>> print(antagonist[-5])
    a

Affectation d’élément
=====================

Un élément peut être remplacé dans une liste en attribuant une valeur à son
indice. La valeur à cet indice est alors remplacée par la nouvelle. Les chaines
de caractères et les tuples sont immuables, un de leur élément ne peut pas être
remplacé.
::

    >>> knights = ["Arthur", "Robin", "Bedevere", "Galaad"]

    >>> knights[1] = 'Lancelot'
    >>> print(knights)
    ['Arthur', 'Lancelot', 'Bedevere', 'Galaad']

    >>> antagonist = 'Killer Rabbit of Caerbannog'

    >>> antagonist[0] = 'M'
    -------------------------------------------------------------------------
    TypeError                               Traceback (most recent call last)
    <ipython-input-49-677a915eb39c> in <module>()
    ----> 1 antagonist[0] = 'M'

    TypeError: 'str' object does not support item assignment

Slicing
=======

Le slicing permet d’extraire des sous-séquences. L’opérateur de slicing est le
suivant (``seq`` étant une séquence de type ``str``, ``list``, ou ``tuple``) :

- ``seq[x:y]`` extrait une séquence de l’indice x à l’indice y exclu
- ``seq[:y]`` extrait une séquence de l’indice 0 à l’indice y exclu
- ``seq[x:]`` extrait une séquence de l’indice x à la fin de la séquence seq
- ``seq[x:y:z]`` extrait une séquence de l’indice x à l’indice y exclu avec un pas de z. x et y sont donc optionnels.

Si les bornes sont en dehors des limites de la séquence, le slicing retournera
une séquence vide.
::

    >>> knights = ["Arthur", "Lancelot", "Robin", "Bedevere", "Galaad"]

    >>> knights[2:4]
    ['Robin', 'Bedevere']

    >>> knights[2:]
    ['Robin', 'Bedevere', 'Galaad']

    >>> knights[:2]
    ['Arthur', 'Lancelot']

    >>> antagonist = 'Killer Rabbit of Caerbannog'

    >>> antagonist[::2]
    'Kle abto arang'

Les ensembles (set)
===================

Le type set permet de gérer des ensembles. Il s’agit d’une **collection non
ordonnée d’éléments non redondants**.

La fonction ``set()`` prend en paramètre une séquence de laquelle elle supprime
les redondances potentielles.

Les sets sont destinés aux opérations ensemblistes.
::

    >>> camelot = ['Arthur', 'Merlin', 'Lancelot', 'Robin']

    >>> wizards = ['Merlin', 'Morgan']

    >>> camelot_set = set(camelot)

    >>> camelot_set.union(wizards)
    {'Arthur', 'Lancelot', 'Merlin', 'Morgan', 'Robin'}

    >>> camelot_set.intersection(wizards)
    {'Merlin'}

    >>> set(wizards).issubset(camelot_set)
    False

Les dictionnaires
=================

Les dictionnaires sont des séquences non-ordonnées de couples clef/valeur. Il
n’y a donc pas de notion de position. Dans un dictionnaire, chaque clef est
unique. La valeur est obtenue à partir de la clef. Clef et valeur sont des
objets.

Un dictionnaire peut-être créé vide (lignes 10 et 11) ou avec des valeurs. La
création de dictionnaire avec des valeur la plus courante est celle de la
ligne 14.
::

    >>> mydict = {}
    >>> mydict = dict()

    >>> mydict = dict(question='Meaning of life', answer=42)
    >>> mydict = dict([['question', 'Meaning of life'], ['answer', 42]])

    >>> mydict = {'question': 'Meaning of life', 'answer': 42}

Pour ajouter un couple clef/valeur ou modifier la valeur d’une clef, on utilise
l’opérateur crochet en spécifiant la clef entre crochets et en affectant une
valeur. Le même opérateur est utilisé pour accéder à une valeur par la clef. Si
la clef n’existe pas, une erreur de type KeyError est levée.
::

    >>> mydict = {'question': 'Meaning of life', 'answer': 42}

    >>> mydict['reference'] = 'Hitchhicker guide'

    >>> mydict['reference']
    'Hitchhicker guide'

    >>> mydict['reference'] = 'H2G2'

    >>> mydict['reference']
    'H2G2'

    In [76]: mydict['nothing']
    ---------------------------------------------------------------------------
    KeyError                                  Traceback (most recent call last)
    <ipython-input-76-584c9c422e37> in <module>()
    ----> 1 mydict['nothing']

    KeyError: 'nothing'

    >>> mydict['reference'] = None

    >>> print(mydict['reference'])
    None

Il est possible de tester la présence d’une clef dans le dictionnaire avec
l’opérateur ``in``. Lorsqu’une valeur est testée via cet opérateur ``in``, cette
valeur  est recherchée parmi les clefs du dictionnaire.
::

    >>> in mydict
    >>> True

    >>> 'nothing' in mydict
    False

Le type ``dict`` propose quelques méthodes utiles. On citera :

- ``dict.get(key[, default])`` : retourne la valeur de key ou défault. Si default n’est pas spécifié, retourne ``None``.
- ``dict.items()`` : retourne un objet similaire à un set contenant la liste des couples clef/valeur
- ``dict.values()`` : retourne un objet la liste des valeurs
- ``dict.clear()`` : vide le dictionnaire
- ``dict.copy()`` : retourne une copie du dictionnaire
- ``dict.pop(key)`` : supprime le couple clef/valeur correspondant à la clef key et retourne la valeur.

.. rubric:: Footnotes

.. [#fdiac] voir : https://fr.wikipedia.org/wiki/Diacritique
.. [#fpep8] voir : https://www.python.org/dev/peps/pep-0008/
.. [#fpep1] voir : https://www.python.org/dev/peps/pep-0001/
.. [#fpeps] voir : https://www.python.org/dev/peps/

****************
Python et le Web
****************

Il existe plusieurs frameworks web pour Python. Tous reposent sur la norme WSGI
(Web Standard Gateway Interface). Cette norme définit comment un serveur Python
et son application peuvent communiquer. De manière simple, le point d’entrée est
un module Python contenant une variable nommée ``application`` et est capable
d’accepter un objet requête HTTP et retourner un objet réponse HTTP.

Parmi les frameworks web, on peut citer:

- Django  https://www.djangoproject.com
- Pyramid, compétiteur de Django influencé par Zope  https://trypyramid.com
- Twisted, qui est un framework Internet  https://twistedmatrix.com/
- Tornado  http://www.tornadoweb.org/
- Cherrypy  https://cherrypy.org
- Flask  http://flask.pocoo.org
- Bottle  https://bottlepy.org/

Cette liste présente ces frameworks dans un ordre décroissant de complexité.

Bottle
======

Il s’agit du plus petit framework Python disponible. Il tient en un fichier.
Bottle est idéal comme outil d’enseignement et pour les petits projets.

Installation
------------

via pip : ``pip install bottle``

Hello World
-----------

Le code suivant permet de créer un Hello World
::

    from bottle import route, run, template

    @route('/hello/')
    def index(name):
        return template('<b>Hello World</b>!’)

    run(host='localhost', port=8080)

Utiliser Bottle consiste à déclarer des fonctions décorées. Le Framework
s’occupe de gérer les requêtes et les réponses via les décorateurs. Chaque
fonction répondra à une URL décrite dans le décorateur.

La dernière ligne lance le serveur de développement sur le port 8080. Une fois
lancé, vous pouvez donc consulter la page générée par ce code sur
l’URL http://127.0.0.1/hello/

Des URLS restful
----------------

Bottle permet de paramétrer les URLs comme le montre le code suivant. Le
paramètre de l’URL devient le nom de la variable de la fonction.

::

    @route('/hello/<name>')
    def index(name):
        return template('<b>Hello {{name}}</b>!', name=name)

Attention, ce path doit contenir deux éléments. Si le paramètre doit être
optionnel, ce doit être une autre URL. L’usage de décorateurs permet de les
empiler comme le montre le code suivant.

::

    @route('/hello/') @route('/hello/<name>')
    def index(name="World"):
        return template('<b>Hello {{name}}</b>!', name=name)

Le paramètre ``name`` devient donc optionnel, il peut être déclaré de la
manière classique.

Paramètres d’URL
----------------

Une URL peut être paramètre, par exemple : https://www.monsite.com/forum?id=1&page=5

Bottle gère les requêtes et les réponses. Bottle fournit donc aux fonctions une
variable ``request`` contenant un objet ``query`` possédant des attributs au
nom de ces paramètres. Il est donc facile d’y accéder dans la fonction.

::

    @route('/forum')
    def display_forum():
        forum_id = request.query.id
        page = request.query.page or '1'
        return template('Forum ID: {{id}} (page {{page}})',
                         id=forum_id, page=page)

Méthodes de requête HTTP
------------------------

Bottle gère évidemment les méthodes de requête HTTP (GET, HEAD, POST...). Le
décorateur ``route`` répond par défaut à la méthode **get**. Afin de spécifier
la réponse à une autre méthode, le décorateur attends un paramètre ``method``.

::

    @route('/login', method="POST")
    def do_login():
        pass

Bottle propose également des décorateurs qui simplifient la déclaration de la
méthode comme dans l’exemple suivant.

::

    @post('/login')
    def do_login():
        pass

Méthode POST et gestion de formulaire
-------------------------------------

Bottle gère les requêtes et les réponses. Bottle fournit donc aux fonctions une
variable ``request`` contenant un objet requête qui contient le formulaire
envoyé. Les champs sont accessibles par la méthode ``get(champ)``.

::

    @post('/login')
    def do_login():
        username = request.forms.get('username')
        password = request.forms.get('password')
        if check_login(username, password):
                return "<p>Your login information was correct.</p>"
            else:
                return "<p>Login failed.</p>"

Les pages d’erreur
------------------
Afin de générer une page d’erreur, Bottle propose un décorateur ``@error``
prenant en paramètre le numéro HTTP de l’erreur pour laquelle la fonction doit
retourner la réponse.

::

    @error(404)
    def error404(error):
        return 'Nothing here, sorry'

Templating
----------

Une chaine de caractères est la type de donnée retourné en réponse. Mais pour
du web, cette chaine doit retourner un document HTML. Pour en faciliter la
gestion, Bottle propose un mécanisme de templates.

Les templates sont des documents texte avec l’extension ``.tpl`` stockés dans le
répertoire ``./ views/``. Ils seront mis en forme par appel à la fonction
``template()`` ou par l’usage du décorateur ``view()``.

Les templates sont évidemment dynamiques et sont donc destinés à recevoir des
paramètres. Dans le cas de la fonction, les paramètres sont passés comme
argument, dans le cas du décorateur, par un dictionnaire. Les deux codes
suivants arrivent au même résultat. Le premier utilise la fonction.

::

    @route('/hello/')
    @route('/hello/<name>')
    def index(name="World"):
        return template('template_name', name=name)

Le second utilise le décorateur.

::

    @route('/hello/')
    @route('/hello/<name>')
    @view('template_name')
    def index(name="World"):
        return dict(name=name)

Les templates proposent un langage simple pour faciliter la mise en forme. Le
code suivant est un extrait d’un template.

::

    Say Hello to...
    <ul>
        % for name in names:
        <li>{{name}}</li>
        % end
    </ul>

Pour plus d’informations sur l’usage des templates, consultez la documentation
du SimpleTemplate Engine : https://bottlepy.org/docs/dev/stpl.html. 

Django
======

Django est un framework d’application web. Il a été développé en 2003 pour un
journal local de la ville de Lawrance (Kansas). La fondation Django Software a
été créée en 2008.

Django repose sur le paradigme *Convention over Configuration*, c’est à dire
que si vous suivez les conventions proposées par Django, vous aurez le minimum
à faire pour tout ce que Django peut prendre en charge. Django a été conçu pour
implémenter le pattern MVC (Model-Vue-Contrôleur).

Django propose ainsi :

- Un gestionnaire de cycle de vie du projet
- Un ORM (Object-Relational Mapping) et les API d’accès aux données
- Un mapping d’URL
- Un langage de template
- Une administration pré-configurée

Django permet de d’organiser son application en composants afin qu’ils soient
réutilisables.

Ce document ne rentrera pas dans les détails de Django qui est complexe. Une
présentation pourra vous être fait en formation.

Django se justifie pour les application web lorsque vous avez besoin d’une prise
en charge d’un modèle objet et de sa persistance. Si vous votre besoin se limite
à une présentation de pages web, préférez les frameworks plus légers.
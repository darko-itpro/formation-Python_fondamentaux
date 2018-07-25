#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Illustration de l'usage Web avec Bottle.
"""

from bottle import route, run, template, post, request, error, view


@route('/hello/')
@route('/hello/<name>')
def index(name="World"):
    """
    Fonction Hello World standard en get

    :param name:
    :return:
    """
    return template('<b>Hello {{name}}</b>! (get)', name=name)


@route('/hello/')
@route('/hello/<name>', method="POST")
def hello(name="World"):
    """
    Fonction Hello World standard en post
    :param name:
    :return:
    """
    return template('<b>Hello {{name}}</b>! (post)', name=name)


@route('/better_hello/')
@route('/better_hello/<name>')
def index(name="World"):
    """
    Fonction Hello World dont la mise en forme repose sur un template.

    :param name:
    :return:
    """
    return template('hello_world', name=name)


@route('/hello/')
@route('/hello/<name>')
@view('hello_world')
def index(name="World"):
    """
    Fonction Hello World dont la mise en forme repose sur un template.

    Attention, même fonction que la précédente, celle-ci masque donc la
    précédente. Les deux cas sont présentés pour illustrer le code.

    :param name:
    :return:
    """
    return dict(name=name)


def check_login(username, password):
    pass


@error(404)
def error404(error):
    return 'Nothing here, sorry'


@route('/forum')
def display_forum():
    forum_id = request.query.id
    page = request.query.page or '1'
    return template('Forum ID: {{id}} (page {{page}})',
                     id=forum_id, page=page)


@post('/login')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


@route('/login', method="POST")
def do_login():
    pass
    username = request.forms.get('username')
    password = request.forms.get('password')
    if check_login(username, password):
        return "<p>Your login information was correct.</p>"
    else:
        return "<p>Login failed.</p>"


run(host='localhost', port=8080)
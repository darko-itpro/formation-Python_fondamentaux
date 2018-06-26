#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from bottle import route, run, template, post, request, error, view

@route('/hello/')
@route('/hello/<name>', method="POST")
def hello(name="World"):
    return template('<b>Hello {{name}}</b>!', name=name)

@route('/hello/')
@route('/hello/<name>')
def index(name="World"):
    return template('<b>Hello {{name}}</b>!', name=name)


@route('/hello/')
@route('/hello/<name>')
def index(name="World"):
    return template('template_name', name=name)


@route('/hello/')
@route('/hello/<name>')
@view('template_name')
def index(name="World"):
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
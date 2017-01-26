#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Exemple d'usage de Battle avec quelques cas.

Commectez-vous en :8080/ ou :8080/tpl/

"""

from bottle import route, run, template, post, request

our_heroes = ['Luke', 'Yoda', 'Han', 'Leia']

@route('/')
def index():
    return '<b>Great, Python Works !</b>!'


@route('/tpl/')
def indextpl():
    return template('hello_world', names = our_heroes)


@route('/hello/<name>')
def hello(name):
    return template('<b>Hello {{name}}</b>!', name=name)


@post('/add/')
def add_hero():
    our_heroes.append(request.forms.get('new_hero'))
    return "<a href='/tpl/'>Go back<a>"


run(host='localhost', port=8080)

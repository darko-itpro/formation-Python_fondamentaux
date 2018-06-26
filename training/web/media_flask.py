#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

our_heroes = ['Luke', 'Yoda', 'Han', 'Leia']


@app.route('/')
def index():
    return '<b>Great, Python Works !</b>'


@app.route('/tpl/')
def indextpl():
    return render_template('hello_world.html', names=our_heroes)


@app.route('/hello/<name>')
def hello(name):
    return '<b>Hello {}</b>'.format(name)


@app.route('/add/', methods=['POST'])
def add_hero():
    our_heroes.append(request.form.get('new_hero'))
    return "<a href='/tpl/'>Go back<a>"

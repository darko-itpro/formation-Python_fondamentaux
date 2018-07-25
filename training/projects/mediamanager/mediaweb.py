#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module illsutrant une interface web.
"""

from bottle import run, route, post, redirect, request, template
from training.projects.mediamanager import media_db

@route('/')
def index():
    return template('media_home')


@route('/shows/')
def index_show():
    _MY_SHOWS.get_shows()
    return template('series', series=_MY_SHOWS.get_shows())


@post('/add/')
def add_show():
    show_title = request.forms.get('new_show')
    my_new_show = media_db.TvShow(show_title)
    del my_new_show
    redirect("/shows/")


if __name__ == '__main__':

    _MY_SHOWS = media_db.MediaDao()

    run(host='localhost', port=8080)

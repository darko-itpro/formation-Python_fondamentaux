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


@route('/show/<name>')
def view_show_details(name):
    name = name.replace('_', ' ')
    selected_show = media_db.TvShow(name)
    return template('show_detail', title=selected_show.name,
                    episodes=selected_show.get_episodes())


@route('/show/<name>/add')
def view_show_details(name):
    name = name.replace('_', ' ')
    selected_show = media_db.TvShow(name)
    return template('show_add', title=selected_show.name)


@post('/add/<name>/episode/add')
def view_add_episode(name):
    episode_title = request.forms.get('episode_title')
    episode_number = request.forms.get('episode_number')
    episode_season = request.forms.get('season_number')
    return template("<b>Ok</b>")


if __name__ == '__main__':

    _MY_SHOWS = media_db.MediaDao()

    run(host='localhost', port=8080)

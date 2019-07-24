#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module illsutrant une interface web.
"""

from flask import Flask, render_template, request, redirect
from training.projects.mediamanager import media_db

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('media_home.html')


@app.route('/shows/')
def index_show():
    _MY_SHOWS = media_db.MediaDao()
    _MY_SHOWS.get_shows()
    return render_template('series.html', series=_MY_SHOWS.get_shows())


@app.route('/add/', methods=['POST'])
def add_show():
    show_title = request.form['new_show']
    my_new_show = media_db.TvShow(show_title)
    del my_new_show
    return redirect("/shows/")


@app.route('/show/<name>')
def view_show_details(name):
    name = name.replace('_', ' ')
    selected_show = media_db.TvShow(name)
    return render_template('show_detail.html', title=selected_show.name,
                           episodes=selected_show.get_episodes())


@app.route('/show/<name>/add')
def add_show_details(name):
    name = name.replace('_', ' ')
    selected_show = media_db.TvShow(name)
    return render_template('show_add.html', title=selected_show.name)


@app.route('/add/<name>/episode/add', methods=['POST'])
def view_add_episode(name):
    episode_title = request.form['episode_title']
    episode_number = request.form['episode_number']
    episode_season = request.form['season_number']
    selected_show = media_db.TvShow(name)
    selected_show.add_episode(episode_title, episode_number, episode_season)
    return redirect("/show/%s" % name)


if __name__ == '__main__':
    app.run()

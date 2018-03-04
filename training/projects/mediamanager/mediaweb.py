#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from bottle import run, route, template
from training.projects.mediamanager import media_file_loader

@route('/')
def index():
    return template('media_home')

@route('/shows/')
def indexseries():
    return template('series', series=sorted(list(set([raw_episode[0]
                                               for raw_episode
                                               in media_file_loader.open_file('/Users/dad3zero/workspace/formations/training-python/assets/showsfiles.txt')]))))



run(host='localhost', port=8080)

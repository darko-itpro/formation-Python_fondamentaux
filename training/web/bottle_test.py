#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import json

from bottle import run, get, post, response

@get('/names')
def get_listing_names_handler():
    response.headers['Content-Type'] = 'application/json'
    response.headers['Cache-Control'] = 'no-cache'
    return json.dumps({'names': ['Arthur', 'Lancelot', 'Galahad']})

if __name__ == '__main__':
    run(host='127.0.0.1', port=8000)
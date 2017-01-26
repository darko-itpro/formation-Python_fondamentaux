#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Extraction des information d'un fichier média série
"""

import re

series_re = re.compile("-s([0-9]{2})e([0-9]{2})-")

series_full_name = "Silicon_Valley-s01e03-Articles_Of_Incorporation.avi"

import os

series_file_name, series_ext = os.path.splitext(series_full_name)

series_match = series_re.search(series_file_name)

if series_match:
    print(series_match.group(1))
    print(series_match.group(2))
    print(series_file_name[:series_match.start()].replace('_', ' '))
    print(series_file_name[series_match.end():].replace('_', ' '))
    print(series_file_name)

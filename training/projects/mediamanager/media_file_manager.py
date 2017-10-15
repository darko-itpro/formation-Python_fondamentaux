#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import re

MEDIA_PATTERN = "-s([0-9]+)e([0-9]+)-"


media_re = re.compile(MEDIA_PATTERN)


def find_files(root_path):
    pass
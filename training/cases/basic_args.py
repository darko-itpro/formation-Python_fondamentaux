#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Demonstrate how to basically access to the command line arguments.
"""

from __future__ import print_function

import sys

if __name__ == '__main__':
    print("-- Exemple usage args --")
    for arg in sys.argv:
        print(arg)

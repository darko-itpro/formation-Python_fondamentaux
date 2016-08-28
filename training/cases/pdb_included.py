#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Example how to use pdb to interrupt an exception and explore the post-mortem.
"""

from __future__ import print_function
import pdb

a = 0

try:
    result = 3/a
except ZeroDivisionError:
    pdb.set_trace()

print('Result is %d' % result)
print('Done')

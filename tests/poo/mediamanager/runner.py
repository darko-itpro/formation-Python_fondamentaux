#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import unittest

from tests.poo.mediamanager.umediamodel import object_episode
from tests.poo.mediamanager.umediamodel import object_show

loader = unittest.TestLoader()
suite = unittest.TestSuite()

suite.addTest(loader.loadTestsFromModule(object_episode))
suite.addTest(loader.loadTestsFromModule(object_show))

runner = unittest.TextTestRunner(verbosity=3)
runner.run(suite)

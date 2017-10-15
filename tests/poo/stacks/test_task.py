#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from training.projects.stacks import tasks


class CreateTask(unittest.TestCase):

    def testSimpleTaskCreate(self):
        task = tasks.Task("Toto")
        self.assertIsNotNone(task)

    def testTitleIsSet(self):
        task = tasks.Task("My title")
        self.assertEqual("My title", task.title)

    def testTitleNotEmpty(self):
        with self.assertRaises(ValueError):
            tasks.Task("")

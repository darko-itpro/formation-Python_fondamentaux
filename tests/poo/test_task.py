#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from training.poo import tasks


class createTask(unittest.TestCase):

    def testSimpleTaskCreate(self):
        task = tasks.Task2("Toto")
        self.assertIsNotNone(task)

    def testTitleIsSet(self):
        task = tasks.Task2("My title")
        self.assertEqual("My title", task.title)

    def testTitleNotEmpty(self):
        with self.assertRaises(ValueError):
            tasks.Task2("")

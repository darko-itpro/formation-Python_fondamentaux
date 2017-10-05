#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from training.projects.stacks import stack


class CreateLifo(unittest.TestCase):

    def testCreateEmptyArgs(self):
        ma_pile = stack.Lifo()
        self.assertEqual(0, len(ma_pile))

    def testCreateOneArg(self):
        ma_pile = stack.Lifo("toto")
        self.assertEqual(1, len(ma_pile))

    def testMoreArgs(self):
        ma_pile = stack.Lifo("toto", "tata", 2)
        self.assertEqual(3, len(ma_pile))

    def testListArg(self):
        ma_pile = stack.Lifo(["toto", "tata"])
        self.assertEqual(1, len(ma_pile), "Les collectoins ne doivent pas etre eclatees")


class DepileLifo(unittest.TestCase):

    def setUp(self):
        self.ma_pile = stack.Lifo("one", "two")

    def tearDown(self):
        del self.ma_pile

    def testDepileOneLessElement(self):
        self.ma_pile.pop()
        self.assertEqual(1, len(self.ma_pile))

    def testDepileLastElement(self):
        self.ma_pile.push("last")
        self.assertEqual("last", self.ma_pile.pop())

    def testDepletedStack(self):
        self.ma_pile.pop()
        self.ma_pile.pop()

        with self.assertRaises(ValueError):
            self.ma_pile.pop()

    @unittest.skip("Waiting spec")
    def testTrucAbsurde(self):
        self.ma_pile.pop()


if __name__ == '__main__':
    unittest.main()

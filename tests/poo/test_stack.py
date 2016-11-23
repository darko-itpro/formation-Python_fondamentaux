#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from training.poo.stacks import stack


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
        self.ma_pile.depile()
        self.assertEqual(1, len(self.ma_pile))

    def testDepileLastElement(self):
        self.ma_pile.empile("last")
        self.assertEqual("last", self.ma_pile.depile())

    def testDepletedStack(self):
        self.ma_pile.depile()
        self.ma_pile.depile()

        with self.assertRaises(ValueError):
            self.ma_pile.depile()

    @unittest.skip("Waiting spec")
    def testTrucAbsurde(self):
        self.ma_pile.depile()


if __name__ == '__main__':
    unittest.main()

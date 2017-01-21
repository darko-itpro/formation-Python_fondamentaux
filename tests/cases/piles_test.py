#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from training.cases import piles


class CreateNewPile(unittest.TestCase):

    def testEmptyCreation(self):
        piles.pile()
        self.assertEqual(piles._pile, [])

    @unittest.skipIf()
    def testCreation(self):
        piles.pile('a', 'b')
        self.assertEqual(piles._pile, ['a', 'b'])

    @unittest.skip('Skipped because not ready')
    def testFollowUpCreation(self):
        piles.pile('a', 'b')
        piles.pile('c', 'd')
        self.assertEqual(piles._pile, ['c', 'd'])

if __name__ == '__main__':
    unittest.main()
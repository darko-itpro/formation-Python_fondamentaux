#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implémentation de piles
-----------------------

Les piles (stacks) LIFO et FIFO permettent de gérer les deux types de piles.

La pile OrderedStack gère une pile où les éléments sont retournés selon leur
ordre naturel

"""


class Stack(object):
    """
    Generic class declaration for a stack
    """
    def __init__(self, *args):
        self._pile = list(args)

    def empile(self, element):
        self._pile.append(element)

    def depile(self):
        """
        depile function must not be used from this Class.

        :except NotImplementedError:
         Because this should be considered as an abstract function.
        """
        raise NotImplementedError("You must use a real implementation")

    def __len__(self):
        return len(self._pile)

    def __getitem__(self, item):
        return self._pile[item]

    def __str__(self):
        return "pile generique"


class Lifo(Stack):
    """
    *Last in First out* stack
    """

    def __str__(self):
        return "LIFO Stack with %d elements" % len(self._pile)

    def depile(self):
        try:
            return self._pile.pop()
        except IndexError:
            raise ValueError("No more element")


class Fifo(Stack):
    """
    *First in First out* stack
    """

    def __str__(self):
        return "FIFO Stack with %d elements" % len(self._pile)

    def depile(self):
        if len(self._pile):
            return self._pile.pop(0)
        else:
            raise ValueError("No more element")


class OrderedStack(Stack):

    def depile(self):
        """
        Returns the lowest ranked element.

        :return:
         Lowest ranked element
        """
        if len(self._pile):
            self._pile.sort()
            return self._pile.pop(0)

    def __str__(self):
        return 'Ordered stack with %d elements' % len(self._pile)

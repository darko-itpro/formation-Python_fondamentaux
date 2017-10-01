#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implémentation de piles
-----------------------

Les piles LIFO (le terme devrait être Stack avec push et pop) et FIFO (le nom
devrait être Queue avec enqueue et dequeue permettent de gérer les deux types
de piles.

La pile OrderedStack gère une pile où les éléments sont retournés selon leur
ordre naturel ou selon la clef de tri passé en paramètre.

"""


class Stack(object):
    """
    Generic class declaration for a stack
    """
    def __init__(self, *args):
        self._pile = list(args)

    def push(self, element):
        """Add an element to the stack"""
        self._pile.append(element)

    def pop(self):
        """
        Must not be used from this Class.

        :except NotImplementedError:
         Because this should be considered as an abstract function.
        """
        raise NotImplementedError("You must use a real implementation")

    def __len__(self):
        return len(self._pile)

    def __str__(self):
        return "pile generique"


class Lifo(Stack):
    """
    *Last in First out* stack
    """

    def __str__(self):
        return "LIFO Stack with %d elements" % len(self._pile)

    def pop(self):
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

    def pop(self):
        if len(self._pile):
            return self._pile.pop(0)
        else:
            raise ValueError("No more element")


class OrderedStack(Stack):

    def __init__(self, *args, key=None):
        """

        :param args:
        :param key: must be un function as for the key parameter of the sorted function.
        """
        Stack.__init__(self, *args)
        self._key = key

    def pop(self):
        """
        Returns the lowest ranked element.

        :return:
         Lowest ranked element
        """
        if len(self._pile):
            self._pile.sort(key=self._key)
            return self._pile.pop(0)

    def __str__(self):
        return 'Ordered stack with %d elements' % len(self._pile)

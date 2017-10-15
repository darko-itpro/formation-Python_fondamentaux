#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implémentation de piles
-----------------------

D'un point de vue sépantique, les piles LIFO devraient s'appeler  Stack avec les
méthodes push et pop. Les piles FIFO, Queue avec les méthodes enqueue et
dequeue.

La pile OrderedStack gère une pile où les éléments sont retournés selon leur
ordre naturel ou selon la clef de tri passé en paramètre.

"""


class Lifo:
    """
    *Last in First out* stack
    """

    def __init__(self, name, *args):
        self.name = name
        self._pile = list(args)

    def push(self, element):
        """Add an element to the stack"""
        self._pile.append(element)

    def __str__(self):
        return "LIFO Stack with %d elements" % len(self._pile)

    def pop(self):
        try:
            return self._pile.pop()
        except IndexError:
            raise ValueError("No more element")


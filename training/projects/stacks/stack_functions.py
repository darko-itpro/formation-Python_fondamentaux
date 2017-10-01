#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Ce module propose les deux implémentations de la gestion de piles : par fonction
et par objets.
"""

stack = []


def create(*elements):
    """
    Creates a new stack with indefined elements to start with.
    :param elements: The initial elements of the stack
    :return: None
    """
    stack.clear()
    stack.extend(elements)


def add(element):
    stack.append(element)


def get():
    return stack.pop()


class Stack:
    def __init__(self, *elements):
        self._stack = list(elements)

    def add(self, element):
        self._stack.append(element)

    def get(self):
        return self._stack.pop()


class person:
    def __init__(self, name, stack=Stack()):
        self.name = name
        self._stack = stack

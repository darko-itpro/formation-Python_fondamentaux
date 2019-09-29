#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import random


class Card:
    def __init__(self, value, color):
        self._value = value
        self._color = color

    @property
    def value(self):
        return self.value

    @property
    def color(self):
        return self._color


class Deck:
    def __init__(self):
        self._deck = []


if __name__ == '__main__':
    pass
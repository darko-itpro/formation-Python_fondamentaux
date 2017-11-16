#!/usr/bin/env python 
# -*- coding: utf-8 -*-

class Playlist:
    def __init__(self, name):
        self.name = name
        self._stack = []

    def add(self, element):
        """
        Ajoute un élément à la playliste
        :param element:
        :return:
        """
        self._stack.append(element)

    def get(self):
        """Retourne le prochain élément de la playlist et le supprime de la
        liste."""
        return self._stack.pop(0)

    def total_time(self):
        """
        Retourne la durée totale de la playlist en minutes.

        :return: Le nombre de minutes de la durée de la playliste.
        """
        return len(self._stack) * 53


if __name__ == '__main__':
    pass
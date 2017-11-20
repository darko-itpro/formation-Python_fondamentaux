#!/usr/bin/env python 
# -*- coding: utf-8 -*-


class Playlist:
    """
    Objet de gestion d'une Playlist d'épisodes uniques identifiée par un nom.
    """

    def __init__(self, name):
        self.name = name
        self._stack = []

    def content(self):
        """
        Retourne le contenu de la playlist.
        :return: Une liste de chaines de caractères représentant les titres dans
        l'ordre.
        """
        return self._stack

    def add(self, title):
        """
        Ajoute un élément à la playliste si il n'est pas déjà présent.

        :param title: le titre de l'épisode
        :return:
        :raise ValueError: si l'élément existe déjà dans la lsite.
        """
        if title not in self._stack:
            self._stack.append(title)

    def get(self):
        """Retourne le prochain titre de la playlist et le supprime de la
        liste."""
        return self._stack.pop(0)

    def total_duration(self):
        """
        Retourne la durée totale de la playlist en minutes en considérant la
        durée de chaque épisode à 53 minutes.

        :return: Le nombre de minutes de la durée de la playliste.
        """
        return sum([media.duration for media in self._stack])


if __name__ == '__main__':
    pass
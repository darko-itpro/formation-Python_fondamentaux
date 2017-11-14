#!/usr/bin/env python 
# -*- coding: utf-8 -*-


class Account:

    def __init__(self, nid, balance=100, overdraft=False):
        self._id = nid
        self._balance = balance
        self.overdraft = overdraft

    def deposit(self, value):
        self._balance += value

    def withdraw(self, value):
        self._balance -= value

    def nid(self):
        return self._id

    def balance(self):
        return self._balance


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
        return len(self._stack) * 53


if __name__ == '__main__':
    pass
#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Ce module illustre la création de classes par prototype
"""

def proto_init_tvshow(self, name):
    """
    Méthode qui est destinée à devenir l'initialiseur de la classe
    :param self: pour l'instance de classe
    :param name: nom du show
    """
    self._name = name
    self.episodes = []


def proto_add_episode_tvshow(self, title):
    """
    Méthode qui est destinée à devenir l'ajout d'épisodes de la classe
    :param self: pour l'instance de classe
    :param title: titre de l'épisode à ajouter
    """
    if title in self.episodes:
        raise ValueError('Duplicate episode')

    self.episodes.append(title)


def name_fget(self):
    """
    Accesseur pour la property name
    :param self: pour l'instance de classe
    :return: la valeur de l'attribut self._name
    """
    return self._name


TvShow = type('TvShowz', (object,), {
    "__init__": proto_init_tvshow,
    "add_episode": proto_add_episode_tvshow,
    "name": property(name_fget)
})

if __name__ == '__main__':
    t = TvShow("My Show Name")
    print(type(t))
    t.add_episode('Test episode')
    t.add_episode('Another test episode')
    print(t.episodes)
    print(t.name)

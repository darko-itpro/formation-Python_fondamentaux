#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Module de gestion de série par des fonctions.
"""

_episodes = []


def create_tvshow(name, *episodes):
    """
    Crée une série.
    :param name: nom de la série.
    :param episodes: tout paramètre supplémentaire est considéré comme étant un
    titre l'épisode non vu.
    """
    global _tvshow_name
    _tvshow_name = name
    _episodes.clear()
    _episodes.extend([[episode, False] for episode in episodes])


def add_episode(episode_name, viewed=False):
    """
    Ajoute un épisode.
    :param episode_name: titre de l'épisode.
    :param viewed: True si vu, False (défaut) si non-vu.
    """
    _episodes.append([episode_name, viewed])


def episode_is_viewed(episode_name):
    """
    Marque l'épisode comme vu. Si l'épisode n'existe pas, un message d'erreur
    est affiché.
    :param episode_name: titre de l'épisode.
    """
    for episode in _episodes:
        if episode[0] == episode_name:
            episode[1] = True
            break
    else:
        print("Episode {} not found".format(episode_name))


def list_episodes(show_all=False):
    """
    Retourne une liste des épisodes.

    La liste retrounée est par défaut les épisodes non-vus.
    :param show_all: Si True, retourne tous les épisodes.
    :return: une liste de titres d'épisodes.
    """
    if show_all:
        return [episode for episode, viewed in _episodes]
    else:
        return [episode for episode, viewed in _episodes if not viewed]


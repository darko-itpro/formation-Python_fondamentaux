#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crée une fenêtre permétant de gérer des épisodes d'une série télévisée.
Les widgets sont dans un module dédié.

Les épisodes sont gérés sous forme d'une liste déclarée dans ce module. Ce
modèle ne permet pas d'être connecté à une autre source de données comme la
base de données. Ce choix est volontaire car cet exemple d'interface a pour but
d'illustrer certaines techniques.
"""

import tkinter as tk

from training.projects.mediamanager import mediamodel
from training.projects.mediamanager import media_widgets

FENETRE = tk.Tk()

EPISODE_LIST = []


def add_episode(title, number):
    """
    Ajoute un épisode à la collection gérée. Ajoute également cet épisode au
    composant `episode_frame`.

    :param title: Titre de l'épisode à ajouter
    :param number: Numéro de l'épisode à ajouter
    """

    episode = mediamodel.Episode(title, number, 0)
    EPISODE_LIST.append(episode)
    EPISODE_LIST.sort(key=lambda x: x.number)
    ep_index = EPISODE_LIST.index(episode)

    EPISODES_FRAME.add_element(title, ep_index)


def select_episode(ep_index):
    """
    Communique les informations d'un épisode à la `form_frame`.

    :param ep_index: indice d'un épisode dans la collection.
    """
    FORM_FRAME.set_values(EPISODE_LIST[ep_index].title, EPISODE_LIST[ep_index].number)


def delete_episode(ep_index):
    """
    Supprime un épisode de la liste des épisodes.

    :param ep_index: indice de l'épisode à supprimer.
    """
    EPISODE_LIST.pop(ep_index)

FENETRE.title('Episode Manager')

BUTTONS_FRAME = tk.Frame(FENETRE)
tk.Button(BUTTONS_FRAME, text='Quit', command=FENETRE.quit).pack(side=tk.RIGHT)
BUTTONS_FRAME.pack(side=tk.BOTTOM)

FORM_FRAME = media_widgets.EpisodeEntry(FENETRE, add_episode, "Titre", "N°")
EPISODES_FRAME = media_widgets.CollectionFrame(FENETRE, select_callback=select_episode,
                                               delete_callback=delete_episode)
EPISODES_FRAME.pack(side=tk.LEFT)
FORM_FRAME.pack()

FENETRE.mainloop()

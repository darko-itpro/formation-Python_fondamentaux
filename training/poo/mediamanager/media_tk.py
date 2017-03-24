#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Crée une fenêtre permétant de gérer des épisodes d'une série télévisée. Les widgets sont dans un
module dédié. Les épisodes sont gérés sous forme d'une collection dans une liste dans ce module.

"""

from tkinter import Tk, Button, LEFT, RIGHT

from training.poo.mediamanager import mediamodel
from training.poo.mediamanager import media_widgets

fenetre = Tk()

episode_list = []


def add_episode(title, number):

    episode = mediamodel.Episode(number, title)
    episode_list.append(episode)
    episode_list.sort(key=lambda x: x.number)
    ep_index = episode_list.index(episode)

    episodes_frame.add_element(title, ep_index)


def select_episode(ep_index):
    form_frame.set_values(episode_list[ep_index].title, episode_list[ep_index].number)


def delete_episode(ep_index):
    episode_list.pop(ep_index)

fenetre.title('Episode Manager')

form_frame = media_widgets.EpisodeEntry(fenetre, add_episode)
episodes_frame = media_widgets.CollectionFrame(fenetre, select_callback=select_episode,
                                               delete_callback=delete_episode)
episodes_frame.pack(side=LEFT)
form_frame.pack()
Button(fenetre, text='Quit', command=fenetre.quit).pack(side=RIGHT)

fenetre.mainloop()
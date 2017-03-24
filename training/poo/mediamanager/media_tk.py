#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

from training.poo.mediamanager import mediamodel
from training.poo.mediamanager import media_widgets

fenetre = Tk()

episode_list = []

def add_episode(title, number):

    episode_list.append(mediamodel.Episode(number, title))
    episode_list.sort(key=lambda x: x.number)

    for episode in episode_list:
        print(episode)

fenetre.title('Episode Manager')

episode_frame = media_widgets.EpisodeEntry(fenetre, add_episode)
episode_frame.pack()
Button(fenetre, text='Quit', command=fenetre.quit).pack(side=RIGHT)

fenetre.mainloop()
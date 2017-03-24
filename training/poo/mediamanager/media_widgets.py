#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *

class EpisodeEntry(Frame):
    def __init__(self, master= None, action_callback=None):
        Frame.__init__(self, master)

        self._callback = action_callback

        form_frame = Frame(self)

        Label(form_frame, text='Titre').grid(column=0, row=0)
        Label(form_frame, text='Numéro').grid(column=0, row=1)

        self.title_value = StringVar()
        self.number_value = IntVar()

        Entry(form_frame, textvariable=self.title_value, width=30).grid(column=1, row=0)
        Entry(form_frame, textvariable=self.number_value, width=30).grid(column=1, row=1)

        form_frame.pack()
        Button(self, text='Ajouter', command=self.button_action).pack()

    def button_action(self):
        self._callback(self.title_value.get(), self.number_value.get())

    def get_values(self):
        return (self.title_value.get(), self.number_value.get())

    def set_values(self, title, number):
        self.title_value.set(title)
        self.number_value.set(number)

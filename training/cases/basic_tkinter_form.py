#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Code demo pour tkInter
"""

from tkinter import *


class UserInfo(Frame):
    """
    La classe UserInfo hérite de Frame. Il s'agit donc d'une Frame avec des
    composants et deux méthodes afin de communiquer avec ces composants.
    """
    def __init__(self, master=None, cnf={}, **kw):
        Frame.__init__(self, master, cnf, **kw)
        Label(self, text='nom').grid(column=0, row=0)
        Label(self, text='prenom').grid(column=0, row=1)

        self.last_name_value = StringVar()
        self.first_name_value = StringVar()

        Entry(self, textvariable=self.last_name_value, width=30)\
            .grid(column=1, row=0)
        Entry(self, textvariable=self.first_name_value, width=30) \
            .grid(column=1, row=1)

    def get_values(self):
        """
        Méthode permétant de récupérer les données du formulaire en dehors de la
        Frame. Cette méthode doit être appelée par une fonction et non par
        l'action d'un bouton.

        :return: les données du formulaire
        :return type: Tuple
        """
        return self.first_name_value.get(), self.last_name_value.get()

    def set_defaut_values(self, first_name='John', last_name='Doe'):
        """
        Méthode permétant d'assigner des données par défaut aux composants du
        Frame.
        """
        self.first_name_value.set(first_name)
        self.last_name_value.set(last_name)


if __name__ == '__main__':

    root = Tk()
    root.title('Demo')

    user_frame = UserInfo(root)
    user_frame.pack()

    def log_form_values():
        first_name, last_name = user_frame.get_values()
        print("Data: ", first_name, "and", last_name)

    buttons_frame = Frame(root)

    Button(buttons_frame, text='Log',
           command=log_form_values).pack(side=RIGHT)

    Button(buttons_frame, text='defaut',
           command=user_frame.set_defaut_values).pack(side=RIGHT)

    buttons_frame.pack()

    root.mainloop()

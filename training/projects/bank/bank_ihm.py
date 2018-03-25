#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import *


class UserInfo(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        Frame.__init__(self, master, cnf, **kw)
        Label(self, text='nom').grid(column=0, row=0)
        Label(self, text='prenom').grid(column=0, row=1)

        self.last_name_value = StringVar()
        self.first_name_value = StringVar()

        Entry(self, textvariable=self.last_name_value, width=30) \
            .grid(column=1, row=0)
        Entry(self, textvariable=self.first_name_value, width=30) \
            .grid(column=1, row=1)

    def get_values(self):
        """
        Called to collect elements from the text fields

        :return: two strings : first name and last name
        """
        first_name = self.first_name_value.get()
        last_name = self.last_name_value.get()

        self.first_name_value.set('')
        self.last_name_value.set('')

        return first_name, last_name


root = Tk()
root.title('Create account')

user_frame = UserInfo(root)
user_frame.pack()

from training.projects.bank import bank_manager


def create_account():
    """
    Create a Person object and displays it.

    :return: None
    """
    first_name, last_name = user_frame.get_values()
    bank_manager.create_client(first_name, last_name)


Button(root, text='Create',
       command=create_account).pack()

root.mainloop()

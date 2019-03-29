#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk


class UserInfo(tk.Frame):
    def __init__(self, master=None, cnf={}, **kw):
        tk.Frame.__init__(self, master, cnf, **kw)
        tk.Label(self, text='nom').grid(column=0, row=0)
        tk.Label(self, text='prenom').grid(column=0, row=1)

        self.last_name_value = tk.StringVar()
        self.first_name_value = tk.StringVar()

        tk.Entry(self, textvariable=self.last_name_value, width=30) \
            .grid(column=1, row=0)
        tk.Entry(self, textvariable=self.first_name_value, width=30) \
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


root = tk.Tk()
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


tk.Button(root, text='Create',
          command=create_account).pack()

root.mainloop()

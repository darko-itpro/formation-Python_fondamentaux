"""
Demo de list box avec ajout, sélection et suppression.

Ce modèle de base ne gère que la liste de données affichée et aucune donnée plus complexe.
"""

import tkinter as tk

window = tk.Tk()
window.title('Demo list')

class ListBoxContainer(tk.Frame):
    def __init__(self, master=None, values=(), cnf={}, **kw):
        super().__init__(master=master, cnf=cnf, **kw)
        self._values = tk.Variable(window, (*values,))
        self._listbox = tk.Listbox(window, listvariable=self._values, selectmode='single')
        self._listbox.pack()


    def insert(self, position:int, data):
        self._listbox.insert(position, data)


    def add(self, data):
        self._listbox.insert(tk.END, data)


    def get_selected(self):
        values = self._values.get()
        selection = self._listbox.curselection()

        return [values[selected_index]
                for selected_index in selection]


    def del_selected(self):
        for selected_index in self._listbox.curselection()[::-1]:
            self._listbox.delete(selected_index)

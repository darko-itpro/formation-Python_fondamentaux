#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tkinter import Entry, Frame, Button, Listbox, Variable, Label
from tkinter import RIGHT, END
from tkinter import StringVar, IntVar


class EpisodeEntry(Frame):
    """
    Frame permétant de grouper le éléments du formulaire de saisie d'un épisode.
    """
    def __init__(self, master=None, action_callback=None, label_1_text=None, label_2_text=None):
        """
        Construct a frame widget with the parent MASTER

        :param master: Conteneur parent
        :param action_callback: Fonction déclenchée à la pression du bouton. Doit accepter deux paramètres.
        :param label_1_text: label à afficher pour le premier champ (texte)
        :param label_2_text: label à afficher pour le second champ (entier)
        """

        Frame.__init__(self, master)

        self._callback = action_callback

        form_frame = Frame(self)

        Label(form_frame, text=label_1_text if label_1_text else 'Label 1').grid(column=0, row=0)
        Label(form_frame, text=label_2_text if label_2_text else 'Label 2').grid(column=0, row=1)

        self.title_value = StringVar()
        self.number_value = IntVar()

        Entry(form_frame, textvariable=self.title_value, width=30).grid(column=1, row=0)
        Entry(form_frame, textvariable=self.number_value, width=30).grid(column=1, row=1)

        form_frame.pack()
        Button(self, text='Ajouter', command=self.button_action).pack()

    def button_action(self):
        """
        Action du bouton ajouter.

        .. note:: cette méthode pourrait être privée, néanmoins la visibilité
        publique laisse la possibilité de faire appel à cette action à partir
        d'un composant externe.
        """
        self._callback(self.title_value.get(), self.number_value.get())
        self.title_value.set("")
        self.number_value.set("")

    def get_values(self):
        """
        Permet d'obtenir les valeurs saisies par l'utilisateur.

        :return: les valeurs des champs de saisie
        :rtype: str, int
        """
        ep_title = self.title_value.get()
        ep_number = self.number_value.get()

        self.title_value.set("")
        self.number_value.set("")

        return ep_title, ep_number

    def set_values(self, title, number):
        """
        Permet de communiquer des valeurs à afficher dans le formulaire

        :param title: Titre de l'épisode
        :type title: str
        :param number: Numéro de l'épisode
        :type number: int
        """
        self.title_value.set(title)
        self.number_value.set(number)


class CollectionFrame(Frame):
    """
    Frame permétant de gérer la collection d'épisodes.
    """
    def __init__(self, master=None, select_callback=None, delete_callback=None):
        """
        Construct a frame widget with the parent MASTER

        :param master: Conteneur parent
        :param select_callback: Fonction déclenchée lors de la sélection d'un élément. Doit accepter un paramètre qui sera l'indice de l'élément sélectionné.
        :param delete_callback: Fonction déclenchée lors de la suppression d'un élément. Doit accepter un paramètre qui sera l'indice de l'élément sélectionné dont la donnée devra être supprimée.
        """
        Frame.__init__(self, master)

        self._select_callback = select_callback
        self._delete_callback = delete_callback

        choices = Variable(self)
        self.listbox = Listbox(self, listvariable=choices, selectmode='single')
        self.listbox.pack()

        buttons_frame = Frame(self)
        Button(buttons_frame, text="Select", command=self.get_selected_element).pack(side=RIGHT)
        Button(buttons_frame, text="Delete", command=self.delete_selected_element).pack(side=RIGHT)
        buttons_frame.pack()

    def add_element(self, element, index=END):
        """
        Ajoute un épisode dans la liste. L'index permet d'ordonner les épisodes.

        :param element: Titre de l'épisode
        :param index: indice d'insertion
        :return: None
        """
        self.listbox.insert(index, element)

    def get_selected_element(self):
        """
        Déclenche la fonction `select_callback` passée en paramètre afin de lui
        communiquer l'indice de l'élément sélectionné.

        .. note:: cette méthode pourrait être privée, néanmoins la visibilité
        publique laisse la possibilité de faire appel à cette action à partir
        d'un composant externe.
        """
        curselection = self.listbox.curselection()
        if len(curselection) != 1:
            print("Pas de selection")
        else:
            self._select_callback(curselection[0])

    def delete_selected_element(self):
        """
        Supprime un épisode de la liste les affichant.

        .. note:: cette méthode pourrait être privée, néanmoins la visibilité
        publique laisse la possibilité de faire appel à cette action à partir
        d'un composant externe.
        """
        curselection = self.listbox.curselection()
        if len(curselection) != 1:
            print("Pas de selection")
        else:
            ep_index = curselection[0]
            self.listbox.delete(ep_index)
            self._delete_callback(ep_index)

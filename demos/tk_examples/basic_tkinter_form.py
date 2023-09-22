"""
Code demo pour tkInter
"""

import tkinter as tk


class UserInfo(tk.Frame):
    """
    La classe UserInfo hérite de Frame. Il s'agit donc d'une Frame avec des
    composants et deux méthodes afin de communiquer avec ces composants.
    """
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)
        tk.Label(self, text='nom').grid(column=0, row=0)
        tk.Label(self, text='prenom').grid(column=0, row=1)

        self._last_name_value = tk.StringVar()
        self._first_name_value = tk.StringVar()

        tk.Entry(self, textvariable=self._last_name_value, width=30)\
            .grid(column=1, row=0)
        tk.Entry(self, textvariable=self._first_name_value, width=30) \
            .grid(column=1, row=1)

    def get_values(self):
        """
        Méthode permétant de récupérer les données du formulaire en dehors de la
        Frame. Cette méthode doit être appelée par une fonction et non par
        l'action d'un bouton.

        :return: les données du formulaire
        :return type: Tuple
        """
        return self._first_name_value.get(), self._last_name_value.get()

    def set_defaut_values(self, first_name='John', last_name='Doe'):
        """
        Méthode permétant d'assigner des données par défaut aux composants du
        Frame.
        """
        self._first_name_value.set(first_name)
        self._last_name_value.set(last_name)


def log_form_values():
    """
    Fonction appelée par le bouton pour faire un log du contenu des champs.
    """
    first_name, last_name = user_frame.get_values()
    print("Data: ", first_name, "and", last_name)


if __name__ == '__main__':

    window = tk.Tk()
    window.title('Demo')

    user_frame = UserInfo(window)
    user_frame.pack()

    buttons_frame = tk.Frame(window)

    tk.Button(buttons_frame, text='Log',
              command=log_form_values).pack(side=tk.RIGHT)

    tk.Button(buttons_frame, text='Defaut',
              command=user_frame.set_defaut_values).pack(side=tk.RIGHT)

    buttons_frame.pack()

    tk.Button(window, text='Quit', command=window.quit).pack()

    window.mainloop()

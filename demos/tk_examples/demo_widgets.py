"""
Ce module propose des widgets custom de base.
"""

import tkinter as tk


class BasicForm(tk.Frame):
    """
    Frame de formulaire
    """
    def __init__(self, master=None, label_1_text=None, label_2_text=None):

        tk.Frame.__init__(self, master)

        tk.Label(self, text=label_1_text if label_1_text else 'Label 1')\
            .grid(column=0, row=0)
        tk.Label(self, text=label_2_text if label_2_text else 'Label 2')\
            .grid(column=0, row=1)

        self.field_1_value = tk.StringVar()
        self.field_2_value = tk.StringVar()

        tk.Entry(self, textvariable=self.field_1_value, width=30)\
            .grid(column=1, row=0)
        tk.Entry(self, textvariable=self.field_2_value, width=30)\
            .grid(column=1, row=1)

    def get_values(self):
        """
        Permet d'obtenir les valeurs saisies par l'utilisateur.
        """
        value_1 = self.field_1_value.get()
        value_2 = self.field_2_value.get()

        self.field_1_value.set("")
        self.field_2_value.set("")

        return value_1, value_2

    def set_values(self, value_1: int, value_2: int):
        """
        Permet de communiquer des valeurs à afficher dans le formulaire

        """
        self.field_1_value.set(value_1)
        self.field_2_value.set(value_2)


if __name__ == "__main__":
    window = tk.Tk()
    BasicForm(window).pack()
    window.mainloop()

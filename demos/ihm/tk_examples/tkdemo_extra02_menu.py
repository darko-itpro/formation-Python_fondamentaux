"""
Démo pour créer un menu basique

Le menu qui apparait dans la barre du haut de la fenêtre est un conteneur pour
les autres éléments du menu. Chaque élément final est l'équivalent d'un bouton
associé à une fonction.
"""

import tkinter as tk

if __name__ == '__main__':

    window = tk.Tk()
    window.title('Demo Menu')

    menubar = tk.Menu(window)
    window.config(menu=menubar)
    file_menu = tk.Menu(menubar)
    file_menu.add_command(label="New")
    file_menu.add_separator()
    file_menu.add_command(label="Load")
    file_menu.add_command(label="Save")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)

    edit_menu = tk.Menu(menubar)
    edit_menu.add_command(label="Cut")
    edit_menu.add_command(label="Copy")
    edit_menu.add_command(label="Past")

    menubar.add_cascade(label="File", menu=file_menu)
    menubar.add_cascade(label="Edit", menu=edit_menu)

    window.mainloop()

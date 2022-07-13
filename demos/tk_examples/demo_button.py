"""
Exemple de code Python avec un bouton de log basique et Quit
"""

import tkinter as tk

window = tk.Tk()
window.geometry('100x50')
window.title('Demo button')


def log():
    print("Click on log")


tk.Button(window, text="log", command=log).pack()
tk.Button(window, text="quit", command=window.quit).pack()

window.mainloop()

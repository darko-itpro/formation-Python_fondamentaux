#!/usr/bin/env python

"""
Demo de l'usage de l'ouverture de fichier.
"""

import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title('Demo file')
window.geometry('100x50')

def load():
    filename = filedialog.askopenfilename(initialdir=".", title="Select file",
                                          filetypes=(("Text files", "*.txt"),
                                                     ("All file", "*.*")))


tk.Button(window, text="Load", command=load).pack()
tk.Button(window, text="Quit", command=window.quit).pack()

window.mainloop()

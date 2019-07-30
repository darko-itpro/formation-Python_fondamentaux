#!/usr/bin/env python 
import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title('Demo file')


def load():
    filename = filedialog.askopenfilename(initialdir=".", title="Select file",
                                          filetypes=(("Text files", "*.txt"),
                                                     ("All file", "*.*")))


tk.Button(window, text="load", command=load).pack()

window.mainloop()

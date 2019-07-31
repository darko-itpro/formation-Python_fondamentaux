#!/usr/bin/env python 
import tkinter as tk

window = tk.Tk()
window.title('Demo label')

tk.Label(window, text="Hello World").pack()

window.mainloop()

#!/usr/bin/env python 
import tkinter as tk

window = tk.Tk()
window.title('Demo button')


def log():
    print("Click on log")


tk.Button(window, text="log", command=log).pack()
tk.Button(window, text="quit", command=window.quit).pack()

window.mainloop()

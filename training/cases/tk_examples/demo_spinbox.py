#!/usr/bin/env python 
import tkinter as tk

window = tk.Tk()
window.title('Demo spinbox')

box = tk.Spinbox(window, from_=0, to=10)
box.pack()


def log():
    print(f"Value is {box.get()}")


tk.Button(window, text="log", command=log).pack()

window.mainloop()

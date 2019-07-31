#!/usr/bin/env python 
import tkinter as tk

window = tk.Tk()
window.title('Demo entry')

value = tk.StringVar()
tk.Entry(window, textvariable=value, width=30).pack()


def set_value():
    value.set("Default value")


def log():
    print(f"Log value {value.get()}")


tk.Button(window, text="set", command=set_value).pack()
tk.Button(window, text="log", command=log).pack()

window.mainloop()

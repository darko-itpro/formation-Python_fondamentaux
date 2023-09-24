"""
Demo de l'interraction avec un champ de saisie.
"""

import tkinter as tk

window = tk.Tk()
window.title('Demo entry')


def set_value():
    value.set("Default value")


def log():
    print(f"Log value {value.get()}")


value = tk.StringVar()
tk.Entry(window, textvariable=value, width=30).pack()

tk.Button(window, text="Set Default", command=set_value).pack()
tk.Button(window, text="Log", command=log).pack()
tk.Button(window, text="Quit", command=window.quit).pack()

window.mainloop()

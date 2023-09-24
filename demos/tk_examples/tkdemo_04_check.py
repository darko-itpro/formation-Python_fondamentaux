"""
Demo de check button complétant la saisie d'un champ.
"""

import tkinter as tk

window = tk.Tk()
window.title('Demo entry')


def log():
    print(f"Log value {value.get() * (1 + vat.get() / 100)}")


value = tk.IntVar()
vat = tk.IntVar()

tk.Entry(window, textvariable=value, width=30).pack()
tk.Checkbutton(window, text="TTC", variable=vat, onvalue=0, offvalue=20).pack()

tk.Button(window, text="Log", command=log).pack()
tk.Button(window, text="Quit", command=window.quit).pack()

window.mainloop()

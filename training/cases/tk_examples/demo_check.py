#!/usr/bin/env python 
import tkinter as tk

window = tk.Tk()
window.title('Demo entry')

value = tk.IntVar()
vat = tk.IntVar()

tk.Entry(window, textvariable=value, width=30).pack()
tk.Checkbutton(window, text="TTC", variable=vat, onvalue=20, offvalue=0).pack()

def log():
    print(f"Log value {value.get() * (1 + vat.get() / 100)}")


tk.Button(window, text="log", command=log).pack()

window.mainloop()

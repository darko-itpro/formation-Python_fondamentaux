#!/usr/bin/env python 
import tkinter as tk

window = tk.Tk()
window.title('Demo list')

other_knights = ['Robin', 'Bedivere', 'Galahad']

values = tk.Variable(window, ('Arthur', 'Merlin', 'Lancelot'))
listbox = tk.Listbox(window, listvariable=values, selectmode='single')
listbox.pack()


def add():
    listbox.insert(tk.END, other_knights.pop(0))


def log_selected():
    print(listbox.curselection())
    print(values.get())
    for selected_index in listbox.curselection():
        print(values.get()[selected_index])


tk.Button(window, text="Add knight", command=add).pack()
tk.Button(window, text="Log selected", command=log_selected).pack()

window.mainloop()

"""
Demo de list box avec ajout et sélection.
"""

import tkinter as tk

window = tk.Tk()
window.title('Demo list')

values = tk.Variable(window, ('Arthur', 'Merlin', 'Lancelot'))
listbox = tk.Listbox(window, listvariable=values, selectmode='single')
listbox.pack()

value = tk.StringVar()
tk.Entry(window, textvariable=value).pack()


def add():
    new_knight = value.get()
    if len(new_knight) > 0 and not new_knight.isspace():
        listbox.insert(tk.END, new_knight)
    value.set("")


def log_selected():
    print(listbox.curselection())
    print(values.get())
    for selected_index in listbox.curselection():
        print(values.get()[selected_index])


tk.Button(window, text="Add knight", command=add).pack()
tk.Button(window, text="Log selected", command=log_selected).pack()
tk.Button(window, text="Quit", command=window.quit).pack()

window.mainloop()

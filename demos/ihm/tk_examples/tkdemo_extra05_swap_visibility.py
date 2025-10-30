"""
Démo pour montrer l'affichage ou la suppression de l'affichage d'un widget.
"""

import tkinter as tk

window = tk.Tk()
window.title('Demo button')

def swap_frame():
    if entry.winfo_ismapped():
        entry.pack_forget()
    else:
        entry.pack()

entry = tk.Entry(window)
entry.pack()

tk.Button(window, text="Quit", command=window.quit).pack(side=tk.BOTTOM)
tk.Button(window, text="Swap", command=swap_frame).pack(side=tk.BOTTOM)

window.mainloop()

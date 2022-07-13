"""
demo de mise en forme avec un grid layout
"""

import tkinter as tk

window = tk.Tk()
window.title('Demo grid Form')

tk.Label(window, text="First Name").grid(row=0, column=0)
tk.Entry(window, width=30).grid(row=0, column=1, columnspan=2)
tk.Label(window, text="Last Name").grid(row=1, column=0)
tk.Entry(window, width=30).grid(row=1, column=1, columnspan=2)

tk.Button(window, text="Submit").grid(row=2, column=1)
tk.Button(window, text="Quit", command=window.quit).grid(row=2, column=2)

window.mainloop()

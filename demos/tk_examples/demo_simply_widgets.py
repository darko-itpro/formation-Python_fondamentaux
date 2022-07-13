"""
Presentation de base de widgets standards.
"""

import tkinter as tk

window = tk.Tk()
window.title('Demo button')

tk.Entry(window).pack()
tk.Checkbutton(window, text="check").pack()
tk.Button(window, text="Log").pack()
tk.Button(window, text="Quit").pack()

window.mainloop()

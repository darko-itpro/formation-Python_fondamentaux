"""
Demo d'une fenêtre de formulaire avec un mix de layouts.
"""

import tkinter as tk

window = tk.Tk()
window.title('Demo mixed Form')

form_frame = tk.Frame(window)
control_frame = tk.Frame(window)

tk.Label(form_frame, text="First Name").grid(row=0, column=0)
tk.Entry(form_frame, width=30).grid(row=0, column=1, columnspan=2)
tk.Label(form_frame, text="Last Name").grid(row=1, column=0)
tk.Entry(form_frame, width=30).grid(row=1, column=1, columnspan=2)

tk.Button(control_frame, text="Quit", command=window.quit).pack(side=tk.RIGHT)
tk.Button(control_frame, text="Submit").pack(side=tk.RIGHT)

form_frame.pack()

control_frame.pack(side=tk.RIGHT)

window.mainloop()

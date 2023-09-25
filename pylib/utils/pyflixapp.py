import tkinter as tk
from tkinter import filedialog
import pylib.load_and_display as ld

SHOWS = {}

def load():
    filename = filedialog.askopenfilename(initialdir=".", title="Select file",
                                          filetypes=(("CSV files", "*.csv"),
                                                     ("All files", "*.*")))

    shows = ld.load_data_from_path(filename)
    SHOWS.update(shows)
    for show in SHOWS.values():
        shows_spinner.insert(tk.END, show.name)

def open_shows():
    filename = filedialog.askopenfilename(initialdir=".", title="Select file",
                                          filetypes=(("Show files", "*.db"),
                                                     ("All files", "*.*")))

if __name__ == '__main__':

    window = tk.Tk()
    window.title('PyFlix BackEnd')

    menubar = tk.Menu(window)
    file_menu = tk.Menu(menubar)
    file_menu.add_command(label="Open shows", command=open_shows)
    file_menu.add_separator()
    file_menu.add_command(label="Load shows", command=load)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=file_menu, underline=0)
    window.config(menu=menubar)

    shows_var = tk.StringVar(window)
    shows_spinner = tk.Spinbox(window, values=list(SHOWS), textvariable=shows_var)
    shows_spinner.pack()

    window.mainloop()

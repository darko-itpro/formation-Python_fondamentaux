"""
Demo de l'usage de l'ouverture de fichier.
"""

import tkinter as tk
from tkinter import filedialog


def load():
    """
    Open a Tkinter file dialog and returns the selected filename.

    :return: The filename of the file selected
    """
    filename = filedialog.askopenfilename(initialdir=".", title="Select file",
                                          filetypes=(("CSV files", "*.csv"),
                                                     ("All files", "*.*")))

    return filename


if __name__ == "__main__":
    window = tk.Tk()
    window.title('Demo file')
    window.geometry('100x50')

    tk.Button(window, text="Load", command=load).pack()
    tk.Button(window, text="Quit", command=window.quit).pack()

    window.mainloop()

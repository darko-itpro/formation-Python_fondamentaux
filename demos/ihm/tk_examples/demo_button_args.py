import tkinter as tk

window = tk.Tk()
window.geometry('100x50')
window.title('Demo button')

widget.bind(event, handler, add=None)

def log(option):
    print("Click on log", option)


tk.Button(window, text="log",
          command=lambda: log("")).pack()
tk.Button(window, text="Fancy log",
          command=lambda: log("with style")).pack()
tk.Button(window, text="quit", command=window.quit).pack()

window.mainloop()

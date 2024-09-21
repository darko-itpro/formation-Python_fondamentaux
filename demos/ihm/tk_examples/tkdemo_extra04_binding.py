import tkinter as tk

window = tk.Tk()
window.geometry('100x100')
window.title('Demo button')


def set_value():
    value.set("Default value")


def log(event=None):
    print(f"Log value {value.get()}")


value = tk.StringVar()
text_field = tk.Entry(window, textvariable=value, width=30)
text_field.bind("<Return>", log)
text_field.pack()

log_button = tk.Button(window, text="log", command=log)
log_button.bind('<Return>', log)
log_button.pack()

tk.Button(window, text="set", command=set_value).pack()
tk.Button(window, text="quit", command=window.quit).pack()

text_field.focus()
window.mainloop()

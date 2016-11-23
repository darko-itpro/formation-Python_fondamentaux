#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *

from training.poo.stacks import tasks


class TaskFrame(Frame):
    def __init__(self, master=None, fcallback=None):
        Frame.__init__(self, master=None)
        Label(self, text="Add task name").pack()

        self.task_name = StringVar()
        Entry(self, textvariable=self.task_name, width=30).pack()

        def get_value():
            task_name_str = self.task_name.get()
            self.task_name.set('')
            fcallback(tasks.Task(task_name_str))

        Button(self, text='Add', command=get_value).pack()


class TasksStack(Frame):
    def __init__(self, master=None, cnf={}, **kw):
        Frame.__init__(self, master=None, cnf={}, **kw)

        choices = Variable(self, (tasks.Task('MyTask'),))
        self.tasks_listbox = Listbox(self, listvariable=choices, selectmode='single')
        self.tasks_listbox.pack()

    def add_task(self, task):
        self.tasks_listbox.insert(END, task)


if __name__ == '__main__':
    root_window = Tk()
    root_window.title("Task Manager")

    def print_value(value):
        print(value)

    stack_view = TasksStack(root_window)
    stack_view.pack(side=RIGHT)
    #TaskFrame(root_window).pack(side=RIGHT)
    TaskFrame(root_window, fcallback=stack_view.add_task).pack()

    root_window.mainloop()
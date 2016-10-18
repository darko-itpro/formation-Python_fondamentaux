#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Ce module propose une interface terminal pour la gestion d'une pile de taches.
Ce module est incomplet et est destiné à être repris par les stagiaires.

"""

from __future__ import print_function
from builtins import input

# Change import module name to your module
import training.poo.stack as stack


def display_help():
    print("Task manager ready")
    try:
        print("Current task size: {}".format(task_manager.stack_size()))
    except AttributeError:
        pass
    print("[a] - Add a Task")
    print("[g] - Get next Task")
    print("[e] - Exit")


if __name__ == '__main__':

    task_manager = stack.Lifo()

    while True:
        display_help()
        try:
            char_choice = str(input("Your choice: "))
            if char_choice not in 'age':
                raise ValueError("Select option in current choices")

        except (TypeError, ValueError):
            print("Please choose an valid option")
            continue

        if char_choice == "a":
            try:
                new_task = str(input("Your task: "))
            except TypeError:
                print("This is not a task...")
                continue

            task_manager.empile(new_task)

        elif char_choice == "g":
            print("Nest task:\n\n\t{}\n".format(task_manager.depile()))

        elif char_choice == "e":
            print("Leaving, bye")
            break

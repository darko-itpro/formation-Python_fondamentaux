#!/usr/bin/env python 
# -*- coding: utf-8 -*-

from training.projects.stacks import stack


def get_next_element():
    """
    Fonction qui affiche le prochain élément en le supprimant de la liste.
    :return:
    """
    print("Prochain élément est {}".format(_stack.pop()))


def add_element():
    """
    Fonction qui permet d'ajouter un élément à la stack
    :return:
    """
    element = input("Élément à ajouter : ")
    _stack.push(element)

actions = {}
actions["a"] = add_element
actions["n"] = get_next_element

if __name__ == "__main__":
    print("Gestion de piles")
    stack_name = input("Nom de la pile ? ")
    _stack = stack.Lifo(stack_name)

    while True:
        print("""
        [a] ajouter un élément
        [n] obtenir prochain élément
        [q] sortie
        """)

        choice = input("Choix ? ")
        if choice == "q":
            break
        elif choice in actions:
            actions[choice]()
        else:
            print("Choix non valide")

    print("Bye")

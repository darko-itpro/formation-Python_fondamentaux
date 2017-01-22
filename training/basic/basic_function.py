#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
    Iteration sur séquence
    ^^^^^^^^^^^^^^^^^^^^^^

    Écrivez une fonction qui permet d'afficher chaque élément d'une séquence.

    #. Affichez chaque caractère d'une chaine à l'aide de cette fonction.

    #. Affichez chaque élément d'une liste à l'aide de cette fonction.

    #. Afficher chaque mot de la chaîne de caractère à l'aide de cette fonction.

"""


def print_each_element(sequence):
    for element in sequence:
        print(element)

if __name__ == '__main__':
    ma_chaine = "hello world"
    ma_liste = ["Python", "Java", "Swift"]

    print_each_element(ma_chaine)
    print('-----')
    print_each_element(ma_liste)
    print('-----')
    print_each_element(ma_chaine.split())

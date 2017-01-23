#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    #. Affichez les entiers de 0 à 15 non compris de 3 en 3 en utilisant la boucle
       **for** et la fonction **range()**
    #. Affichez chaque caractère d'une chaine en utilisant la boucle **for**
    #. Affichez chaque élément d'une liste en utilisant la boucle **for**
"""

from __future__ import print_function

if __name__ == '__main__':

    for i in range(0, 15, 3):
        print(i)

    ma_chaine = "hello world"

    for char in ma_chaine:
        print (char)

    ma_liste = ["Python", "Java", "Swift"]

    for lang in ma_liste:
        print (lang)

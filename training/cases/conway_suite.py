#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Gestion d'une suite de Conway

Ce module utilise les annotations pour informer sur les types attendus.

.. seealso:: https://fr.wikipedia.org/wiki/Suite_de_Conway

"""

import typing


def next_member(member: typing.Union[int, str]) -> int:
    """
    Pour un élément, retourne l'élément suivant de la suite de Conway.

    :param member: Un entier
    :return: L'entier suivant dans la suite de Conway
    """
    member = str(member)

    next_one = []
    last_value = member[0]
    occurrences = 1

    for value in member[1:]:
        if last_value == value:
            occurrences += 1
        else:
            next_one.append(str(occurrences))
            next_one.append(str(last_value))
            last_value = value
            occurrences = 1

    next_one.append(str(occurrences))
    next_one.append(str(last_value))

    return int("".join(next_one))


def print_next_occurences(initial_value: typing.Union[int, str] = 1,
                          occurrences: int = 1):
    """
    Affiche les `occurences` éléments suivants d'une suite avec la valeur de
    départ `initial_value`.

    :param initial_value: Valeur initiale, 1 par défaut.
    :param occurrences: Nombre d'occurences de la suite, 1 par défaut.
    """
    value = str(initial_value)
    print(value)
    for occurrence in range(occurrences):
        value = next_member(value)
        print(value)


if __name__ == '__main__':
    pass

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Démonstration de l'accès basique aux arguments de la ligne de commande.
"""

import sys

if __name__ == '__main__':
    print("-- Exemple usage args --")
    for arg in sys.argv:
        print(arg)

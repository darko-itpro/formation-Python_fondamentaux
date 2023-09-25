"""
Ce module compare l'utilisation du module os.path et l'objet Path pour construire
un chemin dans l'arborescence de fichiers à partir du module en lui-même.

Ce module contient des fonctions qui se focalisent sur une illustration. Décommentez
successivement leur appel pour voir le comportement.
"""

from pathlib import Path
import os.path

SEP = "-" * 10

def display_filepath():
    print("Contenu de la vairable __file__ :")
    print(__file__)
    print(SEP)
    print("Création d'un objet Path avec le paramètre __file__ :")
    print(Path(__file__))

def display_parentpath():
    print("Déduction du parent avec os.path.split :")
    print(f"{os.path.split(__file__)[0]=}")
    print(SEP)
    print("Déduction du parent avec l'objet Path :")
    print(f"{Path(__file__).parent=}")

def display_childpath():
    print("Construction du chemin voisin avec os.path.split :")
    print(f"{os.path.join(os.path.split(__file__)[0], 'argument')=}")
    print(SEP)
    print("Construction du chemin voisin avec l'objet Path :")
    print(f"{Path(__file__).parent / 'arguments' =}")


#display_filepath()
#display_parentpath()
#display_childpath()

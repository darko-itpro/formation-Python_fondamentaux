#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Sujet
-----

- Définir la liste ma_liste = [17, 38, 10, 25, 72]
- triez et affichez la liste
- ajoutez l'élément 12 à la liste et affichez la.
- renversez et affichez la liste
- affichez l'indice de l'élément 17
- enlevez l'élément 38 et affichez la liste
- affichez la sous-liste du 2ème au 3ème élément
- affichez la sous-liste du début au 2ème élément
- affichez la sous-liste du 3ème à la fin de la liste
- Affichez le dernier élément
- créez une copie de votre liste dans une nouvelle variable
- ajoutez à votre nouvelle liste l'élément 42, que remarquez—vous ?

"""

ma_liste = [17, 38, 10, 25, 72]

ma_liste.sort()
print "Ma liste triee : {}".format(ma_liste)

ma_liste.append(12)
print "Ma liste ajout 12 : {}".format(ma_liste)

ma_liste.reverse()
print "Ma liste inversee : {}".format(ma_liste)

print "Ma liste position 17 : {}".format(ma_liste.index(17))

ma_liste.remove(38)
print "Ma liste sans 38 : {}".format(ma_liste)

print "Ma liste de 2 a 3 : {}".format(ma_liste[2:4])

print "Ma liste jusuq'a 2 : {}".format(ma_liste[:3])

print "Ma liste a parir de 3 : {}".format(ma_liste[3:])

print "Ma liste dernier element : {}".format(ma_liste[-1])

# Il n'y a pas ici de ma_deuxieme_liste = ma_liste, voici comment faire une
# copie

ma_deuxieme_liste = ma_liste[:]

ma_deuxieme_liste.append(42)

print ma_liste
print ma_deuxieme_liste

# Et une autre méthode pour faire une copie

ma_deuxieme_liste = list(ma_liste)

ma_deuxieme_liste.append(42)

print ma_liste
print ma_deuxieme_liste

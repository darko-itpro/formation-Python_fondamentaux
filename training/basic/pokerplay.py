#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Simulation d'un jeu de cartes.
"""

deck = [chr(x) for x in (list(range(0x1f0a1, 0x1f0af))
                         + list(range(0x1f0b1, 0x1f0bf))
                         + list(range(0x1f0c1, 0x1f0cf))
                         + list(range(0x1f0d1, 0x1f0df)))]
print(deck)
print(len(deck))

hand = deck[:5]
deck = deck[5:]

print(hand)

hand_player1 = deck[:10:2]
hand_player2 = deck[1:11:2]
deck = deck[10:]

print(hand_player1)
print(hand_player2)

n_players = 4
for player in range(n_players):
    print(deck[0 + player: (5*n_players) + player: n_players])


def new_deck():
    return [chr(x) for x in (list(range(0x1f0a1, 0x1f0af))
                         + list(range(0x1f0b1, 0x1f0bf))
                         + list(range(0x1f0c1, 0x1f0cf))
                         + list(range(0x1f0d1, 0x1f0df)))]


def draw_hands(number_players, fdeck):
    """
    La fonction utilise des variables fdeck et fplayer pour éviter la confusion avec les noms des variables globales.

    :param number_players:
    :param fdeck:
    :return:
    """
    hands = []

    if len(fdeck) == 56:
        import random
        random.shuffle(fdeck)

    for fplayer in range(n_players):
        hands.append(fdeck[0 + fplayer: (5 * n_players) + fplayer: n_players])
    fdeck = fdeck[number_players * 5:]

    return hands, fdeck

print('-----')
print(draw_hands(4, new_deck()))


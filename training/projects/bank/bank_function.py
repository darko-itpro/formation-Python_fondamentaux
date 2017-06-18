#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Ce module présente la gestion de comptes bancaires sous forme de fonctions.
"""

accounts = {}

def create(nid, balance):
    accounts[nid] = float(balance)


def deposit(nid, value):
    if nid in accounts:
        accounts[nid] += float(value)


def withdraw(nid, value):
    if nid in accounts:
        accounts[nid] -= float(value)

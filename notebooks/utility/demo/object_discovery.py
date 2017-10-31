#!/usr/bin/env python 
# -*- coding: utf-8 -*-


class Account:

    def __init__(self, nid, balance=100, overdraft=False):
        self._id = nid
        self._balance = balance
        self.overdraft = overdraft

    def deposit(self, value):
        self._balance += value

    def withdraw(self, value):
        self._balance -= value

    def nid(self):
        return self._id

    def balance(self):
        return self._balance


if __name__ == '__main__':
    pass
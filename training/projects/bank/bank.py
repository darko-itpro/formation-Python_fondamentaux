#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module métier de gestion bancaire
---------------------------------


"""

from datetime import datetime


class BusinessError(Exception):
    """
    Exception destinée à identifier des erreurs métier.
    """
    def __init__(self, value, cause=None):
        super().__init__(value + u', caused by ' + repr(cause))
        self.cause = cause

    def __str__(self):
        return repr(self._value)


class Personne(object):
    """
    My class Personne

    >>> personne = Personne('Durant', 'Gilles')
    >>> personne._nom
    'Durant'

    """

    def __init__(self, nom, prenom):
        self._nom = nom
        self._prenom = prenom

    def nom(self):
        return self._nom

    def prenom(self):
        return self._prenom

    def __str__(self):
        return "Personne object %s %s" % (self._prenom, self._nom)


class Client(Personne):
    def __init__(self, nom, prenom, id, join_date=datetime.now(), is_vip=False):
        Personne.__init__(self, nom, prenom)
        self._identifiant = id
        self._join_date = join_date
        self._is_vip = is_vip
        self._accounts = {}

    def add_account(self, accout):
        self._accounts[accout._id] = accout

    def has_vip_privileges(self):
        """
        Client has VIP privileges if he is VIP or if he is a client for more
        than 5 years (1825 days)

        :return:
        """
        return self._is_vip or (datetime.now() - self._join_date).days > 1825

    def __str__(self):
        return "{}, {}".format(self._nom, self.prenom())


class BankAccount(object):
    """
    A Bank account
    """
    def __init__(self, nid, balance=100):
        if not nid:
            raise ValueError('Bank account must have an ID')

        if float(balance) < 0:
            raise ValueError('Balance cannot be lower than 0, currently %d'
                             % balance)

        self._id = nid
        self._balance = float(balance)

    def deposit(self, value):
        if float(value) >= 0:
            self._balance += float(value)
        else:
            raise ValueError("Negative value")

    def withdraw(self, value):
        if 0 < value < self._balance:
            value -= value
        elif self._balance < value:
            raise BusinessError("Insufficient funds")
        else:
            raise ValueError("Negative value")

    def id(self):
        return self._id

    def _get_balance(self):
        return self._balance

    balance = property(_get_balance)

    def __str__(self):
        return "Compte client {} - solde {}"\
            .format(self._id, self._balance)

    def __repr__(self):
        return "BankAccount.{}".format(self._id)

    def __lt__(self, other):
        return self._id < other.id()


class DeferedAccount(BankAccount):
    """
        For a deffered account, withdraws does not change the balance. A special
        method is added to trigger the actions
    """
    def __init__(self, nid, balance=100):
        BankAccount.__init__(self, nid, balance)
        self._operations = []

    def withdraw(self, value):
        self._operations.append(value)

    def triggerMonthlyOperation(self):
        while self._operations:
            self._balance -= self._operations.pop()


class DebtAccount(BankAccount):
    pass


if __name__ == '__main__':

    import doctest
    doctest.testmod()


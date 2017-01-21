#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Gestion des comptes banquaires
------------------------------


"""


from datetime import datetime
import training.poo.bank

clients = {}

MAX_ACCOUNTS = 5
VIP_MAX_ACCOUNTS = 6
MIN_DEPOSIT = 100


def create_client(first_name, last_name, is_vip=False, join=datetime.now()):
    if not first_name or not last_name:
        raise ValueError('Name should be set')

    clientId = first_name+last_name

    if clients.get(id):
        raise training.poo.bank.BusinessError('Client %s %s already exists'
                                              % first_name, last_name)

    clients[clientId] = training.poo.bank.Client(last_name, first_name, clientId, join, is_vip)


def get_clients():
    return clients.values()


def get_client(client_id):
    return clients.get(client_id)


def add_account(id_client, open_balance):
    """
    Add an account to an existing client
    :param id_client:
    :param open_balance:
    :return: the newly created account id
    """
    client = clients[id_client]

    if not client:
        raise ValueError('Client id %s does not exist' % id_client)

    if open_balance < MIN_DEPOSIT:
        raise training.poo.bank.BusinessError('Minimum deposit required',
                                              ValueError('opne balance : %d' % open_balance))

    if len(client._accounts) < VIP_MAX_ACCOUNTS if client._is_vip else MAX_ACCOUNTS:
        new_bank_account = training.poo.bank.BankAccount(client._identifiant + str(datetime.now().microsecond), open_balance)
        client.add_account(new_bank_account)
        return new_bank_account._id
    else:
        raise training.poo.bank.BusinessError('Client have max accounts')


def deposit(client_id, account_id, ammount):
    clients[client_id][account_id].deposit(ammount)


def withdraw(client_id, account_id, ammount):
    clients[client_id][account_id].withdraw(ammount)
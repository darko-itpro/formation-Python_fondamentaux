#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Ce module illustre les tests avec PyTest.
"""

from training.projects.bank import bank
import pytest


def test_basic_account():
    account = bank.BankAccount('012345')
    assert 100 == account.balance


def test_account_with_balance():
    account = bank.BankAccount('012345', 500)
    assert 500 == account.balance


def test_account_with_balance_as_string():
    account = bank.BankAccount('012345', '500')
    assert 500 == account.balance


@pytest.fixture()
def basic_account():
    return bank.BankAccount('012345', 500)


def test_basic_deposit(basic_account):
    basic_account.deposit(100)
    assert 600 == basic_account.balance


def test_negative_deposit(basic_account):
    with pytest.raises(ValueError):
        basic_account.deposit(-100)

#!/usr/bin/env python 

from faker import Faker
from training.projects.bank import bank
import pytest
fake = Faker('fr_FR')


def test_bank_account_creation():
    iban = fake.iban()
    my_account = bank.BankAccount(iban)
    assert my_account.nid == iban
    assert my_account.balance == 100


def test_account_id_should_not_be_modified():
    iban = fake.iban()
    my_account = bank.BankAccount(iban)
    with pytest.raises(AttributeError):
        my_account.nid = "new one"


def test_balance_should_not_be_modified():
    iban = fake.iban()
    my_account = bank.BankAccount(iban)
    with pytest.raises(AttributeError):
        my_account.balance = 500

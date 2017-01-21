#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import unittest
from training.poo.bank import bank


class TestCreateAccount(unittest.TestCase):

    def testBasicAccount(self):
        account = bank.BankAccount('012345')
        self.assertEqual(100, account.balance())

    def testAccountWithBalance(self):
        account = bank.BankAccount('012345', 500)
        self.assertEqual(500, account.balance())

    def testAccountWithBalanceAsString(self):
        account = bank.BankAccount('012345', '500')
        self.assertEqual(500, account.balance())

class TestDeposit(unittest.TestCase):

    def setUp(self):
        self.account = bank.BankAccount('012345', 500)

    def testBasicDeposit(self):
        self.account.deposit(100)
        self.assertEqual(600, self.account.balance())

    def testNegativeDeposit(self):
        with self.assertRaises(ValueError) as context:
            self.account.deposit(-100)

        self.assertTrue('Negative value' in context.exception)

    def tearDown(self):
        del self.account
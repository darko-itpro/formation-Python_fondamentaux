#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import re

SQL_CREATE_SNCF = "CREATE TABLE IF NOT EXISTS sncf (date, nom_train, ponctualite)"
SQL_INSERT_SNCF = "INSERT INTO sncf values(?, ?, ?)"


class LiteDao:

    def __init__(self):
        self._conn = lite.connect("text.db")
        try:
            cur = self._conn.cursor()
            cur.execute(SQL_CREATE_SNCF)
        except Exception as e:
            print(e)

    def insert_train_data(self, rer_data):
        try:
            cur = self._conn.cursor()
            cur.execute(SQL_INSERT_SNCF,
                        (rer_data[1], rer_data[4], rer_data[5]))
            print(rer_data[1], rer_data[4], rer_data[5])
        except Exception as e:
            print(e)

        self._conn.commit()

    def __del__(self):
        self._conn.close()

def create_sql():
    _conn = lite.connect("text.db")
    try:
        cur = _conn.cursor()
        cur.execute(SQL_CREATE_SNCF)
    except Exception as e:
        print(e)
    return _conn


def open_file(_conn, file_name="ponctualite-mensuelle-transilien.csv"):
    """

    :param _conn:
    :param file_name:
    :return:
    """

    cur = _conn.cursor()

    rer_pat = re.compile('RER [^D]')
    fichier_sncf = open(file_name, 'r')
    for ligne in fichier_sncf:
        if rer_pat.search(ligne):
            rer_data = ligne.split(';')
            try:
                cur.execute(SQL_INSERT_SNCF,
                            (rer_data[1], rer_data[4], rer_data[5]))
                print(rer_data[1], rer_data[4], rer_data[5])
            except Exception as e:
                print(e)

    _conn.commit()


def search_paris(file_name="ponctualite-mensuelle-transilien.csv"):

    rer_pat = re.compile('Paris ([a-zA-Z ]+);')
    fichier_sncf = open(file_name, 'r')
    for ligne in fichier_sncf:
        if rer_pat.search(ligne):
            print(rer_pat.search(ligne).group(1))


if __name__ == '__main__':
    conn = create_sql()
    open_file(conn)
    #search_paris()
    conn.close()

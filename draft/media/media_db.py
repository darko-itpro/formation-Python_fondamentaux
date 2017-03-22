#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import sqlite3 as sqlite

SQL_CREATE_EPISODES_TABME = "CREATE TABLE IF NOT EXISTS episodes (number INT NOT NULL, season INT NOT NULL, title TEXT NOT NULL)"

SQL_ADD_EPISODE = "INSERT INTO episodes values(?, ?, ?)"
SQL_GET_ALL_EPISODES = "SELECT title, season, number FROM episodes ORDER BY season, number"
SQL_GET_EPISODES_FOR_SEASON = "SELECT title, number FROM episodes where season = ? ORDER BY number"


class MediaDao:
    def __init__(self, dbname="test.db"):
        self._db_name = dbname
        self._connect = sqlite.connect(dbname)

        try:
            cur = self._connect.cursor()
            cur.execute(SQL_CREATE_EPISODES_TABME)
        except sqlite.Error as e:
            print("Error occured")
            print(e)

    def __del__(self):
        try:
            self._connect.close()
        except sqlite.Error as e:
            print("Error occured")
            print(e)

    def __str__(self):
        return 'Media DB Connector ({})'.format(self._db_name)

    def add_episode(self, name, season_number, ep_number):
        cur = self._connect.cursor()
        cur.execute(SQL_ADD_EPISODE, (ep_number, season_number, name))
        self._connect.commit()

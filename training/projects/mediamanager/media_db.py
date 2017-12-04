#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import sqlite3 as sqlite

SQL_CREATE_SHOWS_TABLE = "CREATE TABLE IF NOT EXISTS shows(" \
                         "name text NOT NULL, " \
                         "PRIMARY KEY (name));"
SQL_CREATE_EPISODES_TABLE = "CREATE TABLE IF NOT EXISTS episodes (" \
                            "number integer NOT NULL, " \
                            "season integer NOT NULL, " \
                            "title text NOT NULL, " \
                            "show text NOT NULL, " \
                            "PRIMARY KEY(show, number, season), " \
                            "FOREIGN KEY (show) REFERENCES shows (name) " \
                            "ON DELETE CASCADE);"

SQL_ADD_SHOW = "INSERT INTO shows values(?)"
SQL_SELECT_SHOWS = "SELECT name FROM shows"

SQL_ADD_EPISODE = "INSERT INTO episodes values(?, ?, ?, ?)"
SQL_GET_ALL_EPISODES = "SELECT title, season, number " \
                       "FROM episodes " \
                       "WHERE show = ? " \
                       "ORDER BY season, number"
SQL_GET_EPISODES_FOR_SEASON = "SELECT title, number " \
                              "FROM episodes " \
                              "WHERE show = ? AND season = ? " \
                              "ORDER BY number"


class MediaDao:
    def __init__(self, show_name, dbname="test.db"):
        self._db_name = dbname
        self._connect = sqlite.connect(dbname)

        try:
            self._create_table(SQL_CREATE_SHOWS_TABLE)
            self._create_table(SQL_CREATE_EPISODES_TABLE)

            shows_cur = self._connect.cursor()
            shows_cur.execute(SQL_SELECT_SHOWS)
            if show_name in [name for name, in shows_cur.fetchall()]:
                pass
            else:
                show_insert_cur = self._connect.cursor()
                show_insert_cur.execute(SQL_ADD_SHOW, (show_name,))
                self._connect.commit()

            self._show_name = show_name

        except sqlite.Error as e:
            print("Error occured")
            print(e)

    def _create_table(self, create_query):
        """
        private method used to create tables.
        :param create_query: an CREATE TABLE SQL query
        """
        cur = self._connect.cursor()
        cur.execute(create_query)

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
        cur.execute(SQL_ADD_EPISODE, (ep_number, season_number, name,
                                      self._show_name))
        self._connect.commit()

    def get_episodes(self, season_number=None):
        """
        Retourne une liste d'épisodes sous forme de tableaux de données contennat le nom, numéro
        de saison et numéro d'épisode. ou nom et numéro d'épisode si la requête ne concerne qu'une
        saison
        :return: liste d'enregistrements
        """
        cur = self._connect.cursor()
        if season_number:
            cur.execute(SQL_GET_EPISODES_FOR_SEASON, (self._show_name,
                                                      season_number))
        else:
            cur.execute(SQL_GET_ALL_EPISODES, (self._show_name,))
        return cur.fetchall()

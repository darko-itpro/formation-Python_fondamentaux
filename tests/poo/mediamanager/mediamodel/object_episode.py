#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
Module de test de la classe Episode
"""

import unittest

from training.projects.mediamanager import mediamodel


class CreateEpisode(unittest.TestCase):
    """
    Tests de la création d'un épisode
    """

    def test_create_episode_without_season(self):
        episode = mediamodel.Episode("Title", 1)
        self.assertIsNotNone(episode)

    def test_create_episode_with_season(self):
        episode = mediamodel.Episode("Title", 1, 1)
        self.assertIsNotNone(episode)

    def test_title_accessible(self):
        episode = mediamodel.Episode("Title", 1)
        self.assertEqual(episode.title, "Title")

    def test_should_not_assign_title(self):
        episode = mediamodel.Episode("Title", 1)
        with self.assertRaises(AttributeError):
            episode.title = 'Other title'

    def test_number_accessible(self):
        episode = mediamodel.Episode("Title", 1)
        self.assertEqual(episode.number, 1)

    def test_should_not_assign_number(self):
        episode = mediamodel.Episode("Title", 1)
        with self.assertRaises(AttributeError):
            episode.number = 2

    def test_season_accessible(self):
        episode = mediamodel.Episode("Title", 1, 2)
        self.assertEqual(episode.season, 2)

    def test_shouldnt_assign_season(self):
        episode = mediamodel.Episode("Title", 1)
        with self.assertRaises(AttributeError):
            episode.season = 2

    def test_without_season_should_be_none(self):
        episode = mediamodel.Episode("Title", 1)
        self.assertIsNone(episode.season)

    def test_number_must_be_integer_compatible(self):
        episode = mediamodel.Episode('Title', 1)
        self.assertEqual(episode.number, 1)
        episode = mediamodel.Episode('Title', "1")
        self.assertEqual(episode.number, 1)
        with self.assertRaises(ValueError):
            mediamodel.Episode('Title', "un")

    def test_season_must_be_integer_compatible(self):
        episode = mediamodel.Episode('Title', 1, 2)
        self.assertEqual(episode.season, 2)
        episode = mediamodel.Episode('Title', 1, "2")
        self.assertEqual(episode.season, 2)
        with self.assertRaises(ValueError):
            mediamodel.Episode('Title', 1, "un")

    def test_title_should_be_string_or_raise_error(self):
        with self.assertRaises(ValueError):
            mediamodel.Episode(10, 1)

    def test_title_cannot_be_empty(self):
        with self.assertRaises(ValueError):
            mediamodel.Episode('', 1)


if __name__ == '__main__':
    unittest.main()

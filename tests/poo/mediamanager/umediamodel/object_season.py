#!/usr/bin/env python 
# -*- coding: utf-8 -*-

import unittest

from training.projects.mediamanager import mediamodel


class CreateSeason(unittest.TestCase):

    def test_create_first_season(self):
        self.assertIsNotNone(mediamodel.Season(1))

    def test_season_number_must_be_set(self):
        with self.assertRaises(TypeError):
            mediamodel.Season()

    def test_season_number_can_be_none(self):
        self.assertIsNotNone(mediamodel.Season(None))

    def test_season_number_can_be_null(self):
        self.assertIsNotNone(mediamodel.Season(None))

    def test_season_number_cannot_be_negative(self):
        with self.assertRaises(ValueError):
            mediamodel.Season(-1)


class AccessEpisodes(unittest.TestCase):

    def test_season_has_episodes_attribute(self):
        season = mediamodel.Season(None)
        self.assertTrue(hasattr(season, 'episodes'))

    def test_new_season_have_no_episode(self):
        season = mediamodel.Season(None)
        self.assertEqual(len(season.episodes), 0)

    def test_should_not_alter_episodes(self):
        season = mediamodel.Season(1)
        season.add(mediamodel.Episode("First Episode", 1, 1))
        season.add(mediamodel.Episode("Second Episode", 2, 1))
        self.assertEqual(len(season.episodes), 2)

        episodes = season.episodes
        episodes.append(mediamodel.Episode("Intruder", 3, 1))
        self.assertEqual(len(season.episodes), 2)

    def test_episodes_are_ordered(self):
        season = mediamodel.Season(1)
        season.add(mediamodel.Episode("Second Episode", 2, 1))
        season.add(mediamodel.Episode("First Episode", 1, 1))

        episodes = season.episodes
        self.assertEqual(episodes[0].number, 1)
        self.assertEqual(episodes[1].number, 2)


if __name__ == '__main__':
    unittest.main()
